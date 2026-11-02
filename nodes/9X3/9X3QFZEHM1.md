---
tag: 9X3QFZEHM1
kind: statement
role: theorem
name: Bernstein's theorem on analytic functions
msc: [41A25, 41A27, "30E10"]
uses: [YDN0T4MEX0, 0NAHXR1FRH, 0VKCCEXBJ1, M6EAR1JHPP]
about: [TDKKST5AWA]
sources:
  - url: https://en.wikipedia.org/wiki/Bernstein%27s_theorem_(approximation_theory)
---

## Statement

Let $f \colon [-1, 1] \to \R$ be continuous and let $E_n(f)$ be the uniform distance on $[-1, 1]$ from $f$ to the polynomials of degree at most $n$.
For $\rho > 1$, let $\mathcal{E}_\rho$ be the open region bounded by the [[ellipse|0VKCCEXBJ1]] with foci $\pm 1$ whose semi-axes have sum $\rho$.
Then $f$ extends to a [[holomorphic function|0NAHXR1FRH]] on $\mathcal{E}_\rho$ if and only if
$$\limsup_{n \to \infty} E_n(f)^{1/n} \le \frac{1}{\rho}.$$

## Remarks

The region $\mathcal{E}_\rho$ is the image of the annulus $1 < \abs{z} < \rho$ under the map $z \mapsto (z + z^{-1})/2$, together with $[-1, 1]$.
Proof idea for the direct half: for $1 < s < \rho$, the coefficients of the Chebyshev series of $f$ are $O(s^{-n})$, by a contour integral over the image of $\abs{z} = s$.
Truncating the series gives $E_n(f) = O(s^{-n})$.
For the converse, write $f = p_0 + \sum (p_{n+1} - p_n)$ with best approximations $p_n$ and bound each difference on $\mathcal{E}_s$ for $s < \rho$ by its size on $[-1, 1]$.

Example: for $a > 1$ and $f(x) = 1/(x - a)$, the pole $a$ lies on the boundary of $\mathcal{E}_\rho$ with $\rho = a + \sqrt{a^2 - 1}$.
So $E_n(f)$ decays like $(a + \sqrt{a^2 - 1})^{-n}$, up to factors that grow slower than any exponential.
For the Runge function $1/(1 + 25x^2)$, the poles $\pm i/5$ give $\rho = (1 + \sqrt{26})/5 \approx 1.22$.

## Explanations

### L1 human

For an analytic function on $[-1, 1]$, the error of the best polynomial approximation shrinks geometrically with the degree.
The rate is set by how far the function extends into the complex plane, measured by the largest ellipse with foci $\pm 1$ on which it stays analytic.

### L2 human

This explains why Chebyshev methods converge so fast for analytic functions, and why nearby complex singularities slow them down even when $f$ looks harmless on the real line.
It is an inverse and a direct theorem at once: geometric decay of $E_n(f)$ and analyticity in an ellipse are equivalent.
The ellipses $\partial \mathcal{E}_\rho$ are the level curves of the Green function of the complement of $[-1, 1]$, which leads to the general theory of Walsh for other sets.
