---
tag: QB05EN6HEQ
kind: definition
name: Permuting congruences
msc: [08A30, 08B05]
defines: 2BCES6NPYM
uses: [QJGPT2W0FT, DCSXXT4SER, REE07CSXHR]
sources:
  - url: https://en.wikipedia.org/wiki/Congruence-permutable_algebra
---

## Definition

Let $\mathbf{A}$ be an [[algebra|QJGPT2W0FT]] with universe $A$, and let $\theta$ and $\psi$ be [[congruences|DCSXXT4SER]] on $\mathbf{A}$.
Their relational product is
$$\theta \circ \psi = \set{(a, c) \in A \times A : (a, b) \in \theta \text{ and } (b, c) \in \psi \text{ for some } b \in A}.$$
The congruences $\theta$ and $\psi$ *permute* when $\theta \circ \psi = \psi \circ \theta$.
The algebra $\mathbf{A}$ is *congruence-permutable* when every two congruences on $\mathbf{A}$ permute.

## Remarks

The congruences $\theta$ and $\psi$ permute if and only if $\theta \circ \psi$ is a congruence.
In that case $\theta \circ \psi = \theta \vee \psi$, the join in the [[congruence lattice|REE07CSXHR]].
A congruence-permutable algebra has a modular congruence lattice.

Example: let $G$ be a group and $N$, $M$ normal subgroups, with congruences $a \mathrel{\theta} b \iff a^{-1} b \in N$ and $a \mathrel{\psi} b \iff a^{-1} b \in M$.
Then $(a, c) \in \theta \circ \psi$ if and only if $a^{-1} c \in NM$, and $(a, c) \in \psi \circ \theta$ if and only if $a^{-1} c \in MN$.
Since $NM = MN$ for normal subgroups, $\theta$ and $\psi$ permute.

Non-example: on the set $\set{1, 2, 3}$ with no operations, let $\theta$ have classes $\set{1, 2}, \set{3}$ and $\psi$ have classes $\set{1}, \set{2, 3}$.
Then $(1, 3) \in \theta \circ \psi$ through $b = 2$.
But $(1, 3) \notin \psi \circ \theta$, since the only $b$ with $(1, b) \in \psi$ is $1$, and $(1, 3) \notin \theta$.
