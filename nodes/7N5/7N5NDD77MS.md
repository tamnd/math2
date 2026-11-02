---
tag: 7N5NDD77MS
kind: definition
name: Near-unanimity term
msc: [08B05, 08B10]
defines: 4CRH8NNFEF
uses: [AJNZJD8442, N9M2N27END, PKD440G2XW]
sources:
  - url: https://en.wikipedia.org/wiki/Majority_function
---

## Definition

Let $\mathcal{V}$ be a [[variety of algebras|AJNZJD8442]] and let $n \ge 3$ be an integer.
A *near-unanimity term* of arity $n$ for $\mathcal{V}$ is a [[term|N9M2N27END]] $t(x_1, \dots, x_n)$ such that $\mathcal{V}$ satisfies the [[identities|PKD440G2XW]]
$$t(y, x, x, \dots, x) \approx t(x, y, x, \dots, x) \approx \cdots \approx t(x, x, \dots, x, y) \approx x.$$
Here the $i$-th term in the chain has $y$ in position $i$ and $x$ in all other positions.
An algebra $A$ has a near-unanimity term when the variety it generates has one, that is, when the identities hold in $A$.

## Remarks

Example: in the variety of lattices, $t(x, y, z) = (x \wedge y) \vee (y \wedge z) \vee (x \wedge z)$ is a near-unanimity term of arity $3$.
Check: $t(y, x, x) = (y \wedge x) \vee x \vee (y \wedge x) = x$ by absorption, and the other two identities follow in the same way by symmetry of $t$.
A near-unanimity term of arity $3$ is called a [[majority term|9879ZMW5AA]].
Non-example: the variety of groups has no near-unanimity term of any arity.
The reason is that a variety with a near-unanimity term is congruence-distributive, while the group $\Z_2 \times \Z_2$ has a non-distributive lattice of normal subgroups.
If $t$ is a near-unanimity term of arity $n$, then $s(x_1, \dots, x_{n + 1}) = t(x_1, \dots, x_n)$ is one of arity $n + 1$.
The abbreviation NU term is common.
