---
tag: HEVF97NZ14
kind: definition
name: Acyclic object
msc: [18G10]
defines: F2CMPBHQ02
uses: [Y9CZ3MTNF1, KAN07YC9T2, S1G61TDW0K, NPMC3K6J2F]
sources:
  - url: https://en.wikipedia.org/wiki/Acyclic_object
---

## Definition

Let $\mathcal{A}$ and $\mathcal{B}$ be [[abelian categories|Y9CZ3MTNF1]], and assume that $\mathcal{A}$ has enough injectives.
Let $F \colon \mathcal{A} \to \mathcal{B}$ be a left [[exact|S1G61TDW0K]] [[additive functor|KAN07YC9T2]].
An object $X$ of $\mathcal{A}$ is *$F$-acyclic* if $R^n F(X) = 0$ for every $n \ge 1$, where $R^n F$ are the right [[derived functors|NPMC3K6J2F]] of $F$.
Dually, for a right exact $F$ on a category with enough projectives, $X$ is $F$-acyclic if $L_n F(X) = 0$ for every $n \ge 1$.

## Remarks

Example: every injective object $I$ is $F$-acyclic, because $0 \to I \to I \to 0$ is an injective resolution, and applying $F$ gives a complex with no cohomology in degrees $n \ge 1$.
Non-example: for $F = \Hom_\Z(\Z/2\Z, -)$ on abelian groups, the group $\Z$ is not $F$-acyclic, since $R^1 F(\Z) = \operatorname{Ext}^1_\Z(\Z/2\Z, \Z) \cong \Z/2\Z \ne 0$.
For $F = - \otimes_R N$, every [[flat module|73RYYEVDKA]] is $F$-acyclic, since $\operatorname{Tor}_n^R(M, N) = 0$ for flat $M$ and $n \ge 1$.
If $X \to J^\bullet$ is a resolution by $F$-acyclic objects, then $R^n F(X) \cong H^n(F(J^\bullet))$ for every $n$.
