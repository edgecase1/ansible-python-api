#/usr/bin/env python3


import crypt
import random
import string



def gen_password(pw_len):
    password = ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(pw_len))

    # python2
    #print crypt.crypt(password, "$6$random_salt")'
    # python3
    return password, crypt.crypt(password, crypt.mksalt(crypt.METHOD_SHA512))


print(gen_password(12))
