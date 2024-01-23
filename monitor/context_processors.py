from django.conf import settings # import the settings file

def donation_addresses(request):
    return {'BANANO_ADDRESS': settings.BANANO_ADDRESS,
            'NANO_ADDRESS': settings.NANO_ADDRESS,
            'KOFI_ADDRESS': settings.KOFI_ADDRESS}

def constants(request):
    return {
        'DEFAULT_TITLE': settings.DEFAULT_TITLE,
        'DEFAULT_TAB_TITLE': settings.DEFAULT_TAB_TITLE,
        'DEFAULT_SUBTITLE': settings.DEFAULT_SUBTITLE,
        'NANO_SYMBOL_TEXT': settings.NANO_SYMBOL_TEXT,
        'THEME': settings.THEME,
        'REFRESH_TIMER': 10

    }