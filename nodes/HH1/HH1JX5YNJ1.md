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

Let
$$R = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix},$$
the rotation of the plane by a quarter turn, $90°$ counterclockwise.
We show that $R$ is invertible but does not undo itself.

1. Multiply row by column:
$$R^2 = \begin{pmatrix} 0 \cdot 0 + (-1) \cdot 1 & 0 \cdot (-1) + (-1) \cdot 0 \\ 1 \cdot 0 + 0 \cdot 1 & 1 \cdot (-1) + 0 \cdot 0 \end{pmatrix} = \begin{pmatrix} -1 & 0 \\ 0 & -1 \end{pmatrix} = -I.$$
2. So $R^2 \ne I$, and $R$ is not [[involutory|1GVCRBXQT8]].
3. From $R^2 = -I$ we get $R^4 = (-I)^2 = I$, and $R^3 = -R \ne I$. So $R$ has order $4$, not $2$.
4. The inverse of $R$ is $R^3 = -R$, the quarter turn the other way, and not $R$ itself.
5. An involutory matrix has only the eigenvalues $\pm 1$. But $R v = v$ or $R v = -v$ would give $R^2 v = v$, while $R^2 v = -v$, so $v = 0$. Thus $R$ has no eigenvalue $\pm 1$.

## Remarks

The half turn $R^2 = -I$ is involutory, since $(-I)^2 = I$.
The rotation by an angle $\theta$ squares to the rotation by $2\theta$, so it is involutory only when $2\theta$ is a full turn, that is, for $\theta = 0°$ and $\theta = 180°$.

The determinant does not detect the difference.
Here $\det R = 1$, and an involutory matrix also has $\det A = \pm 1$, since $(\det A)^2 = \det I = 1$.
Only the square itself decides.

## Explanations

### L1 human

Turning by a quarter turn twice gives a half turn, not the starting position.
For example, $(1, 0)$ goes to $(0, 1)$ and then to $(-1, 0)$.
So this rotation does not undo itself; it takes four quarter turns to come back.

### L2 human

Over $\mathbb{C}$ the eigenvalues of $R$ are $i$ and $-i$, the roots of $\lambda^2 + 1 = 0$.
They are not $\pm 1$, which confirms that $R$ is not involutory.
Watch out: an invertible matrix whose square is a multiple of $I$ is not automatically involutory; the multiple must be exactly $1$.
