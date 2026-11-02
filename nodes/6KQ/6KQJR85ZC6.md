---
tag: 6KQJR85ZC6
kind: statement
role: theorem
name: Successive over-relaxation
msc: [65F10]
uses: [0GT4WWGWH2, 0KX66CZMBB, 9V7YQA85PC, 2RPE77ACER, G0EDYEDG4S, B8FVHNXAN1]
about: [2RPE77ACER]
sources:
  - url: https://en.wikipedia.org/wiki/Successive_over-relaxation
same_as:
  wikidata: Q1561270
  wikipedia: Successive over-relaxation
---

## Statement

Let $A$ be a real $n \times n$ matrix with nonzero diagonal entries, and let $b \in \R^n$.
Write $A = D + L + U$, with $D$ diagonal, $L$ strictly lower triangular and $U$ strictly upper triangular.
Let $\omega \in \R$ with $\omega \ne 0$.
The method of *successive over-relaxation* (SOR) with parameter $\omega$ starts from any $x^{(0)} \in \R^n$ and sets
$$x^{(k+1)} = (D + \omega L)^{-1} \left( \omega b - \left( \omega U + (\omega - 1) D \right) x^{(k)} \right).$$
Let $G_\omega = (D + \omega L)^{-1} \left( (1 - \omega) D - \omega U \right)$ be its iteration matrix.

1. (Kahan) The [[spectral radius|9V7YQA85PC]] satisfies $\rho(G_\omega) \ge \abs{\omega - 1}$. So if SOR converges for every $b$ and every $x^{(0)}$, then $0 < \omega < 2$.
2. (Ostrowski–Reich) If $A$ is symmetric and [[positive definite|0KX66CZMBB]] and $0 < \omega < 2$, then $\rho(G_\omega) < 1$. Then for every $b$ and every $x^{(0)}$ the iterates converge to $A^{-1} b$.

## Remarks

Componentwise, SOR computes the [[Gauss–Seidel|G0EDYEDG4S]] value $\tilde{x}_i$ for the $i$-th unknown and takes $x^{(k+1)}_i = (1 - \omega) x^{(k)}_i + \omega \tilde{x}_i$.
For $\omega = 1$ it is the Gauss–Seidel method.
Kahan's bound comes from the determinant: $\det G_\omega = \det(D)^{-1} \det((1 - \omega) D) = (1 - \omega)^n$, and this is the product of the eigenvalues.
The Ostrowski–Reich theorem follows because the energy norm of the error decreases strictly at each step when $A$ is positive definite and $0 < \omega < 2$.
Assume moreover that $A$ is consistently ordered, for example tridiagonal.
Assume also that the [[Jacobi|B8FVHNXAN1]] iteration matrix has real eigenvalues and spectral radius $\mu < 1$.
Then Young's theory gives the best parameter $\omega_{\mathrm{opt}} = 2 / (1 + \sqrt{1 - \mu^2})$, with $\rho(G_{\omega_{\mathrm{opt}}}) = \omega_{\mathrm{opt}} - 1$.
For the model Poisson problem with mesh width $h$ this improves the convergence factor from $1 - O(h^2)$ to $1 - O(h)$.

## Explanations

### L1 human

SOR takes the step that Gauss–Seidel suggests and stretches it by a factor $\omega$.
When the iterates creep slowly towards the solution, going a bit further than suggested, with $\omega$ between $1$ and $2$, saves many steps.
The parameter must stay between $0$ and $2$; outside that range it cannot converge for every starting guess.

### L2 human

SOR was for decades the main [[iterative method|2RPE77ACER]] for large elliptic problems, because a good $\omega$ makes it far faster than Jacobi or Gauss–Seidel.
The best $\omega$ depends on the spectrum of the Jacobi matrix, which is known exactly for model problems and estimated otherwise.
Symmetric SOR runs a forward and a backward sweep and gives a symmetric preconditioner for the conjugate gradient method.
