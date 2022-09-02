a = input()
v = 0
c = 0
d = 0
w = 0
for i in a:
    if i in "aeiou" :
        v = v+1
for i in a:
    if i in ' ' :
        w = w+1
for i in a:
    if i in "1234567890":
        d = d+1
print("Vowels: {}".format(v))
print("Consonants: {}".format(len(a)-v-d-w))
print("Digits: {}".format(d))
print("White spaces: {}".format(w))