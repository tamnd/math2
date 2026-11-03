---
tag: 14VMJNXMDC
kind: concept
name: Dual linear program
msc: [90C05, 90C46]
sources:
  - url: https://en.wikipedia.org/wiki/Dual_linear_program
same_as:
  wikidata: Q910436
  wikipedia: Dual linear program
---

## Summary

Every [[linear program|VNMXB0J2KA]], called the primal, has a dual linear program built from the same data.
The constraints of one correspond to the variables of the other.
For the primal "maximize $c^T x$ subject to $A x \le b$, $x \ge 0$", the dual is "minimize $b^T y$ subject to $A^T y \ge c$, $y \ge 0$".
The dual value bounds the primal value by [[weak duality|50026WSZNF]].
The two optimal values are equal by the [[strong duality theorem|JPSCHKN0QP]].
Dual variables are interpreted as prices of the resources in the primal constraints.

## Explanations

### L1 human

A maximization problem is often paired with a minimization problem that gives upper bounds on it.
Each feasible point of the dual is a certificate that says "the primal cannot do better than this number".
The dual variables are like prices: they tell how much one more unit of each resource is worth.
For example, the dual of "maximize $x$ subject to $2x \le 6$, $x \ge 0$" is "minimize $6y$ subject to $2y \ge 1$, $y \ge 0$"; both have optimal value $3$.
