import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for, jsonify
)

# from werkzeug.security import check_password_hash, generate_password_hash
# from flaskr.db import get_db

bp = Blueprint('hello', __name__, url_prefix='/hello')

@bp.route('/bonjour', methods=['GET'])
def bonjour():
    data = {
        "greeting": "hi"
    }
    return jsonify(data)

@bp.route('/hola', methods=['GET'])
def hola():
    data = {
        "greeting": "hola"
    }
    return jsonify(data)
