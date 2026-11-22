---
tag: AD6GEXKCB1
kind: example
name: Dodgson condensation fails at a zero interior entry
msc: ["15A15"]
topics: [DTBK11SR77]
audience: grad
not_instance_of:
  - target: RQ44FKS5QM
    note: the matrix with rows (1, 2, 3), (4, 0, 5), (6, 7, 8) has central entry 0, so condensation divides 0 by 0 and stops, although the determinant is 45
uses: [F7D849A4RZ, 09YB3WQG38, 7H2P40X0MV]
sources:
  - url: https://en.wikipedia.org/wiki/Dodgson_condensation
---

## Example

Let
$$A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 0 & 5 \\ 6 & 7 & 8 \end{pmatrix}$$
over $\mathbb{Q}$.
Its central entry is $0$, and [[Dodgson condensation|F7D849A4RZ]] cannot compute its determinant.

1. Step 1 takes the four connected $2 \times 2$ minors:
$$A^{(1)} = \begin{pmatrix} 1 \cdot 0 - 2 \cdot 4 & 2 \cdot 5 - 3 \cdot 0 \\ 4 \cdot 7 - 0 \cdot 6 & 0 \cdot 8 - 5 \cdot 7 \end{pmatrix} = \begin{pmatrix} -8 & 10 \\ 28 & -35 \end{pmatrix}.$$
2. Step 2 must divide the determinant of $A^{(1)}$ by the central entry $0$ of $A$.
   That determinant is $(-8)(-35) - 10 \cdot 28 = 280 - 280 = 0$.
3. So the method asks for $0/0$, which has no value, and it stops.
4. The determinant itself is not $0$.
   By the [[rule of Sarrus|7H2P40X0MV]],
$$\det A = 0 + 60 + 84 - 0 - 35 - 64 = 45.$$

## Remarks

### Why the numerator is zero too

By the Desnanot-Jacobi identity, the numerator of step 2 equals $\det A$ times the central entry.
So whenever the divisor is $0$, the numerator is $0$ as well, and the numbers computed so far carry no information about $\det A$.

### A repair by moving a row

Move row $1$ to the bottom:
$$A' = \begin{pmatrix} 4 & 0 & 5 \\ 6 & 7 & 8 \\ 1 & 2 & 3 \end{pmatrix}.$$
This cyclic shift of three rows is a product of two [[row swaps|09YB3WQG38]], so $\det A' = \det A$.
The central entry of $A'$ is now $7$, and condensation runs:
$$A'^{(1)} = \begin{pmatrix} 28 & -35 \\ 5 & 5 \end{pmatrix}, \qquad A'^{(2)} = \frac{28 \cdot 5 - (-35) \cdot 5}{7} = \frac{315}{7} = 45.$$
This agrees with the rule of Sarrus.

### What changes with the central entry

Replace the central entry $0$ by a number $t$.
The rule of Sarrus gives $\det = 8t + 60 + 84 - 18t - 35 - 64 = 45 - 10t$.
For every $t \ne 0$ condensation works and gives this value, and only $t = 0$ breaks it.
So the failure belongs to the method, not to the matrix: the determinant $45$ is a perfectly good number.

## Explanations

### L1 human

Condensation divides by inner entries of the matrix.
When an inner entry is zero, the method has to divide by zero, and it stops.
The determinant can still be any number, and here it is $45$.
Moving a row out of the way lets the method run again.

### L2 human

The typical repair is to permute rows or columns so that no interior entry is zero, and to track the sign of the permutation.
A cyclic shift of three rows keeps the sign, while a single swap of two rows changes it.
Watch out: the value $0/0$ does not mean that the determinant is $0$.
