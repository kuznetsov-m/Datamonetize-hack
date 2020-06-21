import json
import os
from db_connector import DbConnector

if not os.path.isdir('cloud'):
    os.mkdir('cloud')

db = DbConnector('cloud', 'db.db')
db.create_db(True)
db.create_recipt('Яичница',
                    ['яйца', 'кетчуп'],
                    'Вкусный рецепт приготовления')

db.create_recipt('Паста',
                    ['спагетти', 'кетчуп', 'фарш говяжий'],
                    'Жарим фарш, и варим спагетти, все смешиваем + кетчуп! Готово!')


print('get_recipts_count()')
count = db.get_recipts_count()
print(f'Recipts count: {count}')


print('get_recipt_by_id()')
print(f'Recipt: {db.get_recipt_by_id(2)}')


print('get_recipts_by_products_list()')
recipts = db.get_recipts_by_products_list(['яйца', 'кетчуп'])
print(f'Recipts ({len(recipts)}): {recipts}')
recipts = db.get_recipts_by_products_list(['кетчуп'])
print(f'Recipts ({len(recipts)}): {recipts}')