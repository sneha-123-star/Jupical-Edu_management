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
