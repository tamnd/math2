---
tag: MFVA8RJ4GN
kind: definition
name: Dantzig–Wolfe decomposition
msc: [90C05, 90C06]
defines: VE54BEPVKT
uses: [VNMXB0J2KA, 300K6CB1KH, 3MSGFJM2NX, 14VMJNXMDC, MH272QHWPM]
sources:
  - url: https://en.wikipedia.org/wiki/Dantzig–Wolfe_decomposition
---

## Definition

Consider a [[linear program|VNMXB0J2KA]] of the form
$$\text{minimize } c^T x \quad \text{subject to} \quad A_0 x = b_0, \quad x \in P,$$
where $A_0$ is a real $m_0 \times n$ matrix, $b_0 \in \R^{m_0}$, $c \in \R^n$, and $P = \set{x \in \R^n : A_1 x = b_1, \ x \ge 0}$ is a nonempty bounded [[convex polytope|300K6CB1KH]].
Let $v_1, \dots, v_K$ be the [[extreme points|3MSGFJM2NX]] of $P$.
The *Dantzig–Wolfe master problem* is the linear program in the weights $\lambda \in \R^K$:
$$\text{minimize } \sum_{k=1}^K (c^T v_k) \lambda_k \quad \text{subject to} \quad \sum_{k=1}^K (A_0 v_k) \lambda_k = b_0, \quad \sum_{k=1}^K \lambda_k = 1, \quad \lambda \ge 0.$$
*Dantzig–Wolfe decomposition* solves the master problem by column generation, repeating these steps.

1. Solve the restricted master problem, which uses only some of the columns $k$. Take its optimal [[dual|14VMJNXMDC]] values: $\pi \in \R^{m_0}$ for the linking constraints and $\mu \in \R$ for $\sum_k \lambda_k = 1$.
2. Solve the subproblem: minimize $(c - A_0^T \pi)^T x$ over $x \in P$, with an optimal extreme point $v$.
3. If $(c - A_0^T \pi)^T v - \mu \ge 0$, stop: the current solution is optimal. Otherwise add the column of $v$ to the restricted master problem.

## Remarks

Every $x \in P$ is a convex combination $\sum_k \lambda_k v_k$ of the extreme points, so the master problem has the same optimal value as the original program.
The number in step 3 is the smallest reduced cost of a master column.
So the method is the [[simplex algorithm|MH272QHWPM]] on the master problem, with columns generated only when needed.
The method pays off when $A_1$ is block diagonal: then the subproblem splits into independent small programs, one per block, each with its own convexity constraint.
For an unbounded polyhedron $P$, extreme rays are added as columns with no convexity constraint.

Example: take variables $(x_1, x_2, x_3, x_4)$ and $P = \set{x \ge 0 : x_1 + x_2 + x_3 + x_4 = 1}$.
Minimize $-x_1 - x_2$ subject to the linking constraint $x_1 + x_2 + x_3 = 1$ and $x \in P$.
The extreme points of $P$ are the unit vectors $e_1, e_2, e_3, e_4$, with costs $-1, -1, 0, 0$ and linking values $1, 1, 1, 0$.
The master problem is: minimize $-\lambda_1 - \lambda_2$ subject to $\lambda_1 + \lambda_2 + \lambda_3 = 1$, $\sum_k \lambda_k = 1$, $\lambda \ge 0$; its optimal value is $-1$, for example at $\lambda_1 = 1$, which is $x = e_1$.

Non-example: the program "minimize $\sum_k (c^T v_k) \lambda_k$ subject to $\sum_k (A_0 v_k) \lambda_k = b_0$, $\lambda \ge 0$" is not the master problem, since it drops the convexity constraint $\sum_k \lambda_k = 1$.
In the example above it allows $\lambda = (1, 0, 0, 5)$, which gives $x = (1, 0, 0, 5)$, a point outside $P$.
