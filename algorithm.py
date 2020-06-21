from db_connector import DbConnector

config = {'cloud_dir': 'cloud', 'database': 'db.db'}

db = DbConnector(config['cloud_dir'], config['database'])
db.create_db()

# while(True):
#     db.create_recipt('Яичница',
#                         ['яйца', 'кетчуп'],
#                         'Вкусный рецепт приготовления')

#     db.create_recipt('Паста',
#                         ['спагетти', 'кетчуп', 'фарш говяжий'],
#                         'Жарим фарш, и варим спагетти, все смешиваем + кетчуп! Готово!')

my_products = ['яйца', 'колбаса', 'кетчуп', 'соль']

def get_recipts_by_my_products(my_products: list):
    recipts = []

    for recipt_id in range(1, db.get_recipts_count() + 1):
        recipt = db.get_recipt_by_id(recipt_id)
        products = recipt['products'].split(',')

        if set(products).issubset(my_products):
            recipts.append(recipt)

    return recipts

print(len(get_recipts_by_my_products(my_products)))