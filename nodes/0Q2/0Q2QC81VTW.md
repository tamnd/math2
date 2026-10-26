---
tag: 0Q2QC81VTW
kind: definition
name: Cumulant generating function
msc: ["60E10"]
defines: 0N2SP6K9ZC
uses: [0NNRNGKMFM, 0STK8KEY9G, 0WRZ170YEH]
sources:
  - url: https://en.wikipedia.org/wiki/Cumulant
    locator: Definition
---

## Definition

Let $X$ be a real random variable with [[moment-generating function|0NNRNGKMFM]] $M_X$.
The cumulant generating function of $X$ is
$$K_X(t) = \ln M_X(t) = \ln E\left[e^{tX}\right],$$
for each $t \in \mathbb{R}$ with $M_X(t) < \infty$.
If $M_X$ is finite on an open interval around $0$, the cumulants $\kappa_n$ of $X$ are the coefficients in $K_X(t) = \sum_{n=1}^{\infty} \kappa_n t^n / n!$, so $\kappa_n = K_X^{(n)}(0)$.

## Remarks

The first cumulants are $\kappa_1 = E[X]$, $\kappa_2 = \operatorname{Var}(X)$ and $\kappa_3 = E[(X - E[X])^3]$.
For independent $X$ and $Y$, $K_{X+Y} = K_X + K_Y$ by the [[product rule for moment-generating functions|0WRZ170YEH]]. So cumulants of independent sums add.
For $X \sim \mathcal{N}(\mu, \sigma^2)$, $K_X(t) = \mu t + \sigma^2 t^2 / 2$. For $X \sim \operatorname{Poisson}(\lambda)$, $K_X(t) = \lambda(e^t - 1)$, so all cumulants equal $\lambda$.
$K_X$ is convex on the interval where it is finite.

## Explanations

### L1 human

Taking the logarithm turns products into sums. So the cumulant generating function of a sum of independent variables is the sum of their cumulant generating functions.
This makes cumulants convenient for sums, for example in the central limit theorem.
