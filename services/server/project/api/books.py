import os

from flask import Blueprint, jsonify, request

from project.api.models import Book
from project import db


books_blueprint = Blueprint('books', __name__)


@books_blueprint.route('/books', methods=['GET', 'POST'])
def all_books():
    response_object = {
        'status': 'success',
        'container_id': os.uname()[1]
    }
    if request.method == 'POST':
        post_data = request.get_json()
        title = post_data.get('title')
        author = post_data.get('author')
        read = post_data.get('read')
        db.session.add(Book(title=title, author=author, read=read))
        db.session.commit()
        response_object['message'] = 'Book added!'
    else:
        response_object['books'] = [book.to_json() for book in Book.query.all()]
    return jsonify(response_object)


@books_blueprint.route('/books/ping', methods=['GET'])
def ping():
    return jsonify({
        'status': 'success',
        'message': 'pong!',
        'container_id': os.uname()[1]
    })


@books_blueprint.route('/books/<book_id>', methods=['PUT', 'DELETE'])
def single_book(book_id):
    response_object = {
      'status': 'success',
      'container_id': os.uname()[1]
    }
    book = Book.query.filter_by(id=book_id).first()
    if request.method == 'PUT':
        post_data = request.get_json()
        book.title = post_data.get('title')
        book.author = post_data.get('author')
        book.read = post_data.get('read')
        db.session.commit()
        response_object['message'] = 'Book updated!'
    if request.method == 'DELETE':
        db.session.delete(book)
        db.session.commit()
        response_object['message'] = 'Book removed!'
    return jsonify(response_object)


if __name__ == '__main__':
    app.run()
