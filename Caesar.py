def rot13(mess):
    In = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
    Out = 'NOPQRSTUVWXYZABCDEFGHIJKLMnopqrstuvwxyzabcdefghijklm'
    rot = str.maketrans(In,Out)
    translation = mess.translate(rot)
    # print (translation)
    return translation


