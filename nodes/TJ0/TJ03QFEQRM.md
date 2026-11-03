---
tag: TJ03QFEQRM
kind: definition
name: Equation of state of seawater
msc: [86A05, 80A10]
defines: M8PJQA6BPK
uses: []
sources:
  - url: https://en.wikipedia.org/wiki/TEOS-10
---

## Definition

Describe a parcel of sea water by its salinity $S$, its temperature $T$ and its pressure $p$.
The salinity is the mass of dissolved salt per unit mass of sea water.
The *equation of state of seawater* is the function $\rho = \rho(S, T, p)$ that gives the density of the parcel.

In TEOS-10, $S$ is the Absolute Salinity.
The equation of state is derived from the specific Gibbs energy $g(S, T, p)$ of sea water by
$$\rho(S, T, p) = \Big( \frac{\partial g}{\partial p} \Big)_{S, T}^{-1}.$$
The *thermal expansion coefficient* and the *haline contraction coefficient* are
$$\alpha = -\frac{1}{\rho} \frac{\partial \rho}{\partial T}, \qquad \beta = \frac{1}{\rho} \frac{\partial \rho}{\partial S}.$$

## Remarks

Example: the *linear equation of state* $\rho = \rho_0 \big( 1 - \alpha_0 (T - T_0) + \beta_0 (S - S_0) \big)$, with constants $\rho_0, \alpha_0, \beta_0 > 0$, is the first-order Taylor approximation of $\rho$ at a reference state $(S_0, T_0)$ and fixed pressure.
It satisfies the definition of $\alpha$ and $\beta$ at the reference state, since there $\alpha = \alpha_0$ and $\beta = \beta_0$.
It is used in simple models such as box models of the thermohaline circulation.

Non-example: the linear equation of state is not exact.
Mix two parcels of equal density but different temperatures and salinities.
With a linear $\rho$ the mixture has the same density.
For real sea water $\rho$ is a concave function of $T$, so the mixture is denser (cabbeling).
Also $\alpha$ grows with pressure (thermobaricity), which no linear function of $(S, T)$ alone can show.

In ocean models the in-situ temperature is often replaced by potential or Conservative Temperature, and the pressure dependence by a reference pressure.
