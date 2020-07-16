import re
def rot13(mess):
    '''Takes a string a turns it into a rot13 cipher encrypted string'''
    In ="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    Out = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    rot = str.maketrans(In,Out)
    message = mess
    print (message.translate(rot))


def deRot13(mess):
    '''Takes a rot13 message/string and decrypts it.'''
    In ="ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
    Out = "NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm"
    rot = str.maketrans(Out,In)
    message = mess
    print (message.translate(rot))



