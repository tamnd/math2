---
tag: S7TTVM3C8A
kind: definition
name: Schechter luminosity function
msc: [85A35, 85A15]
defines: ZSAXM3ETYR
uses: [0H5SYBSED9, D7EAZ5F0YT]
sources:
  - url: https://en.wikipedia.org/wiki/Luminosity_function_(astronomy)
---

## Definition

Let $\phi^* > 0$, $L^* > 0$ and $\alpha \in \R$ be parameters.
The *Schechter luminosity function* is the function $\phi \colon (0, \infty) \to (0, \infty)$ given by
$$\phi(L) \, dL = \phi^* \left( \frac{L}{L^*} \right)^{\alpha} e^{-L / L^*} \, \frac{dL}{L^*}.$$
Here $\phi(L) \, dL$ is the number of galaxies per unit volume with luminosity between $L$ and $L + dL$.
$\phi^*$ is a normalisation density, $L^*$ is the characteristic luminosity, and $\alpha$ is the faint-end slope.

## Remarks

In terms of the [[absolute magnitude|D7EAZ5F0YT]] $M$, with $L / L^* = 10^{0.4 (M^* - M)}$, the same law reads
$$\phi(M) \, dM = 0.4 \ln 10 \; \phi^* \, 10^{0.4 (M^* - M)(\alpha + 1)} \exp\left( -10^{0.4 (M^* - M)} \right) dM.$$

Example: the total luminosity density is
$$j = \int_0^\infty L \, \phi(L) \, dL = \phi^* L^* \, \Gamma(\alpha + 2),$$
by the substitution $x = L / L^*$ and the definition of the [[Gamma function|0H5SYBSED9]].
This is finite for $\alpha > -2$; for $\alpha = -1$ it gives $j = \phi^* L^*$.

Non-example: the number density $\int_0^\infty \phi(L) \, dL = \phi^* \int_0^\infty x^\alpha e^{-x} \, dx$ diverges at $x = 0$ when $\alpha \le -1$.
So for such $\alpha$ the function is not a probability density of luminosities on $(0, \infty)$, and a lower cut-off is needed.
Fitted values of $\alpha$ for galaxies are usually close to $-1$.
