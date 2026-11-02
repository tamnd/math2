---
tag: DQ14ERMRTZ
kind: definition
name: Majority term
msc: [08B05, 08B10]
defines: 9879ZMW5AA
uses: [4CRH8NNFEF, AJNZJD8442, N9M2N27END, PKD440G2XW]
sources:
  - url: https://en.wikipedia.org/wiki/Majority_function
---

## Definition

Let $\mathcal{V}$ be a [[variety of algebras|AJNZJD8442]].
A *majority term* for $\mathcal{V}$ is a ternary [[term|N9M2N27END]] $m(x, y, z)$ such that $\mathcal{V}$ satisfies the [[identities|PKD440G2XW]]
$$m(x, x, y) \approx m(x, y, x) \approx m(y, x, x) \approx x.$$
Equivalently, a majority term is a [[near-unanimity term|4CRH8NNFEF]] of arity $3$.

## Remarks

Example: on $\set{0, 1}$ the Boolean majority function $m(x, y, z) = (x \wedge y) \vee (y \wedge z) \vee (x \wedge z)$ is a majority term of the two-element Boolean algebra.
Check: if two arguments equal $a$, then one of the three meets equals $a$ and the other two are at most $a$, so the join is $a$.
Non-example: the term $p(x, y, z) = x - y + z$ of abelian groups satisfies $p(x, x, y) \approx y$, not $x$, so it fails the first identity.
In fact no variety of groups other than the trivial variety has a majority term, since such a variety is not congruence-distributive.
