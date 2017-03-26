// Copyright (c) 2013, August Infotech and contributors
// For license information, please see license.txt

frappe.query_reports["Expense Report"] = {
	"filters": [
		{
			"fieldname":"expense_category",
			"label": __("Expense Category"),
			"fieldtype": "Link",
			"options": "Expense Category"
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
