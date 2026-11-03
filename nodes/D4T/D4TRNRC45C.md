---
tag: D4TRNRC45C
kind: definition
name: Generating function of a canonical transformation
msc: [70H15, 70H20]
defines: NXK6HD49NZ
uses: [AGA36YKX4F, 0EDKGA2FAK]
sources:
  - url: https://en.wikipedia.org/wiki/Generating_function_(physics)
---

## Definition

Let $n \ge 1$ and let $(q, p)$ and $(Q, P)$ be old and new phase-space variables in $\R^{2n}$, with $t$ the time.

1. A *generating function of type 1* is a function $F_1(q, Q, t)$ of class $C^2$ such that the matrix $\big(\partial^2 F_1 / \partial q_i \partial Q_j\big)$ is invertible.
It generates the transformation $(q, p) \mapsto (Q, P)$ defined implicitly by
$$p_i = \frac{\partial F_1}{\partial q_i}(q, Q, t), \qquad P_i = -\frac{\partial F_1}{\partial Q_i}(q, Q, t).$$
2. A *generating function of type 2* is a function $F_2(q, P, t)$ of class $C^2$ such that the matrix $\big(\partial^2 F_2 / \partial q_i \partial P_j\big)$ is invertible.
It generates the transformation defined implicitly by
$$p_i = \frac{\partial F_2}{\partial q_i}(q, P, t), \qquad Q_i = \frac{\partial F_2}{\partial P_i}(q, P, t).$$

In both cases, the new Hamiltonian is $K = H + \partial F / \partial t$, where $F$ is the generating function and $H$ is the old Hamiltonian.

## Remarks

By the implicit function theorem, the invertibility condition makes the relations define $(Q, P)$ as a function of $(q, p)$ locally.
For each fixed $t$ the resulting map is a [[canonical transformation|AGA36YKX4F]], since $\sum_i p_i \, dq_i - \sum_i P_i \, dQ_i = d_{q, Q} F_1$ is exact, and taking $d$ gives $\sum_i dp_i \wedge dq_i = \sum_i dP_i \wedge dQ_i$.
It maps solutions of the [[Hamiltonian system|0EDKGA2FAK]] of $H$ to solutions of the Hamiltonian system of $K$.
Types 3 and 4 use the variables $(p, Q)$ and $(p, P)$ in the same way.

Example: $F_1 = \sum_i q_i Q_i$ gives $p = Q$ and $P = -q$, the exchange of positions and momenta.
Example: $F_2 = \sum_i q_i P_i$ gives $p = P$ and $Q = q$, the identity.

Non-example: for $n = 1$, $F_1 = q^2 + Q^2$ has $\partial^2 F_1 / \partial q \partial Q = 0$.
The relations $p = 2q$ and $P = -2Q$ do not define $(Q, P)$ from $(q, p)$: they restrict $(q, p)$ to a line and leave $Q$ free.
