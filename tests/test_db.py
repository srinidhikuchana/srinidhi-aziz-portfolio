# test_db.py
import unittest
import os
os.environ['TESTING'] = 'true'
from peewee import *
from app import *
MODELS = [TimelinePost]

test_db = SqliteDatabase(':memory:')

class TestTimelinePost(unittest.TestCase):
    def setUp(self):
        self.db_binding = test_db.bind_ctx(MODELS, bind_refs=False, bind_backrefs=False)
        self.db_binding.__enter__()
        test_db.connect()
        test_db.create_tables(MODELS)

    def tearDown(self):
        test_db.drop_tables(MODELS)
        test_db.close()
        self.db_binding.__exit__(None, None, None)

    def test_timeline_post(self):
        first_post = TimelinePost.create(name='John Doe', email='john@example.com', content='Hello world, I\'m John!')
        assert first_post.id == 1
        second_post = TimelinePost.create(name='Jane Doe', email='jane@example.com', content='Hello world, I\'m Jane!')
        assert second_post.id == 2
        posts = list(TimelinePost.select())
        assert len(posts) == 2
        assert posts[0].name == 'John Doe'
        assert posts[1].name == 'Jane Doe'
