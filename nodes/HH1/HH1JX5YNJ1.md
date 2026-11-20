---
tag: HH1JX5YNJ1
kind: example
name: The rotation by a quarter turn is not involutory
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
not_instance_of:
  - target: NH2QE3671N
    note: the rotation R = (0, -1; 1, 0) has R² = -I, not I, and R has order 4
uses: [1GVCRBXQT8, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Involutory_matrix
    locator: lead section
---

## Example

Let $R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$, the rotation of the plane by $90°$.

1. $R^2 = \begin{pmatrix} 0 \cdot 0 + (-1) \cdot 1 & 0 \cdot (-1) + (-1) \cdot 0 \\ 1 \cdot 0 + 0 \cdot 1 & 1 \cdot (-1) + 0 \cdot 0 \end{pmatrix} = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} = -I$.
2. So $R^2 \neq I$, and $R$ is not [[involutory|1GVCRBXQT8]].
3. $R^4 = (-I)^2 = I$, so $R$ has order $4$, not $2$.
4. $R$ has no real eigenvalue, while an involutory matrix has eigenvalues $\pm 1$.

## Remarks

The rotation by $180°$, which is $R^2 = -I$, is involutory.
A rotation of the plane is involutory only for the angles $0°$ and $180°$.

## Explanations

### L1 human

Turning by a quarter turn twice gives a half turn, not the starting position.
So this rotation does not undo itself.

### L2 human

Both $R$ and an involution have determinant $\pm 1$, so the determinant does not separate them.
The square does.
