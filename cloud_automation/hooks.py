from . import __version__ as app_version

app_name = "cloud_automation"
app_title = "Cloud Automation"
app_publisher = "Douglas Ejiroghene Dominic"
app_description = "An application that automate cloud processes"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "ejise45@gmail.com"
app_license = "MIT"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/cloud_automation/css/cloud_automation.css"
# app_include_js = "/assets/cloud_automation/js/cloud_automation.js"

# include js, css files in header of web template
# web_include_css = "/assets/cloud_automation/css/cloud_automation.css"
# web_include_js = "/assets/cloud_automation/js/cloud_automation.js"

# include custom scss in every website theme (without file extension ".scss")
# website_theme_scss = "cloud_automation/public/scss/website"

# include js, css files in header of web form
# webform_include_js = {"doctype": "public/js/doctype.js"}
# webform_include_css = {"doctype": "public/css/doctype.css"}

# include js in page
# page_js = {"page" : "public/js/file.js"}

# include js in doctype views
# doctype_js = {"doctype" : "public/js/doctype.js"}
# doctype_list_js = {"doctype" : "public/js/doctype_list.js"}
# doctype_tree_js = {"doctype" : "public/js/doctype_tree.js"}
# doctype_calendar_js = {"doctype" : "public/js/doctype_calendar.js"}

# Home Pages
# ----------

# application home page (will override Website Settings)
# home_page = "login"

# website user home page (by Role)
# role_home_page = {
#	"Role": "home_page"
# }

# Generators
# ----------

# automatically create page for each record of this doctype
# website_generators = ["Web Page"]

# Installation
# ------------

# before_install = "cloud_automation.install.before_install"
# after_install = "cloud_automation.install.after_install"

# Uninstallation
# ------------

# before_uninstall = "cloud_automation.uninstall.before_uninstall"
# after_uninstall = "cloud_automation.uninstall.after_uninstall"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "cloud_automation.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
#	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
#	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# DocType Class
# ---------------
# Override standard doctype classes

# override_doctype_class = {
#	"ToDo": "custom_app.overrides.CustomToDo"
# }

# Document Events
# ---------------
# Hook on document methods and events

doc_events = {
	# "*": {
	# 	"on_update": "method",
	# 	"on_cancel": "method",
	# 	"on_trash": "method",
	# 	"on_submit": "cloud_automation.cloud_server.get_server"
	# },
#  	"cloud_automation":{
#       	"on_submit": "cloud_automation.cloud_services.services.submited_form"
#        "erpnext.regional.italy.utils.sales_invoice_on_submit",
#  },
  	"Cloud Automation": {
		"on_submit": [
			"cloud_automation.cloud_services.doctype.cloud_automation.cloud_automation.o_submit"
			# "cloud_automation.cloud_services.services.CloudAutomation.services_on_submit",
			# "cloud_automation.cloud_services.doctype.cloud_automation.cloud_automation.CloudAutomation.on_submit"
		]
	}
 
}

# Scheduled Tasks
# ---------------

# scheduler_events = {
#	"all": [
#		"cloud_automation.tasks.all"
#	],
#	"daily": [
#		"cloud_automation.tasks.daily"
#	],
#	"hourly": [
#		"cloud_automation.tasks.hourly"
#	],
#	"weekly": [
#		"cloud_automation.tasks.weekly"
#	]
#	"monthly": [
#		"cloud_automation.tasks.monthly"
#	]
# }

# Testing
# -------

# before_tests = "cloud_automation.install.before_tests"

# Overriding Methods
# ------------------------------
#
# override_whitelisted_methods = {
#	"frappe.desk.doctype.event.event.get_events": "cloud_automation.event.get_events"
# }
#
# each overriding function accepts a `data` argument;
# generated from the base implementation of the doctype dashboard,
# along with any modifications made in other Frappe apps
# override_doctype_dashboards = {
#	"Task": "cloud_automation.task.get_dashboard_data"
# }

# exempt linked doctypes from being automatically cancelled
#
# auto_cancel_exempted_doctypes = ["Auto Repeat"]

# Request Events
# ----------------
# before_request = ["cloud_automation.utils.before_request"]
# after_request = ["cloud_automation.utils.after_request"]

# Job Events
# ----------
# before_job = ["cloud_automation.utils.before_job"]
# after_job = ["cloud_automation.utils.after_job"]

# User Data Protection
# --------------------

user_data_fields = [
	{
		"doctype": "{doctype_1}",
		"filter_by": "{filter_by}",
		"redact_fields": ["{field_1}", "{field_2}"],
		"partial": 1,
	},
	{
		"doctype": "{doctype_2}",
		"filter_by": "{filter_by}",
		"partial": 1,
	},
	{
		"doctype": "{doctype_3}",
		"strict": False,
	},
	{
		"doctype": "{doctype_4}"
	}
]

# Authentication and authorization
# --------------------------------

# auth_hooks = [
#	"cloud_automation.auth.validate"
# ]

