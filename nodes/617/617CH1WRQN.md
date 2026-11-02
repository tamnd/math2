---
tag: 617CH1WRQN
kind: definition
name: Deformation quantization
msc: [53D55, 16S80]
defines: 3MKSJ1J04K
uses: [A2KQ49Y4NF, 2S0MXDT4YH, 0V33BNKZ9S, 033WGN00BF, QP92G4ZGJE]
sources:
  - url: https://en.wikipedia.org/wiki/Deformation_quantization
---

## Definition

Let $M$ be a [[Poisson manifold|A2KQ49Y4NF]] with [[Poisson bracket|2S0MXDT4YH]] $\set{\cdot, \cdot}$, and let $C^\infty(M)$ be the algebra of real [[smooth functions|0V33BNKZ9S]] on $M$.
Let $C^\infty(M)[\![\hbar]\!]$ be the space of [[formal power series|033WGN00BF]] in $\hbar$ with coefficients in $C^\infty(M)$.
A *star product* on $M$ is an $\R[\![\hbar]\!]$-bilinear associative product $*$ on $C^\infty(M)[\![\hbar]\!]$ such that:

1. $f * g = \sum_{n \ge 0} \hbar^n B_n(f, g)$ for $f, g \in C^\infty(M)$, where each $B_n$ is a bidifferential operator;
2. $B_0(f, g) = fg$;
3. $B_1(f, g) - B_1(g, f) = \set{f, g}$;
4. $1 * f = f * 1 = f$.

A *deformation quantization* of $M$ is a choice of star product on $M$.
Two star products are equivalent when they are equivalent as [[formal deformations|QP92G4ZGJE]] by a series of differential operators.

## Remarks

Clause 3 says $f * g - g * f = \hbar \set{f, g} + O(\hbar^2)$.
Many authors use complex coefficients and ask for $i \hbar \set{f, g}$ instead.
Example: the Moyal product on $\R^2$ with coordinates $x, p$ and $\set{f, g} = \partial_x f \, \partial_p g - \partial_p f \, \partial_x g$ is
$$f * g = \sum_{n \ge 0} \frac{1}{n!} \left(\frac{\hbar}{2}\right)^n \sum_{j=0}^{n} (-1)^j \binom{n}{j} (\partial_x^{n-j} \partial_p^{j} f)(\partial_x^{j} \partial_p^{n-j} g).$$
Its term $B_1(f, g) = \frac{1}{2}\set{f, g}$ is antisymmetric, so clause 3 holds, and $x * p - p * x = \hbar$.
Non-example: the undeformed product $f * g = fg$ satisfies clauses 1, 2 and 4, but fails clause 3 whenever the bracket is nonzero.
