---
tag: CQ7E0V6T2G
kind: statement
role: theorem
name: Converse of the mean value property
msc: [31B05]
uses: [0HYPR64JM2, 0DEB0JMN0W, 0X3WGX95FE, 0E0B6RA8K0]
about: [0DEB0JMN0W]
sources:
  - url: https://en.wikipedia.org/wiki/Harmonic_function
---

## Statement

Let $U \subseteq \R^n$ be an open set and let $u \colon U \to \R$ be [[continuous|0X3WGX95FE]].
Assume that for every $x \in U$ and every $r > 0$ with closed ball $\overline{B}(x, r) \subseteq U$,
$$u(x) = \frac{1}{\abs{\partial B(x, r)}} \int_{\partial B(x, r)} u \, dS,$$
where $\abs{\partial B(x, r)}$ is the area of the sphere $\partial B(x, r)$.
Then $u$ is [[harmonic|0DEB0JMN0W]] on $U$; in particular $u$ is infinitely differentiable.

## Remarks

Proof idea: let $\eta_\varepsilon$ be a smooth radial mollifier supported in $B(0, \varepsilon)$ with integral $1$.
Polar coordinates and the mean value property on each sphere give $u * \eta_\varepsilon = u$ at the points at distance more than $\varepsilon$ from the complement of $U$.
So $u$ is smooth there.
For a smooth function, the average over $\partial B(x, r)$ minus $u(x)$ equals $\frac{r^2}{2n} \Delta u(x) + o(r^2)$; since it is $0$, the [[Laplacian|0E0B6RA8K0]] vanishes.
Together with the [[mean value property|0HYPR64JM2]] of harmonic functions, this shows that, among continuous functions, harmonicity is the same as the mean value property on spheres.
The same holds with averages over balls in place of spheres.
For the version with ball averages, local integrability of $u$ is enough, because a function that equals its ball averages is automatically continuous.
Example: in $\R^2$, $u(x, y) = x y$ is continuous and its average over each circle about $(a, b)$ is $a b$, so $u$ is harmonic, as one checks directly from $\Delta(xy) = 0$.

## Explanations

### L1 human

Harmonic functions have the property that the value at a point is the average of the values on any sphere around it.
This theorem says the converse: any continuous function with this averaging property is harmonic.
So "harmonic" can be defined either by the Laplace equation or by the averaging property.

### L2 human

The averaging definition needs no derivatives, which makes it the natural starting point for harmonic functions on general spaces and for subharmonic functions.
It is also the key step in proving that a locally uniform limit of harmonic functions is harmonic: the mean value property passes to uniform limits, and continuity is preserved.
A stronger result, Koebe's theorem, only asks for the mean value property on all small enough spheres about each point.
