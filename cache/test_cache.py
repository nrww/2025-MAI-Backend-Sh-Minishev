from cache import LRUCache

cache = LRUCache(2)
cache.set('Jesse', 'Pinkman')
cache.set('Walter', 'White')
cache.set('Jesse', 'James')
assert cache.get('Jesse') == 'James'
cache.rem('Walter')
assert cache.get('Walter') == ''
print("pass")