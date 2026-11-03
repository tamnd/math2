---
tag: 2QDWHFCC4H
kind: statement
role: theorem
name: Carleman estimate for harmonic measure
msc: [31A15, 30C85]
uses: [EGRH1KN03C, CFD7BPM51W, 0EWMDD6C14, 0BSW4T7THS, FYR6V2NH6C, SB55PWPRH2]
about: [CFD7BPM51W]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_measure
---

## Statement

Let $\Omega \subseteq \C$ be a [[domain|0EWMDD6C14]], let $r_0 > 0$, and let $z_0 \in \Omega$ with $\abs{z_0} < r_0$.
For $r > 0$, let $\theta(r)$ be the total angular length of the set $\set{t \in [0, 2\pi) : r e^{it} \in \Omega}$.
Set $1/\theta(r) = 0$ when the whole circle $\abs{z} = r$ lies in $\Omega$.
For $R > r_0$, let $\Omega_R$ be the component of $\Omega \cap \set{\abs{z} < R}$ that contains $z_0$.
Let $\omega_R(z_0)$ be the [[harmonic measure|EGRH1KN03C]] at $z_0$ of $\partial\Omega_R \cap \set{\abs{z} = R}$ with respect to $\Omega_R$.
Then there is a constant $C$, independent of $R$, such that for every $R > r_0$
$$\omega_R(z_0) \le C \exp\left(-\pi \int_{r_0}^{R} \frac{dr}{r\,\theta(r)}\right).$$

## Remarks

Idea of the proof: in [[polar coordinates|0BSW4T7THS]] $z = re^{it}$, consider the mean square $m(r) = \int \omega_R(re^{it})^2 \, dt$ over the arcs of $\Omega_R$ on the circle of radius $r$.
The function $\omega_R$ vanishes at the ends of these arcs, so Wirtinger's inequality bounds its angular derivative from below by $\pi/\theta(r)$ times its size.
Together with the Laplace equation, this gives a differential inequality for $m$ in the variable $\log r$, which integrates to the exponential bound.
Example: for the sector $\Omega = \set{z \ne 0 : \abs{\arg z} < \alpha/2}$ with $0 < \alpha \le 2\pi$, $\theta(r) = \alpha$, and the bound reads $\omega_R(z_0) \le C (r_0/R)^{\pi/\alpha}$.
This is the true order of decay, as the harmonic function $\operatorname{Re} z^{\pi/\alpha}$ on the sector shows.
The convention $1/\theta(r) = 0$ is needed: on a full circle the harmonic measure does not vanish anywhere, and Wirtinger's inequality gives no information there.
Ahlfors' distortion theorem refines the estimate for strip-like domains, replacing $\theta(r)$ by the width of a single crossing arc.

## Explanations

### L1 human

Harmonic measure is the chance that a random path started at $z_0$ reaches the far circle $\abs{z} = R$ before it hits the boundary of the domain.
If the domain is narrow, the path must squeeze through a thin channel and is likely to hit the walls first.
The estimate makes this precise: the chance decays exponentially in the integral of $dr/(r\,\theta(r))$, where $\theta(r)$ measures how wide the domain is at distance $r$.

### L2 human

The estimate is a basic tool for growth problems in complex analysis.
Applied to the domain where a holomorphic function is large, it bounds how fast the function can grow along narrow tracts, as in the [[Phragmén–Lindelöf principle|FYR6V2NH6C]] and the [[Denjoy–Carleman–Ahlfors theorem|SB55PWPRH2]].
It is proved by a differential inequality, while Ahlfors' sharper version is proved with the length–area method.
