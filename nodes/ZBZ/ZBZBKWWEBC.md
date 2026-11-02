---
tag: ZBZBKWWEBC
kind: definition
name: Normal form
msc: [34C20, 37G05]
defines: TJ04Y2Z5Q3
uses: [07BNRFQ0PJ, 0G4X36AE0X, 09ZWYRQ41J, 2C3PAQ7H50, 0BQAA2BK3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_form_(dynamical_systems)
---

## Definition

Let $A$ be a real $n \times n$ matrix and consider the [[autonomous system|07BNRFQ0PJ]]
$$x' = A x + f_2(x) + f_3(x) + \cdots + f_r(x) + O(\abs{x}^{r+1})$$
near the [[equilibrium point|0G4X36AE0X]] $0$ of $\R^n$.
Here each $f_m$ is a vector field whose components are [[homogeneous polynomials|2C3PAQ7H50]] of degree $m$.
Let $H_m$ be the vector space of such vector fields of degree $m$.
The homological operator $L_A \colon H_m \to H_m$ is $L_A h(x) = Dh(x) \, A x - A h(x)$.
For each $m \ge 2$ choose a complement $G_m$ of the image $L_A(H_m)$ in $H_m$.
The system is in normal form up to order $r$ with respect to these complements if $f_m \in G_m$ for $m = 2, \ldots, r$.

## Remarks

The normal form theorem states that a near-identity polynomial change of coordinates $x = y + h_2(y) + \cdots + h_r(y)$, with $h_m \in H_m$, brings any such system into normal form up to order $r$.
At degree $m$ the change $x = y + h_m(y)$ replaces $f_m$ by $f_m - L_A h_m$ and changes only terms of degree at least $m$, so $f_m$ can be reduced to its component in $G_m$.
If $A = \mathrm{diag}(\lambda_1, \ldots, \lambda_n)$, then $L_A$ maps the monomial vector field $x_1^{k_1} \cdots x_n^{k_n} e_j$ to $(k_1 \lambda_1 + \cdots + k_n \lambda_n - \lambda_j)$ times itself.
So one can take $G_m$ spanned by the resonant monomials, those with $k_1 \lambda_1 + \cdots + k_n \lambda_n = \lambda_j$, and the normal form keeps only resonant terms.
Example: for $\lambda = (1, 2)$, the only resonant monomial of degree $2$ is $x_1^2 e_2$, since $2 \cdot 1 = 2$; the normal form up to order $2$ is $y_1' = y_1$, $y_2' = 2 y_2 + c\, y_1^2$ for a constant $c$.
Non-example: the system $x_1' = x_1 + x_1 x_2$, $x_2' = 2 x_2$ is not in normal form for $\lambda = (1, 2)$, since $x_1 x_2 e_1$ has $1 + 2 \ne 1$ and is not resonant.

## Explanations

### L1 human

A normal form is the result of simplifying the nonlinear terms of an equation by a change of variables, one degree at a time.
The terms that survive are the resonant ones, which reflect relations between the [[eigenvalues|0BQAA2BK3Q]] of the linear part.
