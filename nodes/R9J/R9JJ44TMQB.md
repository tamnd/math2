---
tag: R9JJ44TMQB
kind: statement
role: theorem
name: Cauchy–Fantappiè formula
msc: [32A26]
uses: [YMHYAEJQ80, M1VKCW3RFW, 507C34W0ZT]
about: [507C34W0ZT]
sources:
  - url: https://en.wikipedia.org/wiki/Bochner%E2%80%93Martinelli_formula
---

## Statement

Let $n \ge 1$ and let $D \subseteq \C^n$ be a bounded domain with $C^1$ boundary $\partial D$, oriented as the boundary of $D$.
Fix $z \in D$.
Let $\eta = (\eta_1, \dots, \eta_n)$ be a map of class $C^1$ from a neighbourhood of $\partial D$ to $\C^n$ such that
$$\sum_{j=1}^n \eta_j(\zeta) (\zeta_j - z_j) = 1 \quad \text{for all } \zeta \in \partial D.$$
Put
$$\omega_\eta(\zeta) = \frac{(n-1)!}{(2\pi i)^n} \sum_{j=1}^n \eta_j(\zeta) \, d\zeta_j \wedge \bigwedge_{k \ne j} \left( \bar\partial \eta_k \wedge d\zeta_k \right),$$
where $\bar\partial$ is the [[$\bar\partial$ operator|M1VKCW3RFW]] in $\zeta$.
Let $f$ be a [[holomorphic function|507C34W0ZT]] on a neighbourhood of $\overline{D}$.
Then
$$f(z) = \int_{\partial D} f(\zeta) \, \omega_\eta(\zeta).$$

## Remarks

The forms $\bar\partial \eta_k \wedge d\zeta_k$ have degree $2$, so the order of the factors in the product does not matter.
With $\eta_j(\zeta) = (\bar\zeta_j - \bar z_j)/\abs{\zeta - z}^2$, the form $\omega_\eta$ is the kernel of the [[Bochner–Martinelli formula|YMHYAEJQ80]], and the statement reduces to that formula for holomorphic $f$.
For a general $\eta$, a homotopy argument joining $\eta$ to the Bochner–Martinelli choice shows that the boundary integral does not depend on $\eta$.
For $n = 1$ the condition forces $\eta = 1/(\zeta - z)$, and the formula is the Cauchy integral formula.
On a convex domain with $C^2$ boundary, one can choose $\eta$ depending holomorphically on $z$, which gives integral formulas with kernels holomorphic in $z$.

## Explanations

### L1 human

There are many integral formulas that recover a holomorphic function inside a domain from its boundary values.
The Cauchy–Fantappiè formula produces one formula for each choice of an auxiliary map $\eta$ satisfying a single linear condition.
Different choices of $\eta$ adapt the formula to the shape of the domain.

### L2 human

The Bochner–Martinelli kernel is universal but not holomorphic in $z$, which limits its use.
The freedom in $\eta$ allows kernels that are holomorphic in $z$ on convex or strongly pseudoconvex domains.
Such kernels, built by Henkin, Ramírez and others, give solutions of the $\bar\partial$ equation with estimates and results on approximation by holomorphic functions.
