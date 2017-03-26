// Copyright (c) 2013, August Infotech and contributors
// For license information, please see license.txt

frappe.query_reports["Income Report"] = {
	"filters": [
		{
			"fieldname":"income_category",
			"label": __("Income Category"),
			"fieldtype": "Link",
			"options": "Income Category"
		},
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
		}
	]
}
