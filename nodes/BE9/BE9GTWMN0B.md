---
tag: BE9GTWMN0B
kind: statement
role: theorem
name: Weitzenböck identity
msc: [53C21, 58J05, 58A10]
uses: [7CBT4SM83Y, CAZYGE1T4E, 4GTNM0WHDH, 0E3G0GRPZ6, 0ZHSTAG8ZY, 1Y4WX4XQWJ]
about: [4GTNM0WHDH]
sources:
  - url: https://en.wikipedia.org/wiki/Weitzenb%C3%B6ck_identity
same_as:
  wikidata: Q7980430
  wikipedia: Weitzenböck identity
---

## Statement

Let $(M, g)$ be an oriented [[Riemannian manifold|7CBT4SM83Y]] of dimension $n$, with [[Levi-Civita connection|CAZYGE1T4E]] $\nabla$.
On [[differential forms|0E3G0GRPZ6]] of degree $k$, let $d$ be the [[exterior derivative|0ZHSTAG8ZY]].
Let $\delta = (-1)^{n(k+1)+1} \star d \star$ be the codifferential, where $\star$ is the [[Hodge star|1Y4WX4XQWJ]].
Let $\Delta_H = d\delta + \delta d$ be the Hodge Laplacian.
Let $\nabla^* \nabla = -\sum_{i=1}^n \bigl(\nabla_{e_i} \nabla_{e_i} - \nabla_{\nabla_{e_i} e_i}\bigr)$ be the rough Laplacian, for a local orthonormal frame $e_1, \dots, e_n$.
Then there is a bundle endomorphism $\mathcal{R}_k$ of $k$-forms such that
$$\Delta_H \omega = \nabla^* \nabla \omega + \mathcal{R}_k(\omega)$$
for every $k$-form $\omega$.
For $k = 1$, the term is the [[Ricci curvature|4GTNM0WHDH]]: $\mathcal{R}_1(\omega)(X) = \operatorname{Ric}(\omega^\sharp, X)$, where $\omega^\sharp$ is the vector field dual to $\omega$.
At each point, $\mathcal{R}_k$ is given by a linear expression in the Riemann curvature tensor.

## Remarks

The idea of the proof: express $d$ and $\delta$ through $\nabla$, namely $d\omega = \sum_i e^i \wedge \nabla_{e_i} \omega$ and $\delta\omega = -\sum_i \iota_{e_i} \nabla_{e_i} \omega$.
Expanding $d\delta + \delta d$ gives the second-order part $\nabla^* \nabla$ plus commutators $[\nabla_{e_i}, \nabla_{e_j}]$, which are curvature terms.

Example: for $\omega = du$ the identity, paired with $du$, gives [[Bochner's formula|DF7KYMAGTC]] for the function $u$.

Bochner's vanishing theorem follows: let $M$ be compact.
If $\omega$ is a harmonic 1-form, integrating $\ip{\Delta_H \omega}{\omega} = 0$ gives $\int_M \abs{\nabla \omega}^2 + \operatorname{Ric}(\omega^\sharp, \omega^\sharp) = 0$.
So if $\operatorname{Ric} \ge 0$, every harmonic 1-form is parallel and the first Betti number is at most $n$; if $\operatorname{Ric} > 0$, the first Betti number is $0$.

## Explanations

### L1 human

There are two natural Laplacians on differential forms: one built from the exterior derivative, and one built from the covariant derivative.
The identity says they differ only by a curvature term with no derivatives.
For 1-forms that term is the Ricci curvature.

### L2 human

Weitzenböck identities are the engine of the Bochner technique.
Combined with the Hodge theorem, which identifies cohomology with harmonic forms, a sign of the curvature term forces harmonic forms to vanish or to be parallel.
The same pattern holds for other Dirac-type operators; for the spin Dirac operator the curvature term is a quarter of the scalar curvature (the Lichnerowicz formula).
