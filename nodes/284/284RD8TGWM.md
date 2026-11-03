---
tag: 284RD8TGWM
kind: definition
name: Wormhole
msc: [83C15, 83C99]
defines: MXBVB858GR
uses: [BY4QYYS788, 3HTF65XMF7, ENWD1YR20P]
sources:
  - url: https://en.wikipedia.org/wiki/Wormhole
---

## Definition

There is no single accepted definition of a wormhole for all spacetimes.
This node uses the standard form of a static, spherically symmetric, traversable wormhole, due to Morris and Thorne.
Let $\Phi \colon \R \to \R$ and $r \colon \R \to (0, \infty)$ be smooth functions.
The [[Lorentzian manifold|BY4QYYS788]] $\R \times \R \times S^2$ with coordinates $(t, \ell, \theta, \phi)$ and metric
$$g = -e^{2\Phi(\ell)} dt^2 + d\ell^2 + r(\ell)^2\left(d\theta^2 + \sin^2\theta\, d\phi^2\right)$$
is a *wormhole* with throat at $\ell = 0$ if:

1. $r$ has its global minimum at $\ell = 0$, with $r(0) = r_0 > 0$; the sphere $\ell = 0$ is the *throat*;
2. $r(\ell)/\abs{\ell} \to 1$ and $\Phi(\ell)$ tends to a finite limit as $\ell \to \pm\infty$, so that both ends are [[asymptotically flat|3HTF65XMF7]];
3. $\Phi$ is bounded, so that $g_{tt}$ never vanishes and there is no horizon.

## Remarks

Example: the [[Ellis wormhole|NGK91EV37X]], with $\Phi = 0$ and $r(\ell) = \sqrt{\ell^2 + n^2}$ for a constant $n > 0$.
Check: $r$ has its minimum $n$ at $\ell = 0$, $\sqrt{\ell^2 + n^2}/\abs{\ell} \to 1$, and $\Phi = 0$ is bounded.

Non-example: $\Phi = 0$ and $r(\ell) = \ell^2 + 1$ satisfy clauses 1 and 3 but fail clause 2, since $r(\ell)/\abs{\ell} \to \infty$.

Consequence for the matter content: for the null vector $k = e^{-\Phi}\partial_t + \partial_\ell$, a computation gives $R_{ab}k^a k^b = \frac{2}{r}\left(\Phi' r' - r''\right)$.
At the throat $r' = 0$ and $r'' \ge 0$, since $\ell = 0$ is a minimum.
If $r''(0) > 0$, then $R_{ab}k^ak^b < 0$, and the Einstein equations force $T_{ab}k^ak^b < 0$: the null [[energy condition|ENWD1YR20P]] fails there.
The ends $\ell \to +\infty$ and $\ell \to -\infty$ may be two universes, or, after identifications far away, two regions of one universe.
