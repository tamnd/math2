---
tag: HYJ5TE7Z7Q
kind: definition
name: WKB approximation in optics
msc: [78M35, 78A05, "34E20"]
defines: ZQ1VYB94GE
uses: [YJEBN8N3G8, MNXKTXJ35G, 9VGK0SP6EQ, HGMX1QGTAZ]
sources:
  - url: https://en.wikipedia.org/wiki/WKB_approximation
---

## Definition

Let $n \colon \R \to (0, \infty)$ be a smooth [[refractive index|9VGK0SP6EQ]] of a medium layered in the direction $x$.
Let $k_0 > 0$ be the vacuum wave number, and let $\beta \ge 0$ be the wave number along the layers.
A mode $u(x) e^{i \beta z}$ of the scalar [[Helmholtz equation|MNXKTXJ35G]] satisfies
$$u''(x) + q(x) u(x) = 0, \qquad q(x) = k_0^2 n(x)^2 - \beta^2.$$
On an interval where $q > 0$, the *WKB approximation* of $u$ is
$$u(x) \approx q(x)^{-1/4} \left( A \exp\Big(i \int_{x_0}^{x} \sqrt{q(s)} \, ds\Big) + B \exp\Big(-i \int_{x_0}^{x} \sqrt{q(s)} \, ds\Big) \right),$$
with constants $A$, $B$ and a base point $x_0$.
It is the leading term of the [[WKB expansion|YJEBN8N3G8]] in the large parameter $k_0$.
It is accurate where $\abs{q'} \ll q^{3/2}$, that is, where $q$ changes little over one local wavelength $2\pi / \sqrt{q}$.

## Remarks

Check of the amplitude at normal incidence, $\beta = 0$: then $q^{-1/4} = (k_0 n)^{-1/2}$.
For the forward wave alone, $\abs{u}^2 \propto 1/n$ and $u' \approx i k_0 n u$, so the energy flux, proportional to $\operatorname{Im}(\bar{u} u') \approx k_0 n \abs{u}^2$, is constant along $x$.
So the approximation conserves energy, as a wave without reflection should.

Example: in a graded-index planar waveguide, let $q > 0$ exactly between two turning points $x_1 < x_2$, where $q(x_1) = q(x_2) = 0$.
Joining the WKB solutions across the turning points with Airy functions gives the mode condition
$$\int_{x_1}^{x_2} \sqrt{k_0^2 n(x)^2 - \beta^2} \, dx = \Big(m + \frac12\Big) \pi, \qquad m = 0, 1, 2, \dots$$

Non-example: at a step in $n$, such as an interface between air and glass, $q'$ is not small, and the condition of validity fails.
The WKB solution has no reflected part there, while the true field has the Fresnel reflection.

In three dimensions the same ansatz $u \approx a \, e^{i k_0 S}$ gives the [[eikonal equation|HGMX1QGTAZ]] $\abs{\nabla S}^2 = n^2$ for the phase and the transport equation $\nabla \cdot (a^2 \nabla S) = 0$ for the amplitude.

## Explanations

### L1 human

The formula says: the phase of the wave is the running sum of the local wave number, and the amplitude is scaled by the inverse fourth root of $q$.
This is exact for a uniform medium and almost exact for a slowly changing one.
At turning points, where $q = 0$, the formula blows up and must be patched with another solution.
