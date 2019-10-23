from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from account.models import Account

admin.site.site_header = 'Admin Panel'

class AccountAdmin(UserAdmin):
	list_display	= ('full_name','username','last_login','is_admin','is_staff')
	search_fields	= ('first_name','last_name','email','username')
	readonly_fields	= ('date_joined','last_login')

	filter_horizontal	= ()
	list_filter 		= ('date_joined', 'last_login')
	fieldsets			= ()

	def full_name(self, obj):
		return '{} {}'.format(obj.first_name, obj.last_name)

admin.site.register(Account, AccountAdmin)
