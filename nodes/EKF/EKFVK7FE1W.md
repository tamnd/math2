---
tag: EKFVK7FE1W
kind: definition
name: Magnetic dipole moment
msc: [78A30]
defines: SSAWJ3JF5Y
uses: [XRED3C547P, 0N5N15HWZ7, 0299VCW1TH, 8PEMR2J7EF, 0H5MR9B6GT]
sources:
  - url: https://en.wikipedia.org/wiki/Magnetic_moment
---

## Definition

Let $J \colon \R^3 \to \R^3$ be a continuous current density, a [[vector field|0299VCW1TH]] with compact support and $\nabla \cdot J = 0$.
Its *magnetic dipole moment* is the vector
$$m = \frac{1}{2} \int_{\R^3} y \times J(y) \, dy,$$
where $\times$ is the [[cross product|0N5N15HWZ7]].
For a steady current $I$ in a thin closed wire $\gamma$, the magnetic dipole moment is $m = \frac{I}{2} \oint_\gamma y \times d\ell$, a [[line integral|0H5MR9B6GT]].

## Remarks

Because $\nabla \cdot J = 0$ and $J$ has compact support, $\int J \, dy = 0$, and so $m$ does not depend on the choice of origin.
For a plane loop enclosing area $a$ with unit normal $n$ fixed by the right-hand rule, $m = I a \, n$.
Far from the currents, the [[vector potential|8PEMR2J7EF]] is $A(x) \approx \frac{\mu_0}{4\pi} \frac{m \times x}{\abs{x}^3}$, and the [[magnetic field|XRED3C547P]] is approximately $\frac{\mu_0}{4 \pi} \frac{3 (m \cdot \hat x) \hat x - m}{\abs{x}^3}$, with $\hat x = x / \abs{x}$.
In a uniform field $B$, the torque on the distribution is $m \times B$ and its energy is $-m \cdot B$.
Example: a circular loop of radius $R$ in the plane $x_3 = 0$ with counterclockwise current $I$ has $m = (0, 0, I \pi R^2)$.
Non-example: a current flowing straight along a line from one point to another is not a closed loop and has $\nabla \cdot J \ne 0$ at its ends, so the definition does not apply.
The unit of $m$ is the ampere square metre.
