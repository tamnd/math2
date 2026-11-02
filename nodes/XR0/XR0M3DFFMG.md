---
tag: XR0M3DFFMG
kind: statement
role: theorem
name: Hodge index theorem
msc: [14C17, 14J25]
uses: [KFTECAATKG, Z9DN23DAE2, RRK8P6TXG2, 4HV4WTAX9P, XMZ09SBM0X, 07EZA80NEH]
about: [4HV4WTAX9P, XMZ09SBM0X]
sources:
  - url: https://en.wikipedia.org/wiki/Hodge_index_theorem
same_as:
  wikidata: Q5876058
  wikipedia: Hodge index theorem
---

## Statement

Let $S$ be a smooth projective [[algebraic surface|KFTECAATKG]] over an algebraically closed field.
For [[divisors|Z9DN23DAE2]] $D$ and $E$ on $S$, let $D \cdot E$ be their [[intersection number|4HV4WTAX9P]].
Let $H$ be an [[ample divisor|RRK8P6TXG2]] on $S$, and let $D$ be a divisor with $D \cdot H = 0$.
Then $D^2 \le 0$, and $D^2 = 0$ holds if and only if $D \cdot E = 0$ for every divisor $E$ on $S$.

## Remarks

Equivalently, the intersection form on the real vector space $\operatorname{NS}(S) \otimes \R$, where $\operatorname{NS}(S)$ is the [[Néron–Severi group|XMZ09SBM0X]], has [[signature|07EZA80NEH]] $(1, \rho - 1)$, where $\rho$ is its dimension.
The proof uses Riemann–Roch on the surface, which shows that if $D^2 > 0$, then $nD$ or $-nD$ is linearly equivalent to an effective divisor for some $n \ge 1$.
A nonzero effective divisor meets the ample $H$ positively, which contradicts $D \cdot H = 0$.
A useful consequence is the inequality $(D^2)(H^2) \le (D \cdot H)^2$ for $H$ ample and $D$ arbitrary, obtained by applying the theorem to $(H^2) D - (D \cdot H) H$.
Example: on $S = \mathbb{P}^1 \times \mathbb{P}^1$ with fibre classes $F_1, F_2$, one has $F_1^2 = F_2^2 = 0$ and $F_1 \cdot F_2 = 1$; the ample $H = F_1 + F_2$ is orthogonal to $D = F_1 - F_2$, and indeed $D^2 = -2 < 0$.
Over $\C$, Hodge theory gives the more general fact that the cup product on $H^2(S, \R)$ has signature $(2 p_g + 1, h^{1,1} - 1)$, where $p_g = h^{2,0}$.

## Explanations

### L1 human

On a surface, curves can be intersected and their intersection numbers form a quadratic form.
The theorem says that this form has only one positive direction, given by an ample curve, and is negative on everything orthogonal to it.
So its shape is like the light cone in special relativity, with one time direction and many space directions.

### L2 human

The Hodge index theorem is the main structural fact about intersection theory on surfaces.
It is used in a proof of the Riemann hypothesis for curves over finite fields, applied to the graph of Frobenius on a product of curves.
It is also used in the study of the Néron–Severi lattice of K3 surfaces and in many inequalities between Chern numbers.
Its higher-dimensional analogues are the Hodge–Riemann bilinear relations and the hard Lefschetz theorem.
