---
tag: 31CV5K5SAJ
kind: statement
role: theorem
name: Demailly's regularization of currents
msc: [32U40, 32U05, 32U25]
uses: [FF2P7ER3QT, WVB60RKC3Z, AHYZMSBBNH, BYJHP6A906, BKM0TQSCD9, 2SRQCEB16J]
about: [BYJHP6A906, FF2P7ER3QT]
sources:
  - url: https://en.wikipedia.org/wiki/Positive_current
---

## Statement

Let $\Omega \subseteq \C^n$ be a bounded [[pseudoconvex|AHYZMSBBNH]] domain and let $\varphi$ be a [[plurisubharmonic function|FF2P7ER3QT]] on $\Omega$, not identically $-\infty$.
For each integer $m \ge 1$, let $\mathcal{H}_m$ be the Hilbert space of holomorphic functions $f$ on $\Omega$ with $\int_\Omega \abs{f}^2 e^{-2m\varphi} \, dV < \infty$.
Let $(\sigma_{m,l})_{l \ge 1}$ be an orthonormal basis of $\mathcal{H}_m$, and let
$$\varphi_m = \frac{1}{2m} \log \sum_{l} \abs{\sigma_{m,l}}^2 .$$
Then there are constants $C_1, C_2 > 0$, independent of $m$, such that for all $z \in \Omega$ and all $r$ with $0 < r < \operatorname{dist}(z, \partial\Omega)$:

1. $\varphi(z) - \dfrac{C_1}{m} \le \varphi_m(z) \le \sup_{\abs{\zeta - z} < r} \varphi(\zeta) + \dfrac{1}{m} \log \dfrac{C_2}{r^n}$;
2. $\nu(\varphi, z) - \dfrac{n}{m} \le \nu(\varphi_m, z) \le \nu(\varphi, z)$, where $\nu$ denotes the [[Lelong number|WVB60RKC3Z]].

In particular $\varphi_m$ converges to $\varphi$ pointwise and in $L^1_{\mathrm{loc}}(\Omega)$ as $m \to \infty$.

## Remarks

Each $\varphi_m$ is plurisubharmonic and has analytic singularities: locally it is $\frac{1}{2m} \log \sum \abs{g_j}^2$ plus a bounded function, for finitely many holomorphic $g_j$, which generate the [[multiplier ideal|BKM0TQSCD9]] $\mathcal{I}(m\varphi)$.
Proof idea: $\varphi_m(z) = \frac{1}{m} \sup\set{\log\abs{f(z)} : f \in \mathcal{H}_m, \norm{f} \le 1}$, so it is the logarithm of a weighted Bergman kernel on the diagonal.
The upper bound follows from the mean value inequality for $\abs{f}^2$ on the ball of radius $r$ around $z$.
The lower bound follows from the [[Ohsawa–Takegoshi extension theorem|2SRQCEB16J]], which gives $f \in \mathcal{H}_m$ with $f(z) = e^{m\varphi(z)}$ and $\norm{f}$ bounded independently of $z$ and $m$.
The Lelong number inequalities follow from these bounds.
Example: for $\varphi = \log\abs{z}$ on the unit disc of $\C$, $\nu(\varphi, 0) = 1$, and the bounds force $1 - \frac{1}{m} \le \nu(\varphi_m, 0) \le 1$.
The method can be globalised with a partition of unity.
On a compact complex manifold, it approximates a closed [[positive current|BYJHP6A906]] of bidegree $(1, 1)$ by closed currents in the same cohomology class.
The approximating currents have analytic singularities, lose only a small amount of positivity, and have Lelong numbers converging to those of the current.

## Explanations

### L1 human

Plurisubharmonic functions can have very complicated singularities.
The theorem replaces such a function by a sequence of simpler ones, built from logarithms of sums of squares of holomorphic functions.
The simpler functions converge to the original one, and their singularities converge too, measured by Lelong numbers.

### L2 human

This is the main regularisation tool of analytic methods in algebraic geometry.
Functions with analytic singularities can be resolved by blowing up, so statements about them reduce to divisors with normal crossings.
The global version for closed positive $(1,1)$-currents is used to study pseudo-effective and nef line bundles.
It also gives a proof of Siu's theorem that the upper level sets of Lelong numbers are analytic.
It relies on the $L^2$ theory of $\bar\partial$, through the Ohsawa–Takegoshi theorem.
