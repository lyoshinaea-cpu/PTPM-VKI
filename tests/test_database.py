import unittest

from src.database import Database


class TestDatabase(unittest.TestCase):

    def setUp(self):
        self.db = Database(":memory:")

    def tearDown(self):
        self.db.close()

    def test_delete_existing_record(self):
        self.db.add_record(
            3, 4, 5, "разносторонний", None
        )

        result = self.db.delete_record(3, 4, 5)

        self.assertTrue(result)
        self.assertIsNone(
            self.db.get_record(3, 4, 5)
        )

    def test_delete_nonexistent_record(self):
        result = self.db.delete_record(10, 20, 30)

        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
