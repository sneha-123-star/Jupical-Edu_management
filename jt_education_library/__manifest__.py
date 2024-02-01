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
    'name': "Library Management",
    'sequence': 8,
    'version': '17.0.1.0.0',
    'summary': "Library Management System",
    'category': 'Library Management',
    'depends': ['contacts', 'jt_education_base','jt_education_fees'],
    'data': [
        'security/ir.model.access.csv',
        'views/action_and_menu.xml',
        'views/sequence.xml',
        'views/books_view.xml',
        'views/issuebooks_view.xml',
        'views/memberships_view.xml',
        'views/authors_view.xml',
        'views/book_lang.xml',
        'views/student.xml',
        'reports/book_detail_report.xml',
        'reports/issuebook_detail_report.xml',
        'reports/membership_detail_report.xml',
        'reports/membership_card.xml',
        'wizard/book_xls_report_view.xml',
        'wizard/membership_xls_report_view.xml',
        'wizard/issuebook_xls_report_view.xml',
        'data/membership_cron.xml',
        'data/email_template.xml',
        'data/issue_email_cron.xml',
    ],
    'application': True,
    'license':'OPL-1',
}
