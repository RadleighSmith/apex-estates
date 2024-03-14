from django.views import generic
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.contrib.humanize.templatetags.humanize import intcomma
from .models import Property
from .forms import PropertyForm


class PropertyList(generic.ListView):
    """
    View for displaying a list of properties for sale.

    Attributes:
        model (class): The model class to query for property listings.
        template_name (str): The name of the template to render for property
        listings.
        paginate_by (int): Number of properties to display per page.
    """
    model = Property
    template_name = "property_listings/property_listings.html"
    paginate_by = 8

    def get_queryset(self):
        """
        Retrieve a queryset of properties for sale.

        Returns:
            queryset: Queryset of properties for sale.
        """
        queryset = super().get_queryset()
        for property in queryset:
            property.formatted_price = intcomma(property.price)
            if self.request.user.is_authenticated:
                property.is_favourite = property.favourite.filter(
                    id=self.request.user.id).exists()
            else:
                property.is_favourite = False
        return queryset


class PropertyDetail(generic.DetailView):
    """
    View for displaying details of a specific property.

    Attributes:
        model (class): The model class representing a property.
        template_name (str): The name of the template to render for
        property details.
    """
    model = Property
    template_name = 'property_detail/property_detail.html'

    def get_context_data(self, **kwargs):
        """
        Retrieve additional context data for rendering the property detail
        view.

        Returns:
            dict: Additional context data for rendering the property detail
            view.
        """
        context = super().get_context_data(**kwargs)
        property = self.object

        # Add formatted_price attribute to the property
        property.formatted_price = intcomma(property.price)

        # Check if the user is authenticated and add is_favourite
        if self.request.user.is_authenticated:
            context['is_favourite'] = property.favourite.filter(
                id=self.request.user.id).exists()
        else:
            context['is_favourite'] = False
        return context


def favourite_property(request, slug):
    """
    Toggle the favourite status of a property for a logged-in user.

    Redirects back to the appropriate page (either property detail page,
    dashboard, or property listings page).

    Args:
        request (HttpRequest): The HTTP request object.
        slug (str): The slug of the property.

    Returns:
        HttpResponseRedirect: Redirects to the appropriate page based on
        the referer.
    """
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
    elif referer and referer == request.build_absolute_uri(
            reverse('dashboard')):
        # Redirect to dashboard page if referred from there
        return redirect(reverse('dashboard'))
    property_detail_url = reverse('property_detail', kwargs={'slug': slug})
    if referer and property_detail_url in referer:
        # Redirect to property detail page if referred from there
        return redirect(reverse('property_detail', kwargs={'slug': slug}))
    elif referer and referer.startswith(request.build_absolute_uri(
            reverse('dashboard'))):
        # Redirect to the dashboard page with the appropriate page number
        # if referred from there
        page_number_index = referer.find('?page=')
        if page_number_index != -1:
            page_number = referer[page_number_index + len('?page='):]
            return redirect(
                reverse('dashboard') + f'?page={page_number}')
        else:
            return redirect(reverse('dashboard'))
    else:
        # Otherwise, redirect to the property listings page
        redirect_url = reverse('property_listings')
        if '?page=' in referer:
            # If the referer URL contains a page parameter, extract it
            # and append it to the redirect URL
            page_number_index = referer.index('?page=') + len('?page=')
            page_number = referer[page_number_index:]
            redirect_url += f'?page={page_number}'

        return redirect(redirect_url)


@login_required
@staff_member_required
def create_property(request):
    """
    View for creating a new property listing.

    Args:
        request (HttpRequest): The HTTP request object.

    Returns:
        HttpResponse: HTTP response with the form for creating a property
        listing.
    """
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES)
        if form.is_valid():
            property = form.save(commit=False)
            property.save()
            return redirect('property_detail', slug=property.slug)
    else:
        form = PropertyForm()
    return render(request, 'property_listings/create_property.html',
                  {'form': form})


@login_required
@staff_member_required
def edit_property(request, slug):
    """
    View for editing an existing property listing.

    Args:
        request (HttpRequest): The HTTP request object.
        slug (str): The slug of the property to edit.

    Returns:
        HttpResponse: HTTP response with the form for editing the property
        listing.
    """
    property = get_object_or_404(Property, slug=slug)
    if request.method == 'POST':
        form = PropertyForm(request.POST, request.FILES, instance=property)
        if form.is_valid():
            form.save()
            return redirect('property_detail', slug=property.slug)
    else:
        form = PropertyForm(instance=property)
    return render(request, 'property_listings/edit_property.html',
                  {'form': form, 'property': property})


@login_required
@staff_member_required
def delete_property(request, slug):
    """
    View for deleting an existing property listing.

    Args:
        request (HttpRequest): The HTTP request object.
        slug (str): The slug of the property to delete.

    Returns:
        HttpResponse: HTTP response for rendering the property detail view.
    """
    property = get_object_or_404(Property, slug=slug)
    if request.method == 'POST':
        try:
            property.delete()
            messages.success(request, 'Property deleted successfully.')
            return redirect('property_listings')
        except Exception as e:
            messages.error(request, f'Error deleting property: {str(e)}')
    return render(request, 'property_listings/property_detail.html',
                  {'property': property})
