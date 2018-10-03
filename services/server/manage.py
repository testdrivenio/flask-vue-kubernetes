from flask.cli import FlaskGroup

from project import create_app, db
from project.api.models import Book


app = create_app()
cli = FlaskGroup(create_app=create_app)


@cli.command('recreate_db')
def recreate_db():
    db.drop_all()
    db.create_all()
    db.session.commit()


@cli.command('seed_db')
def seed_db():
    """Seeds the database."""
    db.session.add(Book(
        title='On the Road',
        author='Jack Kerouac',
        read=True
    ))
    db.session.add(Book(
        title='Harry Potter and the Philosopher\'s Stone',
        author='J. K. Rowling',
        read=False
    ))
    db.session.add(Book(
        title='Green Eggs and Ham',
        author='Dr. Seuss',
        read=True
    ))
    db.session.commit()


if __name__ == '__main__':
    cli()
