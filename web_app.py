# from flask import Flask, jsonify, request, abort
from flask import Flask, jsonify, request, render_template, redirect, url_for, request, session, flash, g, \
    make_response, abort, send_file
from sys import argv

import os
import json

from db_connector import DbConnector

config = {'cloud_dir': 'cloud', 'database': 'db.db'}

app = Flask(__name__)
app.database = config['database']

db = DbConnector(config['cloud_dir'], app.database)
db.create_recipt('Яичница',
                    ['яйца', 'кетчуп'],
                    'Вкусный рецепт приготовления')
db.create_recipt('Паста',
                    ['спагетти', 'кетчуп', 'фарш говяжий'],
                    'Жарим фарш, и варим спагетти, все смешиваем + кетчуп! Готово!')

# ---------------------------- --- --------------------------------
def get_recipts_by_my_products(my_products: list):
    recipts = []

    for recipt_id in range(1, db.get_recipts_count() + 1):
        recipt = db.get_recipt_by_id(recipt_id)
        products = recipt['products'].split(',')

        if set(products).issubset(my_products):
            recipts.append(recipt)

    return recipts

# ---------------------------- --- --------------------------------
@app.route('/')
def home():
    return 'text'
# ---------------------------- api --------------------------------
@app.route('/api/get_recipts_by_my_products', methods=['POST'])
def api_get_recipts_by_my_products():
    if not request.json or not 'my_products' in request.json:
        abort(400)

    recipts = get_recipts_by_my_products(request.json['my_products'])

    return jsonify(recipts), 201

# ---------------------------- --- --------------------------------
if __name__ == "__main__":
    if len(argv) == 2:
        app.run(host='0.0.0.0', port=int(argv[1]))
    else:
        app.run(port=8081, debug=True)