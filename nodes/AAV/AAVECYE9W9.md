---
tag: AAVECYE9W9
kind: definition
name: Input–output model
msc: [91B66, 91B74, 15B48]
defines: PF15E9SVQV
uses: [KTTZ1J9SPZ, JPQCCFCY8X, 0GT4WWGWH2]
sources:
  - url: https://en.wikipedia.org/wiki/Input%E2%80%93output_model
---

## Definition

Let an economy have $n$ sectors, each producing one good with a [[Leontief technology|KTTZ1J9SPZ]].
The *technology matrix* is an $n \times n$ [[nonnegative matrix|JPQCCFCY8X]] $A = (a_{ij})$.
Its entry $a_{ij} \ge 0$ is the amount of good $i$ used to produce one unit of good $j$.
Let $d \in \R^n_+$ be a final demand vector.
The *Leontief input–output model* asks for a gross output vector $x \in \R^n_+$ with
$$x = A x + d, \qquad \text{that is,} \qquad (I - A) x = d,$$
where $I$ is the $n \times n$ identity matrix.
The matrix $A$ is called *productive* if there is $x \in \R^n_+$ with $x_i > (A x)_i$ for every $i$.

## Remarks

Example: $A = \begin{pmatrix} 0 & 0.1 \\ 0.2 & 0 \end{pmatrix}$ and $d = (10, 20)$.
The [[linear system|0GT4WWGWH2]] $x_1 - 0.1 x_2 = 10$, $x_2 - 0.2 x_1 = 20$ has the solution $x = (12/0.98, 22/0.98) \approx (12.24, 22.45)$, which is nonnegative.

Non-example: $A = \begin{pmatrix} 0 & 2 \\ 1 & 0 \end{pmatrix}$ is not productive.
Productivity would need $x_1 > 2 x_2$ and $x_2 > x_1$, which together force $x_2 < 0$.
For $d = (1, 1)$ the unique solution of $(I - A) x = d$ is $x = (-3, -2)$, which has negative outputs.

If $A$ is productive, then $I - A$ is invertible and $(I - A)^{-1} = I + A + A^2 + \cdots \ge 0$, so the model has a unique nonnegative solution for every $d \ge 0$.
The matrix $(I - A)^{-1}$ is called the Leontief inverse.
The [[Hawkins–Simon condition|G7V6BQSPMW]] gives a test for productivity by determinants.
