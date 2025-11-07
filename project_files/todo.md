Requirements:
Your interpreter should be able to:
1. Handle variable assignments:
  o Example:
    ▪ let a = 5;
    ▪ let b = a + 3;
2. Support arithmetic operations:
o Addition (+), subtraction (-), multiplication (*), and division (/) o


Example:
▪ let c = a * b;

3. Print output:
  o Use the print statement to display variable values.
  o Example:
    ▪ print(a);

4. Parse multiple statements:
  o Your program should handle multiple let and print statements, executed sequentially.

5. Handle whitespace and semicolons:
  o Statements should be separated by semicolons (;).

Project Structure:
Your project should include the following components:
  • Lexer: Tokenizes the input string into meaningful symbols like NUMBER, ID, PLUS, MINUS, MUL, etc.
  • Parser: Constructs the AST from the tokenized input.
  • AST Nodes: Represent the various constructs of the language (e.g., variable assignments, arithmetic expressions, print statements).
  • Interpreter: Visits the AST and performs the actual execution (e.g., performing arithmetic operations and printing values).
