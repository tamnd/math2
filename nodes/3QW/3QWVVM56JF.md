---
tag: 3QWVVM56JF
kind: statement
role: theorem
name: Bendixson–Dulac theorem
msc: [34C05, 34C25, 37C27]
uses: [07BNRFQ0PJ, 0MWV6ZTK6S, 0QW64ARSHB, 0AA97XA70K]
about: [0AA97XA70K]
sources:
  - url: https://en.wikipedia.org/wiki/Bendixson–Dulac_theorem
same_as:
  wikidata: Q737892
  wikipedia: Bendixson–Dulac theorem
---

## Statement

Let $D \subseteq \R^2$ be a [[simply connected domain|0QW64ARSHB]] and let $f = (P, Q) \colon D \to \R^2$ be continuously differentiable.
Let $\varphi \colon D \to \R$ be continuously differentiable.
Assume that the [[divergence|0MWV6ZTK6S]]
$$\nabla \cdot (\varphi f) = \frac{\partial (\varphi P)}{\partial x} + \frac{\partial (\varphi Q)}{\partial y}$$
satisfies $\nabla \cdot (\varphi f) \ge 0$ on $D$ and does not vanish identically on any nonempty open subset of $D$.
Then the [[autonomous system|07BNRFQ0PJ]] $x' = P(x, y)$, $y' = Q(x, y)$ has no [[periodic orbit|0AA97XA70K]] contained in $D$.
The same holds when $\nabla \cdot (\varphi f) \le 0$ instead.

## Remarks

Suppose a periodic orbit $\Gamma \subseteq D$ exists, and let $R$ be the region inside $\Gamma$; since $D$ is simply connected, $R \subseteq D$.
By [[Green's theorem|0HR3N02317]], $\iint_R \nabla \cdot (\varphi f) \, dx \, dy$ equals the flux $\oint_\Gamma \varphi \, (P \, dy - Q \, dx)$.
The flux is $0$, because along $\Gamma$ one has $dx = P \, dt$ and $dy = Q \, dt$; but the double integral is positive, since $R$ is a nonempty open set.
The case $\varphi = 1$ is Bendixson's criterion, and a function $\varphi$ that works is called a Dulac function.
Example: for $x' = y$, $y' = -x - y + x^2$ one has $\nabla \cdot f = -1$, so the system has no periodic orbit in $\R^2$.
Simple connectivity is needed: the system $x' = x(1 - x^2 - y^2) - y$, $y' = y(1 - x^2 - y^2) + x$ has $\nabla \cdot f = 2 - 4(x^2 + y^2) < 0$ on the annulus $0.8 < \sqrt{x^2 + y^2} < 2$, yet the unit circle in this annulus is a periodic orbit.

## Explanations

### L1 human

A periodic orbit in the plane encloses a region, and the flow neither gains nor loses area across the orbit.
If the flow, after reweighting by a function $\varphi$, always expands area or always shrinks it, such a closed loop cannot exist.
So the theorem is a simple test that rules out cycles.

### L2 human

Bendixson–Dulac is the standard negative criterion for periodic orbits in the plane, and it complements the [[Poincaré–Bendixson theorem|0EW1X61ZT1]], which proves their existence.
Finding a good Dulac function is an art; for Lotka–Volterra type systems, $\varphi = 1 / (x y)$ is a common choice.
On a domain with one hole, the same argument shows that there is at most one periodic orbit that goes around the hole.
