---
tag: 0PP5ZAJPP7
kind: definition
name: Beta distribution
msc: ["60E05"]
defines: 0EW824Z7G2
uses: [04YG690N5V, 0WGDPYR30Q]
sources:
  - url: https://en.wikipedia.org/wiki/Beta_distribution
    locator: Probability density function
inventory: [VC6VNE8BBC]
---

## Definition

Let $\alpha > 0$ and $\beta > 0$.
The beta distribution with parameters $\alpha$ and $\beta$ is the distribution on $\mathbb{R}$ with the [[probability density function|04YG690N5V]]
$$f(x) = \begin{cases} \dfrac{x^{\alpha - 1} (1 - x)^{\beta - 1}}{B(\alpha, \beta)} & \text{if } 0 < x < 1, \\ 0 & \text{otherwise,} \end{cases}$$
where $B(\alpha, \beta) = \int_0^1 t^{\alpha - 1} (1 - t)^{\beta - 1} \, dt$ is the beta function.

## Remarks

The mean is $\alpha / (\alpha + \beta)$ and the variance is $\dfrac{\alpha\beta}{(\alpha + \beta)^2 (\alpha + \beta + 1)}$.
$\operatorname{Beta}(1, 1)$ is the [[uniform distribution|0WGDPYR30Q]] on $[0, 1]$.
The beta function satisfies $B(\alpha, \beta) = \Gamma(\alpha)\Gamma(\beta)/\Gamma(\alpha + \beta)$.
In Bayesian statistics, the beta distribution is the conjugate prior of the success probability $p$ of binomial data. A $\operatorname{Beta}(\alpha, \beta)$ prior and $k$ successes in $n$ trials give a $\operatorname{Beta}(\alpha + k, \beta + n - k)$ posterior.

## Explanations

### L1 human

The beta distribution describes a random proportion, a number between $0$ and $1$.
Large $\alpha$ pushes the mass toward $1$, large $\beta$ pushes it toward $0$, and $\alpha = \beta$ gives a shape that is symmetric about $1/2$.
