from cgi import parse_qs
from templateCalc import html


def application(environ, start_response):
	ec = parse_qs(environ['QUERY_STRING'])
	
	a = ec.get('a',[''])[0]
	b = ec.get('a',[''])[0]
	
	plus,multi = 0, 0
	
	if '' not in[a,b]:
		a, b = int(a), int(b)
		plus = a + b
		multi = a * b
	response_body = html % {'plus':plus,'multi',multi}
	start_response('200 OK', [
		('Content-Type', 'text/html'),
		('Content-Length', str(len(response_body)))
	])
	return [response_body]
