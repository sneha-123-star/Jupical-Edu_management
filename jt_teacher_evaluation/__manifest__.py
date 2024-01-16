{
    'name': "Teacher's Evaluation",
    'sequence':1,
    'summary': "Managing Teacher's Evaluation",
    'category': 'Evaluation',
    'version': '16.0.1.0.0',
    'depends': ['base_automation','jt_education_base'],
    'data': [
        'security/ir.model.access.csv',        
        'views/evaluation.xml',
        'views/eva_details.xml',
        'reports/eval_rep.xml'

    ],
    'application': True,
    'license':'OPL-1',
}
