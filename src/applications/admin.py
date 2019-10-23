from django.contrib import admin

from .models import LeaveRequest
# Register your models here.

class LeaveRequestAdmin(admin.ModelAdmin):
	list_display	= ('full_name','start_date','end_date','status')
	search_fields	= ('full_name',)
	readonly_fields	= ()

	filter_horizontal	= ()
	list_filter 		= ()
	fieldsets			= ()

	def full_name(self, obj):
		return '{} {}'.format(obj.user.first_name, obj.user.last_name)

admin.site.register(LeaveRequest, LeaveRequestAdmin)
