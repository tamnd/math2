---
tag: ETH7FW1KKA
kind: definition
name: Resolutivity of boundary functions
msc: [31B20, 31A25, 31B05]
defines: JCMTFY6HMA
uses: [02BH3MCBQB, 05D5EGMFYV, X4V2S56YQQ, Z1MHMGFNFW, 0DEB0JMN0W, 8D56GQ4AG8]
sources:
  - url: https://en.wikipedia.org/wiki/Perron_method
---

## Definition

Let $n \ge 2$, let $\Omega \subseteq \R^n$ be a bounded [[open set|02BH3MCBQB]] with [[boundary|05D5EGMFYV]] $\partial\Omega$, and let $f \colon \partial\Omega \to [-\infty, +\infty]$ be a function.

1. The *upper class* $\mathcal{U}_f$ is the set of functions $u$ on $\Omega$ with these properties.
On each connected component of $\Omega$, $u$ is [[superharmonic|X4V2S56YQQ]] or identically $+\infty$.
The function $u$ is bounded below, and $\liminf_{x \to \zeta,\, x \in \Omega} u(x) \ge f(\zeta)$ for every $\zeta \in \partial\Omega$.
2. The *lower class* $\mathcal{L}_f$ is the set of functions $v$ on $\Omega$ with these properties.
On each connected component of $\Omega$, $v$ is [[subharmonic|Z1MHMGFNFW]] or identically $-\infty$.
The function $v$ is bounded above, and $\limsup_{x \to \zeta,\, x \in \Omega} v(x) \le f(\zeta)$ for every $\zeta \in \partial\Omega$.
3. The *upper solution* is $\overline{H}_f(x) = \inf\set{u(x) : u \in \mathcal{U}_f}$ and the *lower solution* is $\underline{H}_f(x) = \sup\set{v(x) : v \in \mathcal{L}_f}$, for $x \in \Omega$.

The function $f$ is *resolutive* if $\overline{H}_f = \underline{H}_f$ on $\Omega$ and this common function is [[harmonic|0DEB0JMN0W]] on $\Omega$, in particular finite.
The common function is then written $H_f$.

## Remarks

The inequality $\underline{H}_f \le \overline{H}_f$ always holds, by the maximum principle applied to $v - u$ for $v \in \mathcal{L}_f$ and $u \in \mathcal{U}_f$.
Wiener's theorem says that every continuous $f$ is resolutive, so $H_f$ is a generalised solution of the [[Dirichlet problem|8D56GQ4AG8]].
For a bounded domain, Brelot showed that $f$ is resolutive if and only if $f$ is integrable with respect to [[harmonic measure|CFD7BPM51W]].
Then $H_f(x)$ is the integral of $f$ against the harmonic measure for $x$.

Example: let $\Omega$ be the unit disc in $\R^2$ and $f$ continuous on the unit circle.
The Poisson integral $P[f]$ is harmonic in $\Omega$ and tends to $f(\zeta)$ at each boundary point $\zeta$.
So $P[f]$ lies in both $\mathcal{U}_f$ and $\mathcal{L}_f$, which gives $\overline{H}_f \le P[f] \le \underline{H}_f$.
With $\underline{H}_f \le \overline{H}_f$ this forces $\overline{H}_f = \underline{H}_f = P[f]$, which is harmonic, so $f$ is resolutive.

Non-example: let $f \equiv +\infty$ on $\partial\Omega$.
The only member of $\mathcal{U}_f$ is the constant $+\infty$, so $\overline{H}_f \equiv +\infty$.
Every constant $c$ lies in $\mathcal{L}_f$, so $\underline{H}_f \equiv +\infty$ too.
The two solutions agree but are not harmonic, so $f$ is not resolutive.
