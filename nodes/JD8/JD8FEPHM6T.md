---
tag: JD8FEPHM6T
kind: example
name: The Lights Out puzzle on a 2 by 2 board
msc: ["15A06", "91A46"]
topics: [DXSXFVDMXQ]
audience: ug1
instance_of: [0GT4WWGWH2]
uses: [0GT4WWGWH2, 0ZXZ82FTX2, 0JVJ2WCXZH, 0ATFVE08MW, 8QM2Y41P69]
sources:
  - url: https://en.wikipedia.org/wiki/Lights_Out_(game)
    locator: Mathematics
  - url: https://en.wikipedia.org/wiki/Lights_Out_(game)
    locator: lead section
---

## Example

Lights Out is a puzzle on a grid of lights.
Pressing a light switches it and its horizontal and vertical neighbors, and the aim is to switch off every light.
Tiger Electronics sold it as a handheld game in 1995, on a $5 \times 5$ grid.
We solve the $2 \times 2$ version as a [[linear system|0GT4WWGWH2]] over [[the field|0ZXZ82FTX2]] $\mathbb{F}_2$.

Name the cells $a, b$ in the top row and $c, d$ in the bottom row.
A state is a vector $s \in \mathbb{F}_2^4$, with $1$ for a light that is on.
A choice of presses is a vector $p \in \mathbb{F}_2^4$, because pressing twice is the same as not pressing, and the order of presses does not matter.
Pressing $a$ switches $a$, $b$ and $c$, so the column of $a$ is $(1, 1, 1, 0)$.
The other columns come in the same way, and
$$A = \begin{bmatrix} 1 & 1 & 1 & 0 \\ 1 & 1 & 0 & 1 \\ 1 & 0 & 1 & 1 \\ 0 & 1 & 1 & 1 \end{bmatrix}.$$
The presses $p$ switch off the state $s$ exactly when $Ap = s$.
We solve this for the state with only $a$ on, $s = (1, 0, 0, 0)$, by [[Gaussian elimination|0JVJ2WCXZH]].

1. The rows of $[A \mid s]$ are $(1, 1, 1, 0 \mid 1)$, $(1, 1, 0, 1 \mid 0)$, $(1, 0, 1, 1 \mid 0)$ and $(0, 1, 1, 1 \mid 0)$.
2. Clear column 1: $R_2 + R_1$ gives $(0, 0, 1, 1 \mid 1)$, and $R_3 + R_1$ gives $(0, 1, 0, 1 \mid 1)$.
3. Swap $R_2$ and $R_3$, so that row 2 has its leading entry in column 2.
4. Clear below: $R_4 + R_2$ gives $(0, 0, 1, 0 \mid 1)$, and then $R_4 + R_3$ gives $(0, 0, 0, 1 \mid 0)$.
5. [[Back substitution|0ATFVE08MW]] gives $p_d = 0$, then $p_c = 1 + p_d = 1$ from row 3, then $p_b = 1 + p_d = 1$ from row 2.
6. Row 1 gives $p_a = 1 + p_b + p_c = 1 + 1 + 1 = 1$. So $p = (1, 1, 1, 0)$: press $a$, $b$ and $c$.
7. Check by adding the columns of $a$, $b$ and $c$ in $\mathbb{F}_2$:
$$(1, 1, 1, 0) + (1, 1, 0, 1) + (1, 0, 1, 1) = (3, 2, 2, 2) = (1, 0, 0, 0).$$

## Remarks

The elimination found four pivots, so $A$ is invertible over $\mathbb{F}_2$, and every state of the $2 \times 2$ board has exactly one solution, by the [[count of solutions over a finite field|8QM2Y41P69]].
In fact $A^2 = I$ over $\mathbb{F}_2$.
The matrix is symmetric, each row has three $1$s, and any two different rows share exactly two $1$s, so each entry of $A^2$ is $3 = 1$ on the diagonal and $2 = 0$ off it.
So the solution for any state $s$ is $p = As$, and the answer above is the column of $a$.

Larger boards behave differently.
On an $n \times n$ board the matrix has size $n^2 \times n^2$, and its rank over $\mathbb{F}_2$ is $9$ for $3 \times 3$, $12$ for $4 \times 4$ and $23$ for $5 \times 5$.
So on the $5 \times 5$ board only $2^{23}$ of the $2^{25}$ states, one in four, can be switched off, and each of them has $2^{25 - 23} = 4$ solutions.

## Explanations

### L1 human

Each light is on or off, which we write as $1$ or $0$.
Pressing a button adds $1$ to some lights, and $1 + 1 = 0$, because switching a light twice brings it back.
So the puzzle is a system of linear equations with only the numbers $0$ and $1$.

### L2 human

To solve any board, write the effect of each button as a column of $0$s and $1$s, put the columns into a matrix $A$, and solve $Ap = s$ by elimination modulo $2$.
Then press the buttons with $p_i = 1$, in any order, and check by adding the pressed columns modulo $2$.
The same method tells you whether a start state can be solved at all, which is the case exactly when the system is consistent.
Watch out: over $\mathbb{R}$ the same matrix gives different answers, because there $1 + 1 = 2$ and not $0$.
