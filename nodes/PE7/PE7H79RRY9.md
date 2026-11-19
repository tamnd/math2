---
tag: PE7H79RRY9
kind: example
name: Unknowns on both sides of the equations
msc: ["15A06"]
topics: [DXSXFVDMXQ]
audience: school
not_instance_of:
  - target: 0HQFZAP3ND
    note: the array read off the left sides is not the coefficient matrix, because unknowns also appear on the right sides
uses: [0P7A2MJD24]
sources:
  - url: https://en.wikipedia.org/wiki/Coefficient_matrix
    locator: lead section
---

## Example

Consider the system over $\R$
$$x + y = 2x + 1, \qquad 3y = x - 2.$$

1. Reading only the left sides gives the array $\begin{bmatrix} 1 & 1 \\ 0 & 3 \end{bmatrix}$.
2. This is not the [[coefficient matrix|0P7A2MJD24]], because $2x$ and $x$ stand on the right sides.
3. Move them: $-x + y = 1$ and $-x + 3y = -2$.
4. So the coefficient matrix is $A = \begin{bmatrix} -1 & 1 \\ -1 & 3 \end{bmatrix}$, with $b = (1, -2)^T$.
5. $R_2 \leftarrow R_2 - R_1$ gives $(0, 2 \mid -3)$, so $y = -\tfrac32$.
6. Then $-x + y = 1$ gives $x = y - 1 = -\tfrac52$.
7. Check: $x + y = -4$ and $2x + 1 = -4$; $3y = -\tfrac92$ and $x - 2 = -\tfrac92$.

## Remarks

The wrong array of step 1 with right sides $(2x + 1, x - 2)$ is not a system with constant right sides at all.

## Explanations

### L1 human

The numbers in the table must belong to the unknowns, and the right side must hold only plain numbers.
So first move every unknown to the left side.

### L2 human

1. Subtract $2x$ from both sides of the first equation.
2. Subtract $x$ from both sides of the second equation.
3. Now read the coefficients.

A trap: when you move a term across the equals sign, its sign changes.
