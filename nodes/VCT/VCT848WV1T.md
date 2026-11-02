---
tag: VCT848WV1T
kind: statement
role: theorem
name: Newlander–Nirenberg theorem
msc: [32Q60, 53C15]
uses: [9SYWRGVTRS, 68FGQEBD6J, F45VQ47GPV, 5Q4BHBFXJY, Q61VFHCH2J]
about: [9SYWRGVTRS]
sources:
  - url: https://en.wikipedia.org/wiki/Almost_complex_manifold
---

## Statement

Let $(M, J)$ be an [[almost complex manifold|9SYWRGVTRS]] of dimension $2n$, with $J$ smooth.
Let $N_J$ be the Nijenhuis tensor of $J$.
Then the following are equivalent.

1. $N_J = 0$ on $M$.
2. $M$ has an atlas of charts $\varphi \colon U \to \C^n$ whose transition maps are holomorphic and such that $d\varphi \circ J = i \cdot d\varphi$ on each $U$.

In that case $J$ is the almost complex structure of a unique complex manifold structure on $M$.

## Remarks

The implication from 2 to 1 is a direct computation: in holomorphic charts $J$ has constant coefficients, so all the brackets in $N_J$ cancel.
The hard direction is from 1 to 2.
When $J$ is real analytic, consider the bundle of $(0,1)$-vectors.
The condition $N_J = 0$ says that this bundle is closed under the bracket, and a complex form of the [[Frobenius theorem|5Q4BHBFXJY]] gives the charts.
For smooth $J$ one must solve a nonlinear system of partial differential equations of $\bar\partial$ type, which is the analytic heart of the proof.

In real dimension $2$ the tensor $N_J$ always vanishes, because $N_J(X, JX) = 0$ and $N_J$ is antisymmetric.
So every almost complex structure on a surface is integrable.
In particular, an oriented surface with a [[Riemannian metric|Q61VFHCH2J]], with $J$ the rotation by a right angle, is a Riemann surface.

## Explanations

### L1 human

An almost complex structure lets one multiply tangent vectors by $i$, but it may not come from complex coordinates.
The theorem gives a test: a certain tensor built from $J$ and brackets of vector fields must vanish.
When it vanishes, complex coordinates exist near every point.

### L2 human

The theorem turns the question "is $M$ a complex manifold" into the vanishing of a tensor, a condition that can be checked locally.
It is used to show that Kähler and many other geometric structures defined by tensors are really complex manifolds.
On surfaces it contains the existence of isothermal coordinates.
In higher dimension many almost complex manifolds have non-integrable structures; on $S^6$ the octonionic structure is not integrable, and whether $S^6$ admits any complex structure is an open problem.
