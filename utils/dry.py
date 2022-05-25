def cut(pathname):
    head, *tail = pathname.strip('/').split('/')
    tailname = '/'.join(tail)
    return head, tailname