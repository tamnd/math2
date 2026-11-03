---
tag: MGPQZ9RS81
kind: definition
name: Benders decomposition
msc: [90C06, 90C11, 90C05]
defines: DK2X0ZZDBH
uses: [VNMXB0J2KA, 14VMJNXMDC, 3MSGFJM2NX]
sources:
  - url: https://en.wikipedia.org/wiki/Benders_decomposition
---

## Definition

Let $A$ be a real $m \times n$ matrix, $B$ a real $m \times p$ matrix, $b \in \R^m$, $c \in \R^n$ and $d \in \R^p$, and let $Y \subseteq \R^p$ be a set, for example $Y = \Z^p \cap [0, 1]^p$.
Consider the problem
$$\text{minimize } c^T x + d^T y \quad \text{subject to} \quad A x + B y \ge b, \quad x \ge 0, \quad y \in Y.$$
For fixed $y$, the subproblem in $x$ is a [[linear program|VNMXB0J2KA]] with [[dual|14VMJNXMDC]]
$$\text{maximize } (b - B y)^T u \quad \text{subject to} \quad A^T u \le c, \quad u \ge 0.$$
Its feasible region $U = \set{u \in \R^m : A^T u \le c, u \ge 0}$ does not depend on $y$, and it is assumed to be nonempty.
Let $u^1, \dots, u^K$ be the [[extreme points|3MSGFJM2NX]] of $U$ and let $r^1, \dots, r^L$ be the extreme rays of $U$.
The *Benders master problem* is
$$\text{minimize } d^T y + \eta \quad \text{subject to} \quad \eta \ge (b - B y)^T u^k \ (k \le K), \quad (b - B y)^T r^l \le 0 \ (l \le L), \quad y \in Y.$$
*Benders decomposition* is the following iteration, which starts with no cuts in the master problem.

1. Solve the master problem with the current cuts and obtain $(\bar y, \bar\eta)$.
2. Solve the dual subproblem at $y = \bar y$.
3. If it is unbounded along an extreme ray $r$, add the *feasibility cut* $(b - B y)^T r \le 0$ and go to step 1.
4. If it has an optimal extreme point $u$ with $(b - B \bar y)^T u > \bar\eta$, add the *optimality cut* $\eta \ge (b - B y)^T u$ and go to step 1.
5. Otherwise stop: $\bar y$, with an optimal $x$ of the subproblem at $\bar y$, is optimal.

## Remarks

By [[strong duality|JPSCHKN0QP]], the full master problem has the same optimal value as the original problem.
Each round adds a cut that the current master solution violates, and $U$ has finitely many extreme points and extreme rays, so the iteration stops after finitely many rounds.
When the initial master problem with no cuts is unbounded in $\eta$, one adds a lower bound on $\eta$ or starts with a few cuts.

Example: minimize $x + 3y$ subject to $x + y \ge 1$, $x \ge 0$, $y \in \set{0, 1}$.
Here $U = [0, 1]$ with extreme points $0$ and $1$, and the cuts read $\eta \ge 0$ and $\eta \ge 1 - y$.
The master problem with both cuts is to minimize $3y + \max(0, 1 - y)$ over $y \in \set{0, 1}$, with optimum $1$ at $y = 0$, and then $x = 1$.

Non-example: if the subproblem for fixed $y$ is a nonlinear nonconvex problem, there is no linear dual to produce the cuts, so this scheme does not apply without change.

The scheme is the dual counterpart of [[Dantzig–Wolfe decomposition|VE54BEPVKT]]: Benders adds rows to a master problem, while Dantzig–Wolfe adds columns.
