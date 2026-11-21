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

Consider the system over $\mathbb{R}$
$$x + y = 2x + 1, \qquad 3y = x - 2.$$
We show that the array of the left sides is not the coefficient matrix, and we find the true one.

1. The left sides alone give the array $\begin{bmatrix} 1 & 1 \\ 0 & 3 \end{bmatrix}$. It is not the [[coefficient matrix|0P7A2MJD24]], because the terms $2x$ and $x$ stand on the right sides.
2. Move every unknown to the left. Subtracting $2x$ in the first equation and $x$ in the second gives
$$-x + y = 1, \qquad -x + 3y = -2.$$
3. So the coefficient matrix is $A = \begin{bmatrix} -1 & 1 \\ -1 & 3 \end{bmatrix}$, with $b = (1, -2)^{\mathsf{T}}$.
4. Solve: $R_2 - R_1$ gives $(0, 2 \mid -3)$, so $y = -\tfrac32$, and then $x = y - 1 = -\tfrac52$.
5. Check in the original equations: $x + y = -4$ and $2x + 1 = -4$, then $3y = -\tfrac92$ and $x - 2 = -\tfrac92$.

## Remarks

The wrong array of step 1, used with the right sides $2x + 1$ and $x - 2$, does not describe a system with constant right sides at all.
If you solved $\begin{bmatrix} 1 & 1 \\ 0 & 3 \end{bmatrix} x = (1, -2)^{\mathsf{T}}$ by mistake, you would get $y = -\tfrac23$ and $x = \tfrac53$, and the first original equation fails, since $1 \ne \tfrac{13}{3}$.

## Explanations

### L1 human

The numbers in the table must belong to the unknowns, and the right side must hold only plain numbers.
So first move every unknown to the left side, and then read the table.

### L2 human

Subtract $2x$ from both sides of the first equation and $x$ from both sides of the second, and only then read the coefficients.
Watch out: a term that moves across the equals sign changes its sign, so $2x$ on the right becomes $-2x$ on the left.
