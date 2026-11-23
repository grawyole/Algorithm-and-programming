#Algorithm Types in Programming

In computer science and programming, algorithms describe step-by-step logic used to solve problems. Most algorithms are built around three fundamental control structures: **Linear (Sequential)**, **Branching (Conditional)**, and **Circular (Iterative)**.

---

## 1. Linear Algorithm (Sequential)

A **linear algorithm** executes instructions sequentially, one after another, strictly from top to bottom. Every line of code runs exactly once, and there are no choices or repetitions involved.

* **Characteristics:** Simple, predictable, and single-path.
* **When to use:** Performing a series of independent actions where order matters, such as basic calculations or simple data conversions.

### Example: Converting Celsius to Fahrenheit
1. Ask the user for the temperature in Celsius ($C$).
2. Calculate Fahrenheit using the formula: $F = (C \times 1.8) + 32$.
3. Display $F$ to the user.

```python
celsius = float(input("Enter temperature in Celsius: "))
fahrenheit = (celsius * 1.8) + 32
print(f"Temperature in Fahrenheit: {fahrenheit}")
```

---

## 2. Branching Algorithm (Conditional / Selection)

A **branching algorithm** makes decisions based on specific conditions. It evaluates whether a condition is true or false and directs the program down different execution paths accordingly.

* **Characteristics:** Dynamic, enables decision-making, executes only the code relevant to the evaluated condition.
* **When to use:** Validating user input, setting permissions, or controlling logic where outcomes depend on specific states or rules.

### Example: Checking Pass/Fail Status
1. Read the student's test score.
2. If the score is 50 or higher, output "Pass".
3. Otherwise, output "Fail".

```python
score = int(input("Enter your exam score: "))

if score >= 50:
    print("Pass")
else:
    print("Fail")
```

---

## 3. Circular Algorithm (Iterative / Looping)

A **circular algorithm** repeats a sequence of instructions multiple times until a specified stopping condition is met. Instead of writing the same code repeatedly, loops cycle execution back to the start of a block of code.

* **Characteristics:** Repetitive, efficient for handling collections or batch processes.
* **When to use:** Processing items in a list, performing recurring calculations, or prompting for input until valid data is provided.

### Example: Countdown Timer
1. Start with a counter set to 5.
2. Print the current counter value.
3. Subtract 1 from the counter.
4. Repeat steps 2 and 3 as long as the counter is greater than 0.
5. Print "Blast off!".

```python
count = 5

while count > 0:
    print(count)
    count -= 1

print("Blast off!")
```

---

## Quick Comparison

| Algorithm Type | Execution Flow | Decision Making | Repetition |
| :--- | :--- | :--- | :--- |
| **Linear** | Top to bottom | No | No |
| **Branching** | Diverges based on conditions | Yes | No |
| **Circular** | Loops until a condition stops it | Yes (exit condition) | Yes |
