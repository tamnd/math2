---
tag: TYGFD8F2NG
kind: statement
role: theorem
name: Charney–Stern theorem
msc: ["76E20", 76U60, 86A10]
uses: [8Z4QBWTWVR, F2D7MXW8V1, 2SVQ4JN85Y, 25ZMP5THH9]
about: [2SVQ4JN85Y]
sources:
  - url: https://en.wikipedia.org/wiki/Baroclinity
---

## Statement

Consider the [[quasi-geostrophic equations|8Z4QBWTWVR]] on a [[beta plane|F2D7MXW8V1]] with Coriolis parameter $f_0 + \beta y$, $f_0 \ne 0$, and buoyancy frequency $N(z) > 0$.
The domain is periodic in $x$, bounded by walls at $y = y_1$ and $y = y_2$ and by rigid lids at $z = 0$ and $z = H$.
Let $U(y, z)$ be a smooth steady zonal basic flow, and let
$$\bar q_y = \beta - \frac{\partial^2 U}{\partial y^2} - \frac{\partial}{\partial z} \left( \frac{f_0^2}{N^2} \frac{\partial U}{\partial z} \right)$$
be the meridional gradient of its quasi-geostrophic potential vorticity.
Suppose the linearised equations have a normal mode $\psi' = \operatorname{Re}[\hat\psi(y, z) e^{ik(x - ct)}]$ with $k \ne 0$ real, $\hat\psi \not\equiv 0$ vanishing at the walls, and $\operatorname{Im} c \ne 0$.
Then
$$\int_{y_1}^{y_2} \int_0^H \frac{\bar q_y \abs{\hat\psi}^2}{\abs{U - c}^2} \, dz \, dy + \int_{y_1}^{y_2} \left[ \frac{f_0^2}{N^2} \frac{\partial_z U \, \abs{\hat\psi}^2}{\abs{U - c}^2} \right]_{z = 0}^{z = H} dy = 0.$$
In particular, suppose $\partial_z U = 0$ at $z = 0$ and $z = H$.
Then a necessary condition for such an unstable mode is that $\bar q_y$ changes sign in the interior of the domain.

## Remarks

The proof follows Rayleigh's argument.
The linearised equation is $(U - c)\left(\partial_y^2 \hat\psi - k^2 \hat\psi + \partial_z (f_0^2 N^{-2} \partial_z \hat\psi)\right) + \bar q_y \hat\psi = 0$, and conservation of buoyancy at the lids gives $(U - c) \partial_z \hat\psi = \partial_z U \, \hat\psi$ there.
Divide by $U - c$, multiply by the complex conjugate of $\hat\psi$ and integrate by parts; the boundary terms are rewritten with the lid condition.
The imaginary part of the resulting identity is $\operatorname{Im} c$ times the left side above, and $\operatorname{Im} c \ne 0$ gives the result.

So instability needs the terms of the identity to have opposite signs.
Treating the boundary terms as sheets of potential vorticity gradient, instability requires one of the following.
(a) $\bar q_y$ changes sign in the interior.
(b) $\bar q_y$ has the sign opposite to $\partial_z U$ at the upper lid.
(c) $\bar q_y$ has the same sign as $\partial_z U$ at the lower lid.
(d) $\partial_z U$ has the same sign at both lids.
In the Eady model $\bar q_y = 0$ in the interior and $\partial_z U = \Lambda > 0$ at both lids, so the last case applies.
In the Charney model of an unbounded atmosphere with $\beta > 0$ and $\partial_z U > 0$ at the ground, $\bar q_y > 0$ in the interior has the same sign as the shear at the lower boundary.

For a flow $U(y)$ without vertical structure, the theorem reduces to the Rayleigh–Kuo criterion: $\beta - U''$ must change sign, which extends [[Rayleigh's inflection point criterion|25ZMP5THH9]].
The condition is only necessary: a flow can satisfy it and still be stable.

## Explanations

### L1 human

The theorem says when a sheared flow on a rotating planet has any chance of becoming unstable.
It looks at the potential vorticity of the flow, a measure of spin adjusted for stratification.
If the northward gradient of this quantity never changes sign, and the boundaries play no role, then no wave can grow.
So a flow can only break into eddies if its potential vorticity gradient takes both signs somewhere, counting the effect of the boundaries.

### L2 human

The result was published by Charney and Stern in 1962 and generalised by Bretherton, who interpreted temperature gradients at the boundaries as thin sheets of potential vorticity.
It is the rotating, stratified analogue of Rayleigh's criterion for shear flows, and it is proved the same way.
In practice one checks the sign of $\bar q_y$ and of the boundary shear for a given jet to see which kind of instability can occur.
In the atmosphere, the positive shear at the ground together with $\beta > 0$ in the interior makes baroclinic instability possible, which is the source of mid-latitude storms.
