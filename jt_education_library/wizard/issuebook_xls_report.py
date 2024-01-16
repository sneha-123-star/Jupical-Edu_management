from odoo import models, fields

class IssueBookXlsReport(models.TransientModel):
    _name = "issuebook.xls.report"
    _description = "Issue Book Xls Report"

    excel_file = fields.Binary("Download Report")
    file_name = fields.Char("File Name", size=64)
