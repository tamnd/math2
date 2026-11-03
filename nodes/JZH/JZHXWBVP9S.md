---
tag: JZHXWBVP9S
kind: conjecture
name: Coarse Baum–Connes conjecture
msc: [19K56, 46L80, 51F30]
uses: [0RN765S7DH, HM2HHE3J51, M2NEP1K5AE, M2WFY1D3SZ, BP86XQRZD2, 41XX3KF72X, 14CB5N0FPW, KEF3ZDF0QH, DXJXVFV79H]
about: [0RN765S7DH, 41XX3KF72X]
sources:
  - url: https://en.wikipedia.org/wiki/Baum–Connes_conjecture
history:
  posed_by: "Nigel Higson and John Roe"
---

## Statement

Let $X$ be a [[proper metric space|0RN765S7DH]] with bounded geometry.
This means that there are a subset $Z \subseteq X$ and a constant $c > 0$ such that every point of $X$ lies within distance $c$ of $Z$.
Moreover, for every $r > 0$, the number of points of $Z$ in a ball of radius $r$ is bounded independently of the centre.
For $d > 0$, let $P_d(Z)$ be the Rips complex.
Its vertex set is $Z$, and its simplices are the finite subsets of $Z$ of diameter at most $d$.
Let $C^*(X)$ be the Roe algebra of $X$.
Fix an ample [[Hilbert space|HM2HHE3J51]] module over $C_0(X)$.
Call a bounded operator $T$ on it locally compact if $fT$ and $Tf$ are [[compact operators|M2NEP1K5AE]] for every compactly supported continuous function $f$ on $X$.
Then $C^*(X)$ is the norm closure of the locally compact operators of finite propagation.
The conjecture states that the coarse assembly map
$$\mu \colon \lim_{d \to \infty} K_*(P_d(Z)) \to K_*(C^*(X))$$
is an isomorphism for $* = 0, 1$.
Here $K_*(P_d(Z))$ is [[K-homology|41XX3KF72X]] and $K_*(C^*(X))$ is the [[K-theory|BP86XQRZD2]] of the [[C*-algebra|M2WFY1D3SZ]] $C^*(X)$.

## Remarks

Both sides depend only on the coarse geometry of $X$: coarsely equivalent spaces give isomorphic groups.
Guoliang Yu proved the conjecture in 2000 for spaces with bounded geometry that admit a coarse embedding into a Hilbert space.
The conjecture is false in general: box spaces built from [[expander graphs|DXJXVFV79H]] give spaces of bounded geometry for which the assembly map is not surjective.
Injectivity of $\mu$ is still open for spaces of bounded geometry.
For a finitely generated group $G$ with its word metric and with a finite model of the classifying space, injectivity of $\mu$ for $G$ implies the [[Novikov conjecture|KEF3ZDF0QH]] for $G$.
The conjecture is a large-scale analogue of the [[Baum–Connes conjecture|14CB5N0FPW]] for groups.

## Explanations

### L1 human

Coarse geometry studies a space as seen from very far away, where only large-scale shape matters.
On one side, one builds simplicial complexes that blur the space at larger and larger scales and takes their K-homology.
On the other side, one builds an operator algebra from operators that move points only a bounded distance and takes its K-theory.
The conjecture says that a natural map from the first to the second is a bijection.
It holds for a large class of spaces, it fails for some spaces built from expander graphs, and its injectivity half has strong consequences for the topology of manifolds.
