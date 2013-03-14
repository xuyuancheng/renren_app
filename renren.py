import web

urls= (
	"/.*","hello",
)

app=web.application(urls,globals())

class hello:
	def GET(self):
		return "Hello, world!"

app = app.cgirun()
