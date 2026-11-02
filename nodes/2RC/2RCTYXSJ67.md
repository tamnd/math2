---
tag: 2RCTYXSJ67
kind: definition
name: Newtonian space
msc: ["46E36", "31E05"]
defines: V90RGBV52W
uses: [0VKD1TP7F3, PR11BZQQPG, 0HATW2VWAZ, SASP14MA1Z, 06GZ956657]
sources:
  - url: https://en.wikipedia.org/wiki/Sobolev_space
---

## Definition

Let $(X, d)$ be a [[metric space|0VKD1TP7F3]] with a Borel [[measure|PR11BZQQPG]] $\mu$, and let $1 \le p < \infty$.
Let $u \colon X \to \R$ be a function, defined at every point.
For a Borel function $g \colon X \to [0, \infty]$ and a [[rectifiable curve|0HATW2VWAZ]] $\gamma \colon [a, b] \to X$, let $\int_\gamma g \, ds$ be the integral of $g$ along $\gamma$ with respect to arc length.
The function $g$ is an *upper gradient* of $u$ if
$$\abs{u(\gamma(a)) - u(\gamma(b))} \le \int_\gamma g \, ds$$
for every rectifiable curve $\gamma \colon [a, b] \to X$.
Let $\widetilde{N}^{1,p}(X)$ be the set of all $u$ in the [[Lp space|SASP14MA1Z]] $L^p(X, \mu)$ with an upper gradient in $L^p(X, \mu)$.
On it put
$$\norm{u}_{\widetilde{N}^{1,p}} = \left( \int_X \abs{u}^p \, d\mu + \inf_g \int_X g^p \, d\mu \right)^{1/p},$$
the infimum over all upper gradients $g$ of $u$.
The *Newtonian space* $N^{1,p}(X)$ is the quotient of $\widetilde{N}^{1,p}(X)$ by the relation $u \sim v$ if $\norm{u - v}_{\widetilde{N}^{1,p}} = 0$, with the induced norm.

## Remarks

Example: on $X = \R$ with Lebesgue measure, $u(x) = \max(0, 1 - \abs{x})$ lies in $\widetilde{N}^{1,p}(\R)$.
Indeed $u \in L^p$, and $g = \mathbf{1}_{[-1, 1]}$ is an upper gradient in $L^p$, since $\abs{u(s) - u(t)} \le \abs{\int_s^t g}$ for real $s, t$ and a curve from $\gamma(a)$ to $\gamma(b)$ covers at least the interval between them.

Non-example: on $X = [0, 1]$ with Lebesgue measure, $u = \mathbf{1}_{[1/2, 1]}$ is in $L^p$ but has no upper gradient in $L^p$.
An upper gradient $g$ would need $\int_{1/2 - \varepsilon}^{1/2 + \varepsilon} g \ge 1$ for every $\varepsilon > 0$, and these integrals tend to $0$ when $g$ is integrable.

The space $N^{1,p}(X)$ is a [[Banach space|06GZ956657]].
Its elements are classes of functions defined at every point, and two functions in one class agree outside a set of $p$-capacity zero, not only almost everywhere.
The definition is often given with $p$-weak upper gradients, which may fail the curve inequality on a family of curves of $p$-modulus zero.
This gives the same space and the same norm.
If $X$ contains no nonconstant rectifiable curves, for example a Cantor set, then $g = 0$ is an upper gradient of every function and $N^{1,p}(X) = L^p(X, \mu)$.
For an open set $\Omega \subset \R^n$ with Lebesgue measure and $1 < p < \infty$, $N^{1,p}(\Omega)$ agrees with the [[Sobolev space|M4CEZ5K9HP]] $W^{1,p}(\Omega)$, each class of $W^{1,p}$ being represented by suitable pointwise defined functions.
