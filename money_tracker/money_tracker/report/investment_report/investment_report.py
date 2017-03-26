# Copyright (c) 2013, August Infotech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import msgprint, _, throw

def execute(filters=None):
	if not filters: filters = {}
	columns = get_columns(filters)
	data = []
	entries = get_investment_data(filters)
	if entries:
		for entry in entries:
			row = [ 
			entry.name, 
			entry.investment_type, 
			entry.investment_date, 
			entry.investment_site,
			entry.rate_of_interest,			
			entry.investment_amount,
			entry.maturity_date,
			entry.maturity_amount,			
			entry.payment_mode,
			entry.cheque_number,
			entry.account_number,
			entry.ledger_folio,
			entry.notes
			]
			data.append(row)
	return columns, data

	
def get_columns(filters):
	columns = []	
	columns.append(_("Investment") + ":Link/Investments:150")
	columns.append(_("Investment Type") + ":Link/Investment Type:150")
	columns.append(_("Investment Date") + ":Date:100")
	columns.append(_("Inveted In") + ":Data:100")
	columns.append(_("Rate of Intrest") + ":Float:100")
	columns.append(_("Investment Amount") + ":Currency:100")
	columns.append(_("Maturity Date") + ":Date:100")
	columns.append(_("Maturity Amount") + ":Currency:170")	
	columns.append(_("Payment Mode") + ":Data:170")
	columns.append(_("Cheque Number") + ":Data:170")
	columns.append(_("Account Number ")+ ":Data:170")
	columns.append(_("Ledger Folio") + ":Data:170")
	columns.append(_("Notes ")+ ":Data:170")
	return columns
	
def get_investment_data(filters):
	conditions, filters = get_conditions(filters)
	
	expense_data = frappe.db.sql("Select * from `tabInvestments` where docstatus < 2 %s order by investment_date"% conditions, filters, as_dict=1)
	if expense_data:
		return expense_data
		
	
	
def get_conditions(filters):
	
	conditions = ""
	if filters.get("from_date"):
		conditions += " and investment_date >= '{0}' ".format(filters.get("from_date"))
	if filters.get("to_date"):
		conditions += " and investment_date <= '{0}'".format(filters.get("to_date"))
	if filters.get("investment_type"):
		conditions += " and investment_type = '{0}'".format(filters.get("investment_type"))		
	if filters.get("from_amount"):
		conditions += " and investment_amount >= '{0}'".format(filters.get("from_amount"))		
	if filters.get("to_amount"):
		conditions += " and investment_amount <= '{0}'".format(filters.get("to_amount"))		
	if filters.get("investment_in"):
		conditions += " and investment_site = '{0}'".format(filters.get("investment_in"))	
	if filters.get("payment_mode"):
		conditions += " and payment_mode = '{0}'".format(filters.get("payment_mode"))	
	if filters.get("is_matured"):
		conditions += " and maturity_date <= '{0}'".format(frappe.utils.today())		
	return conditions, filters
	