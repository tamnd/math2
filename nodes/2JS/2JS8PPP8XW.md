---
tag: 2JS8PPP8XW
kind: definition
name: Simplex algorithm
msc: [90C05, 65K05]
defines: MH272QHWPM
uses: [VNMXB0J2KA, 0VD9ZSWWJG]
sources:
  - url: https://en.wikipedia.org/wiki/Simplex_algorithm
---

## Definition

Let $A$ be a real $m \times n$ [[matrix|0VD9ZSWWJG]] of rank $m$, let $b \in \R^m$ and let $c \in \R^n$.
Consider the [[linear program|VNMXB0J2KA]]: maximize $c^T x$ subject to $A x = b$ and $x \ge 0$.
A *basis* is a set $B$ of $m$ column indices such that the submatrix $A_B$ is invertible; let $N$ be the other indices.
Its *basic solution* is the $x$ with $x_B = A_B^{-1} b$ and $x_N = 0$, and $B$ is *feasible* if $x_B \ge 0$.
The *simplex algorithm* starts from a feasible basis $B$ and repeats the following step.

1. Compute the reduced costs $\bar c_j = c_j - c_B^T A_B^{-1} A_j$ for $j \in N$, where $A_j$ is column $j$ of $A$.
If $\bar c_j \le 0$ for all $j \in N$, stop: the basic solution is optimal.
2. Otherwise choose an entering index $j \in N$ with $\bar c_j > 0$, and compute $d = A_B^{-1} A_j$.
If $d \le 0$, stop: the program is unbounded.
3. Otherwise choose a leaving index $i \in B$ with $d_i > 0$ that minimizes $x_i / d_i$ (the ratio test), and replace $B$ by $(B \setminus \set{i}) \cup \set{j}$.

## Remarks

Feasible basic solutions are exactly the vertices of the feasible region, and several bases can give the same vertex when it is degenerate.
One step moves along an edge to an adjacent vertex, or stays at the same vertex in a degenerate step, and it never decreases $c^T x$.
With an anti-cycling choice of $j$ and $i$, such as Bland's rule of taking the smallest eligible index, the algorithm stops after finitely many steps.

Example: maximize $x_1 + x_2$ subject to $x_1 + 2x_2 + s_1 = 4$, $3x_1 + x_2 + s_2 = 6$ and all variables $\ge 0$.
Start with $B = \set{s_1, s_2}$, the point $x_1 = x_2 = 0$; both reduced costs are $1$.
Let $x_1$ enter; then $d = (1, 3)$, the ratios are $4$ and $2$, so $s_2$ leaves, giving $x_1 = 2$, $s_1 = 2$ and value $2$.
Now $x_2$ has reduced cost $2/3$; it enters, the ratio test removes $s_1$, and the new point is $x_1 = 8/5$, $x_2 = 6/5$.
There the objective equals $14/5 - \frac25 s_1 - \frac15 s_2$, so all reduced costs are negative and $14/5$ is optimal.

Non-example: in the first step, letting $s_1$ leave instead of $s_2$ ignores the ratio test.
It gives $x_1 = 4$ and $s_2 = 6 - 12 = -6 < 0$, which is not a feasible basis.

A first feasible basis can be found by solving an auxiliary linear program, the phase one problem.
