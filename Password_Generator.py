import random

def generatePassword(pwlength):

    alphabet = "abcdefghijklmnopqrstuvwxyz"

    passwords = [] 

    for i in pwlength:
        
        password = "" 
        for j in range(i):
            next_letter_index = random.randrange(len(alphabet))
            password = password + alphabet[next_letter_index]
        
        password = replaceWithNumber(password)
        password = replaceWithUppercaseLetter(password)
        
        passwords.append(password) 
    
    return passwords


def replaceWithNumber(pword):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(pword)//2)
        pword = pword[0:replace_index] + str(random.randrange(10)) + pword[replace_index+1:]
        return pword


def replaceWithUppercaseLetter(pword):
    for i in range(random.randrange(1,3)):
        replace_index = random.randrange(len(pword)//2,len(pword))
        pword = pword[0:replace_index] + pword[replace_index].upper() + pword[replace_index+1:]
        return pword



def main():
    
    numPasswords = 2 # Remplacement du input pas 2 valeurs à tester #
    
    print("Generating " +str(numPasswords)+" passwords")
    
    passwordLengths = [8, 16] # Défini la longeur les valeurs du mdp à tester #

    print("Minimum length of password should be 3")
    
    
    Password = generatePassword(passwordLengths)

    for i in range(numPasswords):
        print ("Password #"+str(i+1)+" = " + Password[i])


if __name__ == "__main__":
    main()