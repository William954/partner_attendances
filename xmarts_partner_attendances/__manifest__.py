# -*- coding: utf-8 -*-
{
    'name': "Partner Attendances",

    'summary': """
        Adecuacion al modulo de Asistencias para verificar la entrara y salida de personal externo""",

    'description': """
        Adecuacion al modulo de Asistencias que permite tomar las asistencias de personal externo a la empresa GTVP
    """,

    'author': "GTVP",
    'website': "https://gtvp.odoo.com/en_US/",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Adecuacion',
    'version': '1.0',

    # any module necessary for this one to work correctly
    'depends': ['base','hr_attendance'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
    ],
    # only loaded in demonstration mode
     'demo': [
        'demo/demo.xml',
    ],
    'qweb': [
        "static/src/xml/attendance.xml", ],
   
}
