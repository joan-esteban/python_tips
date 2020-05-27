# Python Tips

This is a CVS where to keep code fragments that I may need in the future

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
   - [stackoverflow] (How do I convert a string into a formatted string literal at run-time?)
