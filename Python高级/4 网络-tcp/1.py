
recv_msg='111'

z='.\%s'%recv_msg
# print(z)

with open(z,'rb') as f:
    content = f.read()
    for i in content:
        print(i.decode('utf-8'))
    # print(f.readlines())
    print(content)
    print(type(content))
