---
tag: Z7R8J71SJN
kind: statement
role: theorem
name: Sard's theorem
msc: [58K05, 57R45, 26B10]
uses: [0YTCMFB4HC, 047NDTEPCV, 0V33BNKZ9S]
about: [0YTCMFB4HC]
sources:
  - url: https://en.wikipedia.org/wiki/Sard%27s_theorem
same_as:
  wikidata: Q583147
  wikipedia: Sard's theorem
---

## Statement

Let $n, m \ge 1$, let $U \subseteq \R^n$ be open, and let $f \colon U \to \R^m$ be of class $C^k$, where $k \ge \max(n - m + 1, 1)$.
A point $x \in U$ is a [[critical point|0YTCMFB4HC]] of $f$ if the [[Jacobian matrix|047NDTEPCV]] $Df(x)$ has rank less than $m$.
A critical value of $f$ is the image $f(x)$ of a critical point $x$.
Then the set of critical values of $f$ has Lebesgue measure zero in $\R^m$.

## Remarks

When $n < m$, every point is critical, and the theorem says that the image $f(U)$ of a $C^1$ map is a null set.
In the case $n = m$, the idea is this.
Near a critical point, $f$ squeezes a small cube of side $r$ into a set of volume $o(r^n)$, because $Df(x)$ is singular.
Covering the critical set by small cubes then gives total volume as small as one wants.
The general case uses induction on $n$ and needs the higher smoothness to control the Taylor expansion along the critical set.
Example: $f(x) = x^2$ on $\R$ has the single critical point $0$ and the single critical value $0$.
The smoothness hypothesis cannot be dropped.
Hassler Whitney constructed a $C^1$ function on $\R^2$ that is not constant on a connected arc of critical points, so its critical values fill an interval.

## Explanations

### L1 human

A critical value is a value that a map takes at a point where it flattens out.
Sard's theorem says that a smooth enough map has very few critical values: they form a set of measure zero.
So a value picked at random is almost surely a regular value.

### L2 human

The complement of a null set is dense, so regular values are dense in $\R^m$.
If $y$ is a regular value and $f^{-1}(y)$ is not empty, the implicit function theorem shows that $f^{-1}(y)$ is a submanifold of dimension $n - m$.
This makes Sard's theorem a basic tool of differential topology, for example in transversality arguments and in the definition of the degree of a map.
The same statement holds for smooth maps between manifolds, by working in charts.
