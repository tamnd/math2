---
tag: YGSKZFTEX1
kind: statement
role: theorem
name: Gromov's compactness theorem
msc: [53C23, 53C21]
uses: [GT56RTG9X5, 7CBT4SM83Y, 4GTNM0WHDH, 82F5Q4F1S6, 020Q06TYYH, 71AWVBG6KH]
about: [GT56RTG9X5]
sources:
  - url: https://en.wikipedia.org/wiki/Gromov%27s_compactness_theorem_(geometry)
same_as:
  wikidata: Q5610188
  wikipedia: Gromov's compactness theorem (geometry)
---

## Statement

Let $n \ge 2$ be an integer, let $k$ be a real number and let $D > 0$.
Let $\mathcal{M}$ be the class of closed [[Riemannian manifolds|7CBT4SM83Y]] $M$ of dimension $n$ whose [[Ricci curvature|4GTNM0WHDH]] satisfies $\operatorname{Ric} \ge (n - 1) k$ and whose diameter is at most $D$.
Then every sequence in $\mathcal{M}$ has a subsequence that converges in the [[Gromov–Hausdorff sense|GT56RTG9X5]] to a compact metric space.

## Remarks

The proof rests on a criterion of Gromov.
A class of compact metric spaces is precompact for $d_{GH}$ when the diameters are bounded and, for each $\varepsilon > 0$, the number of $\varepsilon$-balls needed to cover each space is bounded.
This is a uniform version of being [[totally bounded|020Q06TYYH]].
For the manifolds in $\mathcal{M}$, the [[Bishop–Gromov inequality|82F5Q4F1S6]] bounds the number of disjoint balls of radius $\varepsilon/2$, and hence the number of covering balls of radius $\varepsilon$.

The limit space need not be a manifold, and its dimension may drop.
For example, the flat tori $\R^2 / (\Z \times \tfrac{1}{m}\Z)$ have $\operatorname{Ric} = 0$ and bounded diameter, and they converge to a circle of length $1$ as $m \to \infty$.
Without the lower curvature bound the statement fails.
Take spheres with $m$ long thin spikes of length $1$ whose tips are pairwise at distance at least $2$.
The diameters stay bounded, but at least $m$ balls of radius $\tfrac{1}{2}$ are needed to cover, so no subsequence converges.

## Explanations

### L1 human

Manifolds whose curvature is not too negative and whose size is bounded cannot be too complicated at any scale.
The theorem says that from any sequence of them one can pick a subsequence that settles down to a limit shape.
The limit may be rougher than the manifolds, for example lower-dimensional.

### L2 human

This is the starting point of the study of limit spaces of manifolds with Ricci curvature bounded below.
Under a lower bound on sectional curvature the limits are [[Alexandrov spaces|71AWVBG6KH]].
The theorem is used to prove finiteness and pinching results by contradiction: take a bad sequence, pass to a limit, and study the limit.
