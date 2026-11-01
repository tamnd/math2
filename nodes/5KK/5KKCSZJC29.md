---
tag: 5KKCSZJC29
kind: statement
role: theorem
name: Mergelyan's theorem
msc: ["30E10", 41A10]
uses: [00R0X1WGPX, 0P27W9RW0G, 0DG0Z72CQD, 0C38S0KMJK, 0D939CMME7, 08HJRTG5N7]
about: [0DG0Z72CQD]
sources:
  - url: https://en.wikipedia.org/wiki/Mergelyan%27s_theorem
same_as:
  wikidata: Q1964537
  wikipedia: Mergelyan's theorem
---

## Statement

Let $K \subseteq \C$ be a [[compact set|00R0X1WGPX]] such that $\C \setminus K$ is [[connected|0D939CMME7]].
Let $f \colon K \to \C$ be [[continuous|0P27W9RW0G]] on $K$ and [[holomorphic|0DG0Z72CQD]] on the [[interior|0C38S0KMJK]] of $K$.
Then for every $\varepsilon > 0$ there is a polynomial $p$ such that
$$\abs{f(z) - p(z)} < \varepsilon \quad \text{for all } z \in K.$$

## Remarks

The conditions on $f$ are necessary, since a [[uniform limit|08HJRTG5N7]] of polynomials on $K$ is continuous on $K$ and holomorphic on its interior.
The condition on $K$ is also necessary.
On the unit circle, $f(z) = 1/z$ is continuous and the interior is empty, yet $f$ is not a uniform limit of polynomials.
Indeed $\oint p(z) \, dz = 0$ for polynomials while $\oint z^{-1} \, dz = 2\pi i$.

Two special cases were known before.
If $f$ is holomorphic on a neighbourhood of $K$, the result is [[Runge's theorem|6DG4CTGXJD]].
If $K$ is the closed unit disc, it suffices to approximate $f$ by $f(rz)$ with $r < 1$ and then truncate its Taylor series.
The general proof is much harder; it uses estimates on Cauchy integrals that are uniform over the shape of $K$.

Example: let $K = [0, 1]$, a segment with empty interior and connected complement.
The theorem says every continuous function on $[0, 1]$ is a uniform limit of complex polynomials, which recovers the Weierstrass approximation theorem.

## Explanations

### L1 human

If a compact set in the plane has no holes, then every function that is continuous on it and holomorphic inside it can be approximated by polynomials.
The approximation is uniform: the error is small at every point of the set at once.
Without holes there is no "hidden" Cauchy integral that polynomials cannot imitate.
This is the best possible result of its kind.

### L2 human

Mergelyan's theorem completes the theory of polynomial approximation on compact sets with connected complement.
It contains the Weierstrass approximation theorem and its complex analogue for sets with empty interior.
For sets with holes, the question of approximation by rational functions is harder and is described by analytic capacity (Vitushkin's theory).
On unbounded closed sets the corresponding statement is [[Arakelyan's theorem|1S20A3R659]].
