---
tag: SK6M9GBKN4
kind: definition
name: Tracy–Widom distribution
msc: [60B20, 15B52, "33E17"]
defines: 89ZY5YRETE
uses: [0DVDCMA2DK, 0BQAA2BK3Q, 0SRYJGXKR4]
sources:
  - url: https://en.wikipedia.org/wiki/Tracy–Widom_distribution
---

## Definition

Let $\mathrm{Ai}$ be the Airy function.
Let $q \colon \R \to \R$ be the Hastings–McLeod solution of the Painlevé II equation
$$q''(s) = s\, q(s) + 2 q(s)^3,$$
that is, the unique solution with $q(s) \sim \mathrm{Ai}(s)$ as $s \to +\infty$.
The *Tracy–Widom distribution* (for $\beta = 2$) is the [[probability distribution|0DVDCMA2DK]] on $\R$ with distribution function
$$F_2(s) = \exp\Big( -\int_s^\infty (x - s)\, q(x)^2 \, dx \Big), \qquad s \in \R.$$
The laws for $\beta = 1$ and $\beta = 4$ are given by
$$F_1(s) = \exp\Big( -\frac12 \int_s^\infty q(x)\, dx \Big) F_2(s)^{1/2}, \qquad F_4\Big(\frac{s}{\sqrt 2}\Big) = \cosh\Big( \frac12 \int_s^\infty q(x)\, dx \Big) F_2(s)^{1/2}.$$

## Remarks

Example: let $H_n$ be an $n \times n$ matrix of the Gaussian unitary ensemble, Hermitian with independent standard real normal diagonal entries and independent complex normal entries above the diagonal with $\mathbb{E}\abs{H_{ij}}^2 = 1$.
If $\lambda_{\max}$ is its largest [[eigenvalue|0BQAA2BK3Q]], then $n^{1/6} (\lambda_{\max} - 2\sqrt n)$ [[converges in distribution|0SRYJGXKR4]] to $F_2$.
Equivalently, $F_2(s) = \det(I - K_{\mathrm{Ai}})$ on $L^2(s, \infty)$, the Fredholm determinant of the Airy kernel $K_{\mathrm{Ai}}(x, y) = \frac{\mathrm{Ai}(x) \mathrm{Ai}'(y) - \mathrm{Ai}'(x) \mathrm{Ai}(y)}{x - y}$.
Non-example: the standard normal law is not a Tracy–Widom law; $F_2$ has mean about $-1.77$ and is not symmetric about its mean.
Baik, Deift and Johansson showed that the length $\ell_n$ of the longest increasing subsequence of a uniform random permutation of $n$ letters satisfies $(\ell_n - 2\sqrt n)/n^{1/6} \to F_2$ in distribution.
