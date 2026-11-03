---
tag: 30GKJN9VF1
kind: definition
name: Branch and cut
msc: [90C57, 90C11, 90C10]
defines: AJ786D5KK7
uses: [ZZ7C50WN56, PR7VMJN5BH, PYMHHM5Z6F, 3PX6EV34QK]
sources:
  - url: https://en.wikipedia.org/wiki/Branch_and_cut
---

## Definition

Let a [[mixed-integer linear program|3PX6EV34QK]] of maximizing $c^T x$ over the set $S$ of $x$ with $A x \le b$ and $x_1, \dots, x_p \in \Z$ be given.
*Branch and cut* is the [[branch and bound|ZZ7C50WN56]] method for this program in which the bound at each subproblem is computed as follows.

1. Solve the [[linear programming relaxation|PYMHHM5Z6F]] of the subproblem, together with the cuts collected so far, and obtain an optimal solution $x^*$.
2. If $x^*$ violates an integrality condition, search for [[cuts|PR7VMJN5BH]] for $x^*$. These are linear inequalities satisfied by every feasible point of the subproblem but violated by $x^*$.
3. If cuts are found, add them to the relaxation and go to step 1. Otherwise return the value at $x^*$ as the bound, and branch on a variable $x_i$ with $i \le p$ and $x_i^* \notin \Z$.

Cuts valid for all of $S$ are *global* and may be kept for all subproblems; cuts valid only for the current subproblem are *local*.

## Remarks

Example: in a $0$-$1$ program with a constraint $3 x_1 + 3 x_2 + 3 x_3 \le 5$, the relaxation may return $x^* = (1, 2/3, 0)$.
The cover inequality $x_1 + x_2 + x_3 \le 1$ is valid, since any two of the variables equal to $1$ would give $6 > 5$.
It is violated by $x^*$, so branch and cut adds it before branching.

Non-example: [[branch and bound|ZZ7C50WN56]] that uses only the original relaxation at each node, never adding inequalities, is not branch and cut.

In practice one stops the cut loop when the bound improves too slowly, and branching then takes over.
