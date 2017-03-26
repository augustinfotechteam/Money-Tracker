// Copyright (c) 2013, August Infotech and contributors
// For license information, please see license.txt

frappe.query_reports["Income Expense Balance"] = {
	"filters": [
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
			"reqd":1
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
			"reqd":1
		}
	]
}
