# Copyright (c) 2023, Douglas Ejiroghene Dominic and contributors
# For license information, please see license.txt

import json
import frappe
from frappe.model.document import Document

class CloudAutomation(Document):
    @frappe.whitelist()
    def on_submit(self):
        data = {
            "disk_type": self.disk_type
        }
        form_data = o_submit(data=data, message="Submit")
        return 

@frappe.whitelist(allow_guest=True)
def o_submit(data, message):
    disk = data
    print(disk)
    return disk
