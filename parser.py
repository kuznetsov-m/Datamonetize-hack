import requests
from lxml import html
import urllib

id = 152293
domain = 'https://www.russianfood.com/recipes/recipe.php?rid='

def getContent(id):

    url = domain + str(id)

    print('getContent(): send request to %s' % url)
    try:
        r = requests.get(url, timeout=30)
    except Exception as e:
        print(e)

    content = ''
    if r.reason == 'OK':
        print('getContent(): status OK')
        
        content = r.text
    
    return content

def get_products(content):
    tree = html.fromstring(content)

    products = []
    for element in tree.xpath('//td[@class="padding_l padding_r"]/span'):
        product = element.text.lower()
        if '-' in product:
            product = product.split(' - ')[0]

        products.append(product)

    return products

def get_label(content):
    tree = html.fromstring(content)

    label = None
    for element in tree.xpath('//span[@class="rcp"]'):
        label = element.text
    return label

def get_text(content):
    tree = html.fromstring(content)

    text = ''
    for element in tree.xpath('//div[@class="step_n"]/p'):
        text += element.text + ' '
    return text

# for id in range(152000, 152005):
content = getContent(id)
label = get_label(content)
products = get_products(content)
text = get_text(content)