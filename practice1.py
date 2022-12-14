import sys

unique_char=[] #unique한 문자열을 받는 리스트이다.
char_count=[] #문자열이 몇 번 나온지를 받는 리스트이다.
word=[] #단어를 받는 리스트이다.
unique_word=[] #unique한 단어를 받는 리스트이다.
while True:
    try:
        filename=input("Enter the file name to read: ")
        f=open(filename,"r",encoding='utf-8')
        try:
            char=f.read()
            print("Successfully read",len(char),"characters")
            unique_c=set(char)
            print(len(unique_c),"unique characters are found:")
            print(unique_c)
            unique_char=list(unique_c)
            unique_char.sort()
            print("sorted alphabetically in ascending order")
            print(unique_char)
            for i in range(len(unique_char)):
                char_count.append(char.count(unique_char[i]))
            dic_char=dict(zip(unique_char,char_count))
            print("The count of each character :")
            print(dic_char)
            while True:
                input_word=input("Enter at least characters to find words which start with the characters: ")
                if len(input_word)>=2:
                    break
            f.close()
            f=open(filename,"r",encoding='utf-8')
            sentence=f.readlines()
            print(sentence[0])
            for i in range(sentence):
                word.extend(sentence[i].split())
            print(word)
        except:
            print("error:", sys.exc_info()[0])
            raise
        finally:
            f.close()
            break
    except IOError as err:
        print("{0}".format(err))
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
        

