---
tag: VV0B6C9CAS
kind: statement
role: theorem
name: Compatibility conditions
msc: [74A05]
uses: [HTYRR2WDQ6, 0QW64ARSHB, 0NF6GQNXMY, F7WK9V3GBP]
about: [HTYRR2WDQ6]
sources:
  - url: https://en.wikipedia.org/wiki/Compatibility_(mechanics)
---

## Statement

Let $\Omega \subseteq \R^3$ be an open, connected and [[simply connected|0QW64ARSHB]] set, and let $F \colon \Omega \to \R^{3 \times 3}$ be a continuously differentiable matrix field with entries $F_{iJ}$.
Then there is a twice continuously differentiable map $\varphi \colon \Omega \to \R^3$ with $\nabla \varphi = F$ if and only if
$$\frac{\partial F_{iJ}}{\partial X_K} = \frac{\partial F_{iK}}{\partial X_J} \quad \text{on } \Omega \text{ for all } i, J, K \in \set{1, 2, 3}.$$
In that case $\varphi$ is unique up to an additive constant vector.

## Remarks

Necessity is the symmetry of second partial derivatives of $\varphi$.
For sufficiency, the condition says that each row $(F_{i1}, F_{i2}, F_{i3})$ has zero [[curl|0NF6GQNXMY]].
On a simply connected set such a field is the gradient of a function $\varphi_i$, obtained by integrating along paths.
So a candidate [[deformation gradient|HTYRR2WDQ6]] field comes from an actual deformation exactly when it is curl-free row by row.
Simple connectivity is needed.
Take $\Omega = \set{X : 1 < X_1^2 + X_2^2 < 4, \ 0 < X_3 < 1}$, and let $F$ have first row $\left(-X_2, X_1, 0\right)/(X_1^2 + X_2^2)$, the gradient of the polar angle, and other rows $e_2^T$ and $e_3^T$.
This $F$ satisfies the condition but is not a gradient, since the angle is not single-valued on $\Omega$.
The analogous condition for the infinitesimal strain tensor is the [[Saint-Venant compatibility condition|F7WK9V3GBP]].

## Explanations

### L1 human

Not every field of matrices can be the local stretching of a real deformation.
If the little pieces are deformed in incompatible ways, they cannot be glued back into one continuous body without gaps or overlaps.
The compatibility conditions are the test that the pieces fit.

### L2 human

In this form the statement is the Poincaré lemma for closed $1$-forms, applied to each component of $\varphi$.
In solid mechanics compatibility is usually imposed on strains rather than on $F$.
For small strains this leads to the Saint-Venant equations, and for finite strains to the vanishing of the Riemann curvature of the metric $C$.
Failure of compatibility in a multiply connected body is the continuum picture of dislocations.
