---
tag: SEG9TKP2KQ
kind: statement
role: theorem
name: Williams crack-tip expansion
msc: [74R10, 74G70, 74B05]
uses: [8D619PN75J, H1J9Q4TVJ6, 6W00ZECYT0, 7ZGSJRYBGK]
about: [8D619PN75J]
sources:
  - url: https://en.wikipedia.org/wiki/Fracture_mechanics
---

## Statement

Let $\Omega \subset \R^2$ contain the slit $\set{(x_1, 0) : -\delta < x_1 \le 0}$ and let $(r, \theta)$, $-\pi < \theta < \pi$, be polar coordinates centred at its tip.
Let the stress $\sigma$ solve the equations of plane [[linear elasticity|6W00ZECYT0]] for an isotropic material in $B_\delta(0)$ minus the slit, without body forces.
Assume that the crack faces $\theta = \pm \pi$ are traction-free and that the elastic energy near the tip is finite.
Then there are real numbers $a_n$, $b_n$ such that, for $r < \delta$,
$$\sigma_{ij}(r, \theta) = \sum_{n=1}^{\infty} r^{n/2 - 1} \left( a_n f_{ij}^{(n)}(\theta) + b_n g_{ij}^{(n)}(\theta) \right).$$
Here $f^{(n)}$ and $g^{(n)}$ are fixed trigonometric functions, symmetric (mode I) and antisymmetric (mode II) with respect to the crack line.
The leading term is the inverse square root singularity with the [[stress intensity factors|8D619PN75J]]; in mode I it reads
$$\sigma_{11} = \frac{K_I}{\sqrt{2 \pi r}} \cos\frac{\theta}{2} \Big(1 - \sin\frac{\theta}{2} \sin\frac{3\theta}{2}\Big), \quad \sigma_{22} = \frac{K_I}{\sqrt{2 \pi r}} \cos\frac{\theta}{2} \Big(1 + \sin\frac{\theta}{2} \sin\frac{3\theta}{2}\Big), \quad \sigma_{12} = \frac{K_I}{\sqrt{2 \pi r}} \cos\frac{\theta}{2} \sin\frac{\theta}{2} \cos\frac{3\theta}{2}.$$
The term with $n = 2$ is a uniform stress $\sigma_{11} = T$ parallel to the crack, the T-stress.

## Remarks

The proof writes the stress with an [[Airy stress function|7ZGSJRYBGK]] $\phi$, which is biharmonic, and looks for separated solutions $\phi = r^{\lambda + 1} F(\theta)$.
The traction-free conditions on $\theta = \pm \pi$ give a homogeneous linear system for the coefficients of $F$, which has nontrivial solutions only when $\sin(2\pi\lambda) = 0$, that is $\lambda = n/2$.
Finite energy near the tip excludes $\lambda \le 0$, which leaves $\lambda = 1/2, 1, 3/2, \dots$.
Without the finite energy hypothesis, solutions with stronger singularities such as $r^{-3/2}$ would be admitted.
At $\theta = 0$ the mode I formulas give $\sigma_{22} = K_I / \sqrt{2 \pi r}$, consistent with the definition of $K_I$.

## Explanations

### L1 human

Near the tip of a crack, the stress field always has the same shape, whatever the body and the loads.
Only a few numbers, the coefficients of the expansion, change from one problem to another.
The first of them is the stress intensity factor, which multiplies a field that blows up like one over the square root of the distance to the tip.

### L2 human

The expansion justifies the one-parameter description of linear elastic [[fracture mechanics|SNRXGRZWR5]]: close to the tip, the first term dominates, so $K_I$, $K_{II}$ and $K_{III}$ characterize the crack-tip loading.
The second term, the T-stress, measures the constraint at the tip and affects the size and shape of the plastic zone and the stability of the crack path.
The same method of separated solutions gives the singularities at the vertex of a wedge or a notch, where the exponents are no longer half-integers.
The [[modes of fracture|H1J9Q4TVJ6]] correspond to the symmetric and antisymmetric parts of the expansion, and mode III arises from the analogous antiplane problem.
