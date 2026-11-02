---
tag: GG6NYPKMHX
kind: statement
role: theorem
name: Chern–Gauss–Bonnet theorem
msc: [53C20, 57R20, 58A10]
uses: [7CBT4SM83Y, RNDDWDAFJ5, ZAJFW1S078, CAZYGE1T4E, NH5HWBPWS9, ESGEHKPD60]
about: [RNDDWDAFJ5, ZAJFW1S078]
sources:
  - url: https://en.wikipedia.org/wiki/Chern%E2%80%93Gauss%E2%80%93Bonnet_theorem
same_as:
  wikidata: Q11704319
  wikipedia: Chern–Gauss–Bonnet theorem
---

## Statement

Let $(M, g)$ be a compact oriented [[Riemannian manifold|7CBT4SM83Y]] without boundary, of even dimension $n = 2m$.
Let $\Omega = (\Omega_{ij})$ be the [[curvature form|ZAJFW1S078]] of the [[Levi-Civita connection|CAZYGE1T4E]] with respect to a local oriented orthonormal frame, a skew-symmetric $n \times n$ matrix of 2-forms.
Then the $n$-form $\operatorname{Pf}(\Omega)$, where $\operatorname{Pf}$ is the [[Pfaffian|NH5HWBPWS9]], does not depend on the frame, and
$$\chi(M) = \frac{1}{(2\pi)^m} \int_M \operatorname{Pf}(\Omega),$$
where $\chi(M)$ is the [[Euler characteristic|RNDDWDAFJ5]] of $M$.

## Remarks

Chern gave an intrinsic proof in 1944: on the unit sphere bundle of $M$, the form $\operatorname{Pf}(\Omega)$ pulled back is exact, $d\Pi$, by a transgression formula.
Take a vector field $X$ with isolated zeros, and integrate over $M$ minus small balls around the zeros.
Stokes' theorem gives the sum of the indices of $X$, which is $\chi(M)$ by the Poincaré–Hopf theorem.

Example: for $m = 1$, $\operatorname{Pf}(\Omega) = \Omega_{12} = K \, dA$ with $K$ the Gaussian curvature, and the formula is the [[Gauss–Bonnet theorem|ESGEHKPD60]] $\int_M K \, dA = 2\pi \chi(M)$.
For $m = 2$ it reads
$$\chi(M) = \frac{1}{32\pi^2} \int_M \bigl(\abs{\operatorname{Rm}}^2 - 4 \abs{\operatorname{Ric}}^2 + R^2\bigr) \, dV,$$
with $\operatorname{Rm}$ the Riemann tensor, $\operatorname{Ric}$ the Ricci tensor and $R$ the scalar curvature.
For the unit sphere $S^4$ the integrand is $24 - 144 + 144 = 24$ and the volume is $8\pi^2/3$, which gives $\chi(S^4) = 2$.

For odd $n$ the Euler characteristic of a closed manifold is $0$, so there is no analogous curvature formula.

## Explanations

### L1 human

Add up the curvature of a closed even-dimensional space over all its points.
The theorem says that the result depends only on the shape up to deformation: it is the Euler characteristic.
However the space is bent, the total curvature stays the same.

### L2 human

The theorem generalizes the Gauss–Bonnet theorem for surfaces to all even dimensions.
In the language of characteristic classes, $\operatorname{Pf}(\Omega / 2\pi)$ represents the Euler class of the tangent bundle in de Rham cohomology.
The theorem then says that the Euler number of the tangent bundle is $\chi(M)$.
It is a model case of Chern–Weil theory and a special case of the Atiyah–Singer index theorem, for the operator $d + \delta$ from even to odd forms.
