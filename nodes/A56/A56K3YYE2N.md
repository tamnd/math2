---
tag: A56K3YYE2N
kind: definition
name: Theil index
msc: [91B82, 62P20, 94A17]
defines: ZXKS5FADM1
uses: [04DXAFN2ES, PQBW43X5RE]
sources:
  - url: https://en.wikipedia.org/wiki/Theil_index
---

## Definition

Let $x_1, \dots, x_n \ge 0$ be incomes with positive mean $\mu = \frac{1}{n} \sum_{i=1}^n x_i$.
The *Theil index* (Theil $T$ index) is
$$T = \frac{1}{n} \sum_{i=1}^n \frac{x_i}{\mu} \ln \frac{x_i}{\mu},$$
with the convention $0 \ln 0 = 0$.
Here $\ln$ is the [[natural logarithm|04DXAFN2ES]].
When all $x_i > 0$, the *Theil $L$ index*, or mean log deviation, is
$$L = \frac{1}{n} \sum_{i=1}^n \ln \frac{\mu}{x_i}.$$

## Remarks

With the income shares $s_i = x_i/(n \mu)$, which sum to $1$, the index is
$$T = \sum_{i=1}^n s_i \ln (n s_i) = \ln n - H(s), \qquad H(s) = -\sum_{i=1}^n s_i \ln s_i.$$
So $T$ is the [[Kullback–Leibler divergence|PQBW43X5RE]] of the shares from the uniform distribution.
Hence $0 \le T \le \ln n$, with $T = 0$ exactly at equality and $T = \ln n$ when one income is positive and the rest are $0$.

Example: incomes $1$ and $4$ have $\mu = 5/2$, so $x_i/\mu$ equals $0.4$ and $1.6$.
Then $T = \frac{1}{2} (0.4 \ln 0.4 + 1.6 \ln 1.6) \approx \frac{1}{2}(-0.367 + 0.752) \approx 0.193$.

Non-example: the $L$ index is not defined for incomes $0$ and $4$, since $\ln(\mu/0)$ is not finite.
The $T$ index of these incomes is $\ln 2$.

Both indices do not change when all incomes are multiplied by the same positive number.
Both split into a within-group term and a between-group term when the population is divided into groups.
