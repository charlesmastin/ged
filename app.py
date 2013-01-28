import json
import datetime
from bson import BSON
from bson import json_util
from bson.objectid import ObjectId

from wtforms import *

from pymongo.connection import Connection
try:
    mongo = Connection()['ged']
except:
    mongo = None

from flask import Flask, jsonify, abort, request, render_template
app = Flask(__name__)
app.config['DEBUG'] = True

"""
Schema

collection.tasks

_id: ObjectId
name: String
description: String (optional)
due_date: DateTime (optional)
origin: String (optional)
url: relevant origin
image: relevant image attachment
intensity: Int (1, 2, 3, 4, 5), default 3
created_at: DateTime
completed_at: DateTime
dismiss: Boolean (mark as inactive/deferred)
tags: related objects from tag db
difficulty: 'easy', 'normal', 'hardcore'

collection.origin

_id: ObjectId
name: String
some cred/auth info
webhook something, api something

"""

class TaskForm(Form):
	name = TextField('Name', [validators.Length(min=3, max=25), validators.Required()])
	description = TextAreaField()
	due_date = DateField()
	#intensity = IntegerField()
	#difficulty = SelectField(choices=[('easy', 'easy'), ('normal', 'normal'), ('hardcore', 'hardcore')])

@app.route('/', methods=['GET'])
def index():
	# json_util.dumps(mongo.tasks.find({})[:])
	return render_template('index.html', tasks=mongo.tasks.find({'completed_at': {"$exists": False}}))

@app.route('/tasks', methods=['GET'])
def get_tasks():
	# introspect the get variables to determine time_since, intensity level, or "category"
	# return json or rendered html sheeze
	tasks = mongo.tasks.find()

	pass

@app.route('/task/<string:object_id>', methods=['GET'])
def get_task():
	# return json object or a rendered html template for the detail
	pass

@app.route('/task', methods=['PUT'])
def put_task():
	# form = TaskForm(request.form)
	# throw her in mongo
	# validate on a form object
	# return back json? or whatever
	data = json.loads(request.data)
	_id = mongo.tasks.insert(data)
	return jsonify(id=str(_id))

@app.route('/task/complete', methods=['UPDATE'])
def complete_task():
	#import pdb
	#pdb.set_trace()
	data = json.loads(request.data)
	"""
	task = mongo.tasks.find_one({'_id': ObjectId(str(data['id']))})
	task['completed_at'] = datetime.datetime.now()
	mongo.tasks.update(task)
	"""
	mongo.tasks.update({'_id': ObjectId(data['id'])}, {"$set": {'completed_at': datetime.datetime.now()}})
	return jsonify(result={'success': True})

@app.route('/task', methods=['UPDATE'])
def update_task():
	data = json.loads(request.data)
	_id = data['id']
	del data['id']
	mongo.tasks.update({'_id': ObjectId(_id)}, {"$set": data})
	return jsonify(result={'success': True})

@app.route('/task', methods=['DELETE'])
def delete_task():
	# validate nothing
	pass

if __name__ == '__main__':
	app.run()