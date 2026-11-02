---
tag: DF7KYMAGTC
kind: statement
role: theorem
name: Bochner's formula
msc: [53C21, 58J05]
uses: [7CBT4SM83Y, 4GTNM0WHDH, F4NWZNTRMD, CAZYGE1T4E]
about: [4GTNM0WHDH, F4NWZNTRMD]
sources:
  - url: https://en.wikipedia.org/wiki/Bochner%27s_formula
same_as:
  wikidata: Q4936239
  wikipedia: Bochner's formula
---

## Statement

Let $(M, g)$ be a [[Riemannian manifold|7CBT4SM83Y]] and let $u \colon M \to \R$ be a smooth function.
Write $\nabla u$ for the gradient of $u$ and $\nabla^2 u$ for its Hessian with respect to the [[Levi-Civita connection|CAZYGE1T4E]].
Write $\Delta u = \tr \nabla^2 u$ for the [[Laplace–Beltrami operator|F4NWZNTRMD]] and $\operatorname{Ric}$ for the [[Ricci curvature|4GTNM0WHDH]].
Then
$$\frac{1}{2} \Delta \abs{\nabla u}^2 = \abs{\nabla^2 u}^2 + \ip{\nabla u}{\nabla (\Delta u)} + \operatorname{Ric}(\nabla u, \nabla u).$$

## Remarks

The idea of the proof: compute at a point in normal coordinates.
The left side is $\sum_{i,j} (\nabla_i \nabla_j u)^2 + \sum_{i,j} \nabla_j u \, \nabla_i \nabla_i \nabla_j u$.
Commuting the covariant derivatives in the last term gives $\nabla_j \nabla_i \nabla_i u$ plus a curvature term, and that curvature term is exactly $\operatorname{Ric}(\nabla u, \nabla u)$.

Example: in $\R^n$ the Ricci term is $0$.
For $u(x) = \abs{x}^2 / 2$ one has $\nabla u = x$, $\nabla^2 u = \id$ and $\Delta u = n$, so the left side is $\frac{1}{2} \Delta \abs{x}^2 = n$ and the right side is $n + 0 + 0$.

A standard application: let $M$ be compact of dimension $n$ with $\operatorname{Ric} \ge (n-1) k \, g$ for some $k > 0$.
Integrating the formula for an eigenfunction shows that every nonzero eigenvalue $\lambda$ of $-\Delta$ satisfies $\lambda \ge n k$.
This is Lichnerowicz's eigenvalue estimate.

## Explanations

### L1 human

The formula compares how a function bends with how the space bends.
It says that the Laplacian of the squared size of the gradient splits into three parts.
They are the size of the second derivatives, a term with the Laplacian of the function, and a Ricci curvature term.
When the Ricci curvature is nonnegative, the squared length of the gradient of a harmonic function is subharmonic, and this gives strong control on the function.

### L2 human

Bochner's formula is the main identity behind the "Bochner technique": a curvature sign forces certain objects to be parallel or to vanish.
It is used in the Cheng–Yau gradient estimate, in the Laplacian comparison theorem, in the proof of the Cheeger–Gromoll splitting theorem and in eigenvalue estimates.
The same computation for 1-forms is the case of the Weitzenböck identity that leads to Bochner's vanishing theorem for the first Betti number.
