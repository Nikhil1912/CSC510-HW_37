from Utils import TestError

def canPrint(content, mess):
    try:
        print(content)
    except:
        raise TestError(mess)
