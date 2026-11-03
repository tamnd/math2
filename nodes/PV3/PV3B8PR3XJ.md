---
tag: PV3B8PR3XJ
kind: statement
role: proposition
name: Stommel's model of western intensification
msc: [86A05, 76U05, 35Q86]
uses: [VQ5Z44PXXR, F2D7MXW8V1, E66111XRRA, YCFPD0GE5G]
about: [VQ5Z44PXXR]
sources:
  - url: https://en.wikipedia.org/wiki/Boundary_current
---

## Statement

Consider a homogeneous ocean of constant depth $H$ and density $\rho_0$ in the rectangular basin $0 \le x \le L$, $0 \le y \le b$ of a [[beta plane|F2D7MXW8V1]] with $\beta > 0$.
Let $\psi(x, y)$ be the [[stream function|E66111XRRA]] of the depth-averaged velocity, $u = -\partial_y \psi$ and $v = \partial_x \psi$.
Let the steady flow be driven by a wind stress $\tau$ and damped by a linear bottom friction with rate $\varepsilon > 0$, so that
$$\varepsilon \nabla^2 \psi + \beta \frac{\partial \psi}{\partial x} = \frac{1}{\rho_0 H} \Big( \frac{\partial \tau^y}{\partial x} - \frac{\partial \tau^x}{\partial y} \Big) \quad \text{in the basin}, \qquad \psi = 0 \text{ on its boundary}.$$
Let $\delta_S = \varepsilon / \beta$, and assume $\delta_S \ll L$.
Then, away from the northern and southern edges:

1. in the interior, $\psi$ is close to the solution of the [[Sverdrup balance|VQ5Z44PXXR]] $\beta \, \partial_x \psi_I = (\rho_0 H)^{-1} \operatorname{curl} \tau$ with $\psi_I = 0$ at the eastern boundary $x = L$;
2. near the western boundary $x = 0$ there is a [[boundary layer|YCFPD0GE5G]] of width of order $\delta_S$, in which $\psi \approx \psi_I(0, y) \big( 1 - e^{-x / \delta_S} \big)$;
3. there is no boundary layer at the eastern boundary.

So the northward or southward return flow is concentrated in a narrow, fast western boundary current.
If instead $\beta = 0$ and the wind stress does not depend on $x$, the solution is symmetric under $x \mapsto L - x$ and there is no intensification.

## Remarks

In the boundary layer, $x$-derivatives dominate, and the equation reduces to $\varepsilon \psi_{xx} + \beta \psi_x = 0$, with solutions $A + B e^{-x/\delta_S}$.
The exponential decays away from the western wall, so it can correct the interior solution there.
Near the eastern wall the same exponential would grow away from the wall, so no layer is possible there; this is why the interior solution must take the eastern condition.

Example: with $\varepsilon = 10^{-6} \ \mathrm{s}^{-1}$ and $\beta = 2 \times 10^{-11} \ \mathrm{m}^{-1} \mathrm{s}^{-1}$, the width is $\delta_S = 50$ km, much smaller than an ocean basin several thousand kilometres wide.
The hypothesis $\beta > 0$ holds on the whole Earth, since $\beta = 2 \Omega \cos \varphi / a$ at latitude $\varphi$, so the intensification is western in both hemispheres.

## Explanations

### L1 human

The great current systems of the oceans are lopsided.
The Gulf Stream and the Kuroshio are narrow and fast on the western side of their oceans, while the return flow on the eastern side is broad and slow.
Henry Stommel explained this in 1948 with a simple model.
He showed that the change of the Coriolis effect with latitude is what breaks the symmetry.
Without that change, his model ocean circulates symmetrically.

### L2 human

The model is the [[Sverdrup balance|VQ5Z44PXXR]] plus a small friction, and it is a singular perturbation problem: the small parameter $\varepsilon$ multiplies the highest derivatives.
The method of matched asymptotic expansions gives the interior solution and the western boundary layer.
Munk's model replaces bottom friction by lateral friction and gives a boundary layer of width $(A_H / \beta)^{1/3}$ with the same western location.
