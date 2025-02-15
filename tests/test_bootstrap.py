import unittest
from ksoft.core.bootstrap import init_db
from ksoft.core.database import get_db
from ksoft.api.models import Base
from ksoft.core.bootstrap import engine

class TestBootstrap(unittest.TestCase):
    def setUp(self):
        """Setup test database"""
        Base.metadata.drop_all(bind=engine)
        Base.metadata.create_all(bind=engine)

    def tearDown(self):
        """Cleanup test database"""
        Base.metadata.drop_all(bind=engine)

    def test_init_db(self):
        """Test database initialization"""
        init_db()
        db = next(get_db())
        self.assertIsNotNone(db)
        db.close()

if __name__ == "__main__":
    unittest.main()
