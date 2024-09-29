#HMAC SHA1
import hashlib
import hmac

def hmac_sha(key, message):
    return hmac.new(key.encode("utf-8"), message.encode("utf-8"), hashlib.sha1).hexdigest()
key = input("Enter your key: ")
message = input("Enter your message: ")
print("HMAC-SHA1 isgnature of your message is ", hmac_sha(key,message))