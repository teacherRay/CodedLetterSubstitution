# Letter substuition to crack encoded message 9 Nov 19

#object: change letter to letter 2 places further along in alphabet. For example,
# a in encoded string becomes c in uncoded string
# b in encoded string becomes d in uncoded string
# c in encoded string becomes e in uncoded string
# ....etc...
# uncoded: a b c d e f g h i j k l m n o p q r s t u v w x y z
# encoded: y z a b c d e f g h i j k l m n o p q r s t u v w x

# The program will translate a coded string into a readable sentence.
# g jmtc nwrfml = i love python
encoded = {'a':'c', 'b':'d', 'c':'e', 'd':'f', 'e':'g', 'f':'h', 'g':'i', 'h':'j', 'i':'k', 'j':'l', 'k':'m', 'l':'n', 'm':'o', 'n':'p', 'o':'q', 'p':'r', 'q':'s', 'r':'t', 's':'u', 't':'v', 'u':'w', 'v':'x', 'w':'y', 'x':'z', 'y':'b' , 'z': 'c' }
print(encoded['x']) # prints uncoded 'z'