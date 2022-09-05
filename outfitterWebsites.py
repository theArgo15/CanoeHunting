import webbrowser

urls ={
    'Ely Outfitters': 'https://elyoutfittingcompany.com/used-kevlar-canoes-for-sale/',
    'Ely Outdoors': 'https://www.elyoutdoor.com/site-content/canoe-rentals/canoes-for-sale',
    'Voyager North Outfitters': 'https://www.vnorth.com/index.php?option=com_mijoshop&view=home&Itemid=56&lang=en',
    'Piragis': 'https://www.piragis.com/canoe-trip-outfitting/used-outfitting-gear.html',
    'Piragis Canoes': 'https://www.piragis.com/used/used-canoes.html',
    'Sawbill Outfitters': 'https://sawbill.com/product-category/used-canoes/',
    'Sawtooth Outfitters': 'http://www.canoecountry.com/sawtoothoutfitters/',
    'Seagull Outfitters': 'https://www.seagulloutfitters.com/used-canoes-for-sale/',
    'Tuscarora Canoe': 'https://tuscaroracanoe.com/used-canoes/',
    'Rockwood BWCA': 'https://www.rockwoodbwca.com/canoe-comparisons/'

}

for urlToOpen in urls.values():
    webbrowser.open(urlToOpen)