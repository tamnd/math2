---
tag: GR9QY362DP
kind: definition
name: Criss-cross algorithm
msc: [90C05, 90C49]
defines: XEAVQFJR1B
uses: [MH272QHWPM, 957S7V3JW8, 14VMJNXMDC, YM58206VR1, 0EB9N0S33C]
sources:
  - url: https://en.wikipedia.org/wiki/Criss-cross_algorithm
---

## Definition

Let $A$ be a real $m \times n$ matrix of rank $m$, let $b \in \R^m$ and $c \in \R^n$, and consider "maximize $c^T x$ subject to $A x = b$, $x \ge 0$".
For a basis $B$ (a set of $m$ indices with $A_B$ [[invertible|0EB9N0S33C]]), let $N$ be the other indices.
Let $\beta = A_B^{-1} b$, let $\alpha_{ij}$ be entry $i$ of $A_B^{-1} A_j$, and let $\bar c_j = c_j - c_B^T A_B^{-1} A_j$.
An index $i \in B$ is *primal infeasible* if $\beta_i < 0$, and an index $j \in N$ is *dual infeasible* if $\bar c_j > 0$.
The *least-index criss-cross algorithm* starts from any basis $B$ and repeats these steps.

1. If no index is primal or dual infeasible, stop: the basic solution is optimal.
2. Otherwise let $k$ be the smallest index that is primal or dual infeasible.
3. If $k \in B$, let $J = \set{j \in N : \alpha_{kj} < 0}$. If $J$ is empty, stop: the program is infeasible. Otherwise let $j$ be the smallest element of $J$, and replace $B$ by $(B \setminus \set{k}) \cup \set{j}$.
4. If $k \in N$, let $I = \set{i \in B : \alpha_{ik} > 0}$. If $I$ is empty, stop: the [[dual program|14VMJNXMDC]] is infeasible, so the program has no optimal solution. Otherwise let $i$ be the smallest element of $I$, and replace $B$ by $(B \setminus \set{i}) \cup \set{k}$.

## Remarks

In step 3, row $k$ reads $x_k = \beta_k - \sum_{j \in N} \alpha_{kj} x_j$ on solutions of $A x = b$.
If all $\alpha_{kj} \ge 0$, then $x_k \le \beta_k < 0$ for every $x \ge 0$ with $A x = b$, so no feasible point exists.
In step 4, the vector $z$ with $z_k = 1$, $z_B = -A_B^{-1} A_k \ge 0$ and other entries $0$ satisfies $A z = 0$, $z \ge 0$ and $c^T z = \bar c_k > 0$.
Then the program is either infeasible or unbounded.

The algorithm stops after finitely many pivots; the proof uses the least-index choices, as for [[Bland's rule|YM58206VR1]].
At an optimal stop, $x$ is a [[basic feasible solution|957S7V3JW8]] and $y^T = c_B^T A_B^{-1}$ is optimal for the dual.

Example: for "maximize $-x_1$ subject to $x_1 - s = 1$, $x_1, s \ge 0$", take $B = \set{2}$ (the variable $s$).
Then $\beta = -1$, so index $2$ is primal infeasible, while $\bar c_1 = -1 \le 0$.
Here $k = 2$, and row $2$ has $\alpha_{21} = -1 < 0$, so $x_1$ enters and $s$ leaves.
The new basis $\set{1}$ gives $x_1 = 1$, $s = 0$ and $\bar c_2 = -1$, which is optimal.

Non-example: the simplex algorithm is not a criss-cross method, since it keeps the basis primal feasible at every step and needs a feasible start.
