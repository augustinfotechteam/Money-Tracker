# -*- coding: utf-8 -*-
# Copyright (c) 2015, August Infotech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Investments(Document):
	pass
	
@frappe.whitelist()	
def investment_maturity_reminder():
	today = frappe.utils.today()
	
	get_matured_investment = frappe.db.sql("""SELECT name, investment_amount FROM `tabInvestments` WHERE maturity_date = '%s'"""% (today),as_dict=1)
	
	frappe.throw(get_matured_investment)
