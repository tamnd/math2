---
tag: R0DSZPRG6T
kind: statement
role: theorem
name: Hilbert's syzygy theorem
msc: [13D02, 13D05, 13F20]
uses: [04C5ZBG1WT, 0SDC934R52, 8KB4SQGC0C, 05QY1VEBYD, HK2AA1YSQ2, 0DZ9DKAKZR]
about: [HK2AA1YSQ2, GWA0T1WKCN]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert's_syzygy_theorem
same_as:
  wikidata: Q779220
  wikipedia: Hilbert's syzygy theorem
---

## Statement

Let $K$ be a [[field|04C5ZBG1WT]], let $n \ge 0$, and let $S = K[x_1, \ldots, x_n]$ be the [[polynomial ring|0SDC934R52]], [[graded|8KB4SQGC0C]] by degree.
Let $M$ be a [[finitely generated|05QY1VEBYD]] graded $S$-module.
Then $M$ has a graded [[free resolution|HK2AA1YSQ2]]
$$0 \to F_m \to F_{m-1} \to \cdots \to F_0 \to M \to 0$$
by finitely generated graded [[free|0DZ9DKAKZR]] $S$-modules $F_i$, with homogeneous maps of degree $0$, of length $m \le n$.

## Remarks

One proof uses the [[Koszul complex|YZY11W08SD]] of $x_1, \ldots, x_n$, which is a free resolution of $K = S/(x_1, \ldots, x_n)$ of length $n$.
It shows that $\operatorname{Tor}_i^S(M, K) = 0$ for $i > n$, and the length of a minimal graded free resolution of $M$ is the largest $i$ with $\operatorname{Tor}_i^S(M, K) \ne 0$.
The bound $n$ is sharp: for $n = 2$, the resolution $0 \to S \xrightarrow{(-y,\, x)^T} S^2 \xrightarrow{(x \;\; y)} S \to K \to 0$ of $K = S/(x, y)$ has length $2$, and no shorter resolution exists.
The same method shows that the [[global dimension|GWA0T1WKCN]] of $K[x_1, \ldots, x_n]$ is $n$.

## Explanations

### L1 human

A syzygy is a relation among generators, and a second syzygy is a relation among relations.
Hilbert showed that for modules over a polynomial ring in $n$ variables this process stops after at most $n$ steps.
So the structure of such a module is described by finitely many finite lists of polynomials.

### L2 human

The theorem says that the polynomial ring $K[x_1, \ldots, x_n]$ has global dimension $n$.
It is closely related to [[Serre's theorem on regular local rings|93RQRG9R1P]], since the localizations of $K[x_1, \ldots, x_n]$ at maximal ideals are regular.
The minimal free resolution gives the graded [[Betti numbers|3B1743XS7S]] of $M$, and Gröbner bases make it computable.
