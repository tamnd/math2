---
tag: RYQJH4RYB4
kind: statement
role: theorem
name: Calderón–Zygmund estimates
msc: [35J05, 42B20, 35B45]
uses: [0E0B6RA8K0, SASP14MA1Z, HTMCEARGDD]
about: [0E0B6RA8K0, HTMCEARGDD]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_integral
---

## Statement

Let $n \ge 1$ be an integer and let $1 < p < \infty$.
Let $\Delta$ be the [[Laplacian|0E0B6RA8K0]] and let $\norm{\cdot}_{L^p}$ be the norm of the [[Lebesgue space|SASP14MA1Z]] $L^p(\R^n)$.
There is $C = C(n, p)$ such that each $u \in C_c^\infty(\R^n)$ satisfies
$$\norm{\partial_i \partial_j u}_{L^p(\R^n)} \le C \norm{\Delta u}_{L^p(\R^n)} \quad \text{for all } i, j \in \set{1, \ldots, n}.$$

## Remarks

On the Fourier side, $\widehat{\partial_i \partial_j u}(\xi) = \frac{\xi_i \xi_j}{\abs{\xi}^2} \widehat{\Delta u}(\xi)$.
So $\partial_i \partial_j u = R_i R_j \Delta u$, up to sign, where $R_i$ is the Riesz transform with multiplier $-i \xi_i / \abs{\xi}$.
Each $R_i R_j$ is a [[singular integral operator|HTMCEARGDD]], and Calderón–Zygmund theory shows that such operators are bounded on $L^p$ for $1 < p < \infty$.
The proof of that bound uses the [[Calderón–Zygmund lemma|K1YKXVPVDG]] to get a weak type $(1,1)$ bound, then interpolation with the $L^2$ bound from Plancherel, then duality.
The estimate fails for $p = 1$ and for $p = \infty$: a function with bounded Laplacian need not have bounded second derivatives.
Combined with cut-off functions, the estimate gives the local $W^{2,p}$ estimates for solutions of $\Delta u = f$, and by freezing coefficients for elliptic equations with continuous leading coefficients.

## Explanations

### L1 human

If you know how large the Laplacian of a function is, on average in the $L^p$ sense, then you also know how large all its second derivatives are.
The Laplacian is only one combination of second derivatives, so this is a surprising gain.
It holds for every exponent strictly between $1$ and $\infty$, but not at the two ends.

### L2 human

These estimates are the $L^p$ counterpart of the Schauder estimates in Hölder spaces.
They are the main tool to show that a weak solution of an elliptic equation with an $L^p$ right-hand side has second derivatives in $L^p$.
They are also a model case of the general theory of singular integrals, which treats operators like the Riesz and Hilbert transforms.
