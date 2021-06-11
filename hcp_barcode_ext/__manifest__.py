# -*- coding: utf-8 -*-
{
    'name': "HCP Barcode Ext",

    'summary': """Shipping Barcode Customization Added in the app""",

    'description': """Shipping Barcode Customization Added in the app""",

    'author': "NITS PVT LTD",
    'website': "http://www.navabrindsol.com",
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','web','stock_barcode'],

    # always loaded
    'data': [
        'views/asset.xml',
    ],

}
