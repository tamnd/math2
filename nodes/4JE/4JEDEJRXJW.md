---
tag: 4JEDEJRXJW
kind: definition
name: Siggers term
msc: [08B05, 08A70]
defines: JYW1H3J8SX
uses: [AJNZJD8442, N9M2N27END, PKD440G2XW, 9FS1JFZSX4, QEAMRNRJJD]
sources:
  - url: https://en.wikipedia.org/wiki/Constraint_satisfaction_problem
---

## Definition

Let $\mathcal{V}$ be a [[variety of algebras|AJNZJD8442]].
A *Siggers term* for $\mathcal{V}$ is a $6$-ary [[term|N9M2N27END]] $s(x_1, \dots, x_6)$ such that $\mathcal{V}$ satisfies the [[identities|PKD440G2XW]]
$$s(x, x, x, x, x, x) \approx x \quad \text{and} \quad s(x, y, x, z, y, z) \approx s(y, x, z, x, z, y).$$
The first identity says that $s$ is [[idempotent|9FS1JFZSX4]].

## Remarks

Example: in the variety of semilattices, $s = x_1 \wedge \cdots \wedge x_6$ is a Siggers term.
Check: it is idempotent, and both sides of the second identity equal $x \wedge y \wedge z$, by commutativity, associativity and idempotence.
Non-example: in the variety of sets with no operations, the only terms are variables, and no variable $x_i$ is a Siggers term.
The two sides of the second identity differ in every place, so for $s = x_i$ it would read $x \approx y$, $x \approx z$ or $y \approx z$.
Every Siggers term is a [[Taylor term|QEAMRNRJJD]]: substituting $z = x$, $y = x$ or $x = y$ in the second identity gives, for each place, an identity in two variables that differs in that place.
A $4$-ary variant, an idempotent term with $s(a, r, e, a) \approx s(r, a, r, e)$, is also used; a finite algebra has a Taylor term exactly when it has a term of this kind.
