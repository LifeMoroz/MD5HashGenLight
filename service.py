import hashlib

import requests


class HashProcessor:
    chunk_size = 4096
    hash_func = None

    @classmethod
    def get_hasher(cls):
        if not cls.hash_func:
            raise ValueError('You must specify hash function in `hash_func` attr')
        return cls.hash_func()

    def _download_url(self, url):  # Just to simplify mocking in tests
        return requests.get(url, timeout=(1, 10))

    def get_hash_for_url(self, url):
        response = self._download_url(url)

        hasher = self.get_hasher()
        for chunk in response.iter_content(self.chunk_size):
            hasher.update(chunk)

        return hasher.hexdigest()


class MD5HashProcessor(HashProcessor):
    hash_func = hashlib.md5


class SHA1Processor(HashProcessor):
    hash_func = hashlib.sha1
