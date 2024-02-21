from django.views import generic
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
        queryset = super().get_queryset()
        for property in queryset:
            property.formatted_price = intcomma(property.price)
        return queryset

class PropertyDetail(generic.DetailView):
    model = Property
    template_name = 'property_detail/property_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        property = context['object']
        property.formatted_price = intcomma(property.price)
        return context
