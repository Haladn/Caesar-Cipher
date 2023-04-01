def caesarCipher(s, k):
    # Write your code here

    uppercase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',\
                'N', 'O', 'P', 'Q', 'R', 'S', 'T','U', 'V', 'W', 'X', 'Y', 'Z']
    lowercase = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n',\
                'o', 'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z']

    crypting = ""
    for i in range(len(s)):
        if s[i] in uppercase:
            inde = uppercase.index(s[i])
            crypt = (inde + k) % 26
            crypting += uppercase[crypt]
        elif s[i] in lowercase:
            inde = lowercase.index(s[i])
            crypt = (inde + k) % 26
            crypting += lowercase[crypt]
        else:
            crypting += s[i]
    return crypting

s="middle-Outz"
k=2

#result is "okffng-Qwvb"
if __name__=="__main__":
    print(caesarCipher(s,k))
