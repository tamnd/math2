---
tag: YWTERZZME5
kind: definition
name: Isomorphism
msc: [08A05, 03C07]
defines: PZMGQMDN25
uses: [983GZBQYT4, KBXSZC6BV1, 0GG9TVW90M]
sources:
  - url: https://en.wikipedia.org/wiki/Isomorphism
---

## Definition

Let $\sigma$ be a signature and let $\mathbf{A}$ and $\mathbf{B}$ be $\sigma$-[[structures|983GZBQYT4]] with domains $A$ and $B$.
An *isomorphism* from $\mathbf{A}$ to $\mathbf{B}$ is a [[bijection|0GG9TVW90M]] $h \colon A \to B$ such that both $h$ and its inverse $h^{-1} \colon B \to A$ are [[homomorphisms|KBXSZC6BV1]].
The structures $\mathbf{A}$ and $\mathbf{B}$ are *isomorphic*, written $\mathbf{A} \cong \mathbf{B}$, if there is an isomorphism from $\mathbf{A}$ to $\mathbf{B}$.

## Remarks

The condition on $h^{-1}$ means that $h$ also reflects relations: $(a_1, \dots, a_n) \in R^{\mathbf{A}}$ if and only if $(h(a_1), \dots, h(a_n)) \in R^{\mathbf{B}}$.
For a signature without relation symbols, the inverse of a bijective homomorphism is automatically a homomorphism, so an isomorphism is the same as a bijective homomorphism.

Example: the map $x \mapsto e^x$ is an isomorphism from $(\R, +, 0)$ to $(\R_{>0}, \cdot, 1)$, because it is a bijection with $e^{x + y} = e^x e^y$ and $e^0 = 1$; its inverse is $\ln$.

Non-example: let $A = \set{1, 2}$ with the empty binary relation and $B = \set{1, 2}$ with the relation $\le$.
The identity map is a bijective homomorphism from $A$ to $B$, but its inverse does not preserve the relation, since $1 \le 2$ in $B$ while $(1, 2)$ is not related in $A$.
