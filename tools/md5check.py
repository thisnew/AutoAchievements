import hashlib

def MD5Check(file):
    md5_value = hashlib.md5()
    with open(file,"rb") as file:
        while True:
            data =  file.read(2048)
            if not data:
                break
            md5_value.update(data)
    return  md5_value.hexdigest()


def hashs(fineName, type="sha256", block_size=64 * 1024):
    """ Support md5(), sha1(), sha224(), sha256(), sha384(), sha512(), blake2b(), blake2s(),
    sha3_224, sha3_256, sha3_384, sha3_512, shake_128, and shake_256
    """
    with open(fineName, 'rb') as file:
        hash = hashlib.new(type, b"")
        while True:
            data = file.read(block_size)
            if not data:
                break
            hash.update(data)
        return hash.hexdigest()
