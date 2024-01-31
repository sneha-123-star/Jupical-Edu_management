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
    'name': "Student Management",
    'sequence':1,
    'summary': "Manage the students details",
    'category': 'Student Extension',
    'version': '16.0.1.0.0',
    'depends': ['contacts','hr_recruitment'],
    'data': [
        'security/base_security.xml',
        'security/ir.model.access.csv',
        'demo/demo.xml',
        'views/student_view.xml',
        'views/district_view.xml',
        'views/village_view.xml',
        'views/province_view.xml',
        'views/student_standard_view.xml',
        'views/faculty_view.xml',
        'views/parent_view.xml',
        'views/how_know.xml',
        'views/action_and_menu.xml',
        'views/sequence.xml',
        'views/admission_inq_view.xml',
    ],
    'application': True,
    'license':'OPL-1',
}