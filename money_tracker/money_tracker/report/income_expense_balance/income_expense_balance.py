# Copyright (c) 2013, August Infotech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe import msgprint, _, throw

def execute(filters=None):
	if not filters: filters = {}
	columns = get_columns(filters)
	opening_data = get_opening(filters)
	entries = get_report_data(filters)
	data = []
	total_bal = 0
	if opening_data: 
		opeing_row = ["", "Opening", "", opening_data]
		data.append(opeing_row)
		total_bal += opening_data
		
	if entries:
		for entry in entries:
			row = [entry.date, entry.type, entry.category, entry.amount]
			if entry.type == "Income":
				total_bal += entry.amount
			else:
				total_bal -= entry.amount
			data.append(row)
		
		total_row = ["" ,"Balance", "", total_bal]
		data.append(total_row)
	
	return columns, data


def get_columns(filters):
	columns = []
	columns.append(_("Date") + ":Date:100")
	columns.append(_("Income/Expense Category") + ":Data:150")
	columns.append(_("Category") + ":Data:170")
	columns.append(_("Amount") + ":Currency:170")	
	return columns
	
def get_conditions(filters):
	conditions = ""
	if filters.get("from_date"):
		conditions += " and date >= '{0}'".format(filters.get("from_date"))
	if filters.get("to_date"):
		conditions += " and date <= '{0}'".format(filters.get("to_date"))
		
	if conditions != "":
		return conditions, filters	
		
		
def get_report_data(filters):
	conditions, filters = get_conditions(filters)	

	
	report_data = frappe.db.sql("""SELECT * FROM(SELECT "Income" AS type, income_category as category, date_of_income as date, amount as amount FROM `tabIncome` 
		UNION
		SELECT "Expense" AS type, expense_category as category, expense_date as date, amount as amount FROM `tabExpense`)
		AS Moneytable where 1=1 %s ORDER BY date""" % conditions, filters, as_dict=1)
	
	if report_data:
		return report_data
	
def get_opening(filters):
	
	if filters.get("from_date"):	
		opening_income = frappe.db.sql("""Select COALESCE(SUM(amount),0) as amount from `tabIncome` where date_of_income <= %s""",(filters.from_date),as_dict = 1)
		opening_expense = frappe.db.sql("""Select COALESCE(SUM(amount),0) as amount from `tabExpense` where expense_date <= %s""",(filters.from_date),as_dict = 1)
		opening_val = 0
		if opening_income and opening_expense:
			opening_val = opening_income[0]['amount'] - opening_expense[0]['amount']
		elif opening_income and not opening_expense:
			opening_val = opening_income[0]['amount']
		elif opening_expense and not opening_income:
			opening_val = 0 - opening_expense[0]['amount']
			
		if opening_val:
			return opening_val
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
		
	
	