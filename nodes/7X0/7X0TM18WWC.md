---
tag: 7X0TM18WWC
kind: statement
role: theorem
name: Plus equals Q theorem
msc: [19D06]
uses: [J9XP7CS943, XFGZFM8PC6, BK3091CPGF, BFFA03GE3V, 2JFF5F3EGF, XZG6MTSWCN, Q14JS2MA1C, NJQY3GHY7H]
about: [J9XP7CS943, XFGZFM8PC6]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_K-theory
---

## Statement

Let $R$ be a ring with identity.
Let $\mathcal{P}(R)$ be the exact category of finitely generated [[projective|BFFA03GE3V]] left $R$-modules, with the split short exact sequences.
Let $BQ\mathcal{P}(R)$ be the classifying space of its [[Q-construction|J9XP7CS943]].
Let $BGL(R)^+$ be the [[plus construction|XFGZFM8PC6]] of the [[classifying space|BK3091CPGF]] $BGL(R)$ with respect to the commutator subgroup of $GL(R)$.
Then there is a [[homotopy equivalence|XZG6MTSWCN]]
$$\Omega BQ\mathcal{P}(R) \simeq K_0(R) \times BGL(R)^+,$$
where $\Omega$ is the [[loop space|2JFF5F3EGF]] and the group [[$K_0(R)$|Q14JS2MA1C]] has the discrete topology.
In particular $\pi_{n+1}(BQ\mathcal{P}(R)) \cong \pi_n(BGL(R)^+)$ for all $n \ge 1$, and $\pi_1(BQ\mathcal{P}(R)) \cong K_0(R)$.

## Remarks

The theorem is due to Quillen; a proof was written by Grayson.
The proof passes through a third model, the category $S^{-1}S$.
It is built from the groupoid $S$ of finitely generated projective modules and their isomorphisms, as in the [[K-theory of a symmetric monoidal category|NJQY3GHY7H]].
One shows first that $\Omega BQ\mathcal{P}(R) \simeq B(S^{-1}S)$, and then, by the group completion theorem, that $B(S^{-1}S) \simeq K_0(R) \times BGL(R)^+$.

At work in degree $1$: the theorem gives $\pi_2(BQ\mathcal{P}(R)) \cong \pi_1(BGL(R)^+) = GL(R)/[GL(R), GL(R)]$, the classical group $K_1(R)$.
So the K-groups defined by the Q-construction contain the classical $K_0$ and $K_1$.

## Explanations

### L1 human

There are two ways to define the higher K-groups of a ring.
One kills the elementary matrices in a space built from invertible matrices; the other builds a space from projective modules and their subquotients.
The theorem says the two ways give the same groups.
So one can use whichever is easier for the problem at hand.

### L2 human

The plus construction is good for computations with matrices, such as the K-theory of finite fields, and for products.
The Q-construction applies to any exact category and gives the resolution, dévissage and localization theorems.
The theorem lets results from one side be used on the other.
For example, the localization sequence for a Dedekind domain is proved with the Q-construction, but its terms are the groups $\pi_n(BGL(R)^+)$.
