{
    'name': "Portal For Education",
    'sequence': 10,
    'version': '16.0.1.0.0',
    'category': 'Portal Module',
    'summary': "Manage the Portal users for all education modules",
    'depends': ['portal','website','jt_education_base','jt_education_event','jt_education_exam',
    'jt_education_fees','jt_education_library','jt_education_assignment','jt_education_timetable'],
    'data': [
        'security/ir.model.access.csv',
        'views/portal_view.xml'
    ],
    'application': True,
    'license':'OPL-1',
}