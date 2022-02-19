import hashlib
import os
import sys
import datetime


startTime = datetime.datetime.now()

def error(msg):
    print ("[!]  . " + msg)
 
def errorExit(msg) :
    raise SystemExit("[!] - " + msg)

def md5(string) :
    return hashlib.md5(string.encode()).hexdigest()

def xpermutation(characters,size):
    if size == 0:
        yield []
    else:
        for x in range(len(characters)):
            for y in xpermutation(characters[:x] + characters[x:] , size - 1):
                yield [characters[x]] + y
def bruteForce(hash):
    attempt = 0
    characters = list("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
    maxLength = range(0,25)
    stringBuilder = ''
    for length in maxLength:
        for x in xpermutation(characters,length):
            permutation = stringBuilder + ''.join(x)
            attempt = attempt + 1
            if md5(permutation) == hash:
                end_time = str(datetime.datetime.now() - startTime).split('.')[0]
                print ('[' + str(attempt) + ' - ' + permutation + '  CRACKED!  ' + end_time)
                input('\n press <ENTER> to EXIT...')
                sys.exit()
            else:
                print ('[' + str(attempt) + '] - ' + permutation)
    errorExit('MD% Crack Failed.')

if os.name == 'nt' : os.system('cls')
else: os.system('clear')


if len(sys.argv) == 2:
    if len(sys.argv[1]) == 32 and sys.argv[1].isalnum():
        bruteForce(sys.argv[1])
    else:
        error('Invalid MD5 hash:')
        errorExit('Usage - python md5 crack by [HASH]')
else:
    error('Neccessary argurments not found.')
    errorExit('Usage - python md5 crach by [HASH]')