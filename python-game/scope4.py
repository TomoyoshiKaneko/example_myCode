message = "Hello"

def say():
    global message
    message = 'Hi'
    print("say:message"+message)
    obj_id = id(message)
    print("say:id(message)={:}".format(obj_id))

def main():
    say()
    print("main:massage"+message)
    obj_id = id(message)
    print("main:id(message)={0:d}".format(obj_id))

if __name__ == '__main__':
    main()
