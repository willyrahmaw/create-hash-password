import random

random.seed(42) #jangan ganti bila tidak terlalu mengerti

def banner():
    print('''
██╗  ██╗ █████╗ ███████╗██╗  ██╗    ██████╗  █████╗ ███████╗███████╗██╗    ██╗ ██████╗ ██████╗ ██████╗     
██║  ██║██╔══██╗██╔════╝██║  ██║    ██╔══██╗██╔══██╗██╔════╝██╔════╝██║    ██║██╔═══██╗██╔══██╗██╔══██╗    
███████║███████║███████╗███████║    ██████╔╝███████║███████╗███████╗██║ █╗ ██║██║   ██║██████╔╝██║  ██║    
██╔══██║██╔══██║╚════██║██╔══██║    ██╔═══╝ ██╔══██║╚════██║╚════██║██║███╗██║██║   ██║██╔══██╗██║  ██║    
██║  ██║██║  ██║███████║██║  ██║    ██║     ██║  ██║███████║███████║╚███╔███╔╝╚██████╔╝██║  ██║██████╔╝    
╚═╝  ╚═╝╚═╝  ╚═╝╚══════╝╚═╝  ╚═╝    ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝ ╚══╝╚══╝  ╚═════╝ ╚═╝  ╚═╝╚═════╝     
                                                                                                           
                    ██████╗ ██╗   ██╗    ██╗    ██╗██████╗ ██╗    ██╗                                      
                    ██╔══██╗╚██╗ ██╔╝    ██║    ██║██╔══██╗██║    ██║                                      
                    ██████╔╝ ╚████╔╝     ██║ █╗ ██║██████╔╝██║ █╗ ██║                                      
                    ██╔══██╗  ╚██╔╝      ██║███╗██║██╔══██╗██║███╗██║                                      
                    ██████╔╝   ██║       ╚███╔███╔╝██║  ██║╚███╔███╔╝                                      
                    ╚═════╝    ╚═╝        ╚══╝╚══╝ ╚═╝  ╚═╝ ╚══╝╚══╝                                       
                                                                                                           
''')

def generate_custom_encoding():
    base_words = ['willy', 'rahma', 'wijaya', 'rw', 'wr','wrw'] #ganti dengan kebutuhan anda
    custom_encoding = {}
    characters = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()-_=+[]{};:'\",.<>/?|"
    
    for index, char in enumerate(characters):
        encoded_value = base_words[index % len(base_words)] + str(100 + index) + base_words[(index + 1) % len(base_words)]
        custom_encoding[char] = encoded_value
    
    for year in range(2000, 2100):
        encoded_value = base_words[year % len(base_words)] + str(year) + base_words[(year + 1) % len(base_words)]
        custom_encoding[str(year)] = encoded_value
    
    return custom_encoding

custom_encoding = generate_custom_encoding()
reverse_encoding = {v: k for k, v in custom_encoding.items()}

def encrypt_password(password: str) -> str:
    encrypted_chars = [custom_encoding.get(char, 'XXXXX') for char in password]
    return ' '.join(encrypted_chars)

def decrypt_password(encrypted_password: str) -> str:
    words = encrypted_password.split(' ')
    decrypted_chars = [reverse_encoding.get(word, '?') for word in words]
    return ''.join(decrypted_chars)

def main():
    banner()
    print("1. Enkripsi Password")
    print("2. Dekripsi Password")
    pilihan = input("Pilih opsi (1/2): ")
    
    if pilihan == '1':
        password = input("Masukkan password: ")
        encrypted = encrypt_password(password)
        print(f"Password terenkripsi: {encrypted}")
    elif pilihan == '2':
        encrypted_password = input("Masukkan password terenkripsi: ")
        decrypted = decrypt_password(encrypted_password)
        print(f"Password terdekripsi: {decrypted}")
    else:
        print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
