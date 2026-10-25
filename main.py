import argparse,secrets,string

def generate_password(length=20, use_symbols=True):
    if not 12<=length<=128: raise ValueError("Length must be between 12 and 128")
    letters_digits=string.ascii_letters+string.digits
    if not use_symbols:
        return "".join(secrets.choice(letters_digits) for _ in range(length))
    symbols="!@#$%^&*()-_=+[]{}?"
    chars=[secrets.choice(letters_digits),secrets.choice(symbols)]
    alphabet=letters_digits+symbols
    chars.extend(secrets.choice(alphabet) for _ in range(length-len(chars)))
    secrets.SystemRandom().shuffle(chars)
    return "".join(chars)

def main():
    ap=argparse.ArgumentParser(); ap.add_argument("--length",type=int,default=20); ap.add_argument("--no-symbols",action="store_true"); a=ap.parse_args()
    print(generate_password(a.length,not a.no_symbols)); print("Store it in a password manager; this program does not save it.")
if __name__=="__main__": main()
