---
tag: EV1TZJ0KTM
kind: statement
role: theorem
name: CPT theorem
msc: [81T05, 81R05]
uses: [5QTZQV6TNG, QWK3BYVJ9W, 8ZQ9TA4Q2Q]
about: [W031YNVRE3]
sources:
  - url: https://en.wikipedia.org/wiki/CPT_symmetry
---

## Statement

Let a quantum field theory on Minkowski space $\R^{1,3}$ satisfy the [[Wightman axioms|5QTZQV6TNG]], with vacuum $\Omega$.
Let $U(a, \Lambda)$ be its representation of the covering group of the proper orthochronous [[Poincaré group|8ZQ9TA4Q2Q]].
Assume the normal commutation relations at spacelike separation.
That is, two fields anticommute if both have half-integer spin, and commute otherwise.
Then there is an antiunitary operator $\Theta$ on the Hilbert space such that:

1. $\Theta \Omega = \Omega$;
2. $\Theta U(a, \Lambda) \Theta^{-1} = U(-a, \Lambda)$ for all $(a, \Lambda)$;
3. $\Theta$ maps each field $\phi(x)$ to its adjoint at $-x$, up to a constant phase depending on the Lorentz type of the field.
   For a Hermitian scalar field, $\Theta \phi(x) \Theta^{-1} = \phi(-x)$.

## Remarks

The idea of Jost's proof: the Wightman functions extend analytically to the forward tube and are covariant under the complex [[Lorentz group|QWK3BYVJ9W]].
The proper complex Lorentz group contains $-1$, which is not in the real proper orthochronous group.
At real points of the extended tube (Jost points), where all differences are spacelike, locality lets one reverse the order of the fields.
Combining the two gives an identity between Wightman functions at $x$ and at $-x$ in reversed order.
This identity is exactly the statement that $\Theta$ defined on states is antiunitary and has the stated properties.

Consequences: a particle and its antiparticle have the same mass and the same lifetime.
Jost also showed that CPT invariance is equivalent to weak local commutativity, a condition on Wightman functions at Jost points.

## Explanations

### L1 human

C swaps particles and antiparticles, P reflects space, and T reverses time.
Each of these alone can fail to be a symmetry of nature, and the weak interaction violates C, P and even CP.
The CPT theorem says that the combination of all three is always a symmetry of a relativistic local quantum field theory.

### L2 human

In the Wightman framework the theorem needs only Lorentz invariance, positivity of the energy and locality.
It sits next to the [[spin–statistics theorem|5QYRVQY3T7]], which uses the same analytic continuation.
A measured difference between the masses of a particle and its antiparticle would refute local relativistic quantum field theory, and such experiments are standard tests.
