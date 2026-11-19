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

1. For integers $x, y$, the left side $2(x + 2y)$ is even, and the right side $1$ is odd.
2. So the equation has no solution in $\mathbb{Z}^2$.
3. Over the field $\mathbb{Q}$, put $y = 0$; then $x = \tfrac12$.
4. Check: $2 \cdot \tfrac12 + 0 = 1$.
5. So as a linear system over $\mathbb{Q}$, the equation is [[consistent|0X6V9B1V10]], not inconsistent.

## Remarks

Consistency is defined for systems over a field.
Integer solutions are a different question, about linear Diophantine equations.
The equation $ax + by = c$ has an integer solution exactly when $\gcd(a, b)$ divides $c$, and here $\gcd(2, 4) = 2$ does not divide $1$.

## Explanations

### L1 human

If $x$ and $y$ are whole numbers, $2x + 4y$ is always even, so it is never $1$.
But with fractions we can take $x = \tfrac12$ and $y = 0$.
So the answer depends on which numbers we allow.

### L2 human

To avoid this confusion, always fix the field before you row reduce.

1. Over $\mathbb{Q}$ or $\R$, the row $(2, 4 \mid 1)$ has a pivot in column $1$, so the system is consistent.
2. Over $\mathbb{Z}$, row reduction does not apply in the same way, because we cannot divide by $2$.

A trap: row reduction over $\mathbb{Q}$ can introduce fractions, so it does not answer questions about integer solutions.
