---
tag: 70QYCEWHVY
kind: statement
role: theorem
name: Inverse iteration
msc: [65F15]
uses: [0BQAA2BK3Q, 0N6960W0BV, H4MQD841BR, YWZQC5E54B]
about: [HCJ2ETX89Z]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_iteration
same_as:
  wikidata: Q1671724
  wikipedia: Inverse iteration
---

## Statement

Let $A \in \C^{n \times n}$ be diagonalizable with [[eigenvalues|0BQAA2BK3Q]] $\lambda_1, \dots, \lambda_n$ and a basis of [[eigenvectors|0N6960W0BV]] $v_1, \dots, v_n$, $A v_i = \lambda_i v_i$.
Let $\mu \in \C$ be a shift that is not an eigenvalue, and suppose that there is an index $j$ with
$$\abs{\lambda_j - \mu} < \abs{\lambda_i - \mu} \quad \text{for all } i \text{ with } \lambda_i \ne \lambda_j.$$
Let $x_0 = \sum_i c_i v_i$ with $\sum_{i : \lambda_i = \lambda_j} c_i v_i \ne 0$, and define *inverse iteration* by
$$x_{k+1} = \frac{(A - \mu I)^{-1} x_k}{\norm{(A - \mu I)^{-1} x_k}}.$$
Then the angle between $x_k$ and the eigenspace of $\lambda_j$ tends to $0$, and its sine is $O(\rho^k)$ with
$$\rho = \frac{\abs{\lambda_j - \mu}}{\min_{\lambda_i \ne \lambda_j} \abs{\lambda_i - \mu}} < 1.$$

## Remarks

The matrix $(A - \mu I)^{-1}$ has the same eigenvectors as $A$, with eigenvalues $1/(\lambda_i - \mu)$.
The hypothesis makes $1/(\lambda_j - \mu)$ the eigenvalue of largest modulus, so inverse iteration is [[power iteration|H4MQD841BR]] applied to $(A - \mu I)^{-1}$.
Expanding $(A - \mu I)^{-k} x_0 = \sum_i c_i (\lambda_i - \mu)^{-k} v_i$ and dividing by $(\lambda_j - \mu)^{-k}$ shows that the other components shrink like $\rho^k$.

Example: for $A = \mathrm{diag}(1, 2, 4)$ and $\mu = 2.1$, the ratio is $\rho = 0.1/1.1 \approx 0.09$, so each step gains about one decimal digit toward $e_2$.
If two distinct eigenvalues are equally close to $\mu$, then $\rho = 1$ and the iteration need not converge to an eigenvector.
In practice one factors $A - \mu I = LU$ once and solves a linear system at each step instead of forming the inverse.
The near-singularity of $A - \mu I$ for a good shift does not harm the method: the error in the solve is concentrated in the direction of the wanted eigenvector.

## Explanations

### L1 human

Power iteration finds the eigenvector with the largest eigenvalue.
Inverse iteration finds the eigenvector whose eigenvalue is closest to a chosen number $\mu$, by running power iteration on the inverse of $A - \mu I$.
The closer $\mu$ is to the wanted eigenvalue, the faster it converges.

### L2 human

Inverse iteration is the standard way to compute an eigenvector once a good approximation of its eigenvalue is known.
Such an approximation may come from the [[QR algorithm|B6F8YWHYZ5]] or from bisection on a tridiagonal matrix.
Updating the shift at each step with the Rayleigh quotient gives [[Rayleigh quotient iteration|Y119KHA4VG]], which converges much faster.
The [[rate of convergence|YWZQC5E54B]] is linear with ratio $\rho$, which is why a shift near the eigenvalue matters.
