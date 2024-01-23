from django.shortcuts import render

from monitor.utility import display_time
from monitor.views_rpc import get_account_balance, get_available_supply, get_telemetry, get_uptime, get_block_count


def account_balance(request):
    account_balance = get_account_balance()
    context = {'account_balance': account_balance}
    return render(request, 'monitor/partials/account/balance.html', context)





def block_count(request):
    block_count = get_block_count()
    context = {'node_block_count': block_count}
    return render(request, 'monitor/partials/node_status_row/block_count.html', context)

def telemetry(request):
    # return multiple rows

    telemetry = get_telemetry()
    telemetry['block_count'] =  "{:,}".format(int(telemetry['block_count']))
    telemetry['cemented_count'] =  "{:,}".format(int(telemetry['cemented_count']))
    telemetry['account_count'] =  "{:,}".format(int(telemetry['account_count']))
    telemetry['uptime'] = display_time(int(telemetry['uptime']))
    available_supply = get_available_supply()
    available_supply['available'] = "{:,}".format(int(available_supply['available']) / 1000000000000000000000000000000)
    context = {'network_available_supply': available_supply['available'],
               'telemetry': telemetry}
    return render(request, 'monitor/partials/network_status_row/telemetry.html', context)


def available_supply(request):
    available_supply = get_available_supply()
    available_supply['available'] = "{:,}".format(int(available_supply['available']) / 1000000000000000000000000000000)
    context = {'network_available_supply': available_supply['available']}
    return render(request, 'monitor/partials/network_status_row/available_supply.html', context)


def node_uptime(request):
    """
    returns uptime in seconds.
    :return:
    {
        "seconds": "6000"
    }
    """

    uptime = display_time(int(get_uptime()['seconds']))
    context = {"node_uptime": str(uptime)}
    return render(request, 'monitor/partials/node_status_row/uptime.html', context)
