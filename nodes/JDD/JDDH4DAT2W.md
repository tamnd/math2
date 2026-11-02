---
tag: JDDH4DAT2W
kind: statement
role: theorem
name: Symmetry of the Green function
msc: [31B10, 35J08, 31A15]
uses: [M36SD56MWQ, 02BH3MCBQB]
about: [M36SD56MWQ]
sources:
  - url: https://en.wikipedia.org/wiki/Green%27s_function
---

## Statement

Let $n \ge 2$ and let $\Omega \subseteq \R^n$ be a bounded connected [[open set|02BH3MCBQB]] that has a [[Green's function|M36SD56MWQ]] $G$ for the Laplacian with zero boundary values.
Then
$$G(x, y) = G(y, x) \quad \text{for all } x, y \in \Omega \text{ with } x \ne y.$$

## Remarks

Proof idea for a smooth boundary: fix $x \ne y$ and apply Green's second identity to $v(z) = G(z, x)$ and $w(z) = G(z, y)$ on $\Omega$ with small balls around $x$ and $y$ removed.
Both functions are harmonic there and vanish on $\partial\Omega$, so only the small spheres contribute.
As the radii tend to $0$, the sphere around $x$ gives $G(x, y)$ and the sphere around $y$ gives $G(y, x)$, up to the same constant, and the two must be equal.
For a general domain one approximates it from inside by smooth domains, whose Green's functions increase to $G$.
Example: on the unit disc, $G(z, w) = \log\abs{\frac{1 - \bar w z}{z - w}}$, and this is symmetric because $\abs{1 - \bar w z} = \abs{1 - \bar z w}$.

## Explanations

### L1 human

Put a unit charge at $y$ in a grounded box and measure the potential at $x$.
Then put the charge at $x$ and measure at $y$.
The two numbers are the same.
This reciprocity is the symmetry of the Green's function.

### L2 human

Symmetry means that the Green operator $f \mapsto \int_\Omega G(\cdot, y) f(y) \, dy$ is self-adjoint on $L^2(\Omega)$, which matches the self-adjointness of the Dirichlet Laplacian.
It lets one treat $G(x, \cdot)$ as a function of the second variable, for example to see that $G(x, y)$ is harmonic in $y$ away from $x$.
For operators that are not self-adjoint, the Green's function of the adjoint operator appears instead, and symmetry fails.
