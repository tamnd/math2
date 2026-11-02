---
tag: TTXDZENFVB
kind: statement
role: theorem
name: Bianchi identities
msc: [53C05, 53B20]
uses: [ZAJFW1S078, JA29ETCM02, JZNQAN00ZJ, 5FZDQQHQKM, JX65KSVHSJ]
about: [ZAJFW1S078, JA29ETCM02]
sources:
  - url: https://en.wikipedia.org/wiki/Curvature_form
  - url: https://en.wikipedia.org/wiki/Riemann_curvature_tensor
---

## Statement

1. Let $G$ be a Lie group with Lie algebra $\mathfrak{g}$, and let $P \to M$ be a principal $G$-bundle with connection form $\omega$. Let $\Omega = d\omega + \frac12 [\omega \wedge \omega]$ be its [[curvature form|ZAJFW1S078]]. Then
$$d\Omega + [\omega \wedge \Omega] = 0,$$
where $[\omega \wedge \Omega](X, Y, Z)$ is the sum over cyclic permutations $(X, Y, Z)$ of $[\omega(X), \Omega(Y, Z)]$.
2. Let $M$ be a smooth manifold with a torsion-free [[affine connection|JX65KSVHSJ]] $\nabla$ (its [[torsion|JZNQAN00ZJ]] vanishes) and [[curvature tensor|JA29ETCM02]] $R$. Then for all vector fields $X, Y, Z, W$:
   - (first Bianchi identity) $R(X, Y) Z + R(Y, Z) X + R(Z, X) Y = 0$;
   - (second Bianchi identity) $(\nabla_X R)(Y, Z) W + (\nabla_Y R)(Z, X) W + (\nabla_Z R)(X, Y) W = 0$, where $\nabla_X R$ is the [[covariant derivative|5FZDQQHQKM]] of the tensor field $R$.

## Remarks

For part 1, apply $d$ to the structure equation: $d\Omega = \frac12 d[\omega \wedge \omega] = \frac12\big([d\omega \wedge \omega] - [\omega \wedge d\omega]\big)$, substitute $d\omega = \Omega - \frac12[\omega \wedge \omega]$, and use the Jacobi identity to see that $[[\omega \wedge \omega] \wedge \omega] = 0$.
Part 1 is often written $D\Omega = 0$, with $D$ the exterior covariant derivative.
For the first identity in part 2, expand $R$ and use $\nabla_X Y - \nabla_Y X = [X, Y]$; the cyclic sum reduces to the Jacobi identity for the Lie bracket.
Without the torsion-free hypothesis the identities get extra terms involving the torsion and its covariant derivative.
Example: tracing the second identity for the Levi-Civita connection gives $\mathrm{div}\, \mathrm{Ric} = \frac12 \, d\,\mathrm{scal}$, so the Einstein tensor $\mathrm{Ric} - \frac12 \mathrm{scal}\, g$ is divergence-free.

## Explanations

### L1 human

Curvature is not an arbitrary collection of numbers: it satisfies some built-in rules.
The Bianchi identities are these rules.
One is algebraic and says that a certain cyclic sum of curvatures is zero.
The other says that a cyclic sum of derivatives of curvature is zero, much like the rule that the divergence of a curl is zero.

### L2 human

The first identity, together with the symmetries of the Riemann tensor, cuts down its number of independent components to $n^2(n^2 - 1)/12$ in dimension $n$.
The contracted second identity is the reason the left side of Einstein's field equations is divergence-free, which matches conservation of energy and momentum.
In gauge theory, part 1 says that the field strength $F$ of a gauge field satisfies $D F = 0$; for electromagnetism this gives the two homogeneous Maxwell equations.
Part 1 is also the key step in showing that the forms $f(\Omega)$ of Chern–Weil theory are closed.
