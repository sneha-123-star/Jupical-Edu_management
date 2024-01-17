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
    'name': 'Health Management',
    'version': '16.0.0.0.0',
    'category': 'Student/Faculty Health',
    'summary': 'Manage Health',
    'description': """
        This module adds the feature of health in Education.
    """,
    'author': 'Jupical Technologies Pvt. Ltd.',
    'maintainer': 'Jupical Technologies Pvt. Ltd.',
    'website': 'http://www.jupical.com',
    'depends': ['jt_education_base'],
    'data': [
        'security/ir.model.access.csv',
        'views/health_view.xml',
        'views/action_and_menu.xml',
        'views/report_reg.xml',
        'views/health_register_view.xml',
        'views/health_history_view.xml',
        'views/student_view.xml',
        'views/faculty_view.xml',
    ],
    'demo': [
        'demo/health_line_demo.xml',
        'demo/health_demo.xml'
    ],
    'installable': True,
}
