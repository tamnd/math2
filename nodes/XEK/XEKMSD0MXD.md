---
tag: XEKMSD0MXD
kind: definition
name: Yield surface
msc: [74C05]
defines: CWWCEXZ8BH
uses: [KG2XWEMJ30, M6ZWV4Y29A]
sources:
  - url: https://en.wikipedia.org/wiki/Yield_surface
---

## Definition

Let $\mathrm{Sym}(3)$ be the space of symmetric $3 \times 3$ real matrices, the possible values of the [[Cauchy stress tensor|KG2XWEMJ30]] $\sigma$.
A yield function of a material is a continuous function $f \colon \mathrm{Sym}(3) \to \R$ with $f(0) < 0$.
It is chosen so that stresses with $f(\sigma) < 0$ produce only elastic deformation.
Stresses with $f(\sigma) > 0$ are not admissible.
The *yield surface* is the set
$$\set{\sigma \in \mathrm{Sym}(3) : f(\sigma) = 0},$$
the boundary of the elastic domain $\set{\sigma : f(\sigma) < 0}$.

## Remarks

If the material is isotropic, $f$ is a symmetric function of the [[principal stresses|M6ZWV4Y29A]] $\sigma_1, \sigma_2, \sigma_3$.
The yield surface is then drawn in the space with coordinates $(\sigma_1, \sigma_2, \sigma_3)$.
If $f$ also does not depend on the mean stress $\tfrac13 \tr \sigma$, the surface is a cylinder with axis the line $\sigma_1 = \sigma_2 = \sigma_3$.
Example: $f(\sigma) = \sqrt{\tfrac32 s : s} - \sigma_y$, where $s = \sigma - \tfrac13 (\tr \sigma) I$ and $\sigma_y > 0$, gives the von Mises surface, a circular cylinder of radius $\sqrt{2/3}\,\sigma_y$ about the hydrostatic axis.
Non-example: $f(\sigma) = \tr \sigma + 1$ has $f(0) = 1 > 0$, so it does not have the zero stress in its elastic domain and is not a yield function.
When the material hardens, $f$ also depends on internal variables, and the yield surface moves or grows with plastic deformation.

## Explanations

### L1 human

The yield surface is the boundary between the stresses that a material carries elastically and those that make it flow.
It is the zero level set of a yield function on stress space.
