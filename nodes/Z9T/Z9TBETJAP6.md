---
tag: Z9TBETJAP6
kind: statement
role: theorem
name: Young–Laplace equation
msc: [76B45, 76D45, 53A10]
uses: [PA78NFEPCF]
about: [PA78NFEPCF]
sources:
  - url: https://en.wikipedia.org/wiki/Young%E2%80%93Laplace_equation
same_as:
  wikidata: Q905258
  wikipedia: Young–Laplace equation
---

## Statement

Let $S$ be a smooth surface in $\R^3$ that separates two fluids at rest, with a constant surface tension $\sigma > 0$.
Choose a unit normal field $n$ on $S$.
Let $\kappa_1$ and $\kappa_2$ be the principal curvatures of $S$, signed so that they are positive when $S$ bends away from $n$.
Let $H = \tfrac{1}{2}(\kappa_1 + \kappa_2)$ be the [[mean curvature|PA78NFEPCF]].
Let $p_-$ be the pressure on the side into which $n$ does not point and $p_+$ the pressure on the side into which $n$ points.
Then at every point of $S$,
$$p_- - p_+ = \sigma(\kappa_1 + \kappa_2) = 2\sigma H.$$
When $R_1 = 1/\kappa_1$ and $R_2 = 1/\kappa_2$ are the principal radii of curvature, this reads $p_- - p_+ = \sigma\left(\frac{1}{R_1} + \frac{1}{R_2}\right)$.

## Remarks

The idea of the proof: surface tension is the energy per unit area of the interface.
With the sign convention above, the first variation of area under a displacement of $S$ by $\delta n$ is $\int_S 2H\delta \, dA$.
At equilibrium the work $\int_S (p_- - p_+)\delta\,dA$ done by the pressure difference must balance the change $\sigma\,\delta(\text{area})$ for every $\delta$, which gives the equation pointwise.
Example: for a spherical drop of radius $R$ with $n$ pointing outward, $\kappa_1 = \kappa_2 = 1/R$, so the pressure inside exceeds the pressure outside by $2\sigma/R$.
A soap bubble has two surfaces, so its excess pressure is $4\sigma/R$.
A soap film with equal pressures on both sides has $H = 0$, so it is a minimal surface.

## Explanations

### L1 human

The skin of a drop or bubble is under tension, and when it is curved it squeezes what is inside.
So the pressure is higher on the inner, concave side of a curved surface.
The more sharply the surface is curved, the bigger the pressure jump, which is why small bubbles have a higher inner pressure than big ones.

### L2 human

The equation is the boundary condition for the normal stress at a fluid interface at rest, and it enters the dynamic condition of capillary waves.
Combined with the hydrostatic pressure it gives the shape of menisci, pendant drops and the capillary rise in a thin tube.
When the pressure difference is constant, it says that interfaces in equilibrium are surfaces of constant mean curvature.
This links fluid statics to the differential geometry of such surfaces.
