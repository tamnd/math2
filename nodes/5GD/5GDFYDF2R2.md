---
tag: 5GDFYDF2R2
kind: statement
role: theorem
name: Cartan–Iwasawa–Malcev theorem
msc: ["22E15", 22C05]
uses: [7JBRGCVJRB, T2EB8R9HEV, 0TVJZYB6SH, A5JB9JQKR0]
about: [T2EB8R9HEV]
sources:
  - url: https://en.wikipedia.org/wiki/Maximal_compact_subgroup
---

## Statement

Let $G$ be a connected [[Lie group|7JBRGCVJRB]].
Then:

1. $G$ has a [[maximal compact subgroup|T2EB8R9HEV]], and each compact subgroup of $G$ is contained in a maximal compact subgroup;
2. any two maximal compact subgroups of $G$ are conjugate in $G$;
3. each maximal compact subgroup $K$ is connected, and $G$ is homeomorphic to $K \times \R^n$ for some $n \ge 0$.

## Remarks

For semisimple groups with finite center, the result follows from the [[Cartan decomposition|A5JB9JQKR0]] $G = K \exp(\mathfrak{p})$ and from Cartan's fixed point theorem.
That theorem says that a compact group acting by isometries on the nonpositively curved space $G/K$ has a fixed point.
So each compact subgroup lies in the stabilizer of a point, a conjugate of $K$.
The general case is due to Malcev and Iwasawa.

Example: $G = \mathrm{GL}_n^+(\R)$, the invertible real matrices of positive determinant.
A maximal compact subgroup is $\mathrm{SO}(n)$, and the polar decomposition gives a homeomorphism of $G$ with $\mathrm{SO}(n) \times \R^{n(n+1)/2}$, the second factor being the symmetric matrices.

The conclusions extend to Lie groups with finitely many connected components, except that $K$ then has one component for each component of $G$.
For groups with infinitely many components, maximal compact subgroups may fail to exist.

## Explanations

### L1 human

Every connected Lie group contains a largest bounded subgroup, unique up to conjugation.
The whole group is this bounded subgroup times a flat space with no holes.
So all the topology of the group, for example its loops and its holes, lives in the compact part.

### L2 human

The theorem reduces the homotopy type of a connected Lie group to that of a compact Lie group.
For example $\mathrm{SL}_2(\R)$ has the homotopy type of a circle, and $\mathrm{SL}_n(\C)$ that of $\mathrm{SU}(n)$, which is simply connected.
It also says that the classifying space of $G$ is that of $K$, which is why characteristic classes of $G$-bundles only depend on $K$.
Uniqueness up to conjugacy makes $K$ an invariant of $G$, used for example to define the symmetric space $G/K$.
