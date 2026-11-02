---
tag: 1BK7TC6PW9
kind: definition
name: Exponential integral
msc: ["33B20", "33E20"]
defines: EV6ZDQ0NDY
uses: [05KQ3F99BQ, 0SYR10HD4R]
sources:
  - url: https://en.wikipedia.org/wiki/Exponential_integral
---

## Definition

1. For a real number $x > 0$, the exponential integral $E_1$ is the [[improper integral|05KQ3F99BQ]]
$$E_1(x) = \int_x^\infty \frac{e^{-t}}{t}\, dt.$$
2. For a real number $x \ne 0$, the exponential integral $\operatorname{Ei}$ is
$$\operatorname{Ei}(x) = \int_{-\infty}^x \frac{e^t}{t}\, dt,$$
where for $x > 0$ the integral is a [[Cauchy principal value|0SYR10HD4R]] at $t = 0$.

## Remarks

The substitution $t \mapsto -t$ gives $E_1(x) = -\operatorname{Ei}(-x)$ for $x > 0$.
With the [[Euler–Mascheroni constant|00C5P9JZBK]] $\gamma$, the series
$$\operatorname{Ei}(x) = \gamma + \ln \abs{x} + \sum_{k=1}^\infty \frac{x^k}{k \cdot k!}, \qquad E_1(x) = -\gamma - \ln x - \sum_{k=1}^\infty \frac{(-x)^k}{k \cdot k!}$$
hold for $x \ne 0$ and $x > 0$ respectively.

Example: as $x \to \infty$, $E_1(x) \sim \frac{e^{-x}}{x}$, and $E_1(x) = \Gamma(0, x)$ is the upper [[incomplete gamma function|YB7ZV0HG7K]] with $s = 0$.

Non-example of a valid argument: $E_1(0)$ is not defined, since $\int_0^1 \frac{e^{-t}}{t}\, dt \ge e^{-1} \int_0^1 \frac{dt}{t} = \infty$.

$E_1$ extends to a holomorphic function on $\C \setminus (-\infty, 0]$.
