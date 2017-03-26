from __future__ import unicode_literals
from frappe import _

def get_data():
	return [
		{
			"label": _("Documents"),
			"icon": "icon-star",
			"items": [
				
				{
					"type": "doctype",
					"name": "Income",
					"description": _("Income."),
				},
				
				{
					"type": "doctype",
					"name": "Expense",
					"description": _("Expense."),
				},
				{
					"type": "doctype",
					"name": "Investments",
					"description": _("Investments."),
				},
				
				
				
			]
		},
		{
			"label": _("Setup"),
			"icon": "icon-wrench",
			"items": [
				{
					"type": "doctype",
					"name": "Income Category",
					"description": _("Income Category."),
				},
				{
					"type": "doctype",
					"name": "Expense Category",
					"description": _("Expense Category."),
				},
				{
					"type": "doctype",
					"name": "Investment Type",
					"description": _("Investment Type."),
				},
				{
					"type": "doctype",
					"name": "Investment Site",
					"description": _("Investment Site."),
				}
			]
		},
		
		{
			"label": _("Standard Reports"),
			"icon": "icon-list",
			"items": [
				{
					"type": "report",
					"is_query_report": True,
					"name": "Income Report",
					"doctype": "Income",
					"description": _("Income Report.")
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Expense Report",
					"doctype": "Expense",
					"description": _("Expense Report.")
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Income Expense Balance",
					"doctype": "Income",
					"description": _("Income Expense Balance.")
				},
				{
					"type": "report",
					"is_query_report": True,
					"name": "Investment Report",
					"doctype": "Investments",
					"description": _("Investment Report.")
				},
				
				
			]
		},
	]