---
tag: YMHYAEJQ80
kind: statement
role: theorem
name: Bochner–Martinelli formula
msc: [32A26, 32W05]
uses: [DC81TCR98Y, M1VKCW3RFW, 507C34W0ZT]
about: [M1VKCW3RFW, 507C34W0ZT]
sources:
  - url: https://en.wikipedia.org/wiki/Bochner%E2%80%93Martinelli_formula
same_as:
  wikidata: Q4936246
  wikipedia: Bochner–Martinelli formula
---

## Statement

Let $n \ge 1$ and let $D \subseteq \C^n$ be a bounded domain with $C^1$ boundary $\partial D$, oriented as the boundary of $D$.
For $\zeta \ne z$ in $\C^n$, let $\omega(\zeta, z)$ be the Bochner–Martinelli kernel, the $(n, n-1)$-form in $\zeta$
$$\omega(\zeta, z) = \frac{(n-1)!}{(2\pi i)^n} \frac{1}{\abs{\zeta - z}^{2n}} \sum_{j=1}^n (\bar\zeta_j - \bar z_j) \, d\zeta_j \wedge \bigwedge_{k \ne j} \left( d\bar\zeta_k \wedge d\zeta_k \right).$$
Let $f$ be a function of class $C^1$ on a neighbourhood of the closure $\overline{D}$.
Then for every $z \in D$,
$$f(z) = \int_{\partial D} f(\zeta) \, \omega(\zeta, z) - \int_{D} \bar\partial f(\zeta) \wedge \omega(\zeta, z),$$
where $\bar\partial$ is the [[$\bar\partial$ operator|M1VKCW3RFW]] in $\zeta$.

## Remarks

The forms $d\bar\zeta_k \wedge d\zeta_k$ have degree $2$, so the order of the factors in the product does not matter.
For fixed $z$, the kernel satisfies $d_\zeta \, \omega(\zeta, z) = 0$ on $\zeta \ne z$.
Apply Stokes' theorem on $D$ minus a small ball around $z$ and let the radius tend to $0$; the small sphere contributes $f(z)$ in the limit.
If $f$ is [[holomorphic|507C34W0ZT]] near $\overline{D}$, then $\bar\partial f = 0$ and $f(z) = \int_{\partial D} f(\zeta) \, \omega(\zeta, z)$.
For $n = 1$, $\omega(\zeta, z) = \frac{1}{2\pi i} \frac{d\zeta}{\zeta - z}$ and the formula is the Cauchy–Pompeiu formula, which contains the Cauchy integral formula.
For $n \ge 2$ the kernel is not holomorphic in $z$, unlike the Cauchy kernel of the polydisc, but it works on every bounded domain with $C^1$ boundary.

## Explanations

### L1 human

The formula recovers the values of a function inside a domain from its values on the boundary.
A correction term measures how far the function is from being holomorphic.
For holomorphic functions the correction is zero.
It is a version of the Cauchy integral formula that works on any reasonable bounded domain of $\C^n$, not only on products of discs.

### L2 human

The kernel is built from the fundamental solution of the Laplacian on $\R^{2n}$, which is why it is not holomorphic in $z$ when $n \ge 2$.
The formula is a main tool for solving the equation $\bar\partial u = g$ and for proving extension results such as the Hartogs–Bochner theorem.
It is the special case $\eta_j = (\bar\zeta_j - \bar z_j)/\abs{\zeta - z}^2$ of the [[Cauchy–Fantappiè formula|R9JJ44TMQB]] for holomorphic functions.
