---
tag: WDQTBSK6ES
kind: definition
name: Matrix function
msc: [15A16, 47A60]
defines: W7MPTRPXYD
uses: [0MZB06ST2B, 0JXZKX526R, 9V7YQA85PC]
sources:
  - url: https://en.wikipedia.org/wiki/Analytic_function_of_a_matrix
---

## Definition

Let $f(z) = \sum_{k=0}^{\infty} c_k z^k$ be a complex [[power series|0MZB06ST2B]] with radius of convergence $R > 0$, where $R = \infty$ is allowed.
Let $n \ge 1$ and let $A$ be an $n \times n$ complex [[matrix|0JXZKX526R]] whose [[spectral radius|9V7YQA85PC]] satisfies $\rho(A) < R$.
Then the series $\sum_{k=0}^{\infty} c_k A^k$ converges, with $A^0 = I$, and its sum is the matrix $f(A)$.

## Remarks

If $A = P D P^{-1}$ with $D = \operatorname{diag}(\lambda_1, \ldots, \lambda_n)$, then $f(A) = P \operatorname{diag}(f(\lambda_1), \ldots, f(\lambda_n)) P^{-1}$.
The matrix $f(A)$ is always a polynomial in $A$, so it commutes with $A$.
Example: $f(z) = 1/(1 - z) = \sum_k z^k$ has $R = 1$, and $N = \begin{pmatrix} 0 & 1 \\ 0 & 0 \end{pmatrix}$ has $\rho(N) = 0$.
Since $N^2 = 0$, $f(N) = I + N$, and indeed $(I - N)(I + N) = I - N^2 = I$.
Non-example: for the same $f$ and $A = 2I$, $\rho(A) = 2 > 1$, and the series $\sum_k 2^k I$ diverges.
For $f$ holomorphic near the spectrum of $A$, the Cauchy integral or the Jordan form gives a more general definition; see the holomorphic functional calculus.
