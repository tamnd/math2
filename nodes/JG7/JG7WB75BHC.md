---
tag: JG7WB75BHC
kind: statement
role: theorem
name: Correspondence theorem for congruences
msc: [08A30]
uses: [QJGPT2W0FT, DCSXXT4SER, N5KE7FH6CX, REE07CSXHR]
about: [REE07CSXHR, N5KE7FH6CX]
sources:
  - url: https://en.wikipedia.org/wiki/Isomorphism_theorems
---

## Statement

Let $\mathbf{A}$ be an [[algebra|QJGPT2W0FT]] with universe $A$ and let $\theta$ be a [[congruence|DCSXXT4SER]] on $\mathbf{A}$.
For a congruence $\psi \supseteq \theta$ on $\mathbf{A}$, put
$$\psi/\theta = \set{(a/\theta, b/\theta) : (a, b) \in \psi}.$$
Then $\psi \mapsto \psi/\theta$ is an isomorphism from the interval $\set{\psi \in \operatorname{Con} \mathbf{A} : \theta \subseteq \psi}$ of the [[congruence lattice|REE07CSXHR]] onto $\operatorname{Con}(\mathbf{A}/\theta)$.

## Remarks

Proof idea.
Let $\nu \colon \mathbf{A} \to \mathbf{A}/\theta$ be the natural map of the [[quotient algebra|N5KE7FH6CX]].
For $\psi \supseteq \theta$, the relation $\psi/\theta$ is a congruence, and its preimage under $\nu \times \nu$ is $\psi$ again, because $\psi$ contains $\theta$.
Conversely, the preimage of any congruence on $\mathbf{A}/\theta$ is a congruence on $\mathbf{A}$ containing $\theta$.
These two maps are inverse to each other and preserve inclusion, so they are lattice isomorphisms.

Example: in the group $\Z$, take $\theta$ to be congruence modulo $12$.
The congruences above $\theta$ are congruence modulo $d$ for the divisors $d$ of $12$, and they match the six subgroups of $\Z/12\Z$.

The hypothesis $\psi \supseteq \theta$ is needed.
For $\psi$ not containing $\theta$, the relation $\psi/\theta$ can fail to be transitive, and different $\psi$ can give the same relation.

## Explanations

### L1 human

Gluing elements of an algebra in two steps is the same as gluing them in one step.
So the ways to glue the quotient $\mathbf{A}/\theta$ further are exactly the gluings of $\mathbf{A}$ that are coarser than $\theta$.
The theorem says this matching keeps the order, so the two lattices have the same shape.

### L2 human

This is the general form of the correspondence theorems for groups, rings and modules, where congruences are replaced by normal subgroups, ideals and submodules.
Together with the second isomorphism theorem $(\mathbf{A}/\theta)/(\psi/\theta) \cong \mathbf{A}/\psi$, it shows that a quotient of a quotient is again a quotient.
It is used to prove that $\mathbf{A}/\theta$ is [[simple|9CJCXNYNK8]] exactly when $\theta$ is a maximal proper congruence, and in the proof of [[Birkhoff's subdirect representation theorem|CZF5696TPY]].
