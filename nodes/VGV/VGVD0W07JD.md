---
tag: VGVD0W07JD
kind: definition
name: Revised simplex method
msc: [90C05, 65K05, 90C49]
defines: AFXMKRC41H
uses: [MH272QHWPM, 957S7V3JW8, 0EB9N0S33C, 0GT4WWGWH2]
sources:
  - url: https://en.wikipedia.org/wiki/Revised_simplex_method
---

## Definition

Let $A$ be a real $m \times n$ matrix of rank $m$, let $b \in \R^m$ and $c \in \R^n$, and consider "maximize $c^T x$ subject to $A x = b$, $x \ge 0$".
For a basis $B$, let $A_B$ be the [[invertible|0EB9N0S33C]] matrix of the basic columns, $N$ the set of other indices and $A_j$ the column $j$.
The *revised simplex method* starts from a [[basic feasible solution|957S7V3JW8]] with basis $B$ and $x_B = A_B^{-1} b$, and repeats these steps.

1. Solve the [[linear system|0GT4WWGWH2]] $A_B^T y = c_B$ for the vector $y \in \R^m$ of simplex multipliers.
2. Compute the reduced costs $\bar c_j = c_j - y^T A_j$ for $j \in N$. If $\bar c_j \le 0$ for all $j \in N$, stop: $x$ is optimal.
3. Otherwise choose $j \in N$ with $\bar c_j > 0$ and solve $A_B d = A_j$. If $d \le 0$, stop: the program is unbounded.
4. Otherwise let $t = \min \set{x_i / d_i : i \in B, \ d_i > 0}$, attained at some $i \in B$.
5. Set $x_B \leftarrow x_B - t d$ and $x_j \leftarrow t$, replace $B$ by $(B \setminus \set{i}) \cup \set{j}$, and update the representation of $A_B^{-1}$.

## Remarks

The steps are those of the [[simplex algorithm|MH272QHWPM]], and the sequence of bases is the same for the same pivot choices.
Only $A_B$, or a factorization of it, is stored; the columns $A_j$ are read from the original sparse matrix $A$.
A common update writes the new inverse as $E A_B^{-1}$, where $E$ differs from the identity matrix in one column.
Solvers refactorize $A_B$ from time to time for accuracy.

Example: maximize $x_1 + x_2$ subject to $x_1 + 2 x_2 + s_1 = 4$, $3 x_1 + x_2 + s_2 = 6$ and all variables $\ge 0$.
Start with the basis $B = \set{s_1, s_2}$, so $A_B = I$.
Step 1 gives $y = 0$, so $\bar c_{x_1} = \bar c_{x_2} = 1$.
Choosing $x_1$, step 3 gives $d = (1, 3)$, the ratios are $4$ and $2$, so $t = 2$ and $s_2$ leaves.
The new basis $\set{s_1, x_1}$ has $x_1 = 2$ and $s_1 = 2$.

Non-example: an iteration that updates every entry of the $m \times (n + 1)$ tableau is the standard tableau simplex method, not the revised one, even though it produces the same bases.
