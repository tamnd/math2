---
tag: MME3Y9VCHR
kind: example
name: An equation without integer solutions that is consistent
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: ug1
not_instance_of:
  - target: 0X6V9B1V10
    note: the equation 2x + 4y = 1 has no integer solution, but over the field of rationals it has solutions, so it is not an inconsistent system
uses: [0X6V9B1V10]
sources:
  - url: https://en.wikipedia.org/wiki/Diophantine_equation
    locator: Linear Diophantine equations
---

## Example

Consider the equation $2x + 4y = 1$.
It has no solution in integers, and yet it is not an inconsistent system.

1. For integers $x, y$, the left side is $2(x + 2y)$, which is even, and the right side $1$ is odd. So the equation has no solution in $\mathbb{Z}^2$.
2. Over the field $\mathbb{Q}$, put $y = 0$, and the equation gives $x = \tfrac12$. Check: $2 \cdot \tfrac12 + 4 \cdot 0 = 1$.
3. So as a linear system over $\mathbb{Q}$, the equation is [[consistent|0X6V9B1V10]].

## Remarks

Consistency is defined for systems over a field, and $\mathbb{Z}$ is not a field.
The question of integer solutions belongs to the theory of linear Diophantine equations.
There the answer is a divisibility test: $ax + by = c$ has an integer solution exactly when $\gcd(a, b)$ divides $c$.
Here $\gcd(2, 4) = 2$ does not divide $1$.
If you change the right side to $2$, the test passes, and $(1, 0)$ is an integer solution.

## Explanations

### L1 human

If $x$ and $y$ are whole numbers, $2x + 4y$ is always even, so it is never $1$.
With fractions we can take $x = \tfrac12$ and $y = 0$.
So the answer depends on which numbers we allow.

### L2 human

To avoid this confusion, fix the field before you row reduce.
Over $\mathbb{Q}$ or $\mathbb{R}$, the row $(2, 4 \mid 1)$ has a pivot in column $1$, and no row has the form $(0, 0 \mid c)$ with $c \ne 0$, so the system is consistent.
Over $\mathbb{Z}$ we cannot divide by $2$, so row reduction does not apply in the same way.
Watch out: row reduction over $\mathbb{Q}$ brings in fractions, so it does not answer questions about integer solutions.
