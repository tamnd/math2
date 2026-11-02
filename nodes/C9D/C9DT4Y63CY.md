---
tag: C9DT4Y63CY
kind: statement
role: theorem
name: Cheeger–Müller theorem
msc: [58J52, 57Q10]
uses: [MZT9D34B0A, 7CBT4SM83Y, 74BPYJNZTM, S1XK3HXHFX]
about: [MZT9D34B0A]
sources:
  - url: https://en.wikipedia.org/wiki/Analytic_torsion
---

## Statement

Let $M$ be a closed oriented Riemannian manifold, and let $\rho$ be an acyclic orthogonal or unitary representation of $\pi_1(M)$.
Then the [[analytic torsion|MZT9D34B0A]] of $(M, \rho)$ equals the Reidemeister torsion of $(M, \rho)$, computed from any smooth triangulation of $M$.
Here both torsions are normalized with the same convention.

## Remarks

Ray and Singer conjectured the equality, and Cheeger and Müller proved it independently.
Cheeger's proof compares the two sides under surgery; Müller's approximates the de Rham complex by the combinatorial cochain complex of finer and finer triangulations.
Müller extended it to unimodular representations, and Bismut and Zhang gave a proof by Witten deformation that covers all flat bundles, with an explicit correction term.
Example: on the circle with the character $\rho(1) = e^{2\pi i a}$, $0 < a < 1$, the Reidemeister torsion is $\abs{1 - e^{2\pi i a}}$, and the analytic torsion is $2\sin(\pi a)$, the same number.
For lens spaces the theorem gives an analytic way to compute the Reidemeister torsions that distinguish non-homeomorphic homotopy equivalent lens spaces.

## Explanations

### L1 human

Reidemeister torsion is computed by cutting a manifold into simplices and doing linear algebra.
Analytic torsion is computed from the eigenvalues of Laplacians, with no triangulation at all.
The theorem says that these two very different recipes give the same number.

### L2 human

The theorem identifies a spectral invariant with a combinatorial one, in the spirit of index theory but for a secondary invariant.
It motivated the study of torsion in families (the Bismut–Lott torsion forms) and the use of analytic torsion to study torsion in the cohomology of arithmetic groups.
