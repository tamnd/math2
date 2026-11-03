---
tag: E0WD2ATFZD
kind: statement
role: theorem
name: Betti's reciprocal theorem
msc: [74B05, 74G05]
uses: [6W00ZECYT0, SX32X1D537, 0JX86PSSA9]
about: [6W00ZECYT0]
sources:
  - url: https://en.wikipedia.org/wiki/Betti%27s_theorem
same_as:
  wikidata: Q794269
  wikipedia: Betti's theorem
---

## Statement

Let $\Omega \subseteq \R^3$ be a bounded domain with piecewise smooth boundary $\partial \Omega$ and outward unit normal $n$.
Let $C$ be an [[elasticity tensor|SX32X1D537]] field on $\Omega$ with the minor and major symmetries.
For $\alpha = 1, 2$, let $u^{(\alpha)}$ be a displacement field of class $C^2$ on $\overline\Omega$ in static equilibrium in [[linear elasticity|6W00ZECYT0]] under body force $f^{(\alpha)}$.
So $\nabla \cdot \sigma^{(\alpha)} + f^{(\alpha)} = 0$ with $\sigma^{(\alpha)} = C : \varepsilon(u^{(\alpha)})$.
Let $t^{(\alpha)} = \sigma^{(\alpha)} n$ be the surface traction of state $\alpha$.
Then
$$\int_\Omega f^{(1)} \cdot u^{(2)} \, dV + \int_{\partial \Omega} t^{(1)} \cdot u^{(2)} \, dS = \int_\Omega f^{(2)} \cdot u^{(1)} \, dV + \int_{\partial \Omega} t^{(2)} \cdot u^{(1)} \, dS.$$

## Remarks

By the [[divergence theorem|0JX86PSSA9]] and the equilibrium equations, the left side equals $\int_\Omega \sigma^{(1)} : \varepsilon(u^{(2)}) \, dV = \int_\Omega \varepsilon(u^{(1)}) : C : \varepsilon(u^{(2)}) \, dV$.
The major symmetry of $C$ makes this expression symmetric in the two states, which gives the right side.
In words: the work done by the first system of loads through the displacements of the second equals the work done by the second through the displacements of the first.
For point loads on a structure it gives Maxwell's reciprocity.
The displacement at a point $A$ due to a unit load at $B$ equals the displacement at $B$ due to a unit load at $A$, in the corresponding directions.
Without the major symmetry, which holds when the material has a stored energy, the theorem fails in general.

## Explanations

### L1 human

Push on a beam at point $A$ and measure how much point $B$ moves.
Then push equally hard at $B$ and measure how much $A$ moves.
Betti's theorem says the two answers are the same.
More generally, two ways of loading an elastic body are linked by a simple exchange rule for the work they do.

### L2 human

The theorem is the basis of the boundary integral equations of elastostatics.
Taking the second state to be the Kelvin point-force solution gives the Somigliana identity.
This identity expresses the displacement inside the body by integrals over the boundary.
It also underlies influence lines in structural analysis and the symmetry of stiffness and flexibility matrices.
