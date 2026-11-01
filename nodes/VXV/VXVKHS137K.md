---
tag: VXVKHS137K
kind: definition
name: Stable distribution
msc: ["60E07", 60G52]
defines: F3N6E1Y2AY
uses: [0PNRKMRC55, 00MRN0FARV, 0V5B6D6BQH, 05AQE0QR0D, 0GPG24Q3GR]
sources:
  - url: https://en.wikipedia.org/wiki/Stable_distribution
---

## Definition

Let $X$ be a real [[random variable|0PNRKMRC55]] that is not almost surely constant.
Let $X_1, X_2$ be independent random variables with the same law as $X$.
The law of $X$ is *stable* if for all $a, b > 0$ there are $c > 0$ and $d \in \R$ such that $a X_1 + b X_2$ has the same law as $c X + d$.
It is *strictly stable* if moreover $d = 0$ can be chosen for all $a, b > 0$.

## Remarks

For a stable law there is a unique $\alpha \in (0, 2]$, the index, such that $c^\alpha = a^\alpha + b^\alpha$ always.
The [[characteristic function|0V5B6D6BQH]] of a stable law has the form $\varphi(t) = \exp\left(i \mu t - \abs{\gamma t}^\alpha (1 - i \beta \sgn(t) \Phi(t))\right)$, with $\Phi(t) = \tan(\pi\alpha/2)$ for $\alpha \ne 1$ and $\Phi(t) = -\frac{2}{\pi} \log \abs{t}$ for $\alpha = 1$, where $\beta \in [-1, 1]$, $\gamma > 0$ and $\mu \in \R$.
Example: let $X$ be [[normal|05AQE0QR0D]] with mean $0$ and variance $1$.
Then $a X_1 + b X_2$ is normal with mean $0$ and variance $a^2 + b^2$.
So it has the law of $c X$ with $c = \sqrt{a^2 + b^2}$, and the index is $2$.
Example: for the standard [[Cauchy|0GPG24Q3GR]] law, $\varphi(t) = e^{-\abs{t}}$, so $a X_1 + b X_2$ has characteristic function $e^{-(a + b)\abs{t}}$, the law of $(a + b) X$; this is index $1$.
Non-example: let $X$ be Poisson with mean $\lambda > 0$. Then $X_1 + X_2$ is Poisson with mean $2\lambda$, and takes all values in $\N$. If it had the law of $cX + d$, comparing the two smallest values of the supports would force $c = 1$ and $d = 0$, but $X$ has mean $\lambda \ne 2\lambda$.
For $\alpha < 2$, $E[\abs{X}^p] < \infty$ if and only if $p < \alpha$; so the variance is infinite, and the mean is finite only for $\alpha > 1$.
Some authors also call the point masses stable.
