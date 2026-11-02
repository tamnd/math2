---
tag: XE3GCCV96H
kind: definition
name: Modulation space
msc: [42B35, "46E30", 42C15]
defines: JT3G2NF0VX
uses: [3DHNP5NEWH, CG9JEATW3Q, AES2T5JPFP, SASP14MA1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Modulation_space
---

## Definition

Let $d \ge 1$ and let $g$ be a nonzero function in the [[Schwartz space|CG9JEATW3Q]] $\mathcal{S}(\R^d)$, called the window.
For a [[tempered distribution|AES2T5JPFP]] $f \in \mathcal{S}'(\R^d)$, let $V_g f$ be its [[short-time Fourier transform|3DHNP5NEWH]]:
$$V_g f(x, \omega) = \int_{\R^d} f(t) \, \overline{g(t - x)} \, e^{-2\pi i t \cdot \omega} \, dt, \quad x, \omega \in \R^d,$$
understood as the action of $f$ on the Schwartz function $t \mapsto \overline{g(t - x)} e^{-2\pi i t \cdot \omega}$.
Let $1 \le p, q < \infty$.
The *modulation space* $M^{p,q}(\R^d)$ is the set of $f \in \mathcal{S}'(\R^d)$ with
$$\norm{f}_{M^{p,q}} = \left( \int_{\R^d} \left( \int_{\R^d} \abs{V_g f(x, \omega)}^p \, dx \right)^{q/p} d\omega \right)^{1/q} < \infty.$$
If $p = \infty$ or $q = \infty$, the corresponding integral is replaced by an essential supremum.

## Remarks

The space does not depend on the choice of the window $g$, and different windows give equivalent norms.
With this norm $M^{p,q}(\R^d)$ is a Banach space.
One writes $M^p = M^{p,p}$.
Special cases are $M^{2} = L^2(\R^d)$ with an equivalent norm, and $M^{1}$, the Feichtinger algebra.
Weighted versions $M^{p,q}_m$ insert a weight $m(x, \omega)$ into the integrand.

Example: let $d = 1$ and $\varphi(t) = e^{-\pi t^2}$, and take $g = \varphi$.
Completing the square in $t$ gives
$$\abs{V_\varphi \varphi(x, \omega)} = 2^{-1/2} e^{-\pi (x^2 + \omega^2)/2}.$$
This is integrable to every power in $x$ and in $\omega$, so $\varphi \in M^{p,q}(\R)$ for all $p, q$.

Non-example: the constant function $f = 1$ is not in $M^{p,q}(\R)$ for $p < \infty$.
Here $\abs{V_g 1(x, \omega)} = \abs{\hat{\overline{g}}(\omega)}$ does not depend on $x$, so the inner integral is infinite whenever $\hat{\overline{g}}(\omega) \ne 0$.
It does lie in $M^{\infty, 1}(\R)$.
