---
tag: AJ5RG9XQYZ
kind: statement
role: theorem
name: Milman–Pettis theorem
msc: [46B10, 46B20]
uses: [06GZ956657, BEAMC5011M, NN8RWPC8WG]
about: [BEAMC5011M, NN8RWPC8WG]
sources:
  - url: https://en.wikipedia.org/wiki/Milman%E2%80%93Pettis_theorem
same_as:
  wikidata: Q6860180
  wikipedia: Milman–Pettis theorem
---

## Statement

Let $X$ be a [[Banach space|06GZ956657]] over $\R$ or $\C$.
If $X$ is [[uniformly convex|BEAMC5011M]], then $X$ is [[reflexive|NN8RWPC8WG]].

## Remarks

Let $J \colon X \to X^{**}$ be the canonical embedding, and let $\xi \in X^{**}$ with $\norm{\xi} = 1$.
By the [[Goldstine theorem|K4S9G3AQBM]], $\xi$ is a weak* limit of a net $J(x_\alpha)$ with $\norm{x_\alpha} \le 1$.
Given $\varepsilon > 0$, let $\delta$ be as in the definition of uniform convexity, and choose $f \in X^*$ of norm $1$ with $\operatorname{Re} \xi(f) > 1 - \delta$.
For late indices $\alpha, \beta$ one has $\operatorname{Re} f(x_\alpha + x_\beta) > 2 - 2\delta$, so $\norm{(x_\alpha + x_\beta)/2} > 1 - \delta$, and uniform convexity gives $\norm{x_\alpha - x_\beta} < \varepsilon$.
This shows that $\xi$ is within any given $\varepsilon$ of the closed set $J(X)$, so $\xi \in J(X)$.

Example: $L^p$ spaces for $1 < p < \infty$ are uniformly convex by [[Clarkson's inequalities|1V11QM5C07]], so they are reflexive.
Completeness is needed.
The space of finitely supported sequences with the norm of $\ell^2$ is an inner product space, hence uniformly convex, but it is not complete and therefore not reflexive.
The converse fails: there are reflexive spaces with no equivalent uniformly convex norm.

## Explanations

### L1 human

Uniform convexity is a geometric condition on the shape of the unit ball: it is round in a uniform way.
Reflexivity is an abstract condition about the double dual.
The theorem says that the geometric condition is enough to give the abstract one.

### L2 human

The theorem is the usual quick route to the reflexivity of $L^p$ for $1 < p < \infty$, without computing the dual twice.
In a uniformly convex space, weak convergence plus convergence of norms implies norm convergence, and closed convex sets have unique nearest points.
These facts and reflexivity make such spaces convenient in variational problems.
Being reflexive is invariant under isomorphism, so every Banach space isomorphic to a uniformly convex one is reflexive.
