from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/", include("apps.accounts.urls")),
    path("api/companies/", include("apps.companies.urls")),
    path("api/assets/", include("apps.assets.urls")),
    path("api/projects/", include("apps.projects.urls")),
    path("api/auctions/", include("apps.auctions.urls")),
    path("api/bids/", include("apps.bidding.urls")),
    path("api/orders/", include("apps.orders.urls")),
    path("api/payments/", include("apps.payments.urls")),
    path("api/pickup/", include("apps.pickup.urls")),
    path("api/notifications/", include("apps.notifications.urls")),
]
