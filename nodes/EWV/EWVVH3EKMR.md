---
tag: EWVVH3EKMR
kind: example
name: Renewal equation
msc: [45D05, 60K05]
instance_of: [SNFYTC1TTA]
uses: [45V0W838BQ]
sources:
  - url: https://en.wikipedia.org/wiki/Renewal_theory
---

## Example

Let $F$ be the distribution function of a nonnegative random variable with $F(0) = 0$, and let $g$ be a locally bounded function on $[0, \infty)$.
The *renewal equation* for an unknown locally bounded function $u$ on $[0, \infty)$ is
$$u(t) = g(t) + \int_0^t u(t - s) \, dF(s), \quad t \ge 0.$$
When $F$ has a density $k = F'$, the integral is $\int_0^t k(t - s) \, u(s) \, ds$, and the equation is a [[Volterra equation of convolution type|SNFYTC1TTA]] of the second kind.

In [[renewal theory|45V0W838BQ]], let $X_1, X_2, \dots$ be independent waiting times with distribution function $F$, and let $N(t)$ be the number of $n \ge 1$ with $X_1 + \cdots + X_n \le t$.
Conditioning on the first waiting time $X_1$ shows that the renewal function $m(t) = \mathbb{E}[N(t)]$ solves the renewal equation with $g = F$:
$$m(t) = F(t) + \int_0^t m(t - s) \, dF(s).$$

Check on the exponential case: let $F(t) = 1 - e^{-\lambda t}$ with $\lambda > 0$, so $dF(s) = \lambda e^{-\lambda s} \, ds$.
Then $N$ is a Poisson process of rate $\lambda$, and $m(t) = \lambda t$.
Indeed $\int_0^t \lambda (t - s) \lambda e^{-\lambda s} \, ds = \lambda t - 1 + e^{-\lambda t}$, and adding $F(t) = 1 - e^{-\lambda t}$ gives $\lambda t$.

## Remarks

The renewal equation has a unique locally bounded solution, $u = g + m * g$, that is, $u(t) = g(t) + \int_0^t g(t - s) \, dm(s)$.
Let $\varphi_F(p) = \int_{[0, \infty)} e^{-ps} \, dF(s)$.
Taking Laplace transforms gives $\hat u = \hat g / (1 - \varphi_F)$, as in the [[Laplace transform method|EHGECREYB4]].
For the exponential case, $\hat F(p) = \frac{\lambda}{p(p + \lambda)}$ and $\varphi_F(p) = \frac{\lambda}{p + \lambda}$, so $\hat m(p) = \frac{\lambda}{p(p + \lambda)} \cdot \frac{p + \lambda}{p} = \frac{\lambda}{p^2}$, the transform of $\lambda t$.

## Explanations

### L1 human

Think of a light bulb that is replaced each time it fails.
The expected number of replacements by time $t$ is the chance of a first failure by $t$, plus what happens after a first failure at time $s$.
After that failure, the same problem starts again with $t - s$ time left.
This "restart" argument gives the renewal equation, an integral equation in which the unknown appears with a time shift.
