# -*- coding: utf-8 -*-
"""
Created on Mon Jun  8 17:17:33 2020

@author: Michał Gutowski
"""

from flask import Flask, request, jsonify, abort, make_response
app= Flask(__name__)
app.config['JSON_SORT_KEYS'] = False

lego_set_database={
        '75192':{
                'name':'Millennium Falcon - UCS',
                'year':2017,
                'bricks_number':7513,
                'minifigs_number':8,
                'theme':'Star Wars'
                },
        '10256':{
                'name':'Taj Mahal (Reissue)',
                'year':2017,
                'bricks_number':5923,
                'minifigs_number':0,
                'theme':'Creator'
                }
        }
@app.route('/')
def HelloWorld():
    return "Strona startowa, dzień dobry"
@app.route('/sets',methods=['GET','POST'])
def no_uri():
    if request.method=='GET':
        sets_list=[]
        for set in lego_set_database:
            sets_list.append(set)
        return jsonify(sets_list)
    
    if request.method=='POST':
        if not request.json or 'set_id' not in request.json:
            abort(400)
        set_id=request.json['set_id'].split(':')
        if len (set_id)==0 or len (set_id)>1: 
            abort(400)
        else:
            if set_id[0] in lego_set_database:
                abort(400)
            else:
                new_set={'name':None,'year':None,'bricks_number':None,'minifigs_number':None,'theme':None}
                lego_set_database[set_id[0]]=new_set        
                return jsonify({set_id[0]: new_set}), 201
@app.route('/sets/<string:id>',methods=['PUT','DELETE','GET'])
def question(id):
     set_id=id.split(':')
     
     if request.method=='GET':
        if len(set_id)==1:
            if set_id[0] in lego_set_database:
                return jsonify({set_id[0]:lego_set_database[set_id[0]]})
            else:
               abort(404)
               
     if request.method=='DELETE':
        if len (set_id)==0 or len (set_id)>1: 
            abort(400)
        else:
            if not set_id[0] in lego_set_database:
                abort(404)
            else:
                del lego_set_database[set_id[0]]
                return jsonify({'result': True})
            
     if request.method=='PUT':
         if not request.json and 'name' and 'year' and 'bricks_number' and 'minifigs_number' and 'theme'not in request.json:
             abort(400)
         if not set_id[0] in lego_set_database:
                abort(404)
         data=request.get_json()
         lego_set_database[set_id[0]]=data        
         return jsonify({set_id[0]: data}), 201
@app.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Page not found :('}), 404)
@app.errorhandler(400)
def bad_request(error):
    return make_response(jsonify({'error': 'Bad request :('}), 400)
if __name__=='__main__':
    app.debug=True
    app.run(host='0.0.0.0', port=5000)