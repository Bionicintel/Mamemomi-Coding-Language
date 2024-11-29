# My Custom Programming Language

## Overview
**My Custom Programming Language** is a simple, easy-to-understand programming language designed to showcase basic compiler/interpreter concepts. It includes features like function definitions, conditionals, and basic arithmetic operations. 

The language uses custom keywords:
- `me` for function definitions.
- `mi` for `if` statements.
- `ma` for `else` statements.
- `mo` for `return` statements.

This project includes a lexer, parser, and interpreter written in Python. The goal is to provide a basic structure for creating a programming language from scratch and to allow others to learn and experiment with language design.

## Features
- **Function Definitions**: Use `me` to define functions with parameters.
- **Conditionals**: Use `mi` for `if` and `ma` for `else` blocks.
- **Return Statements**: Use `mo` to return values from functions.
- **Simple Arithmetic**: Supports basic operators like `+`, `-`, `*`, `/`.

## Installation

### 1. Clone the repository
Start by cloning this repository to your local machine:
```bash
git clone https://github.com/username/my-language.git
cd my-language

2. Install Python dependencies

Install any necessary dependencies (if any) by using the requirements.txt file:

pip install -r requirements.txt

Usage

To use the language, write your code in a .txt file (e.g., example.txt) and run the interpreter.

Example Usage:

	1.	Write your code in a file, for example example.txt:

me add(a, b) {
    mo a + b;
}

mi a > b {
    mo true;
} ma {
    mo false;
}

	2.	Run the code with the interpreter:

python main.py example.txt

Output:

true

This code defines a function add that returns the sum of a and b, and an if statement that checks if a > b. Based on the condition, it returns either true or false.

Language Syntax

Function Definitions

me function_name(param1, param2) {
    mo param1 + param2;
}

Conditionals

mi condition {
    mo result_if_true;
} ma {
    mo result_if_false;
}

Return Statement

mo value;

Example Program

me greet(name) {
    mo "Hello, " + name;
}

me main() {
    mo greet("World");
}

In this example, the greet function takes a name and returns a greeting string. The main function calls greet with “World”.

Project Structure

	•	lexer.py: The lexer that converts raw source code into tokens.
	•	parser.py: The parser that builds an Abstract Syntax Tree (AST) from the tokens.
	•	interpreter.py: The interpreter that executes the AST.
	•	main.py: The main entry point for running programs written in your language.
	•	examples/: A folder containing example programs written in the language.
	•	README.md: This documentation file.

Contributing

Feel free to contribute to this project! You can:
	•	Report issues or bugs.
	•	Submit pull requests with new features or bug fixes.
	•	Fork the project and create your own version.

To contribute:
	1.	Fork the repository.
	2.	Create a new branch (git checkout -b feature-name).
	3.	Commit your changes (git commit -m 'Add feature').
	4.	Push to your fork (git push origin feature-name).
	5.	Create a pull request.

License

This project is licensed under the MIT License. See the LICENSE file for more details.

Happy coding! 🎉

### Key Sections of the README:

1. **Overview**: Brief explanation of the project and its purpose.
2. **Features**: List of key features of your language.
3. **Installation**: Step-by-step instructions to set up the project locally.
4. **Usage**: Instructions on how to write and run code using your language.
5. **Language Syntax**: Overview of the syntax for defining functions, conditionals, and return statements.
6. **Project Structure**: Explanation of the directory structure and important files.
7. **Contributing**: How others can contribute to the project.
8. **License**: Information about the project's license (e.g., MIT).

### Final Steps:
- Replace `https://github.com/username/my-language.git` with your actual GitHub repository link.
- If you want to include more complex examples or details, feel free to extend the sections.