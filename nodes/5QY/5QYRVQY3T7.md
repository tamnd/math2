---
tag: 5QYRVQY3T7
kind: statement
role: theorem
name: Spin–statistics theorem
msc: [81T05, 81S05]
uses: [5QTZQV6TNG, QWK3BYVJ9W, YBS1CHXFTW]
about: [W031YNVRE3, Y64G7W4BEC]
sources:
  - url: https://en.wikipedia.org/wiki/Spin%E2%80%93statistics_theorem
same_as:
  wikidata: Q523876
  wikipedia: Spin–statistics theorem
---

## Statement

Let $\phi$ be a field on Minkowski space $\R^{1,3}$ in a theory satisfying the [[Wightman axioms|5QTZQV6TNG]].
Assume the inner product on the Hilbert space is positive definite.
Assume that $\phi$ transforms under the irreducible representation $(j, k)$ of $SL(2, \C)$, the double cover of the [[Lorentz group|QWK3BYVJ9W]], where $j, k \in \set{0, \tfrac12, 1, \tfrac32, \dots}$.
Write $[A, B]_{\pm} = AB \pm BA$.

1. If $j + k$ is an integer and $[\phi(x), \phi(y)^*]_{+} = 0$ for all spacelike $x - y$, then $\phi = 0$.
2. If $j + k$ is a half-integer and $[\phi(x), \phi(y)^*]_{-} = 0$ for all spacelike $x - y$, then $\phi = 0$.

So a nonzero field of integer [[spin|YBS1CHXFTW]] must commute at spacelike separation (Bose statistics), and a nonzero field of half-integer spin must anticommute (Fermi statistics).

## Remarks

The proof uses the analytic continuation of the two-point function $\ip{\Omega}{\phi(x)\phi(y)^*\Omega}$ to the complex Lorentz group, which contains the map $x \mapsto -x$.
This continuation relates $\ip{\Omega}{\phi(x)\phi(y)^*\Omega}$ to $\ip{\Omega}{\phi(y)^*\phi(x)\Omega}$ with the sign $(-1)^{2j+2k}$.
With the wrong commutation rule, smearing this relation with test functions gives a sum of two squared norms equal to zero.
This forces $\phi(f)^*\Omega = 0$ for every test function $f$, and then $\phi = 0$ by the separating property in the [[Reeh–Schlieder theorem|A0N6031YWZ]].
Positivity of the inner product is necessary: with an indefinite metric, as for the Faddeev–Popov ghosts of gauge theories, scalar fields with anticommutation relations occur.

Example: the Dirac field has $(j, k) = (\tfrac12, 0) \oplus (0, \tfrac12)$ and is quantized with anticommutators, which is why electrons obey the [[Pauli exclusion principle|ZQGC326NP7]].

## Explanations

### L1 human

Particles come in two kinds: bosons, such as photons, which like to share a state, and fermions, such as electrons, which never share one.
The theorem explains which is which: particles of integer spin are bosons and particles of half-integer spin are fermions.
It follows from relativity, positive energy and the fact that measurements at spacelike separation do not interfere.

### L2 human

In nonrelativistic quantum mechanics the link between spin and statistics is an extra postulate.
In relativistic quantum field theory it becomes a theorem, first argued by Pauli for free fields and later proved in the Wightman framework.
It is closely related to the [[CPT theorem|EV1TZJ0KTM]]: both rest on the analytic continuation of Wightman functions to the complex Lorentz group.
Its consequences include the structure of the periodic table and the stability of matter.
