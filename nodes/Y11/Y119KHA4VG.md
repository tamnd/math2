---
tag: Y119KHA4VG
kind: statement
role: theorem
name: Rayleigh quotient iteration
msc: [65F15]
uses: [0VR671PHE5, 06WHP8SE98, 0BQAA2BK3Q, 0N6960W0BV, 70QYCEWHVY, YWZQC5E54B]
about: [HCJ2ETX89Z, 06WHP8SE98]
sources:
  - url: https://en.wikipedia.org/wiki/Rayleigh_quotient_iteration
same_as:
  wikidata: Q7298489
  wikipedia: Rayleigh quotient iteration
---

## Statement

Let $A \in \R^{n \times n}$ be [[symmetric|0VR671PHE5]], and let $v$ be a unit [[eigenvector|0N6960W0BV]] of $A$ for a simple [[eigenvalue|0BQAA2BK3Q]] $\lambda$.
*Rayleigh quotient iteration* starts from a unit vector $x_0$.
For $k \ge 0$ it sets
$$\mu_k = x_k^T A x_k, \qquad x_{k+1} = \frac{(A - \mu_k I)^{-1} x_k}{\norm{(A - \mu_k I)^{-1} x_k}}.$$
It stops if $A - \mu_k I$ is singular, in which case $\mu_k$ is an eigenvalue.
Let $\theta_k \in [0, \pi/2]$ be the angle between $x_k$ and $v$.
Then there are constants $\delta > 0$ and $C > 0$ such that $\theta_k \le \delta$ implies $\theta_{k+1} \le C \theta_k^3$.
In particular, if $x_0$ is close enough to $\pm v$, then $x_k \to \pm v$ in direction cubically, and $\mu_k \to \lambda$.

## Remarks

Write $x_k = \cos\theta_k \, v + \sin\theta_k \, w$ with $w$ a unit vector orthogonal to $v$.
For symmetric $A$ the [[Rayleigh quotient|06WHP8SE98]] is stationary at eigenvectors, so $\abs{\mu_k - \lambda} \le \norm{A - \lambda I} \sin^2\theta_k = O(\theta_k^2)$.
Let the gap be the distance from $\mu_k$ to the other eigenvalues.
One step of [[inverse iteration|70QYCEWHVY]] with shift $\mu_k$ multiplies the ratio of the $w$-component to the $v$-component by at most $\abs{\mu_k - \lambda}/\mathrm{gap}$.
So $\tan\theta_{k+1} \le O(\theta_k^2) \tan\theta_k$, which is cubic.

Example: for $A = \mathrm{diag}(1, 3)$ and $x_k = (\cos\theta, \sin\theta)$, one finds $\mu_k = 1 + 2\sin^2\theta$ and $\tan\theta_{k+1} = \tan^3\theta_k$ exactly.
Symmetry is needed for cubic convergence: for a general matrix with a simple eigenvalue the Rayleigh quotient error is only $O(\theta_k)$, and the local convergence is quadratic.
Which eigenvector the iteration finds depends on $x_0$ in a complicated way, so the method is used to refine a good approximation rather than to locate eigenvalues from scratch.

## Explanations

### L1 human

Inverse iteration needs a guess $\mu$ of the eigenvalue and converges faster the better the guess.
Rayleigh quotient iteration updates the guess at every step with the best estimate available from the current vector.
For symmetric matrices the number of correct digits roughly triples at each step once the vector is close.

### L2 human

Each step costs a fresh factorization of $A - \mu_k I$, unlike inverse iteration with a fixed shift, but very few steps are needed.
The cubic rate comes from two facts.
The Rayleigh quotient is a second-order accurate eigenvalue estimate for symmetric matrices, and inverse iteration converges at a rate proportional to the shift error.
The shifted [[QR algorithm|B6F8YWHYZ5]] with Rayleigh quotient shifts is closely related, and this explains its fast convergence on symmetric matrices.
