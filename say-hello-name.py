def main(name=None):
    if name is None:
        print("Provide a NAME!!")
    else:
        print(f'Hello {name}!!')

main() # Without Providing a Name
main('Jonak') #Providing a Name
