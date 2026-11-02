---
tag: QPMM2ZPWBW
kind: problem
name: Hilbert's nineteenth problem
msc: [35B65, 49N60, 35J60]
uses: [PQ25NHV0KS, PS0VV149ET, 081WKEDK6C]
about: [PQ25NHV0KS]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert%27s_nineteenth_problem
same_as:
  wikidata: Q5761157
  wikipedia: Hilbert's nineteenth problem
history:
  posed_by: "David Hilbert"
  first_stated: "1900"
---

## Problem

Let $\Omega \subseteq \R^n$ be an open set and let $L \colon \R^n \to \R$, written $L(p)$, be a real [[analytic function|081WKEDK6C]].
Assume $L$ is uniformly convex: for constants $0 < \lambda \le \Lambda$, the eigenvalues of the Hessian matrix $D^2 L(p)$ lie in $[\lambda, \Lambda]$ for all $p$.
Consider the functional $J(u) = \int_\Omega L(\nabla u) \, dx$ of the [[calculus of variations|PQ25NHV0KS]].
Call $u \in W^{1,2}_{\mathrm{loc}}(\Omega)$ a local minimiser of $J$ if $\int_{S} L(\nabla u) \, dx \le \int_{S} L(\nabla u + \nabla \varphi) \, dx$ for every $\varphi \in W^{1,2}(\Omega)$ that vanishes outside a compact set $S \subseteq \Omega$.
Decide whether every local minimiser of $J$ is real analytic in $\Omega$.
In Hilbert's words, the question is whether the solutions of regular problems of the calculus of variations are always analytic.

## Remarks

Hilbert asked the question in a more general form, for analytic Lagrangians $L(x, u, \nabla u)$ that satisfy the Legendre condition; the form above is the model case, with the same answer.
The answer is yes for scalar functions $u$.
Bernstein proved in 1904 that $C^3$ solutions of analytic nonlinear elliptic equations in two variables are analytic.
The general case was settled by De Giorgi in 1957 and, independently, by Nash in 1958.
They proved that weak solutions of linear elliptic equations in divergence form with bounded measurable coefficients are Hölder continuous.
The derivatives of a minimiser solve such an equation, so $u \in C^{1,\alpha}$.
Then Schauder theory gives $u \in C^\infty$, and the analyticity of smooth solutions of analytic elliptic equations gives that $u$ is analytic.
For vector-valued $u$ the answer is no: De Giorgi gave a counterexample in 1968 of a non-smooth minimiser for an elliptic system.

## Explanations

### L1 human

Hilbert noticed that the minimisers of natural energies, such as the area of a soap film, tend to be not just smooth but analytic, given by convergent power series.
He asked whether this is always so for well-behaved energies.
The answer, found more than fifty years later, is yes for a single unknown function and no for systems of unknown functions.
The work on this problem created much of modern regularity theory for elliptic equations.
