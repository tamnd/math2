---
tag: QAY5HXG1G2
kind: definition
name: Magnetic helicity
msc: [78A30, 76W05]
defines: 5V4YEMZ0EA
uses: [XRED3C547P, 8PEMR2J7EF, SFJ329YB9F, 0JX86PSSA9]
sources:
  - url: https://en.wikipedia.org/wiki/Magnetic_helicity
---

## Definition

Let $V \subseteq \R^3$ be a bounded open set with smooth boundary and outward unit normal $n$.
Let $B$ be a smooth [[magnetic field|XRED3C547P]] on the closure of $V$ such that $\nabla \cdot B = 0$ in $V$ and $B \cdot n = 0$ on $\partial V$.
Let $A$ be a smooth [[vector potential|8PEMR2J7EF]] of $B$ on $V$, that is, $\nabla \times A = B$.
The *magnetic helicity* of $B$ in $V$ is
$$\mathcal{H}(B) = \int_V A \cdot B \, dV.$$

## Remarks

The boundary condition makes $\mathcal{H}$ independent of the choice of $A$ up to gauge.
If $\chi$ is a smooth function on the closure of $V$ and $A' = A + \nabla \chi$, then $\nabla \cdot (\chi B) = \nabla \chi \cdot B$, so by the [[divergence theorem|0JX86PSSA9]]
$$\int_V A' \cdot B \, dV - \int_V A \cdot B \, dV = \int_{\partial V} \chi \, B \cdot n \, dS = 0.$$
On a region that is not simply connected, adding to $A$ a curl-free field that is not a gradient can change the integral, and one fixes extra conditions on $A$.

Example: for two thin untwisted closed flux tubes with fluxes $\Phi_1$ and $\Phi_2$, the helicity is $2 \, \mathrm{Lk} \, \Phi_1 \Phi_2$, where $\mathrm{Lk}$ is the [[linking number|SFJ329YB9F]] of their core curves.
So linked tubes have nonzero helicity and unlinked untwisted tubes have helicity $0$.

Non-example: the uniform field $B = (0, 0, 1)$ on the open unit cube does not satisfy $B \cdot n = 0$ on the top and bottom faces.
There the integral depends on the potential: $A = (-y, 0, 0)$ gives $\int A \cdot B \, dV = 0$, while $A = (-y, 0, 1)$, which has the same curl, gives $1$.

The same integral, written for the vorticity of a fluid, is the kinetic helicity of the flow.
