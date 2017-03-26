# -*- coding: utf-8 -*-
from __future__ import unicode_literals

app_name = "money_tracker"
app_title = "Money Tracker"
app_publisher = "August Infotech"
app_description = "Money Track"
app_icon = "octicon octicon-file-directory"
app_color = "grey"
app_email = "info@augustinfotech.com"
app_version = "0.0.1"

# Includes in <head>
# ------------------

# include js, css files in header of desk.html
# app_include_css = "/assets/money_tracker/css/money_tracker.css"
# app_include_js = "/assets/money_tracker/js/money_tracker.js"

# include js, css files in header of web template
# web_include_css = "/assets/money_tracker/css/money_tracker.css"
# web_include_js = "/assets/money_tracker/js/money_tracker.js"

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

# before_install = "money_tracker.install.before_install"
# after_install = "money_tracker.install.after_install"

# Desk Notifications
# ------------------
# See frappe.core.notifications.get_notification_config

# notification_config = "money_tracker.notifications.get_notification_config"

# Permissions
# -----------
# Permissions evaluated in scripted ways

# permission_query_conditions = {
# 	"Event": "frappe.desk.doctype.event.event.get_permission_query_conditions",
# }
#
# has_permission = {
# 	"Event": "frappe.desk.doctype.event.event.has_permission",
# }

# Document Events
# ---------------
# Hook on document methods and events

# doc_events = {
# 	"*": {
# 		"on_update": "method",
# 		"on_cancel": "method",
# 		"on_trash": "method"
#	}
# }

# Scheduled Tasks
# ---------------

# scheduler_events = {
# 	"all": [
# 		"money_tracker.tasks.all"
# 	],
# 	"daily": [
# 		"money_tracker.tasks.daily"
# 	],
# 	"hourly": [
# 		"money_tracker.tasks.hourly"
# 	],
# 	"weekly": [
# 		"money_tracker.tasks.weekly"
# 	]
# 	"monthly": [
# 		"money_tracker.tasks.monthly"
# 	]
# }

# Testing
# -------

# before_tests = "money_tracker.install.before_tests"

# Overriding Whitelisted Methods
# ------------------------------
#
# override_whitelisted_methods = {
# 	"frappe.desk.doctype.event.event.get_events": "money_tracker.event.get_events"
# }

scheduler_events = {

"daily": [
		"money_tracker.money_tracker.doctype.investments.investments.investment_maturity_reminder"
 	],
 }
