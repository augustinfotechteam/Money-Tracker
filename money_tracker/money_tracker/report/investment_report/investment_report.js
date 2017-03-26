// Copyright (c) 2013, August Infotech and contributors
// For license information, please see license.txt

frappe.query_reports["Investment Report"] = {
	"filters": [
		
		{
			"fieldname":"from_date",
			"label": __("From Date"),
			"fieldtype": "Date",
		},
		{
			"fieldname":"to_date",
			"label": __("To Date"),
			"fieldtype": "Date",
		},
		{
			"fieldname":"investment_type",
			"label": __("Investment Type"),
			"fieldtype": "Link",
			"options": "Investment Type"
		},
		{
			"fieldname":"from_amount",
			"label": __("From Amount"),
			"fieldtype": "Currency",
		},
		{
			"fieldname":"to_amount",
			"label": __("To Amount"),
			"fieldtype": "Currency",
		},
		{
			"fieldname":"investment_in",
			"label": __("Investment In"),
			"fieldtype": "Link",
			"options": "Investment Site"
		},
		{
			"fieldname":"payment_mode",
			"label": __("Payment Mode"),
			"fieldtype": "Select",
			"options": "Bank\nCash\nOnline"
		},
		{
			"fieldname":"is_matured",
			"label": __("Is Matured"),
			"fieldtype": "Check",
			
		},
		
	]
}
