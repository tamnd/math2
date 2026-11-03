---
tag: 3CE48D4MWW
kind: statement
role: theorem
name: Reynolds transport theorem
msc: [76A02, 74A99]
uses: [43949CJRF6, HTYRR2WDQ6, 0MWV6ZTK6S, 0JX86PSSA9, 00KDZRW4C0]
about: [43949CJRF6]
sources:
  - url: https://en.wikipedia.org/wiki/Reynolds_transport_theorem
same_as:
  wikidata: Q953062
  wikipedia: Reynolds transport theorem
---

## Statement

Let $B \subseteq \R^3$ be open and let $I$ be an open time interval.
Let $\chi \colon B \times I \to \R^3$ be a motion of class $C^2$, and let $v(x, t)$ be its velocity field in the [[Eulerian description|43949CJRF6]].
Let $\Omega_0$ be a bounded open set with $\overline{\Omega_0} \subset B$, and let $\Omega_t = \chi(\Omega_0, t)$.
Let $f$ be a real function of class $C^1$ on $\set{(x, t) : t \in I, \ x \in \chi(B, t)}$.
Then for every $t \in I$,
$$\frac{d}{dt} \int_{\Omega_t} f(x, t)\, dx = \int_{\Omega_t} \left( \frac{\partial f}{\partial t} + \operatorname{div}(f v) \right) dx,$$
where $\operatorname{div}$ is the [[divergence|0MWV6ZTK6S]] in $x$.
If moreover $\Omega_t$ has a $C^1$ boundary with outward unit normal $n$, the right side equals
$$\int_{\Omega_t} \frac{\partial f}{\partial t}\, dx + \int_{\partial \Omega_t} f\, v \cdot n\, dA.$$

## Remarks

The proof changes variables to the fixed set $\Omega_0$: $\int_{\Omega_t} f\, dx = \int_{\Omega_0} f(\chi(X, t), t)\, J(X, t)\, dX$, where $J = \det F$ is the [[determinant|00KDZRW4C0]] of the [[deformation gradient|HTYRR2WDQ6]].
Differentiating under the integral sign and using Euler's identity $\partial_t J = J \operatorname{div} v$ gives the first form; the [[divergence theorem|0JX86PSSA9]] gives the second.
With $f = 1$ it says that the volume of $\Omega_t$ changes at the rate $\int_{\Omega_t} \operatorname{div} v\, dx$, so a motion with $\operatorname{div} v = 0$ preserves volume.
With $f = \rho$, the mass density, it turns conservation of mass of every part into the continuity equation $\partial_t \rho + \operatorname{div}(\rho v) = 0$.

## Explanations

### L1 human

Suppose you follow a blob of moving fluid and want to know how fast the amount of something inside it changes.
Two things contribute: the quantity changes in time at each fixed place, and the blob moves and changes shape, sweeping new regions in.
The Reynolds transport theorem adds these two effects precisely.

### L2 human

It is the tool that converts balance laws for moving parts of a body into local differential equations.
Applied to mass, momentum and energy, it yields the continuity equation, the Cauchy momentum equation and the energy equation.
It is the moving-domain version of the Leibniz rule for differentiating integrals.
