---
tag: NZ8PF59MTJ
kind: example
name: Row space of a matrix with a non-reduced echelon form
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug1
instance_of: [069MCGX635]
illustrates: [1JGMW9DM4Z]
uses: [0EP73HK4C4, 0F27PBRWD7]
sources:
  - url: https://en.wikipedia.org/wiki/Row_and_column_spaces
    locator: Row space
---

## Example

Any echelon form gives a basis of the row space, and the reduced form is not needed.
Let
$$A = \begin{pmatrix} 0 & 2 & 4 \\ 1 & 1 & 1 \\ 1 & 3 & 5 \end{pmatrix}$$
over $\mathbb{R}$.

1. Exchange rows 1 and 2; the rows become $(1, 1, 1)$, $(0, 2, 4)$ and $(1, 3, 5)$.
2. Subtract row 1 from row 3; row 3 becomes $(0, 2, 4)$.
3. Subtract row 2 from row 3; row 3 becomes $(0, 0, 0)$, and the result is
$$U = \begin{pmatrix} 1 & 1 & 1 \\ 0 & 2 & 4 \\ 0 & 0 & 0 \end{pmatrix}.$$
4. The matrix $U$ is in [[row echelon form|0F27PBRWD7]] but not reduced, with pivots $1$ and $2$ in columns 1 and 2.
5. So $(1, 1, 1)$ and $(0, 2, 4)$ form a basis of the [[row space|0EP73HK4C4]] of $A$, and $\dim \operatorname{Row}(A) = 2$.
6. Check: row 3 of $A$ is $(1, 3, 5) = (1, 1, 1) + (0, 2, 4)$, and row 1 of $A$ is $(0, 2, 4)$ itself.
7. The vector $n = (1, -2, 1)$ is orthogonal to both basis vectors, since $1 - 2 + 1 = 0$ and $0 - 4 + 4 = 0$, so $\operatorname{Row}(A)$ is the plane $x - 2y + z = 0$ in $\mathbb{R}^3$.
8. Check with the original rows:
$$An = (0 - 4 + 4,\ 1 - 2 + 1,\ 1 - 6 + 5) = (0, 0, 0),$$
so $n$ lies in the null space of $A$, which is orthogonal to the row space.

## Remarks

The example shows that the reduced form is a convenience and not a requirement.
The staircase shape of $U$ alone makes the nonzero rows independent: a combination $a(1, 1, 1) + b(0, 2, 4)$ has first entry $a$, so it vanishes only when $a = 0$, and then $2b = 0$.
Continuing to the reduced form would give the rows $(1, 0, -1)$ and $(0, 1, 2)$, another basis of the same plane, and both satisfy $x - 2y + z = 0$.

The row exchange in step 1 is a row operation like the others, and it does not change the span of the rows.
If we change the last entry of $A$ from $5$ to $6$, the third row of $U$ becomes $(0, 0, 1)$, the rank becomes $3$, and the row space is all of $\mathbb{R}^3$.

## Explanations

### L1 human

Row operations do not change which vectors are combinations of the rows.
After two subtractions a zero row appears, so the three rows span only a flat plane through the origin.
The plane is described by one equation, $x - 2y + z = 0$, and every row of $A$ satisfies it.

### L2 human

The two nonzero rows of the echelon form are a basis, because of the staircase of pivots.
To describe the plane by an equation, solve $n \cdot (1, 1, 1) = 0$ and $n \cdot (0, 2, 4) = 0$, which gives $n = (1, -2, 1)$ up to a multiple.
Over $\mathbb{R}$ the null space is the orthogonal complement of the row space, so this normal vector also solves $An = 0$.
Watch out: the zero row of $U$ does not say that some row of $A$ is zero.
It says that the rows of $A$ satisfy one linear relation, here row 3 = row 1 + row 2, since $(0, 2, 4) + (1, 1, 1) = (1, 3, 5)$.
