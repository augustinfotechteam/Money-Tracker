# Copyright (c) 2013, August Infotech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import msgprint, _, throw

def execute(filters=None):
	if not filters: filters = {}
	columns = get_columns(filters)
	data = []
	entries = get_expense_data(filters)
	if entries:
		for entry in entries:
			row = [ entry.expense_category, entry.expense_date, entry.amount]
			data.append(row)
	return columns, data

	
def get_columns(filters):
	columns = []	
	columns.append(_("Expense Category") + ":Link/Expense Category:150")
	columns.append(_("Date") + ":Date:100")
	columns.append(_("Amount") + ":Currency:170")
	
	return columns
	
def get_expense_data(filters):
	conditions, filters = get_conditions(filters)
	
	expense_data = frappe.db.sql("Select * from `tabExpense` where docstatus < 2 %s order by expense_date"% conditions, filters, as_dict=1)
	if expense_data:
		return expense_data
		
	
	
def get_conditions(filters):
	conditions = ""
	if filters.get("from_date"):
		conditions += " and expense_date >= '{0}' ".format(filters.get("from_date"))
	if filters.get("to_date"):
		conditions += " and expense_date <= '{0}'".format(filters.get("to_date"))
	if filters.get("expense_category"):
		conditions += " and expense_category = '{0}'".format(filters.get("expense_category"))		
	return conditions, filters
	