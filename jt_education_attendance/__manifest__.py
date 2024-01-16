{
    'name': "Attendance Management",
    'sequence':6,
    'version': '16.0.1.0.0',
    'summary': "Manage the Attendance of students",
    'category': 'Student Attendance',
    'depends': ['jt_education_base','jt_education_exam'],
    'data': [

        'security/ir.model.access.csv',
        'views/attendance_view.xml',
        'reports/report_attendance.xml',
        'wizard/print_attendance.xml',
    ],
    'application': True,
    'license':'OPL-1',
}
