---
tag: 3QTT95DMFH
kind: statement
role: theorem
name: Wigner semicircle law
msc: [60B20, 15B52, 60F05]
uses: [0EKZCX4K3P, 0BQAA2BK3Q, 00MRN0FARV, 0SRYJGXKR4]
about: [0BQAA2BK3Q]
sources:
  - url: https://en.wikipedia.org/wiki/Wigner_semicircle_distribution
---

## Statement

Let $(Y_{ij})_{1 \le i < j}$ be [[independent and identically distributed|00MRN0FARV]] real random variables with mean $0$ and variance $1$.
Let $(Y_{ii})_{i \ge 1}$ be independent and identically distributed real random variables with mean $0$ and finite variance, independent of the $Y_{ij}$ with $i < j$.
For $n \ge 1$, let $W_n$ be the real symmetric $n \times n$ matrix with entries $W_n(i, j) = W_n(j, i) = Y_{ij} / \sqrt n$ for $i \le j$.
Let $\lambda_1, \ldots, \lambda_n$ be the [[eigenvalues|0BQAA2BK3Q]] of $W_n$, and let
$$\mu_n = \frac1n \sum_{k=1}^n \delta_{\lambda_k}$$
be its empirical spectral measure.
Then, almost surely, $\mu_n$ [[converges weakly|0SRYJGXKR4]] as $n \to \infty$ to the semicircle distribution, the probability measure on $\R$ with density
$$\rho(x) = \frac{1}{2\pi} \sqrt{4 - x^2} \quad \text{for } \abs{x} \le 2, \qquad \rho(x) = 0 \quad \text{for } \abs{x} > 2.$$

## Remarks

The moment method is the classical proof.
One shows that $\mathbb{E} \int x^k \, d\mu_n = \frac1n \mathbb{E} \tr W_n^k$ tends to the $k$-th moment of the semicircle law, which is $0$ for odd $k$ and the Catalan number $\frac{1}{m+1}\binom{2m}{m}$ for $k = 2m$.
Expand the trace as a sum over closed paths.
In the limit only paths that trace a tree and cross each edge exactly twice contribute, and Catalan numbers count them.
A variance bound and a truncation of the entries then give almost sure convergence.
The same result holds for complex [[Hermitian|0EKZCX4K3P]] matrices with independent and identically distributed entries above the diagonal, of mean $0$ and $\mathbb{E}\abs{Y_{ij}}^2 = 1$.

## Explanations

### L1 human

Fill a large symmetric matrix with independent random numbers and scale it by $1/\sqrt n$.
Its eigenvalues then spread over the interval $[-2, 2]$, and their histogram takes the shape of a half-disc.
The shape does not depend on the law of the entries, only on their mean and variance.

### L2 human

It is the law of large numbers of random matrix theory, the analogue for spectra of the law of large numbers for averages.
Wigner introduced such matrices as models for the energy levels of heavy atomic nuclei.
Finer questions, such as the fluctuations of the largest eigenvalue, lead to the [[Tracy–Widom distribution|89ZY5YRETE]].
For sample covariance matrices the analogue is the [[Marchenko–Pastur law|DCK63WTY5E]].
