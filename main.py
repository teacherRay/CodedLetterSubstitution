#python challenge 1
print (2 ** 38) # 2 to the power of 38

#python challenge 2
# Letter substiution to crack encoded message 9 Nov 19

#object: change letter to letter 2 places further along in alphabet. For example,
# a in encoded string becomes c in uncoded string
# b in encoded string becomes d in uncoded string
# c in encoded string becomes e in uncoded string
# ....etc...
# uncoded: a b c d e f g h i j k l m n o p q r s t u v w x y z
# encoded: y z a b c d e f g h i j k l m n o p q r s t u v w x

# The program will translate a coded string into a readable sentence.
# g jmtc nwrfml = i love python
encoded = {'a':'c', 'b':'d', 'c':'e', 'd':'f', 'e':'g', 'f':'h', 'g':'i', 'h':'j', 'i':'k', 'j':'l', 'k':'m', 'l':'n', 'm':'o', 'n':'p', 'o':'q', 'p':'r', 'q':'s', 'r':'t', 's':'u', 't':'v', 'u':'w', 'v':'x', 'w':'y', 'x':'z', 'y':'a' , 'z': 'b', ' ':' ', '.':'.', ':':':', '/':'/', '(':'(' , ')':')' }
#print(encoded['x']) # prints uncoded 'z'

message = ('')
encodedword ="g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyrq ufw rfgq rcvr gq qm jmle. sqgle rpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."
for letter in encodedword:
    message = message + (encoded[letter])

#print(message)    

outtab = "abcdefghijklmnopqrstuvwxyz"
intab = "yzabcdefghijklmnopqrstuvwx"
trantab = str.maketrans(intab, outtab)

str = "g fmnc wms bgblr rpylqjyrc gr zw fylb. rfyrq ufyr amknsrcpq ypc dmp. bmgle gr gl zw fylb gq glcddgagclr ylb rfyrq ufw rfgq rcvr gq qm jmle. sqgle qrpgle.kyicrpylq() gq pcamkkclbcb. lmu ynnjw ml rfc spj."

#str = "http://www.pythonchallenge.com/pc/def/map.html"
print (str.translate(trantab))