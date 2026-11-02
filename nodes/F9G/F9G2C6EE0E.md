---
tag: F9G2C6EE0E
kind: definition
name: Subdirect product
msc: [08B26]
defines: 88WN3AD2VQ
uses: [QJGPT2W0FT, WJ73XYBNE4, 01RVCMSN5N]
sources:
  - url: https://en.wikipedia.org/wiki/Subdirect_product
---

## Definition

Let $(\mathbf{A}_i)_{i \in I}$ be a family of [[algebras|QJGPT2W0FT]] of the same signature, and let $\pi_j$ denote the projection of the [[direct product|WJ73XYBNE4]] $\prod_{i \in I} \mathbf{A}_i$ onto $\mathbf{A}_j$.
A *subdirect product* of the family is a subalgebra $\mathbf{B}$ of $\prod_{i \in I} \mathbf{A}_i$ such that $\pi_j$ restricted to $B$ is [[surjective|01RVCMSN5N]] onto $A_j$ for every $j \in I$.
An embedding $\alpha \colon \mathbf{A} \to \prod_{i \in I} \mathbf{A}_i$ is *subdirect* when $\alpha(\mathbf{A})$ is a subdirect product.

## Remarks

Let $(\theta_i)_{i \in I}$ be a family of congruences on an algebra $\mathbf{A}$.
The map $a \mapsto (a/\theta_i)_{i \in I}$ is a subdirect embedding of $\mathbf{A}$ into $\prod_{i \in I} \mathbf{A}/\theta_i$ if and only if $\bigcap_{i \in I} \theta_i = \Delta_A$.

Example: the map $n \mapsto (n \bmod p)_p$ is a subdirect embedding of the ring $\Z$ into $\prod_{p \text{ prime}} \Z/p\Z$.
It is a homomorphism, it is injective because a nonzero integer has only finitely many prime divisors, and each coordinate map $\Z \to \Z/p\Z$ is onto.

Non-example: the subgroup $\set{(x, 0) : x \in \Z/2\Z}$ of $\Z/2\Z \times \Z/2\Z$ is not a subdirect product.
Its projection onto the second factor is $\set{0}$, not all of $\Z/2\Z$.
