def swap():

    path1 = input("Enter first file path: ")
    path2 = input("Enter second file path: ")

    with open(path1,'r') as f1:
        text1 = f1.read()

    with open(path2,'r') as f2:
        text2 = f2.read()


    with open(path1,'w') as f1:
        f1.write(text2)

    with open(path2,'w') as f2:
        f2.write(text1)

swap()