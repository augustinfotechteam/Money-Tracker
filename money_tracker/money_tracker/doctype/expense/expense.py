# -*- coding: utf-8 -*-
# Copyright (c) 2015, August Infotech and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document

class Expense(Document):
	def validate(self):
		#frappe.throw(frappe.db.get_table_columns(self, doctype))
		pass
