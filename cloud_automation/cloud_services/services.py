# import frappe

# from cloud_automation.doctype.cloud_automation. import on_submit

# @frappe.whitelist()
# def submited_form(doc, method):
#     data = on_submit()
#     print("hello")
#     print(data)
#     return data
# Copyright (c) 2023, Douglas Ejiroghene Dominic and contributors
# For license information, please see license.txt

# import frappe
# from frappe.model.document import Document

# class CloudAutomation(Document):
# 	pass

# 	@frappe.whitelist()
# 	def services_on_submit(data, self):
# 		disk_type = self.disk_type
# 		data = {
# 			"disk_type": disk_type
# 		}
# 		print(data)

# 		return data
    # def services_on_submit(data, message):
    #     print("hello")

# def services_on_submit(data, message):
#     print("hello")
# 	# # Validate payment details
	# if get_company_country(doc.company) not in [
	# 	"Italy",
	# 	"Italia",
	# 	"Italian Republic",
	# 	"Repubblica Italiana",
	# ]:
	# 	return

	# if not len(doc.payment_schedule):
	# 	frappe.throw(_("Please set the Payment Schedule"), title=_("E-Invoicing Information Missing"))
	# else:
	# 	for schedule in doc.payment_schedule:
	# 		if not schedule.mode_of_payment:
	# 			frappe.throw(
	# 				_("Row {0}: Please set the Mode of Payment in Payment Schedule").format(schedule.idx),
	# 				title=_("E-Invoicing Information Missing"),
	# 			)
	# 		elif not frappe.db.get_value(
	# 			"Mode of Payment", schedule.mode_of_payment, "mode_of_payment_code"
	# 		):
	# 			frappe.throw(
	# 				_("Row {0}: Please set the correct code on Mode of Payment {1}").format(
	# 					schedule.idx, schedule.mode_of_payment
	# 				),
	# 				title=_("E-Invoicing Information Missing"),
	# 			)

	# prepare_and_attach_invoice(doc)