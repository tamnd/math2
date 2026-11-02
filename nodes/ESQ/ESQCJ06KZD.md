---
tag: ESQCJ06KZD
kind: definition
name: Kruskal–Wallis test
msc: [62G10]
defines: EG4VCBXDKZ
uses: [087P03NEND, 0AJN7WHBJZ, 0RFMMBHFTV, 0JDAQHWA9N]
sources:
  - url: https://en.wikipedia.org/wiki/Kruskal%E2%80%93Wallis_test
---

## Definition

Let $k \ge 2$, and for $g = 1, \dots, k$ let $X_{g1}, \dots, X_{g n_g}$ be [[i.i.d.|0AJN7WHBJZ]] real random variables with a continuous distribution function $F_g$, the $k$ samples being independent.
Let $N = n_1 + \dots + n_k$.
Rank all $N$ observations together from $1$ to $N$, let $R_g$ be the sum of the ranks in sample $g$, and let $\bar R_g = R_g / n_g$.
The *Kruskal–Wallis statistic* is
$$H = \frac{12}{N(N+1)} \sum_{g=1}^{k} n_g \Big( \bar R_g - \frac{N + 1}{2} \Big)^2 = \frac{12}{N(N+1)} \sum_{g=1}^{k} \frac{R_g^2}{n_g} - 3(N + 1).$$
The *Kruskal–Wallis test* of $H_0 \colon F_1 = \dots = F_k$ rejects $H_0$ when $H$ is large.

## Remarks

Under $H_0$ the law of $H$ depends only on $n_1, \dots, n_k$.
As all $n_g \to \infty$, $H$ [[converges in distribution|0JDAQHWA9N]] to the [[chi-squared distribution|0RFMMBHFTV]] with $k - 1$ degrees of freedom, which gives approximate critical values.
The number $(N+1)/2$ is the mean of the ranks $1, \dots, N$.

Example: $k = 2$, samples $(1, 2)$ and $(3, 4)$, so $N = 4$, $R_1 = 3$, $R_2 = 7$.
Then $H = \frac{12}{20}\big(\frac{9}{2} + \frac{49}{2}\big) - 15 = 17.4 - 15 = 2.4$.
The first form gives the same: $\frac{12}{20}\big(2(1.5 - 2.5)^2 + 2(3.5 - 2.5)^2\big) = 0.6 \cdot 4 = 2.4$.

Non-example: repeated measurements on the same subjects under $k$ conditions are not independent samples.
The clause on independence fails; the Friedman test is used for such blocked data.
