---
tag: H3GWX277EF
kind: definition
name: Bogdanov–Takens bifurcation
msc: [34C23, 37G10]
defines: ACN92H5M6D
uses: [0G4X36AE0X, 047NDTEPCV, 0BQAA2BK3Q, 0V33BNKZ9S]
sources:
  - url: https://en.wikipedia.org/wiki/Bogdanov%E2%80%93Takens_bifurcation
---

## Definition

Let $f \colon \R^2 \times \R^2 \to \R^2$ be [[smooth|0V33BNKZ9S]], and consider the family of planar systems $x' = f(x, \mu)$ with a parameter $\mu \in \R^2$.
Let $x_0$ be an [[equilibrium point|0G4X36AE0X]] of the system with $\mu = \mu_0$, and let $A$ be the [[Jacobian matrix|047NDTEPCV]] of $x \mapsto f(x, \mu_0)$ at $x_0$.
The family has a *Bogdanov–Takens bifurcation* at $(x_0, \mu_0)$ if:

1. $0$ is an [[eigenvalue|0BQAA2BK3Q]] of $A$ of algebraic multiplicity $2$, that is, $\tr A = 0$ and $\det A = 0$;
2. $A \ne 0$, so that $A$ is similar to $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$;
3. two nondegeneracy conditions on the quadratic terms of $f(\cdot, \mu_0)$ at $x_0$ hold;
4. the map from $\mu$ to the unfolding parameters of the normal form is a local diffeomorphism at $\mu_0$.

## Remarks

Under these conditions, the family is locally topologically equivalent, near $(x_0, \mu_0)$, to the normal form
$$y_1' = y_2, \qquad y_2' = \beta_1 + \beta_2 y_1 + y_1^2 + s\, y_1 y_2, \qquad s = \pm 1,$$
with parameters $(\beta_1, \beta_2)$ near $0$.
In the $(\beta_1, \beta_2)$-plane, a saddle-node curve, a Hopf curve and a homoclinic bifurcation curve start at the origin.

Example: the normal form itself at $\beta = 0$ has the equilibrium $0$ with Jacobian $\begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$, so clauses 1 and 2 hold.

Non-example: if $A = 0$, then $0$ is a double eigenvalue but clause 2 fails; this degenerate case needs more parameters to unfold.
In higher dimensions, the same definition applies to the system reduced to a two-dimensional centre manifold.
