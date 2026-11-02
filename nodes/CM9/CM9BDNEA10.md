---
tag: CM9BDNEA10
kind: statement
role: theorem
name: Makarov's theorem on harmonic measure
msc: [30C85, 31A15, 28A78]
uses: [CFD7BPM51W, SSNFTHZ6YJ, 0QW64ARSHB]
about: [CFD7BPM51W]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_measure
---

## Statement

Let $\Omega \subseteq \C$ be a bounded domain whose boundary $\partial\Omega$ is a Jordan curve.
Let $z \in \Omega$, and let $\omega$ be the [[harmonic measure|CFD7BPM51W]] of $\Omega$ at $z$.
Then:

1. $\omega(E) = 0$ for every Borel set $E \subseteq \partial\Omega$ of [[Hausdorff dimension|SSNFTHZ6YJ]] less than $1$.
2. There is a Borel set $F \subseteq \partial\Omega$ of Hausdorff dimension $1$ with $\omega(\partial\Omega \setminus F) = 0$.

## Remarks

In short, the harmonic measure of a [[simply connected|0QW64ARSHB]] planar domain has dimension exactly $1$, whatever the dimension of the boundary.
Let $f$ be a conformal map from the unit disc onto $\Omega$ with $f(0) = z$.
By Carathéodory's theorem $f$ extends to the circle, and $\omega$ is the image of normalised arc length under this extension.
Idea of the proof: the growth of $\log f'$, a Bloch function, is controlled by a law of the iterated logarithm.
This shows that $f$ distorts the size of small arcs at almost every point only by subpower factors, which gives both parts.
Example: for the domain bounded by the Koch snowflake, the boundary has dimension $\log 4 / \log 3 > 1$, yet $\omega$ is carried by a subset of dimension $1$.
Simple connectivity matters for part 1: let $K$ be the middle-thirds Cantor set, of dimension $\log 2 / \log 3 < 1$ and of positive logarithmic capacity.
The harmonic measure of the complement of $K$ in the Riemann sphere, at $\infty$, is carried by $K$ and so by a set of dimension less than $1$.
The theorem was proved by N. G. Makarov in 1985.

## Explanations

### L1 human

Release a random walker inside a planar region bounded by a single closed curve, and record where it first hits the curve.
Even if the curve is wildly wiggly and has dimension larger than $1$, the hitting places concentrate on a part of dimension exactly $1$.
The walker almost never reaches the deep fjords of the curve.

### L2 human

Makarov's theorem started the study of the dimension of harmonic measure.
For general planar domains, Jones and Wolff showed that harmonic measure is always carried by a set of dimension at most $1$.
In higher dimensions the picture is different.
Bourgain proved a bound strictly below the dimension of the space, and Wolff built domains in $\R^3$ whose harmonic measure has dimension larger than $2$.
The proof links harmonic measure with the boundary behaviour of conformal maps and with probabilistic limit theorems.
