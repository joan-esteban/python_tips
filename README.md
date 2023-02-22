# Python Tips

This is a CVS where to keep code fragments that I may need in the future

## Make a https server with no extra package
```
from http.server import BaseHTTPRequestHandler, HTTPServer
import ssl
# Generating key:  https://serverfault.com/a/366374/504134
# openssl req  -nodes -new -x509  -keyout server.key -out server.cert

class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):

    def do_GET(self):
        print("do_Get")
        self.send_response(200)
        self.end_headers()
        self.wfile.write(b'Hello, world!')
    def do_POST(self):
        print("do_POST")

httpd = HTTPServer(("0.0.0.0", 443), SimpleHTTPRequestHandler)

httpd.socket = ssl.wrap_socket (httpd.socket,
        keyfile="./server.key",
        certfile='./server.cert', server_side=True)

httpd.serve_forever()
```

## Make a class serializable to JSON
Check stackoverflow answer here: https://stackoverflow.com/questions/3768895/how-to-make-a-class-json-serializable

🚨 If you need serialization but don't need to be in json format you could use: [pickle](https://docs.python.org/3/library/pickle.html)

The steps are:
- Change the Json Encoder function for our own version, that first try to use `to_json` function if exists, if not call the default Enconder
- Each class that we want to be serializable must implement `to_json` method

You must execute this code before a class definition
```
from json import JSONEncoder

#https://stackoverflow.com/questions/3768895/how-to-make-a-class-json-serializable
def _default(self, obj):
    return getattr(obj.__class__, "to_json", _default.default)(obj)

_default.default = JSONEncoder().default
JSONEncoder.default = _default
```

After that you could create class with the method `to_json` that must return a dict
```
class MyClass:
    def __init__(self):
        self.field1 = 1234
        self.field2 = "1234"
   
       def to_json(self):
        return self.__dict__
```
## Create 'functional' attributes 
Sometimes your class are going to have some field that could be calculated you can use decorator `@property`

```
class MyClass:
    def __init__(self,h , w):
        self.height = h
        self.width = w
   @property
   def area():
        return self.height * self.width
```


## Run-time PEP 498: Formatted string literals
- Since Python 3.6 there are a new way to format string prefixing with f"name variable in context is equal to {name}"
- How to do that reading data from a file?
```
a=4
s="a={a}"
ss=eval(f'f"{s}"')
print(ss)
```

This is a code snippet to apply to a entire variable:
```
    def var_sustitution(self,data):
        if isinstance(data, dict):
            new_data = {}
            for k in data.keys():
                v = data[k]
                if isinstance(v,str):
                    v = eval(f'f"{v}"')
                else:
                    v = self.var_sustitution(v)
                new_data[k] = v
            return new_data
        elif isinstance(data, list):
            new_data = []
            for v in data:
                if isinstance(v,str):
                    v = eval(f'f"{v}"')
                else:
                    v = self.var_sustitution(v)
                new_data.append(v)
            return new_data
        else:
            v = data
            v = eval(f'f"{v}"')
            return v
```
- Refs:
   - [PEP498](https://docs.python.org/3/whatsnew/3.6.html#whatsnew36-pep498)
   - [stackoverflow:How do I convert a string into a formatted string literal at run-time?] (https://stackoverflow.com/questions/49852860/how-do-i-convert-a-string-into-a-formatted-string-literal-at-run-time)
