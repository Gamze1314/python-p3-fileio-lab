def write_file(file_name, file_content):
    # Open the file in write mode with utf-8 encoding, 'with' closes the file automatically.
    with open(f'{file_name}.txt', mode='w', encoding='utf-8') as file:
        # Write the content to the file
        file.write(file_content)


def append_file(file_name, append_content):
    with open(f'{file_name}.txt', mode='a' , encoding='utf-8') as file:
        return file.write(append_content)

def read_file(file_name):
    with open(f'{file_name}.txt', mode='r', encoding='utf-8') as file:
        return file.read()

