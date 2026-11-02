---
tag: QYVY3DV9K4
kind: statement
role: theorem
name: Cartan's classification of bounded symmetric domains
msc: [32M15, 53C35]
uses: [Y7Q2SNKG0C, FX92PP3HZR, NT4797Z9H8, 9P8VK3H4YZ]
about: [Y7Q2SNKG0C]
sources:
  - url: https://en.wikipedia.org/wiki/Hermitian_symmetric_space
---

## Statement

1. Every [[bounded symmetric domain|Y7Q2SNKG0C]] is [[biholomorphic|FX92PP3HZR]] to a product of irreducible bounded symmetric domains, and the factors are unique up to order and biholomorphism.
2. Every irreducible bounded symmetric domain is biholomorphic to one of the following domains.
   Here $Z^*$ is the conjugate transpose of $Z$, and $M > 0$ means that the Hermitian matrix $M$ is positive definite.
   - type $I_{m,n}$: $\set{Z \in M_{m \times n}(\C) : I_n - Z^* Z > 0}$;
   - type $II_n$: $\set{Z \in M_{n \times n}(\C) : Z^T = -Z,\ I_n - Z^* Z > 0}$;
   - type $III_n$: $\set{Z \in M_{n \times n}(\C) : Z^T = Z,\ I_n - Z^* Z > 0}$;
   - type $IV_n$: $\set{z \in \C^n : \abs{z^T z} < 1,\ 1 - 2 z^* z + \abs{z^T z}^2 > 0}$;
   - two exceptional domains, of complex dimensions $16$ and $27$.

## Remarks

Élie Cartan obtained the classification in 1935.
The proof passes to Lie theory.
A bounded symmetric domain is $G/K$, where $G$ is the identity component of its automorphism group, a semisimple Lie group, and $K$ is a maximal compact subgroup.
Irreducible domains correspond to simple $G$ for which $K$ has a nontrivial centre.
Reading these off from the [[classification of symmetric spaces|9P8VK3H4YZ]] gives the list: $G$ is $SU(m, n)$, $SO^*(2n)$, $Sp(2n, \R)$, $SO_0(n, 2)$, or real forms of $E_6$ and $E_7$.

Example: $I_{m,1}$ is the unit ball of $\C^m$, and $I_{1,1} = III_1$ is the unit disc.
The type $III_n$ domain is the bounded model of the [[Siegel upper half-space|5PTYE97PF6]] of degree $n$.

For small indices some types coincide, so the list is without repetitions only for suitable ranges of the indices.

## Explanations

### L1 human

Bounded symmetric domains are the most symmetric bounded regions in $\C^n$.
The theorem says that there are only four infinite families of them, made of matrices of small norm, plus two exceptional ones, and products of these.
So a seemingly general class of domains is described by an explicit list.

### L2 human

Through the list, analysis on bounded symmetric domains reduces to matrix computations.
The domains are the [[Hermitian symmetric spaces|NT4797Z9H8]] of noncompact type, and each has a compact dual, such as a Grassmannian for type $I$.
Quotients of these domains by arithmetic groups include the Shimura varieties and the moduli spaces of abelian varieties, so the list organises much of the theory of automorphic forms.
