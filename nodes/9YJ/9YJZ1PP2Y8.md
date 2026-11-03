---
tag: 9YJZ1PP2Y8
kind: statement
role: fact
name: Fourier's law of heat conduction
msc: [80A19, 35K05]
uses: [1Y36434YTE, XBQBT9E7JT, SW8X60GYZT, 0ABK9V9Y64, KK46Q2YV1D]
about: [SW8X60GYZT]
sources:
  - url: https://en.wikipedia.org/wiki/Thermal_conduction
    locator: Fourier's law
---

## Statement

Let a homogeneous isotropic body occupy an open set $\Omega \subseteq \R^3$, with [[temperature|KK46Q2YV1D]] field $T(x, t)$ that is differentiable in $x$.
Let $k > 0$ be the [[thermal conductivity|XBQBT9E7JT]] of the material.
Then the [[heat flux|1Y36434YTE]] of [[conduction|SW8X60GYZT]] is
$$\mathbf{q}(x, t) = -k \, \nabla T(x, t),$$
where $\nabla T$ is the [[gradient|0ABK9V9Y64]] of $T$ in $x$.
In one space dimension, $q = -k \, \partial T / \partial x$.

## Remarks

Fourier's law is a constitutive law, found by experiment, not a theorem derived from other laws.
It holds very well for most solids and fluids at rest when the temperature changes slowly on the scale of the molecules.
The minus sign says that heat flows down the temperature gradient, from hot to cold, in agreement with the second law of thermodynamics.

Example: take a glass window of thickness $L = 0.005$ metres and conductivity $k = 1$ watt per metre per kelvin.
If its faces are at $20$ and $0$ degrees Celsius, the linear steady profile gives $\abs{q} = k \cdot 20 / L = 4000$ watts per square metre.

Combined with conservation of energy, $\rho c \, \partial_t T = -\nabla \cdot \mathbf{q}$, and with constant $k$, it gives the [[heat equation|VP2HN86VAG]] $\partial_t T = \alpha \Delta T$ with the [[thermal diffusivity|CS4ZZX092Z]] $\alpha = k / (\rho c)$.

## Explanations

### L1 human

Heat flows from hot to cold, and it flows faster when the temperature drops more steeply.
Fourier's law says the flow is exactly proportional to the steepness of the temperature drop.
The constant of proportionality is a property of the material: large for copper, small for wool.

### L2 human

Fourier's law is the closing relation that turns the energy balance into a solvable equation for the temperature.
For a material whose conductivity depends on direction, it becomes $\mathbf{q} = -K \nabla T$ with a [[conductivity tensor|M1J161A2QY]] $K$.
It predicts that a disturbance is felt everywhere at once, which is unphysical at very short times; the [[Cattaneo–Vernotte equation|FFD8ZJBMMD]] corrects this.
It has the same form as Ohm's law for electric current and Fick's law for diffusion.
So heat conduction problems can be treated like circuit problems with [[thermal resistance|1CB45W4GA6]].
