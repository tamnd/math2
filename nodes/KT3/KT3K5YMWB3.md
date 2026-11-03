---
tag: KT3K5YMWB3
kind: definition
name: KK-theory
msc: [19K35, 46L80]
defines: 1W9Q7W378J
uses: [M2WFY1D3SZ, KBPJH3J56K]
sources:
  - url: https://en.wikipedia.org/wiki/KK-theory
---

## Definition

Let $A$ be a separable [[C*-algebra|M2WFY1D3SZ]] and $B$ a $\sigma$-unital C*-algebra, both with the trivial grading.
For a [[Hilbert C*-module|KBPJH3J56K]] $E$ over $B$, let $\mathcal{L}(E)$ be the C*-algebra of adjointable operators on $E$.
Let $\mathcal{K}(E)$ be its ideal of compact operators, the closed span of the operators $\theta_{x, y}(z) = x \langle y, z \rangle$.
A *Kasparov $(A, B)$-module* is a triple $(E, \varphi, F)$ where:

1. $E = E^{(0)} \oplus E^{(1)}$ is a countably generated $\Z/2$-graded Hilbert $B$-module;
2. $\varphi \colon A \to \mathcal{L}(E)$ is a $*$-homomorphism into the even operators, those that preserve $E^{(0)}$ and $E^{(1)}$;
3. $F \in \mathcal{L}(E)$ is odd, that is, it maps $E^{(0)}$ to $E^{(1)}$ and $E^{(1)}$ to $E^{(0)}$;
4. for all $a \in A$, the operators $(F^2 - 1)\varphi(a)$, $(F - F^*)\varphi(a)$ and $F \varphi(a) - \varphi(a) F$ lie in $\mathcal{K}(E)$.

Two Kasparov $(A, B)$-modules are *homotopic* if they are the images, under evaluation at $0$ and at $1$, of a Kasparov $(A, C([0, 1], B))$-module.
The group $KK(A, B)$ is the set of homotopy classes of Kasparov $(A, B)$-modules, with addition given by the direct sum of modules.

## Remarks

The direct sum makes $KK(A, B)$ an abelian group; modules with all operators in clause 4 equal to $0$ represent $0$.
Example: a $*$-homomorphism $\varphi \colon A \to B$ gives the class of $(B \oplus 0, \varphi, 0)$, where $B$ is a Hilbert module over itself with $\mathcal{K}(B) = B$; clause 4 holds since $\varphi(a) \in B = \mathcal{K}(B)$.
Example: for $A = B = \C$, a module is essentially a Hilbert space $E^{(0)} \oplus E^{(1)}$ with an odd Fredholm operator, and $[(E, \id, F)] \mapsto \operatorname{ind}(F|_{E^{(0)}})$ gives $KK(\C, \C) \cong \Z$.
Non-example: $(\ell^2(\N) \oplus 0, \id, 0)$ as an $(\C, \C)$-module fails clause 4, since $(0^2 - 1) \cdot 1 = -1$ is not compact on an infinite-dimensional space.
The odd groups are $KK^1(A, B) = KK(A, C_0(\R) \otimes B)$, and Bott periodicity holds in both variables.
