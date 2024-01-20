from .lib.constant.constant import *

def coba(request):
    return {
        'sidebar': SIDEBAR,
        'company_name': COMPANY_NAME
    }