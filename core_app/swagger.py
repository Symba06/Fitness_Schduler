from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
   openapi.Info(
      title="Fitness Scheduler API",
      default_version='v1',
      description="API for managing fitness scheduler",
      terms_of_service="http://localhost:8000/terms/",
      contact=openapi.Contact(email="contact@fitness-scheduler.com"),
      license=openapi.License(name="BSD License"),
   ),
   public=True,
)

