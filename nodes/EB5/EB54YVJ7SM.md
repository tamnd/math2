---
tag: EB54YVJ7SM
kind: statement
role: theorem
name: Complementary slackness
msc: [90C05, 90C46]
uses: [14VMJNXMDC, 50026WSZNF, JPSCHKN0QP, 5VE5GVSNHK]
about: [14VMJNXMDC]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_programming
    locator: Complementary slackness
---

## Statement

Let $A$ be a real $m \times n$ matrix, let $b \in \R^m$ and let $c \in \R^n$.
Let (P) be "maximize $c^T x$ subject to $A x \le b$, $x \ge 0$", and let (D) be its [[dual linear program|14VMJNXMDC]] "minimize $b^T y$ subject to $A^T y \ge c$, $y \ge 0$".
Let $x$ be feasible for (P) and $y$ be feasible for (D).
Then $x$ and $y$ are both optimal if and only if

1. $y_i \, (b - A x)_i = 0$ for every $i = 1, \dots, m$, and
2. $x_j \, (A^T y - c)_j = 0$ for every $j = 1, \dots, n$.

## Remarks

Proof: one has the identity $b^T y - c^T x = y^T (b - A x) + x^T (A^T y - c)$.
Both terms are sums of products of nonnegative numbers, so the left side is $0$ if and only if conditions 1 and 2 hold.
By [[weak duality|50026WSZNF]] and the [[strong duality theorem|JPSCHKN0QP]], $x$ and $y$ are both optimal exactly when $b^T y = c^T x$.

In words: if a dual variable is positive, the corresponding primal constraint is tight, that is, its [[slack|5VE5GVSNHK]] is $0$.
If a primal variable is positive, the corresponding dual constraint is tight.

Example: for "maximize $x_1 + x_2$ subject to $x_1 + 2 x_2 \le 4$, $3 x_1 + x_2 \le 6$, $x \ge 0$", take $x = (8/5, 6/5)$ and $y = (2/5, 1/5)$.
Both primal constraints are tight, since $8/5 + 12/5 = 4$ and $24/5 + 6/5 = 6$.
Both dual constraints are tight, since $2/5 + 3/5 = 1$ and $4/5 + 1/5 = 1$.
So conditions 1 and 2 hold, and both points are optimal.

The conditions alone are not enough without feasibility: $x = 0$ and $y = 0$ satisfy conditions 1 and 2 for $c = (1, 1)$ above, but $y = 0$ is not dual feasible and $x = 0$ is not optimal.

## Explanations

### L1 human

At an optimum, a resource that is not used up has price zero, and a resource with a positive price is used up completely.
Likewise, an activity that is actually carried out exactly breaks even at the dual prices.
These conditions let one check optimality, or find a dual solution from a primal one, by solving equations.

### L2 human

Complementary slackness turns the optimality of a pair $(x, y)$ into a system of equations and inequalities, which is the linear case of the Karush–Kuhn–Tucker conditions.
Primal–dual algorithms, such as the Hungarian method for the assignment problem, keep feasible $x$ and $y$ and work to satisfy complementary slackness.
In the simplex algorithm, a basic solution and its dual vector $c_B^T A_B^{-1}$ always satisfy the conditions; optimality is reached when the dual vector becomes feasible.
