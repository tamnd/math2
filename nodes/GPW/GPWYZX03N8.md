---
tag: GPWYZX03N8
kind: definition
name: Retract
msc: [08A30, 08A35]
defines: 68PFSGP39B
uses: [QJGPT2W0FT, KBXSZC6BV1]
sources:
  - url: https://en.wikipedia.org/wiki/Section_(category_theory)
---

## Definition

Let $\mathbf{A}$ be an [[algebra|QJGPT2W0FT]] and let $\mathbf{B}$ be a [[subalgebra|7CHG6SD365]] of $\mathbf{A}$ with universe $B$.
The subalgebra $\mathbf{B}$ is a *retract* of $\mathbf{A}$ when there is a [[homomorphism|KBXSZC6BV1]] $r \colon \mathbf{A} \to \mathbf{B}$ with $r(b) = b$ for all $b \in B$.
Such a map $r$ is called a *retraction*.

## Remarks

Up to isomorphism, an algebra $\mathbf{C}$ is a retract of $\mathbf{A}$ when there are homomorphisms $s \colon \mathbf{C} \to \mathbf{A}$ and $r \colon \mathbf{A} \to \mathbf{C}$ with $r \circ s = \id_C$.
Then $s$ is injective and $s(\mathbf{C})$ is a retract of $\mathbf{A}$ in the sense above.

Example: in the group $\Z \times \Z$, the subgroup $\Z \times \set{0}$ is a retract.
The map $r(m, n) = (m, 0)$ is a homomorphism onto $\Z \times \set{0}$ and fixes each $(m, 0)$.

Non-example: the subgroup $2\Z$ of $\Z$ is not a retract.
A homomorphism $r \colon \Z \to 2\Z$ is determined by $x = r(1) \in 2\Z$, and then $r(2) = 2x$.
The condition $r(2) = 2$ forces $x = 1 \notin 2\Z$.
