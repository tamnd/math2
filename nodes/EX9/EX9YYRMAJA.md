---
tag: EX9YYRMAJA
kind: example
name: Radiative transfer equation
msc: [85A25, 45K05, 35Q49]
instance_of: [TH4NGC4016]
sources:
  - url: https://en.wikipedia.org/wiki/Radiative_transfer
---

## Example

Let $D \subseteq \R^3$ be a region filled with a medium, and let $S^2$ be the unit sphere of directions.
The unknown is the specific intensity $I(x, \Omega)$ of radiation at a point $x \in D$ travelling in the direction $\Omega \in S^2$, at one fixed frequency.
Let $\kappa(x) \ge 0$ and $\sigma(x) \ge 0$ be the absorption and scattering coefficients, $B(x)$ the emission source, and $p(\Omega' \cdot \Omega) \ge 0$ the phase function, normalized by $\frac{1}{4\pi} \int_{S^2} p(\Omega' \cdot \Omega) \, d\Omega' = 1$.
The stationary radiative transfer equation is
$$\Omega \cdot \nabla_x I(x, \Omega) + \big(\kappa(x) + \sigma(x)\big) I(x, \Omega) = \kappa(x) B(x) + \frac{\sigma(x)}{4\pi} \int_{S^2} p(\Omega' \cdot \Omega) \, I(x, \Omega') \, d\Omega'.$$
It contains a derivative of $I$ along the direction $\Omega$ and an integral of $I$ over all directions.
So it is an [[integro-partial differential equation|TH4NGC4016]].

Check: if $\kappa$, $\sigma$ and $B$ are constant, the constant intensity $I = B$ is a solution.
The left side is $(\kappa + \sigma) B$, and by the normalization of $p$ the right side is $\kappa B + \sigma B$.

## Remarks

The left side describes the loss of intensity along a ray by absorption and by scattering out of the direction $\Omega$.
The right side describes thermal emission and scattering into $\Omega$ from all other directions.
Along each ray $x + s\Omega$ the equation is a linear ordinary differential equation, and integrating it turns the problem into an integral equation for $I$.
For a plane-parallel atmosphere with isotropic scattering this leads to equations such as the [[Milne problem|KKT4Y0TBRZ]].

## Explanations

### L1 human

Light travelling through fog, a star or a furnace is partly absorbed, partly scattered into new directions, and new light is emitted.
The equation keeps track of how much light goes in each direction at each point.
The scattering term collects light from all directions, which is why an integral over directions appears next to the derivative along the ray.
