---
tag: G3X02FKQCR
kind: statement
role: theorem
name: Hirzebruch–Riemann–Roch theorem
msc: [14C40, 14C17, 32L10]
uses: [A4H4CZ2V35, EXKGG9X6J0, P4DZM975BV, PQ6Q143ARJ, PAD37GKDPD, 2YDB5089FR]
about: [P4DZM975BV, PAD37GKDPD, 2YDB5089FR]
sources:
  - url: https://en.wikipedia.org/wiki/Hirzebruch–Riemann–Roch_theorem
same_as:
  wikidata: Q4663326
  wikipedia: Hirzebruch–Riemann–Roch theorem
---

## Statement

Let $X$ be a [[smooth|EXKGG9X6J0]] [[projective variety|A4H4CZ2V35]] of dimension $n$ over $\C$, and let $\mathcal{E}$ be a [[vector bundle|P4DZM975BV]] of rank $r$ on $X$.
Let $\chi(X, \mathcal{E}) = \sum_{i=0}^{n} (-1)^i \dim_\C H^i(X, \mathcal{E})$, where $H^i$ is [[sheaf cohomology|PQ6Q143ARJ]].
Let $\alpha_1, \dots, \alpha_r$ be the Chern roots of $\mathcal{E}$ and $\beta_1, \dots, \beta_n$ those of the tangent bundle $T_X$.
So the [[Chern classes|PAD37GKDPD]] are the elementary symmetric functions in these roots.
Let $\operatorname{ch}(\mathcal{E}) = \sum_{j=1}^{r} e^{\alpha_j}$ be the Chern character and $\operatorname{td}(T_X) = \prod_{j=1}^{n} \frac{\beta_j}{1 - e^{-\beta_j}}$ the [[Todd class|2YDB5089FR]], both in $H^{*}(X, \Q)$.
Then
$$\chi(X, \mathcal{E}) = \int_X \operatorname{ch}(\mathcal{E}) \, \operatorname{td}(T_X),$$
where $\int_X$ takes the degree $2n$ component and evaluates it on the fundamental class.

## Remarks

Hirzebruch proved the theorem with Thom's cobordism theory: both sides are multiplicative and compatible with the relevant operations, and they agree on enough generators.
Later proofs come from the Grothendieck–Riemann–Roch theorem, applied to $X \to \operatorname{Spec} \C$, and from the Atiyah–Singer index theorem, which extends it to all compact complex manifolds.
The same formula holds for smooth projective varieties over any field, with the Chow ring in place of $H^*(X, \Q)$.

Example: for a curve $X$ of genus $g$ and a line bundle $L$ of degree $d$, $\operatorname{ch}(L) = 1 + c_1(L)$ and $\operatorname{td}(T_X) = 1 + \tfrac{1}{2} c_1(T_X)$ with $\deg c_1(T_X) = 2 - 2g$.
The degree $2$ part is $c_1(L) + \tfrac12 c_1(T_X)$, so $\chi(L) = d + 1 - g$, the classical Riemann–Roch theorem.

For a surface, the case $\mathcal{E} = \mathcal{O}_X$ gives Noether's formula $\chi(\mathcal{O}_X) = \tfrac{1}{12}(c_1^2 + c_2)$.

## Explanations

### L1 human

The Euler characteristic of a vector bundle is an alternating count of the dimensions of its cohomology groups.
The theorem computes this number from topological data alone: the Chern classes of the bundle and of the variety.
So a quantity defined through hard analysis or algebra turns out to depend only on characteristic classes.

### L2 human

In practice $\chi(\mathcal{E})$ is computed by the formula, and a vanishing theorem then kills all but one cohomology group, which gives the dimension of the space of sections.
This is how one finds the dimension of linear systems on surfaces and higher-dimensional varieties.
The theorem generalizes the Riemann–Roch theorem for curves and for surfaces, and it is in turn a special case of both the Grothendieck–Riemann–Roch theorem and the Atiyah–Singer index theorem.
