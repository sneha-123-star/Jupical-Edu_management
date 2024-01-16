{
    'name': "Assignment Management",
    'sequence': 9,
    'version': '16.0.1.0.0',
    'summary': "Assignment Management System",
    'category': 'Student Assignment',
    'depends': ['jt_education_base','jt_education_exam','base_automation','jt_education_library'],
    'data': [
        'security/ir.model.access.csv',
        'demo/assignment_type_demo.xml',
        'views/action_and_menu.xml',
        'views/assignment_submission_view.xml',
        'views/assignment_type_view.xml',
        'views/assignment_view.xml',
        'views/student_view.xml',
    ],
    'application': True,
    'license':'OPL-1',
}
