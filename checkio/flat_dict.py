def flatten(dictionary):
    stack = [((), dictionary)]
    result = {}
    while stack:
        path, current = stack.pop()
        if current == {}:
            result["/".join(path)] = ''
        else:
            for k, v in current.items():
                if isinstance(v, dict):
                    stack.append((path + (k,), v))
                    print(stack)
                else:
                    result["/".join((path + (k,)))] = v
    return result
    
print(flatten( {"key": {"deeper": {"more": {"enough": "value"}}}}))
print(flatten( {"empty": {}}))