from django.contrib import admin
from .models import Stats
from .models import Nonprofit_Partner
from .models import Opportunity_Request
from .models import Attorney_List
# Register your models here.


admin.site.register(Stats)
admin.site.register(Nonprofit_Partner)
admin.site.register(Opportunity_Request)
admin.site.register(Attorney_List)
