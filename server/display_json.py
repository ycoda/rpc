def custom_format_display(method, params, param_types, request_id):
    print("Received request:")
    print("{")
    print(f'    "method": "{method}",')
    print(f'    "params": {params},')
    print(f'    "param_types": {param_types},')
    print(f'    "id": {request_id}')
    print("}")  