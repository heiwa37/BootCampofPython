if __name__ == '__main__':
    try:
        f=open('testfile', 'w')
        f.write("I'm writing inside the file from editor using file operation from python")
        with open('testfile','r') as f:
            print(f.read())
    except:
        print("exception in the try block")

    finally:
        print("I'm the final block code")
