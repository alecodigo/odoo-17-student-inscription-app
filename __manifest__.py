# -*- coding: utf-8 -*-

{
    'name': 'Sistema de Gestión de Inscripciones',
    'version': '0.1',
    'author': 'Alejandro Sánchez',
    'sequence': 1,
    'summary': 'Sistema de Gestión de Inscripciones',
    'description': """
        Sistema de gestion de inscripciones de un sistema educativo.
    """,
    'depends': [
        'base',
        'contacts',
        'product',
    ],
    'data': [
        'security/unam_test_groups.xml',
        'security/ir.model.access.csv',
        
        'views/course_views.xml',
        'views/inscription_views.xml',
        'views/professor_views.xml',
        'views/student_views.xml',
        'views/subject_views.xml',
        'views/unam_test_menus.xml',
    ],
    'demo': [
        'data/unam_test_demo.xml',
    ],
    'installable': True,
    'application': True,
    'license': 'LGPL-3', 

}