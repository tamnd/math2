---
tag: Z97S62SRYV
kind: definition
name: Kasparov product
msc: [19K35, 46L80]
defines: 57D1AGY7DJ
uses: [1W9Q7W378J, KBPJH3J56K]
sources:
  - url: https://en.wikipedia.org/wiki/KK-theory
---

## Definition

Let $A$ and $D$ be separable C*-algebras and $B$ a $\sigma$-unital C*-algebra.
Let $x \in KK(A, D)$ be the class of a Kasparov module $(E_1, \varphi_1, F_1)$ and $y \in KK(D, B)$ the class of $(E_2, \varphi_2, F_2)$, as in [[KK-theory|1W9Q7W378J]].
Let $E = E_1 \hat{\otimes}_{\varphi_2} E_2$ be the graded interior tensor product, a [[Hilbert C*-module|KBPJH3J56K]] over $B$.
For $\xi \in E_1$ homogeneous of degree $\partial \xi$, let $T_\xi \colon E_2 \to E$ be the operator $T_\xi(\eta) = \xi \otimes \eta$.
An operator $F \in \mathcal{L}(E)$ is an *$F_2$-connection* if for every homogeneous $\xi \in E_1$,
$$T_\xi F_2 - (-1)^{\partial \xi} F T_\xi \in \mathcal{K}(E_2, E) \quad \text{and} \quad F_2 T_\xi^* - (-1)^{\partial \xi} T_\xi^* F \in \mathcal{K}(E, E_2).$$
The *Kasparov product* $x \otimes_D y \in KK(A, B)$ is the class of $(E, \varphi_1 \hat{\otimes} 1, F)$, where $F \in \mathcal{L}(E)$ is any odd operator such that:

1. $(E, \varphi_1 \hat{\otimes} 1, F)$ is a Kasparov $(A, B)$-module;
2. $F$ is an $F_2$-connection;
3. for all $a \in A$, $\varphi_1(a) [F_1 \hat{\otimes} 1, F] \varphi_1(a)^*$ is positive modulo $\mathcal{K}(E)$, where $[\cdot, \cdot]$ is the graded commutator.

## Remarks

Kasparov proved that such an $F$ exists and that the class does not depend on the choices of $F$ and of the representing modules.
The description by connections is due to Connes and Skandalis.
The product is bilinear and associative, and it is functorial in all three algebras.
Example: if $x = [\alpha]$ and $y = [\beta]$ come from $*$-homomorphisms $\alpha \colon A \to D$ and $\beta \colon D \to B$, then $x \otimes_D y = [\beta \circ \alpha]$.
Example: let $A = B = \C$, let $D$ be unital, and let $(H, \rho, F)$ be an even Fredholm module over $D$.
The product of $[p] \in KK(\C, D) \cong K_0(D)$ with its class is the index of $\rho(p) F \rho(p)$ from $\rho(p) H^{(0)}$ to $\rho(p) H^{(1)}$.
This is the pairing of K-theory with K-homology.
The operator $1 \hat{\otimes} F_2$ is in general not defined on $E$, because $F_2$ need not commute with $\varphi_2(D)$; the connection condition replaces it.
