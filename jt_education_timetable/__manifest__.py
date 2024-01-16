{
    'name': "Student Timetable",
    'sequence':5,
    'version': '16.0.1.0.0',
    'summary': "Manage Students Timetable",
    'category': 'Timetable Management',
    'depends': ['jt_education_base','jt_education_exam'],
    'data': [
        'security/ir.model.access.csv',
        # 'demo/demo.xml',
        'views/action_and_menu.xml',
        'views/timetable_view.xml',
        'views/period_view.xml',
    ],
    'application': True,
    'license':'OPL-1',
}
