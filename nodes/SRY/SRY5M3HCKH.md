---
tag: SRY5M3HCKH
kind: definition
name: Convergence of Fourier series
msc: [42A20, 42A24]
defines: V6Q24CHJG8
uses: [G12KXDHPPS, 09RJ859N7A, 0GFGK40582, 08VZ57PT26, SASP14MA1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Convergence_of_Fourier_series
---

## Definition

Let $f \colon \R \to \C$ be $2\pi$-periodic and integrable on $[-\pi, \pi]$, and let $S_N f(x) = \sum_{n=-N}^{N} \hat f(n) e^{inx}$ be the symmetric [[partial sums|09RJ859N7A]] of its [[Fourier series|G12KXDHPPS]].

1. The Fourier series of $f$ *converges at* $x \in \R$ if the limit $\lim_{N \to \infty} S_N f(x)$ exists in $\C$.
It *converges to $f$ at $x$* if this limit equals $f(x)$.
2. It *converges pointwise* on a set $E \subseteq \R$ if it converges at each $x \in E$ (see [[pointwise convergence|0GFGK40582]]).
It converges *almost everywhere* if it converges to $f$ at each $x$ outside a set of measure zero.
3. It *converges uniformly* to $f$ on $E$ if $\sup_{x \in E} \abs{S_N f(x) - f(x)} \to 0$ as $N \to \infty$ (see [[uniform convergence|08VZ57PT26]]).
4. For $1 \le p < \infty$ and $f \in L^p(\mathbb{T})$, it *converges in $L^p$* if $\int_{-\pi}^{\pi} \abs{S_N f - f}^p \, dx \to 0$ as $N \to \infty$, in the [[Lebesgue space|SASP14MA1Z]] $L^p(\mathbb{T})$.

## Remarks

The partial sums are taken symmetric in $n$; with this convention the real form $\frac{a_0}{2} + \sum_{n=1}^{N} (a_n \cos nx + b_n \sin nx)$ has the same partial sums.
Example: for $f(x) = \abs{x}$ on $[-\pi, \pi]$, extended periodically, $\abs{\hat f(n)} \le \frac{2}{\pi n^2}$, so the series converges uniformly to $f$ on $\R$.
Non-example: for the square wave equal to $\operatorname{sgn} x$ on $(-\pi, \pi)$, the series converges at every point but not uniformly on $\R$.
Indeed a uniform limit of continuous functions would be continuous.
Convergence of $S_N f(x)$ is a different question from summability, where averages such as the Cesàro means of $S_N f(x)$ are used.
