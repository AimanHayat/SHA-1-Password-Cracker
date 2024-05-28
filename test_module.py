import unittest
from password_cracker import crack_sha1_hash

class TestPasswordCracker(unittest.TestCase):
    def test_without_salts(self):
        self.assertEqual(crack_sha1_hash("b305921a3723cd5d70a375cd21a61e60aabb84ec"), "sammy123")
        self.assertEqual(crack_sha1_hash("c7ab388a5ebefbf4d550652f1eb4d833e5316e3e"), "abacab")
        self.assertEqual(crack_sha1_hash("5baa61e4c9b93f3f0682250b6cf8331b7ee68fd8"), "password")

    def test_with_salts(self):
        self.assertEqual(crack_sha1_hash("4f5c5e98173ec3b64ae5b0b5db64185d4256d78b", use_salts=True), "superman")
        self.assertEqual(crack_sha1_hash("d7f97b8e4cfebef7f01f493cf6ae109c5a76eeb4", use_salts=True), "q1w2e3r4t5")
        self.assertEqual(crack_sha1_hash("1f36d1582db64a66962de514353115485b530551", use_salts=True), "bubbles1")

    def test_not_in_database(self):
        self.assertEqual(crack_sha1_hash("aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"), "PASSWORD NOT IN DATABASE")

if __name__ == "__main__":
    unittest.main()
