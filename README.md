# Compiler For C

Compiler For C is a lexical analyzer for a subset of the C language, designed to identify and categorize tokens from a C source file. The project is implemented in Python, aiming to illustrate the structure and functionality of a simplified compiler, focusing on the tokenization phase.

## Features

- Recognizes common C keywords like `int`, `string`, `if`, `else`, `return`, `scanf`, `printf`, and `float`.
- Identifies arithmetic and logical operators: `+`, `++`, `-`, `--`, `*`, `/`, `%`, `=`, `==`, `!=`, `<`, `>`, `<=`, `>=`, `&&`, `||`, `!`, `&`.
- Delimits separators: `(`, `)`, `{`, `}`, `,`, `;`, `[`, `]`.
- Supports preprocessor directives (e.g., `#include`).
- Ignores comments of the form `//` and `/* ... */`.
- Recognizes various token types such as identifiers, integers, decimal numbers, strings, and comments.
- Manages lexical errors for unrecognized characters.

## Project Structure

- `main.py`: The main Python script containing the code for tokenizing a C file. It reads the file `input.c` and outputs all identified tokens, including information about the token type, line, length, and starting position.
- `input.c`: A test file containing C code to test the capabilities of the lexical analyzer.

## How It Works

The `main.py` script, written in Python, uses a `tokenize` function to sequentially parse the source file and identify tokens based on predefined rules. These tokens are then output with relevant details, including their type, length, and line number.

### Steps in Tokenization

1. Whitespace and newlines (ignored).
2. Preprocessor directives (marked as "preprocessor directive").
3. Keywords and identifiers.
4. Integers and decimal numbers.
5. Strings, including multi-line strings and escape sequences.
6. Comments of type `//` and `/* ... */` (ignored in lexical analysis).
7. Recognized operators and separators.
8. Lexical error handling for unknown characters.

