from cryptography.fernet import Fernet

def main():
    key = Fernet.generate_key()

    file_name = input("Enter the filename of your key: ")

    if file_name.find(".") == -1:
        file_name += ".key"

    try:   
        with open(file_name, "wb") as key_file:
            key_file.write(key)
        print(f"Generated key saved to {file_name}")
        
    except FileNotFoundError as error:
        print(error)
          
if __name__ == "__main__":
    main()