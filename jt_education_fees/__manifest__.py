# -*- coding: utf-8 -*-
##############################################################################
#
#    Jupical Technologies Pvt. Ltd.
#    Copyright (C) 2018-TODAY Jupical Technologies(<http://www.jupical.com>).
#    Author: Jupical Technologies Pvt. Ltd.(<http://www.jupical.com>)
#    you can modify it under the terms of the GNU LESSER
#    GENERAL PUBLIC LICENSE (LGPL v3), Version 3.
#
#    It is forbidden to publish, distribute, sublicense, or sell copies
#    of the Software or modified copies of the Software.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU LESSER GENERAL PUBLIC LICENSE (LGPL v3) for more details.
#
#    You should have received a copy of the GNU LESSER GENERAL PUBLIC LICENSE
#    GENERAL PUBLIC LICENSE (LGPL v3) along with this program.
#    If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################
{
    'name': 'Fees Management',
    'sequence':7,
    'version': '16.0.1.0.0',
    'summary': 'Fees Management System',
    'category': 'Fees management',
    'depends': ['jt_education_base','product','sale_management','account'],
    'data': [
        'security/fees_security.xml',
        'security/ir.model.access.csv',
        'demo/demo.xml',
        'data/ir_actions_server_data.xml',
        'wizard/pay_yearly_fees_wizard_view.xml',
        'wizard/export_fees_history_wizard_view.xml',
        'wizard/due_fees_summary_report_view.xml',
        'wizard/export_fees_receipt_view.xml',
        'views/student.xml',
        'views/fees_sequence.xml',
        'views/fees_view.xml',
        'views/view_account_move_form.xml',
        'reports/fee_receipt.xml',
    ],
    'application': True,
    'license':'OPL-1',
}
