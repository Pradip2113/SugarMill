# Copyright (c) 2023, SugarMill and contributors
# For license information, please see license.txt
import requests
import frappe
import requests
from frappe.model.document import Document

class AgriPlantations(Document):
	def before_save(self):
		frappe.msgprint("sendxsddsa sms")
		url = "https://www.fast2sms.com/dev/bulk"
		p = "testing Pradip"
		payload = "sender_id=FSTSMS&message="+p+"&language=english&route=p&numbers=8308020899" #+self.mobile_number
		# payload = f'sender_id=TXTIND&message={p}&route=v3&language=english&numbers=7397911080'
		headers = {
		'authorization': "AZUIFeldwx0o54qiRJaN6mXyfhGukPWK7D38Sv2LYstc1nMHBT5PUAICm8fGR92kcWr1FZj0thXegLqp",
		'Content-Type': "application/x-www-form-urlencoded",
		'Cache-Control': "no-cache",
		}
		response = requests.request("POST", url, data=payload, headers=headers)
		print(response.text)
		frappe.msgprint("response.text")
