---
tag: J6A58MEM8R
kind: example
name: Linear systems over finite fields
msc: ["15A06", "11T99"]
topics: [DXSXFVDMXQ]
audience: ug1
instance_of: [0GT4WWGWH2]
uses: [0GT4WWGWH2, 0ZXZ82FTX2, 03VFZ2WETT, 0JVJ2WCXZH, 8QM2Y41P69]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_field
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Lights_Out_(game)
    locator: Mathematics
---

## Example

Row reduction works over every field, and that includes the [[finite fields|0ZXZ82FTX2]] $\mathbb{F}_p = \mathbb{Z}/p$ for a prime $p$, the [[integers modulo p|03VFZ2WETT]].
The steps are the same as over $\mathbb{R}$, and only the arithmetic changes.
We solve one system over $\mathbb{F}_5$ and one over $\mathbb{F}_2$, and we compare the counts with the [[count of solutions over a finite field|8QM2Y41P69]].

The first system is $x + 2y + 3z = 1$, $2x + y + z = 4$ over $\mathbb{F}_5$.

1. Start from the augmented matrix and apply $R_2 - 2R_1$:
$$\left[\begin{array}{rrr|r} 1 & 2 & 3 & 1 \\ 2 & 1 & 1 & 4 \end{array}\right] \to \left[\begin{array}{rrr|r} 1 & 2 & 3 & 1 \\ 0 & -3 & -5 & 2 \end{array}\right] = \left[\begin{array}{rrr|r} 1 & 2 & 3 & 1 \\ 0 & 2 & 0 & 2 \end{array}\right],$$
where the last step reduces modulo $5$.
2. Row 2 reads $2y = 2$. The inverse of $2$ in $\mathbb{F}_5$ is $3$, since $2 \cdot 3 = 6 = 1$, so $y = 3 \cdot 2 = 1$.
3. Column 3 has no pivot, so $z$ is free. Put $z = t$, and row 1 gives $x = 1 - 2 - 3t = 4 + 2t$.
4. So the solutions are $(4 + 2t, 1, t)$ for $t \in \mathbb{F}_5$. There are $5 = 5^{3-2}$ of them, one for each value of $t$.
5. Check $t = 1$, the point $(1, 1, 1)$: $1 + 2 + 3 = 6 = 1$ and $2 + 1 + 1 = 4$. Check $t = 0$, the point $(4, 1, 0)$: $4 + 2 = 6 = 1$ and $8 + 1 = 9 = 4$.

The second system is $x + y + z = 1$, $y + z + w = 0$, $x + w = 1$ over $\mathbb{F}_2$.

1. In $\mathbb{F}_2$, subtraction is the same as addition. So $R_3 + R_1$ and then $R_3 + R_2$ give
$$\left[\begin{array}{rrrr|r} 1 & 1 & 1 & 0 & 1 \\ 0 & 1 & 1 & 1 & 0 \\ 1 & 0 & 0 & 1 & 1 \end{array}\right] \to \left[\begin{array}{rrrr|r} 1 & 1 & 1 & 0 & 1 \\ 0 & 1 & 1 & 1 & 0 \\ 0 & 0 & 0 & 0 & 0 \end{array}\right].$$
2. There are two pivots and no pivot in the last column. So the system is consistent, and $z$ and $w$ are free.
3. Row 2 gives $y = z + w$, and row 1 gives $x = 1 + y + z = 1 + w$, because $z + z = 0$.
4. So there are $2^{4-2} = 4$ solutions: $(1, 0, 0, 0)$, $(1, 1, 1, 0)$, $(0, 1, 0, 1)$ and $(0, 0, 1, 1)$.
5. Check $(0, 0, 1, 1)$: $0 + 0 + 1 = 1$, $0 + 1 + 1 = 0$ and $0 + 1 = 1$.

## Remarks

Over $\mathbb{F}_2$ the only nonzero scalar is $1$, so scaling is never needed, and $R_i + R_j$ is the [[exclusive or|PTMR3P9J6C]] of two rows of bits.
The [[Gaussian elimination|0JVJ2WCXZH]] algorithm itself does not change.
In both systems the count of solutions is $q^{n - r}$, where $q$ is the size of the field, $n$ the number of unknowns and $r$ the number of pivots.
The field does change which systems are consistent: [[an equation over two fields|WT7RS59FGD]] is solvable over $\mathbb{Q}$ and not over $\mathbb{F}_2$.
For a puzzle that is a system over $\mathbb{F}_2$, see [[the Lights Out example|JD8FEPHM6T]].

## Explanations

### L1 human

In $\mathbb{F}_5$ we compute with the remainders $0, 1, 2, 3, 4$ after division by $5$.
Elimination works as usual, except that $6$ counts as $1$, and dividing by $2$ means multiplying by $3$.
Each free unknown has only $5$ possible values, so we can count the solutions exactly.

### L2 human

To solve a system over $\mathbb{F}_p$, reduce all numbers modulo $p$ after each step.
To divide by a pivot $a$, multiply by its inverse modulo $p$, which exists because $p$ is prime.
Then give each free variable a value in $\mathbb{F}_p$, and the number of solutions is $p$ to the power of the number of free variables.
Systems of this kind appear in coding theory, in cryptography and in puzzles, where the data are bits or residues.
Watch out: modulo a number that is not prime, such as $6$, the nonzero number $2$ has no inverse, because $2 \cdot 3 = 0$, and the method can break down.
