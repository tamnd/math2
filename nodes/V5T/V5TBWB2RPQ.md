---
tag: V5TBWB2RPQ
kind: definition
name: Perron–Wiener–Brelot solution
msc: [31B20, 31C05, 31A25]
defines: R12KQGVGN6
uses: [X4V2S56YQQ, Z1MHMGFNFW, 02BH3MCBQB, 05D5EGMFYV, 0BTMQ04556, 04KFTA34C5]
sources:
  - url: https://en.wikipedia.org/wiki/Perron_method
---

## Definition

Let $n \ge 2$, let $\Omega \subseteq \R^n$ be a bounded [[open set|02BH3MCBQB]] with [[boundary|05D5EGMFYV]] $\partial\Omega$, and let $f \colon \partial\Omega \to [-\infty, +\infty]$ be a function.

1. The *upper class* $\mathcal{U}_f$ consists of the functions $u$ on $\Omega$, [[superharmonic|X4V2S56YQQ]] or identically $+\infty$ and bounded below, with $\liminf_{x \to \xi} u(x) \ge f(\xi)$ for all $\xi \in \partial\Omega$.
2. The *lower class* $\mathcal{L}_f$ consists of the functions $v$ on $\Omega$, [[subharmonic|Z1MHMGFNFW]] or identically $-\infty$ and bounded above, with $\limsup_{x \to \xi} v(x) \le f(\xi)$ for all $\xi \in \partial\Omega$.
3. The *upper solution* is $\overline{H}_f = \inf_{u \in \mathcal{U}_f} u$ and the *lower solution* is $\underline{H}_f = \sup_{v \in \mathcal{L}_f} v$, using the [[infimum|04KFTA34C5]] and [[supremum|0BTMQ04556]] pointwise.

The function $f$ is *resolutive* if $\overline{H}_f = \underline{H}_f$ and this function is harmonic on $\Omega$.
In that case the *Perron–Wiener–Brelot solution* of $f$ is $H_f = \overline{H}_f = \underline{H}_f$.

## Remarks

Always $\underline{H}_f \le \overline{H}_f$, by the maximum principle applied to $u - v$ for $u \in \mathcal{U}_f$ and $v \in \mathcal{L}_f$.
Each of $\overline{H}_f$ and $\underline{H}_f$ is harmonic, identically $+\infty$, or identically $-\infty$ on each connected component of $\Omega$.
Example: let $f$ be continuous on $\partial\Omega$, and let $u$ be continuous on $\overline{\Omega}$, harmonic on $\Omega$ and equal to $f$ on $\partial\Omega$.
Then $u$ lies in both classes, so $\overline{H}_f \le u \le \underline{H}_f$ and $H_f = u$.
Non-example: let $f \equiv +\infty$ on $\partial\Omega$.
By the minimum principle, a superharmonic function in $\mathcal{U}_f$ would be at least every constant $M$.
So $\mathcal{U}_f$ contains only the constant $+\infty$, and $\overline{H}_f \equiv +\infty$ is not harmonic; hence $f$ is not resolutive.
For $\Omega = \set{0 < \abs{x} < 1}$ in $\R^2$, let $f = 0$ on $\abs{x} = 1$ and $f(0) = 1$.
Then $f$ is resolutive with $H_f = 0$, which does not attain the value $f(0)$.
So the PWB solution need not solve the classical Dirichlet problem.
By Wiener's theorem every continuous $f$ is resolutive.
