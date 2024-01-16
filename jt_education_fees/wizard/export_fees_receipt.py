from odoo import models, fields

class ExportFeesReceiptXls(models.Model):
    _name = 'export.fees.receipt'
    _description = "Fees Receipt XLS Report"

    excel_file = fields.Binary('Download Report :- ')
    file_name = fields.Char('Excel File', size=64)