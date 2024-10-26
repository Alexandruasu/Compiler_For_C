keywords = {"int", "string", "if", "else", "return", "scanf", "printf", "float"}
operators = {"+", "++", "-", "--", "*", "/", "%", "=", "==", "!=", "<", ">", "<=", ">=", "&&", "||", "!", "&"}
separators = {"(", ")", "{", "}", ",", ";", "[", "]"}

def tokenize(file_content):
    pointer = 0
    current_line = 1
    tokens = []
    
    while pointer < len(file_content):
        while pointer < len(file_content) and file_content[pointer] in {' ', '\t', '\n'}:
            if file_content[pointer] == '\n':
                current_line += 1
            pointer += 1
        
        if pointer >= len(file_content):
            break

        start_pointer = pointer  

        if file_content[pointer] == '#':
            start_pointer = pointer
            pointer += 1
            while pointer < len(file_content) and file_content[pointer] != '\n':
                pointer += 1
            token = file_content[start_pointer:pointer]
            tokens.append((token, current_line, "preprocessor directive", pointer - start_pointer, start_pointer))

        elif file_content[pointer].isalpha() or file_content[pointer] == '_':
            while pointer < len(file_content) and (file_content[pointer].isalnum() or file_content[pointer] == '_'):
                pointer += 1
            token = file_content[start_pointer:pointer]
            token_type = "keyword" if token in keywords else "identifier"
            tokens.append((token, current_line, token_type, pointer - start_pointer, start_pointer))
        
        elif file_content[pointer].isdigit():
            while pointer < len(file_content) and file_content[pointer].isdigit():
                pointer += 1
            if pointer < len(file_content) and file_content[pointer] == '.':
                pointer += 1
                while pointer < len(file_content) and file_content[pointer].isdigit():
                    pointer += 1
            tokens.append((file_content[start_pointer:pointer], current_line, "number", pointer - start_pointer, start_pointer))
        
        elif file_content[pointer] == '"':
            start_line = current_line  
            pointer += 1
            start_pointer = pointer
            while pointer < len(file_content) and file_content[pointer] != '"':
                if file_content[pointer] == '\\':  
                    if pointer + 1 < len(file_content) and file_content[pointer + 1] == '\n': 
                        current_line += 1
                        pointer += 2
                    else:
                        pointer += 2
                else:
                    if file_content[pointer] == '\n':
                        current_line += 1
                    pointer += 1
            token = file_content[start_pointer:pointer]
            pointer += 1  
            tokens.append((token, start_line, "string", pointer - start_pointer, start_pointer))  
        
        elif file_content[pointer] == '/' and pointer + 1 < len(file_content) and file_content[pointer + 1] == '/':
            start_pointer = pointer
            pointer += 2  
            while pointer < len(file_content) and file_content[pointer] != '\n':
                pointer += 1
            tokens.append((file_content[start_pointer:pointer].strip(), current_line, "comment", pointer - start_pointer, start_pointer))
        
        elif file_content[pointer] == '/' and pointer + 1 < len(file_content) and file_content[pointer + 1] == '*':
            pointer += 2  
            start_pointer = pointer
            start_line = current_line  
            while pointer + 1 < len(file_content) and (file_content[pointer] != '*' or file_content[pointer + 1] != '/'):
                if file_content[pointer] == '\n': 
                    current_line += 1
                pointer += 1
            pointer += 2  
            
            comment_text = file_content[start_pointer:pointer-2]  
            tokens.append((comment_text, start_line, "comment", len(comment_text), start_pointer))
        
        elif file_content[pointer] in operators:
            if pointer + 1 < len(file_content) and file_content[pointer:pointer + 2] in operators:
                tokens.append((file_content[pointer:pointer + 2], current_line, "operator", 2, start_pointer))
                pointer += 2
            else:
                tokens.append((file_content[pointer], current_line, "operator", 1, start_pointer))
                pointer += 1
        
        elif file_content[pointer] in separators:
            tokens.append((file_content[pointer], current_line, "separator", 1, start_pointer))
            pointer += 1
        
        elif file_content[pointer] in {'#', '&', '.', '<', '>'}:
            tokens.append((file_content[pointer], current_line, "operator", 1, start_pointer))
            pointer += 1
        
        else:
            token = file_content[pointer]
            print(f'Eroare lexicală la linia {current_line}, caracter necunoscut: "{token}" la poziția {start_pointer}')
            tokens.append((token, current_line, "lexical error", 1, start_pointer))
            pointer += 1

    return tokens

def analyze_file(file_name):
    with open(file_name, 'r') as f:
        file_content = f.read()
    
    tokens = tokenize(file_content)
    
    for token, line, token_type, length, start_pointer in tokens:
        print(f'Token: "{token}", Line: {line}, Type: {token_type}, Length: {length}, Pointer: {start_pointer}')

if __name__ == "__main__":
    analyze_file("input.c")
