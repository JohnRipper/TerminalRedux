from decimal import Decimal

from django.http import JsonResponse
from django.shortcuts import render
import requests
import json

from NanoMonitor.settings import NODE_ACCOUNT, CHAIN, Chain

# TODO MOVE TO SETTINGS.PY OR A TOML CONFIG.

HOST = "http://127.0.0.1"
PORT = "7072"
# URL = f"{HOST}:{PORT}"
URL = "https://bananode.makes.trade"





########## PAGES #################
def index(request):
    """
    Create a status page for Nano Node statistics.

    TODO -> elaborate on what all this shit means,
    TODO woudl probably become #1 if I can present data clearly
    TODO enough stupid people feel smart understanding it.

    Show syncronization status
    Show blockchain used, make interchangeable between nano and banano
    Show block count, checked blocks, unchecked blocks.
    Show # of accounts on nano, -> go deeper and show active past month?
    Show database back end used. ( Database REsources used? )
    Show TPS? Transactions Per Second, Hour, Day?
    Show system statistics.  CPU, RAM used, Uptime
    Show Peers -> go further and record peers over time to measure growth.
    Show Historical statistics? Or a new page for node growth over time.
    Show Node wallet and donations page. Kofi and Nano wallet.
    Look into possibility of being a representative.
    advertise link to  main blog.
    Show node accoutn statistics, balance, pending, prepresentative chosen. vote weight

    # More Extras
    Internal site statistics
    addresses searched, Rich list, Transfer leaderboards, Notable Wallets
    Beaner friendly - Spanish support.

    """


    # node data
    #node_block_count = get_block_count()
    #uptime = display_time(int(get_uptime()['seconds']))

    # server data
#    telemetry = get_telemetry()

    # node account data
   # node_account_balance = get_account_balance(NODE_ACCOUNT)


   # sync_percent = (Decimal(node_block_count['count']) / Decimal(telemetry['block_count'])) * 100
 #   print(sync_percent)
  #  sync_percent = sync_percent.quantize(Decimal(000.00))
 #   if sync_percent > 99.9:
        # close enough to be considered fully synced. being behind by a second doesnt mean ur unsynced
  #      sync_percent = 100



    # sync_estimated_time = display_time(int(100 / sync_percent) * int(get_uptime()['seconds']))

    # configure data to be easier to read.
  #  telemetry['uptime'] = display_time(telemetry['uptime'])


    # TODO GET CURRENCY VALUE FROM COINGECKO API? OR FROM SELFHOSTED INFLUXDB?

    return render(request, 'monitor/draft_pages/dashboard_example.html')



def search(request):
    query :str = request.GET.get("search_query", "")
    if query:
        # what is difference between block , address, or alias

        # account
        # performs redirects to appropriate page
        if query.startswith("ban"):
            # search account
            return

        # get search details.
        context = {}

        return render(request,"",context=context)



def account(request):
    """
    """
    account: str = request.GET.get("account", None)
    if account:
        if CHAIN == Chain.BANANO:
            prefix = "ban_"
        elif CHAIN == Chain.NANO:
            prefix = "nano_"

        if account.startswith(prefix):
            print("test")


    # if no accoutn raise error message

    return render()





def maintenance(request):
    """
    Landing page for wahtever.
    :param request:
    :return:
    """
    context = {}
    return render(request, "monitor/pages/down.html", context=context)