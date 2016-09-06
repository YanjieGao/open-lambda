def handler(conn, event):
    try:
        return "Hello, %s!\n" % event['name']
    except Exception as e:
        return {'error': str(e)} 
