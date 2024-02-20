from django.views import generic
from .models import Property

class PropertyList(generic.ListView):
    """
    Returns all for sale properties in :model:`property.Property`

    **Template:**

    :template:`property/property_listings.html`
    """
    queryset = Property.objects.all()
    template_name = "property_listings/property_listings.html"
    paginate_by = 8
