---
tag: Y9KSMY8A1Q
kind: statement
role: theorem
name: Elliott's classification of AF algebras
msc: [46L35, 46L80, 19K14]
uses: [4Y7VENNBVK, BP86XQRZD2, WSH8TY6MK9, KRDR04RQ7N]
about: [4Y7VENNBVK, BP86XQRZD2]
sources:
  - url: https://en.wikipedia.org/wiki/Approximately_finite-dimensional_C*-algebra
---

## Statement

For a unital C*-algebra $A$, let $K_0(A)^+$ be the set of classes of projections in matrix algebras over $A$ in [[K0|BP86XQRZD2]].
Let $[1_A]$ be the class of the unit.
Let $A$ and $B$ be unital [[AF algebras|4Y7VENNBVK]].

1. $A$ and $B$ are isomorphic if and only if there is a group isomorphism $\varphi \colon K_0(A) \to K_0(B)$ with $\varphi(K_0(A)^+) = K_0(B)^+$ and $\varphi([1_A]) = [1_B]$.
2. Every such $\varphi$ is induced by a $*$-isomorphism $\psi \colon A \to B$, that is, $\varphi = \psi_*$.

## Remarks

The proof uses that a $*$-homomorphism between finite-dimensional C*-algebras is determined up to unitary equivalence by its map on $K_0$, which is given by a matrix of multiplicities.
An approximate intertwining argument then builds an isomorphism between the two inductive limits from the isomorphism of their $K_0$-groups.
For non-unital AF algebras the same holds with the scaled ordered group, and the stabilizations $A \otimes \mathcal{K}$ and $B \otimes \mathcal{K}$ are isomorphic if and only if $(K_0(A), K_0(A)^+) \cong (K_0(B), K_0(B)^+)$ as ordered groups.
Example: the UHF algebras $M_{2^\infty}$ and $M_{3^\infty}$ have ordered $K_0$-groups $\Z[1/2]$ and $\Z[1/3]$ inside $\R$, which are not isomorphic, so these algebras are not isomorphic.
The range of the invariant is known: by the Effros–Handelman–Shen theorem, the ordered groups $(K_0(A), K_0(A)^+)$ of AF algebras are exactly the countable [[dimension groups|WSH8TY6MK9]].

## Explanations

### L1 human

An AF algebra is a limit of algebras of matrices.
Elliott's theorem says that such an algebra is completely determined by its $K_0$-group together with its order and the class of the unit.
So a question about infinite-dimensional algebras reduces to a question about ordered abelian groups.

### L2 human

The theorem refines Glimm's classification of UHF algebras by supernatural numbers and Bratteli's description of AF algebras by diagrams.
It was the model for the Elliott classification program, which tries to classify larger classes of simple nuclear C*-algebras by K-theoretic data.
Combined with the Effros–Handelman–Shen theorem, it gives a bijection between isomorphism classes of unital AF algebras and isomorphism classes of countable dimension groups with an order unit.
