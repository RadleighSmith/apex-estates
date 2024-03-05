from django.views import generic
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse
from django.contrib.humanize.templatetags.humanize import intcomma
from .models import Property

class PropertyList(generic.ListView):
    """
    Returns all for sale properties in :model:`property.Property`

    **Template:**

    :template:`property/property_listings.html`
    """
    model = Property
    template_name = "property_listings/property_listings.html"
    paginate_by = 8

    def get_queryset(self):
        """
        Adds formatted_price and is_favourite attributes to each property in the queryset
        """
        queryset = super().get_queryset()
        for property in queryset:
            property.formatted_price = intcomma(property.price)
            if self.request.user.is_authenticated:
                property.is_favourite = property.favourite.filter(id=self.request.user.id).exists()
            else:
                property.is_favourite = False
        return queryset

class PropertyDetail(generic.DetailView):
    """
    Returns details of a specific property.

    **Template:**

    :template:`property_detail/property_detail.html`
    """
    model = Property
    template_name = 'property_detail/property_detail.html'

    def get_context_data(self, **kwargs):
        """
        Adds formatted_price and is_favourite data to the context.
        """
        context = super().get_context_data(**kwargs)
        property = self.object
        property.formatted_price = intcomma(property.price)
        if self.request.user.is_authenticated:
            context['is_favourite'] = property.favourite.filter(id=self.request.user.id).exists()
        else:
            context['is_favourite'] = False
        return context
    

def favourite_property(request, slug):
    """
    Toggles the favourite status of a property for a logged-in user.
    Redirects back to the appropriate page (either property detail page or property listings page).
    """
    # Get the property object based on the slug
    property = get_object_or_404(Property, slug=slug)
    
    # Toggle favourite status for the logged-in user
    if request.user.is_authenticated:
        if property.favourite.filter(id=request.user.id).exists():
            property.favourite.remove(request.user)
        else:
            property.favourite.add(request.user)

    # Determine the appropriate redirect URL based on the referer
    referer = request.META.get('HTTP_REFERER')
    if referer and referer == request.build_absolute_uri(reverse('home')):
        # Redirect to home page if referred from there
        return redirect(reverse('home'))
    elif referer and reverse('property_detail', kwargs={'slug': slug}) in referer:
        # Redirect to property detail page if referred from there
        return redirect(reverse('property_detail', kwargs={'slug': slug}))
    else:
        # Otherwise, redirect to the property listings page
        redirect_url = reverse('property_listings')
        if '?page=' in referer:
            # If the referer URL contains a page parameter, extract it and append it to the redirect URL
            page_number_index = referer.index('?page=') + len('?page=')
            page_number = referer[page_number_index:]
            redirect_url += f'?page={page_number}'

        return redirect(redirect_url)