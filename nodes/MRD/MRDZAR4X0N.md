---
tag: MRDZAR4X0N
kind: definition
name: Bounded mean oscillation
msc: [30H35, 42B35]
defines: QJYTXFT8Y4
uses: [0XPR1E85W0]
sources:
  - url: https://en.wikipedia.org/wiki/Bounded_mean_oscillation
---

## Definition

Let $n \ge 1$ and let $f \colon \R^n \to \C$ be locally integrable for Lebesgue measure on [[Euclidean space|0XPR1E85W0]].
Let $Q \subseteq \R^n$ be a cube with sides parallel to the axes, and let $\abs{Q}$ be its volume.
Let $f_Q = \frac{1}{\abs{Q}} \int_Q f \, dx$ be the mean of $f$ on $Q$, a Lebesgue integral.
The function $f$ has *bounded mean oscillation* if
$$\norm{f}_{\mathrm{BMO}} = \sup_Q \frac{1}{\abs{Q}} \int_Q \abs{f(x) - f_Q} \, dx < \infty,$$
where the supremum is over all such cubes $Q$.
The space of these functions is denoted $\mathrm{BMO}(\R^n)$.

## Remarks

$\norm{\cdot}_{\mathrm{BMO}}$ vanishes exactly on the constant functions, so it is a norm on BMO modulo constants, which is a Banach space.
The same definition with arcs of the unit circle in place of cubes gives $\mathrm{BMO}(\mathbb{T})$.
Every bounded function lies in BMO with $\norm{f}_{\mathrm{BMO}} \le 2 \sup \abs{f}$.
The John–Nirenberg inequality says that a BMO function is exponentially integrable on each cube after subtracting its mean.

Example: $f(x) = \log \abs{x}$ on $\R$ lies in BMO.
For $\lambda > 0$ one has $f(\lambda x) = f(x) + \log \lambda$, and adding a constant does not change the mean oscillation.
So it suffices to bound the mean oscillation on intervals of length $1$, where a direct estimate works.

Non-example: $f(x) = x$ on $\R$.
On $Q = [0, L]$ one has $f_Q = L/2$ and $\frac{1}{L} \int_0^L \abs{x - L/2} \, dx = L/4$, which is unbounded in $L$.
