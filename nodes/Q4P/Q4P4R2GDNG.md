---
tag: Q4P4R2GDNG
kind: problem
name: dbar-Neumann problem
msc: [32W05, 35N15]
uses: [M1VKCW3RFW, DC81TCR98Y, 86B7HF79PQ, AHYZMSBBNH]
about: [M1VKCW3RFW]
sources:
  - url: https://en.wikipedia.org/wiki/Dolbeault_cohomology
history:
  posed_by: "Donald C. Spencer"
---

## Problem

Let $\Omega \subseteq \C^n$ be a bounded open set with smooth boundary, and let $1 \le q \le n$.
Let $L^2_{(0,q)}(\Omega)$ be the Hilbert space of [[(0,q)-forms|DC81TCR98Y]] on $\Omega$ with square integrable coefficients.
Regard $\bar\partial$ as a closed, densely defined operator from $L^2_{(0,q)}(\Omega)$ to $L^2_{(0,q+1)}(\Omega)$.
It acts in the sense of distributions on the forms for which the result is square integrable.
Let $\bar\partial^*$ be its [[Hilbert space adjoint|86B7HF79PQ]], and let
$$\square = \bar\partial \bar\partial^* + \bar\partial^* \bar\partial$$
on the set of $u \in L^2_{(0,q)}(\Omega)$ with $u \in \operatorname{Dom}(\bar\partial) \cap \operatorname{Dom}(\bar\partial^*)$, $\bar\partial u \in \operatorname{Dom}(\bar\partial^*)$ and $\bar\partial^* u \in \operatorname{Dom}(\bar\partial)$.
Given $\alpha \in L^2_{(0,q)}(\Omega)$, find $u$ in this domain with $\square u = \alpha$, and study the regularity of $u$ up to the boundary.

## Remarks

For forms smooth up to the boundary, membership in the domain of $\square$ means two boundary conditions, the $\bar\partial$-Neumann conditions.
If $\rho$ is a defining function of $\Omega$, they say that the contraction of $u$ with $\bar\partial \rho$ and the contraction of $\bar\partial u$ with $\bar\partial \rho$ both vanish on $\partial\Omega$.
These conditions are not elliptic, so the standard theory of elliptic boundary value problems does not apply.
Spencer proposed the problem in the 1950s as a way to extend Hodge theory to manifolds with boundary.
Kohn solved it for strongly pseudoconvex domains in 1963: $\square$ has a bounded inverse $N$, the Neumann operator.
Moreover $N$ maps forms that are smooth up to the boundary to forms that are smooth up to the boundary.
For a bounded [[pseudoconvex|AHYZMSBBNH]] domain, Hörmander's $L^2$ estimates show that $\square$ is invertible on $L^2_{(0,q)}(\Omega)$ for $q \ge 1$.
When $\bar\partial \alpha = 0$, the form $\bar\partial^* N \alpha$ solves $\bar\partial v = \alpha$ and is the solution of least $L^2$ norm.
Regularity up to the boundary may fail for smooth bounded pseudoconvex domains: Christ showed that $N$ does not preserve $C^\infty(\overline{\Omega})$ on worm domains.

## Explanations

### L1 human

The problem asks to invert a Laplace-type operator built from $\bar\partial$, with boundary conditions that come from the adjoint of $\bar\partial$ in a Hilbert space.
Once it is inverted, one gets a canonical solution of the equation $\bar\partial v = \alpha$ with good estimates.
The difficulty is that the boundary conditions are weaker than in classical problems, so the behaviour at the boundary depends on the shape of the domain.
