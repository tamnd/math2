---
tag: 39HWNYW5EF
kind: definition
name: Symbolic method
msc: [05A15]
defines: JP11D90EJC
uses: [0PHAC833JF, 0JHXPVFKT0, 033WGN00BF]
sources:
  - url: https://en.wikipedia.org/wiki/Symbolic_method_(combinatorics)
---

## Definition

A *combinatorial class* is a set $\mathcal{A}$ with a size function $\abs{\cdot} \colon \mathcal{A} \to \N$ such that each set $\mathcal{A}_n = \set{a \in \mathcal{A} : \abs{a} = n}$ is finite.
Its ordinary [[generating function|0PHAC833JF]] is $A(z) = \sum_{n \ge 0} \abs{\mathcal{A}_n} z^n$.
A construction $\Phi$ builds a class from given classes $\mathcal{B}, \mathcal{C}, \ldots$.
It is *admissible* if the counts of $\Phi(\mathcal{B}, \mathcal{C}, \ldots)$ depend only on the counts of $\mathcal{B}, \mathcal{C}, \ldots$.
Let $\mathcal{E}$ be the neutral class, with one object of size $0$, and $\mathcal{Z}$ the atomic class, with one object of size $1$.
The *symbolic method* has two steps:

1. describe the class by an equation built from $\mathcal{E}$, $\mathcal{Z}$ and admissible constructions;
2. replace each construction by its rule on generating functions, which gives an equation for $A(z)$.

## Remarks

For unlabelled classes the basic rules are as follows.
The disjoint union $\mathcal{B} + \mathcal{C}$ gives $B(z) + C(z)$.
The Cartesian product $\mathcal{B} \times \mathcal{C}$, with sizes added, gives $B(z) C(z)$.
The sequence construction $\operatorname{SEQ}(\mathcal{B})$, for $\mathcal{B}_0 = \emptyset$, gives $1 / (1 - B(z))$.
The multiset construction $\operatorname{MSET}(\mathcal{B})$, for $\mathcal{B}_0 = \emptyset$, gives $\exp\big(\sum_{k \ge 1} B(z^k) / k\big)$.
For labelled classes one uses [[exponential generating functions|0JHXPVFKT0]].
Then the labelled product gives $B(z) C(z)$, and, for $\mathcal{B}_0 = \emptyset$, sets give $\exp(B(z))$ and cycles give $\log \frac{1}{1 - B(z)}$.

Example: binary trees satisfy $\mathcal{B} = \mathcal{E} + \mathcal{Z} \times \mathcal{B} \times \mathcal{B}$, with size the number of internal nodes.
The rules give $B(z) = 1 + z B(z)^2$.
Example: permutations are labelled sets of cycles, so their exponential generating function is $\exp\big(\log \frac{1}{1 - z}\big) = \frac{1}{1 - z}$, which gives $n!$.

Non-example: the operation "keep the objects of $\mathcal{B}$ that are trees of height at most $2$" is not admissible.
Its counts depend on the inner structure of the objects of $\mathcal{B}$, and not only on the numbers $\abs{\mathcal{B}_n}$.
