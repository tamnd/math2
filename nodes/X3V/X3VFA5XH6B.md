---
tag: X3VFA5XH6B
kind: statement
role: theorem
name: Quillen–Lichtenbaum conjecture
msc: [19F27, 19D50, 14F20]
uses: [ANJ5719F7F, CC2HWX9X2Y, XKMBKAN1MR, 7YX76G0838, 5Q5VN56QH4, 261PM5FZN8]
about: [CC2HWX9X2Y, ANJ5719F7F]
sources:
  - url: https://en.wikipedia.org/wiki/Quillen%E2%80%93Lichtenbaum_conjecture
same_as:
  wikidata: Q7271997
  wikipedia: Quillen–Lichtenbaum conjecture
---

## Statement

Let $\ell$ be a prime number and let $\nu \ge 1$ be an integer.
Let $F$ be a field whose characteristic is not $\ell$, and let $d = \operatorname{cd}_\ell(F)$ be its [[$\ell$-cohomological dimension|XKMBKAN1MR]], assumed finite.
Write $K_n(F; \Z/\ell^\nu)$ for the [[K-groups with finite coefficients|ANJ5719F7F]] of $F$ and $K^{\mathrm{et}}_n(F; \Z/\ell^\nu)$ for its [[étale K-groups|CC2HWX9X2Y]].
Then the natural map
$$K_n(F; \Z/\ell^\nu) \to K^{\mathrm{et}}_n(F; \Z/\ell^\nu)$$
is an isomorphism for all $n \ge d - 1$.

## Remarks

Quillen proposed the conjecture, inspired by earlier conjectures of Lichtenbaum on values of zeta functions.
The étale K-groups are computed from [[étale cohomology|7YX76G0838]] with coefficients $\mu_{\ell^\nu}^{\otimes i}$ by a descent spectral sequence.
So the conjecture says that algebraic K-theory with finite coefficients is computed by étale cohomology in high degrees.
It is now a theorem: it follows from the [[norm residue isomorphism theorem|5Q5VN56QH4]] of Voevodsky and Rost, through the [[motivic spectral sequence|261PM5FZN8]].
For $F = \C$ one has $d = 0$, and $K_n(\C; \Z/\ell^\nu)$ is $\Z/\ell^\nu$ for even $n \ge 0$ and $0$ for odd $n$, which is what étale cohomology of a point predicts.

## Explanations

### L1 human

Algebraic K-groups of a field are very hard to compute directly.
Étale cohomology is much easier to compute, since it is controlled by Galois theory.
The conjecture says that, after reducing modulo a prime power different from the characteristic, the two agree in all degrees above a small bound.
So hard K-theory questions become Galois cohomology questions.

### L2 human

The comparison map goes to Thomason's étale K-theory, which is built so that it satisfies étale descent.
The bound $d - 1$ comes from the shape of the descent spectral sequence, whose columns vanish beyond the cohomological dimension.
The proof goes through motivic cohomology.
The norm residue isomorphism theorem identifies motivic cohomology with finite coefficients with étale cohomology in a range of degrees.
The motivic spectral sequence carries this to K-theory.
For rings of integers in number fields, the theorem gives the groups $K_n(\mathcal{O}_F) \otimes \Z_\ell$ in terms of étale cohomology.
