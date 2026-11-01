---
tag: HS9VYE19Z2
kind: definition
name: Castelnuovo–Mumford regularity
msc: [13D02, 13D45]
defines: Y76T2DQJPQ
uses: [0SDC934R52, 05QY1VEBYD, 8KB4SQGC0C, 3B1743XS7S, HK2AA1YSQ2, 6JB30BXDA2]
sources:
  - url: https://en.wikipedia.org/wiki/Castelnuovo–Mumford_regularity
---

## Definition

Let $k$ be a field and let $S = k[x_1, \ldots, x_n]$ be the [[polynomial ring|0SDC934R52]] graded by total degree.
For an integer $j$, let $S(-j)$ be $S$ with grading shifted so that $S(-j)_d = S_{d - j}$.
Let $M \ne 0$ be a [[finitely generated|05QY1VEBYD]] [[graded|8KB4SQGC0C]] $S$-module.
Let
$$0 \to F_p \to \cdots \to F_1 \to F_0 \to M \to 0$$
be a minimal graded free [[resolution|HK2AA1YSQ2]] of $M$, with $F_i = \bigoplus_j S(-j)^{\beta_{i,j}}$.
The numbers $\beta_{i,j}$ are the graded [[Betti numbers|3B1743XS7S]] of $M$.
The *Castelnuovo–Mumford regularity* of $M$ is
$$\operatorname{reg} M = \max \set{ j - i : \beta_{i,j} \ne 0 }.$$

## Remarks

Let $f \in S$ be homogeneous of degree $d \ge 1$ and $M = S/(f)$.
The minimal resolution is $0 \to S(-d) \to S \to M \to 0$, so $\beta_{0,0} = 1$ and $\beta_{1,d} = 1$.
Hence $\operatorname{reg} M = \max(0, d - 1) = d - 1$.

Minimality of the resolution is needed.
Take $S = k[x]$ and $M = S/(x)$, so that $\operatorname{reg} M = 0$.
Add the exact summand $S(-5) \to S(-5)$ in homological degrees $1$ and $0$.
The result is a non-minimal resolution with the pair $(i, j) = (0, 5)$, and it would give the wrong value $5$.

An equivalent form uses [[local cohomology|6JB30BXDA2]] with respect to $\mathfrak{m} = (x_1, \ldots, x_n)$: $\operatorname{reg} M = \max_i \set{ a_i(M) + i }$, where $a_i(M)$ is the largest degree $d$ with $H^i_{\mathfrak{m}}(M)_d \ne 0$, and the maximum is over the $i$ with $H^i_{\mathfrak{m}}(M) \ne 0$.
For a nonzero proper homogeneous ideal $I$, one has $\operatorname{reg} I = \operatorname{reg}(S/I) + 1$.
