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

Let $A = \begin{pmatrix} 1 & 2 & 3 \\ 4 & 0 & 5 \\ 6 & 7 & 8 \end{pmatrix}$ over $\mathbb{Q}$.
Its central entry is $0$.

1. Step 1 of the [[condensation|F7D849A4RZ]] gives $A^{(1)} = \begin{pmatrix} 1 \cdot 0 - 2 \cdot 4 & 2 \cdot 5 - 3 \cdot 0 \\ 4 \cdot 7 - 0 \cdot 6 & 0 \cdot 8 - 5 \cdot 7 \end{pmatrix} = \begin{pmatrix} -8 & 10 \\ 28 & -35 \end{pmatrix}$.
2. Step 2 must divide $(-8)(-35) - 10 \cdot 28 = 280 - 280 = 0$ by the central entry $0$.
3. So the method gives $0/0$, which has no value.
4. But $\det A \ne 0$: by the [[rule of Sarrus|7H2P40X0MV]], $\det A = 0 + 60 + 84 - 0 - 35 - 64 = 45$.

## Remarks

### Why the numerator is also zero

The numerator in step 2 is $\det A$ times the central entry, by the Desnanot-Jacobi identity.
So a zero divisor always gives $0/0$, and the numbers computed so far do not determine $\det A$.

### A remedy

Move row $1$ to the bottom, which gives $A' = \begin{pmatrix} 4 & 0 & 5 \\ 6 & 7 & 8 \\ 1 & 2 & 3 \end{pmatrix}$.
This is a cyclic permutation of three rows, which is a product of two [[row swaps|09YB3WQG38]], so $\det A' = \det A$.
Condensation of $A'$ gives $A'^{(1)} = \begin{pmatrix} 28 & -35 \\ 5 & 5 \end{pmatrix}$ and then $(28 \cdot 5 - (-35) \cdot 5) / 7 = 315/7 = 45$.
This agrees with the value from the rule of Sarrus.
If the central entry $0$ is changed to any $t \ne 0$, then the method works, and it gives $\det A = 45 - 10t$, as Sarrus confirms.

## Explanations

### L1 human

Condensation divides by inner entries of the matrix.
When an inner entry is zero, the method must divide by zero, and it stops.
The determinant itself can still be any number.

### L2 human

The typical remedy is to move rows or columns so that no inner entry is zero, and to track the sign.
A trap: the value $0/0$ does not mean that the determinant is $0$; here it is $45$.
