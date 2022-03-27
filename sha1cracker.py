import hashlib

def convert_text_to_sha1(text):
    digest = hashlib.md5(
        text.encode()
    ).hexdigest()

    return digest

def main():
    user_sha1 = input("Enter the SHA1 to Crack: ")
    clean_user_sha1 = user_sha1.strip().lower()
    with open('./passwords.txt') as f:
        for line in f:
            password = line.strip()
            converted_sha1 = convert_text_to_sha1(password)

            if clean_user_sha1 == converted_sha1:
                print(f"Password Found: {password}")
                return
    print("could not find password")
