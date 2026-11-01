---
tag: 55XX5A7XZV
kind: statement
role: theorem
name: Class number formula
msc: [11R42, 11R29]
uses: [MWBDFS2KJ5, KXS5DQDFYD, KTKK9B1X41, RWK0HNF1NA, E0VZTNPJXA, 0YV2CKP2AV, 1D99CSKX6N, 9D2Z543EJQ]
about: [KXS5DQDFYD, KTKK9B1X41]
sources:
  - url: https://en.wikipedia.org/wiki/Class_number_formula
same_as:
  wikidata: Q3291120
  wikipedia: Class number formula
---

## Statement

Let $K$ be an [[algebraic number field|MWBDFS2KJ5]].
Let $r_1$ be the number of real embeddings of $K$ and $r_2$ the number of pairs of complex conjugate non-real embeddings.
Let $h_K$ be the [[class number|KTKK9B1X41]] of $K$, $R_K$ its [[regulator|RWK0HNF1NA]], $w_K$ the number of [[roots of unity|0YV2CKP2AV]] in $K$ and $d_K$ its [[discriminant|E0VZTNPJXA]].
Then the [[Dedekind zeta function|KXS5DQDFYD]] $\zeta_K(s)$ has a simple pole at $s = 1$, and
$$\lim_{s \to 1^+} (s - 1)\, \zeta_K(s) = \frac{2^{r_1} (2\pi)^{r_2}\, h_K\, R_K}{w_K \sqrt{\abs{d_K}}}.$$

## Remarks

The proof counts ideals of norm at most $x$ in each ideal class.
This count reduces to counting lattice points in a region of $\R^{r_1} \times \C^{r_2}$ cut out using the units.
So its leading term is a volume; the volume brings in $R_K$ and $\sqrt{\abs{d_K}}$, and the classes bring in $h_K$.
Example: for $K = \Q$ one has $r_1 = 1$, $r_2 = 0$, $h = R = 1$, $w = 2$, $d = 1$, and the formula gives residue $1$, as for the Riemann zeta function.
For an imaginary quadratic field of discriminant $d < 0$, the formula becomes $h_K = \frac{w_K \sqrt{\abs{d}}}{2\pi} L(1, \chi_d)$, where $\chi_d$ is the Kronecker character of $K$ and $L$ its [[Dirichlet L-function|9D2Z543EJQ]].
For $K = \Q(i)$: $w = 4$, $d = -4$ and $L(1, \chi_{-4}) = 1 - \frac13 + \frac15 - \dots = \frac{\pi}{4}$, so $h_K = 1$.

## Explanations

### L1 human

The class number measures how far unique factorisation fails in a number field.
The formula says that this number, together with other basic invariants of the field, can be read off from the behaviour of an analytic function near the point $s = 1$.
So a purely algebraic quantity is computed by analysis.

### L2 human

For an abelian field $K$, the function $\zeta_K(s)$ is the product of $\zeta(s)$ and Dirichlet $L$-functions, so the residue becomes a product of values $L(1, \chi)$.
This gives Dirichlet's class number formulas for quadratic fields, and the fact that $L(1, \chi) \ne 0$ for real characters, which is the key step in [[Dirichlet's theorem on arithmetic progressions|0GNVN3CA2P]].
The units enter through the regulator, which is defined by means of [[Dirichlet's unit theorem|1D99CSKX6N]].
