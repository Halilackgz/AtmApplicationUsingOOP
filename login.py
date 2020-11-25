from context import Context

def login(username,password):
    context = Context("users.txt")
    users = context.readContext()
    for i in users:

        if username == i[1] and password == i[2]:
            return list(i)
        else:
            continue
    return None
