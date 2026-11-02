---
tag: TYYS649FAJ
kind: definition
name: Subdirectly irreducible algebra
msc: [08B26]
defines: DASF939439
uses: [QJGPT2W0FT, DCSXXT4SER, REE07CSXHR, 88WN3AD2VQ]
sources:
  - url: https://en.wikipedia.org/wiki/Subdirectly_irreducible_algebra
---

## Definition

Let $\mathbf{A}$ be an [[algebra|QJGPT2W0FT]] with universe $A$ having at least two elements, and let $\Delta_A = \set{(a, a) : a \in A}$.
The algebra $\mathbf{A}$ is *subdirectly irreducible* when the set of [[congruences|DCSXXT4SER]] on $\mathbf{A}$ different from $\Delta_A$ has a least element.
This least element is called the *monolith* of $\mathbf{A}$.

## Remarks

Equivalently, $\mathbf{A}$ is subdirectly irreducible when, for every subdirect embedding $\alpha \colon \mathbf{A} \to \prod_{i \in I} \mathbf{A}_i$, some composite $\pi_i \circ \alpha$ is an isomorphism.
This is the form that gives the name, through [[subdirect products|88WN3AD2VQ]].
In terms of the [[congruence lattice|REE07CSXHR]]: the intersection of all congruences other than $\Delta_A$ is not $\Delta_A$.

Example: the group $\Z/4\Z$ is subdirectly irreducible.
Its congruences come from the subgroups $\set{0} \subset \set{0, 2} \subset \Z/4\Z$, which form a chain, so the congruence of $\set{0, 2}$ is the monolith.

Non-example: the group $\Z/6\Z$ is not subdirectly irreducible.
The congruences modulo $2$ and modulo $3$ are both different from $\Delta$, and their intersection is $\Delta$, so there is no least one.

The ring $\Z$ is not subdirectly irreducible either, since the congruences modulo the primes intersect in $\Delta_\Z$.
