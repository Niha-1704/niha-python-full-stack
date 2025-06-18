import json
inp = '{"name":"Alice","age":30}'
res = json.loads(inp)
print(res)
print(type(res))
res = json.dumps(inp)
print(res)
print(type(res))