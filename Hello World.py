def msg_contain(hello_msg: str, world_msg: str):
    real_msg = hello_msg + ", " + world_msg + "!"
    return real_msg

hello = ""
world = ""
msg = ""
	
hello = "Hello"
world = "World"
msg = msg_contain(hello, world)

for i in range(5):
    print(msg)
