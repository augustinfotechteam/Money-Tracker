# Copyright (c) 2013, August Infotech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import msgprint, _, throw

def execute(filters=None):
	if not filters: filters = {}
	columns = get_columns(filters)
	data = []
	entries = get_income_data(filters)
	if entries:
		for entry in entries:
			row = [ entry.income_category, entry.date_of_income, entry.amount]
			data.append(row)
	return columns, data

	
def get_columns(filters):
	columns = []	
	columns.append(_("Income Category") + ":Link/Income Category:150")
	columns.append(_("Date") + ":Date:100")
	columns.append(_("Amount") + ":Currency:170")
	
	return columns
	
def get_income_data(filters):
	conditions, filters = get_conditions(filters)
	
	expense_data = frappe.db.sql("Select * from `tabIncome` where docstatus < 2 %s order by date_of_income"% conditions, filters, as_dict=1)
	if expense_data:
		return expense_data
		
	
	
def get_conditions(filters):
	conditions = ""
	if filters.get("from_date"):
		conditions += " and date_of_income >= '{0}' ".format(filters.get("from_date"))
	if filters.get("to_date"):
		conditions += " and date_of_income <= '{0}'".format(filters.get("to_date"))
	if filters.get("income_category"):
		conditions += " and income_category = '{0}'".format(filters.get("income_category"))		
	return conditions, filters
	