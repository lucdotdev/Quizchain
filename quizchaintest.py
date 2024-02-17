


def main():

    try:
        with open('second.txt', 'r') as file:
            text = file.read()

            dictt = text.split(' ')

        print( f'{len(dictt)}')
        return text
    

    except FileNotFoundError:
       
        return None


main()