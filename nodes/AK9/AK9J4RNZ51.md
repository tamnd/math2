---
tag: AK9J4RNZ51
kind: statement
role: theorem
name: Bauer–Fike theorem
msc: [15A42, 65F15, 15A18]
uses: [07SQCNV233, 0BQAA2BK3Q, 06EKW1AKXF, AB3S6MHJ8X]
about: [0BQAA2BK3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Bauer%E2%80%93Fike_theorem
same_as:
  wikidata: Q2226602
  wikipedia: Bauer–Fike theorem
---

## Statement

Let $A$ be an $n \times n$ complex matrix that is [[diagonalisable|07SQCNV233]], with $A = V \Lambda V^{-1}$ for an invertible matrix $V$ and a diagonal matrix $\Lambda$.
Let $1 \le p \le \infty$, let $\norm{\cdot}_p$ be the [[operator norm|06EKW1AKXF]] induced by the $p$-norm on $\C^n$, and let $\kappa_p(V) = \norm{V}_p \norm{V^{-1}}_p$ be the [[condition number|AB3S6MHJ8X]] of $V$.
Let $E$ be an $n \times n$ complex matrix, and let $\mu$ be an [[eigenvalue|0BQAA2BK3Q]] of $A + E$.
Then there is an eigenvalue $\lambda$ of $A$ with
$$\abs{\lambda - \mu} \le \kappa_p(V) \norm{E}_p.$$

## Remarks

If $\mu$ is an eigenvalue of $A$, there is nothing to prove.
Otherwise $\Lambda - \mu I$ is invertible, and $A + E - \mu I = V(\Lambda - \mu I)\big(I + (\Lambda - \mu I)^{-1} V^{-1} E V\big) V^{-1}$ is singular.
So $1 \le \norm{(\Lambda - \mu I)^{-1} V^{-1} E V}_p \le \kappa_p(V) \norm{E}_p / \min_\lambda \abs{\lambda - \mu}$, which is the claim.

If $A$ is [[normal|0MR0BYF0K2]], $V$ can be chosen unitary, so $\kappa_2(V) = 1$ and each eigenvalue of $A + E$ is within $\norm{E}_2$ of an eigenvalue of $A$.

The diagonalisability hypothesis is needed for a bound linear in $\norm{E}$.
For $A = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ and $E = \begin{pmatrix} 0 & 0 \\ \varepsilon & 0 \end{pmatrix}$ with $\varepsilon > 0$, the eigenvalues of $A + E$ are $\pm \sqrt{\varepsilon}$, much larger than $\varepsilon$ when $\varepsilon$ is small.

## Explanations

### L1 human

If a diagonalisable matrix is changed by a small amount, its eigenvalues move by a small amount too.
The theorem gives the size of the move: the size of the change times a factor that measures how far the eigenvectors are from being orthogonal.

### L2 human

The theorem is a basic tool of [[eigenvalue perturbation|VR89YHC0TX]] theory and of the error analysis of eigenvalue algorithms.
It shows that the eigenvalue problem of a normal matrix is well conditioned.
When the eigenvectors are nearly parallel, $\kappa_p(V)$ is large and the eigenvalues can be very sensitive.
