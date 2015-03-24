# Generate Unique WebID
class WebIdGenerator(object):
	"""
	This is a middleware class that produces a unique id
	"""

	def __init__(self, static_index):
		self.index = 0
		self.static_index = static_index

	def __call__(self):
	    # we generate the guid late because many requests don't need one
	    self.index += 1
	    return 'g%sh%s' % (self.static_index, self.index)

# MyMiddleware class used in Middleware for my app
class MyMiddleware:
	"""
	Attaches a web-valid guid generator to each request
	"""
	def __init__(self):
		self.generator = self.get_next()
		self.static_index = 0

	def get_next(self):
	    while True:
	        # create the next unique id and yield it
	        yield self.static_index 
	        self.static_index += 1

	def process_request(self, request):
		# add the generator to the request
		request.get_webid = WebIdGenerator(next(self.generator))


# For testing
if __name__ == "__main__":
	md = MyMiddleware()
	print(md.get_next_id())
	print(md.get_next_id())
	print(md.get_next_id())