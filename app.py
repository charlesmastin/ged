import json
import datetime

from pymongo.connection import Connection
try:
    mongo = Connection()['ged']
except:
    mongo = None

from flask import Flask, jsonify, abort, request
app = Flask(__name__)

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

@app.route('/$', methods=['GET'])
def index():
	pass

@app.route('/tasks', methods=['GET'])
def get_tasks():
	# introspect the get variables to determine time_since, intensity level, or "category"
	# return json or rendered html sheeze
	pass

@app.route('/task/<string:object_id>', methods=['GET'])
def get_task():
	# return json object or a rendered html template for the detail
	pass

@app.route('/task/<string:object_id>', methods=['PUT'])
def put_task():
	# throw her in mongo
	# validate on a form object
	# return back json? or whatever
	pass

@app.route('/task/<string:object_id>', methods=['UPDATE'])
def update_task():
	# validate on form, then update mongo object
	pass

@app.route('/task/<string:object_id>', methods=['DELETE'])
def delete_task():
	# validate nothing
	pass

if __name__ == '__main__':
	app.run()