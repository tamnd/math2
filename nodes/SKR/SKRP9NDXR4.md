---
tag: SKRP9NDXR4
kind: statement
role: theorem
name: Euler–Gauss limit formula
msc: [33B15]
uses: [0V3FZMVB4K, 0NSD1TPHR0]
about: [0H5SYBSED9]
sources:
  - url: https://en.wikipedia.org/wiki/Gamma_function
---

## Statement

Let $\Gamma$ be the [[gamma function|0V3FZMVB4K]], extended to a [[meromorphic function|0NSD1TPHR0]] on $\C$.
For every $z \in \C \setminus \set{0, -1, -2, \ldots}$,
$$\Gamma(z) = \lim_{n \to \infty} \frac{n! \; n^{z}}{z (z + 1) (z + 2) \cdots (z + n)},$$
where $n^z = e^{z \ln n}$.

## Remarks

For $\operatorname{Re} z > 0$, the quotient equals $\int_0^n t^{z-1} (1 - t/n)^n \, dt$, by repeated integration by parts.
Since $(1 - t/n)^n$ increases to $e^{-t}$, the [[dominated convergence theorem|BYNV84PF86]] gives the limit $\int_0^\infty t^{z-1} e^{-t}\,dt = \Gamma(z)$.
For other $z$, the functional equation $\Gamma(z + 1) = z\Gamma(z)$ moves the argument into the half-plane, and the quotients transform in the same way up to a factor that tends to $1$.
Example: at $z = 1$ the quotient is $\frac{n!\, n}{(n+1)!} = \frac{n}{n+1} \to 1 = \Gamma(1)$.
In Mathlib the statement is `Complex.GammaSeq_tendsto_Gamma`.

## Explanations

### L1 human

The formula computes the gamma function as a limit of simple fractions built from factorials and powers.
It was Euler's first way to extend the factorial to non-integer arguments, and Gauss used it as the definition.

### L2 human

The limit makes sense for every allowed complex $z$ at once, so it can serve as a definition of the meromorphic gamma function.
Taking reciprocals and rewriting $n^z = \exp\big(z(\ln n - 1 - \tfrac12 - \cdots - \tfrac1n)\big)\exp\big(z(1 + \cdots + \tfrac1n)\big)$ turns it into the [[Weierstrass product|53MZ2DGDTQ]].
It is also the limit that appears in the proof of the [[Bohr–Mollerup theorem|QFF87AXWN2]].
