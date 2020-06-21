from parser import getContent, get_products, get_label, get_text
from db_connector import DbConnector

config = {'database': 'db.db'}

db = DbConnector(None, config['database'])

for id in range(150000, 152000):
    content = getContent(id)
    label = get_label(content)
    products = get_products(content)
    text = get_text(content)
    db.create_recipt(label, products, text)