---
tag: T761KPKPV6
kind: definition
name: Trigonometric integrals
msc: ["33E20", "33B10"]
defines: VB37Q6FY1Y
uses: [08WFZP6P89, 05KQ3F99BQ, 00C5P9JZBK]
sources:
  - url: https://en.wikipedia.org/wiki/Trigonometric_integral
---

## Definition

Let $\sin$ and $\cos$ be the [[sine and cosine|08WFZP6P89]] functions.
1. The *sine integral* is the function $\operatorname{Si} \colon \R \to \R$ given by
$$\operatorname{Si}(x) = \int_0^x \frac{\sin t}{t}\, dt,$$
where the integrand is given the value $1$ at $t = 0$.
2. The *cosine integral* is the function on $x > 0$ given by the [[improper integral|05KQ3F99BQ]]
$$\operatorname{Ci}(x) = -\int_x^\infty \frac{\cos t}{t}\, dt.$$
3. The *hyperbolic sine integral* and *hyperbolic cosine integral* are $\operatorname{Shi}(x) = \int_0^x \frac{\sinh t}{t}\, dt$ for real $x$ and $\operatorname{Chi}(x) = \gamma + \ln x + \int_0^x \frac{\cosh t - 1}{t}\, dt$ for $x > 0$, where $\gamma$ is the [[Euler–Mascheroni constant|00C5P9JZBK]].

## Remarks

Equivalently, $\operatorname{Ci}(x) = \gamma + \ln x + \int_0^x \frac{\cos t - 1}{t}\, dt$ for $x > 0$.

Example: $\operatorname{Si}$ is odd, $\operatorname{Si}(0) = 0$, and $\lim_{x \to \infty} \operatorname{Si}(x) = \frac{\pi}{2}$ by the [[Dirichlet integral|0GZNSHMG4Q]].
The largest value of $\operatorname{Si}$ on $[0, \infty)$ is $\operatorname{Si}(\pi) \approx 1.8519$.

Non-example: $\int_0^x \frac{\cos t}{t}\, dt$ is not a valid definition of $\operatorname{Ci}$; it diverges at $0$ because $\frac{\cos t}{t} \sim \frac{1}{t}$ there.
This is why $\operatorname{Ci}$ is defined from $\infty$, and it has a logarithmic singularity at $0$.

The shifted function $\operatorname{si}(x) = \operatorname{Si}(x) - \frac{\pi}{2} = -\int_x^\infty \frac{\sin t}{t}\, dt$ is also used.
