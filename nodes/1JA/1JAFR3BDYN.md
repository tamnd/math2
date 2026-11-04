---
tag: 1JAFR3BDYN
kind: proof
name: Proof that the binomial series has radius of convergence 1
msc: [30B10]
proves: 0KX1MXJ5MR
uses: [0HB0XKDXHH, 0JBMYAA9QH, 0WH916TJNY, 09G6KHS6GY, 0RAM4E07NR, 0734RSVF2V]
sources:
  - url: https://en.wikipedia.org/wiki/Binomial_series
    locator: Conditions for convergence
---

## Proof

We apply the [[ratio formula for the radius of convergence|0JBMYAA9QH]].

1. Let $\alpha$ be a real number that is not a natural number. For each natural number $k$, let $c_k = \binom{\alpha}{k} = \alpha (\alpha - 1) \cdots (\alpha - k + 1) / k!$, the coefficients of the [[binomial series|0HB0XKDXHH]].
2. For each natural number $j$, $\alpha - j \ne 0$, since $\alpha$ is not a natural number. So $c_k$ is a product of nonzero numbers divided by $k!$, and $c_k \ne 0$ for all $k$.
3. From the formula in step 1, $c_{k+1} = c_k \cdot (\alpha - k)/(k + 1)$. So $\abs{c_{k+1}} / \abs{c_k} = \abs{\alpha - k} / (k + 1)$.
4. For $k > \abs{\alpha}$ we have $\alpha - k < 0$. So $\abs{\alpha - k}/(k + 1) = (k - \alpha)/(k + 1) = 1 - (1 + \alpha)/(k + 1)$.
5. We show $1/(k + 1) \to 0$. Let $\varepsilon > 0$. There is a natural number $n \ge 1$ with [[$1/n < \varepsilon$|0WH916TJNY]].
6. For $k \ge n$, $0 < 1/(k + 1) < 1/n < \varepsilon$. By the [[epsilon-N form|09G6KHS6GY]], $1/(k + 1) \to 0$.
7. By the [[product rule|0734RSVF2V]] and the [[sum rule|0RAM4E07NR]] for limits, $1 - (1 + \alpha)/(k + 1) \to 1 - 0 = 1$.
8. By steps 3 and 4, $\abs{c_{k+1}} / \abs{c_k} \to 1$ as $k \to \infty$.
9. By step 2 and step 8, the ratio formula applies with $L = 1$. So the radius of convergence is $R = 1/1 = 1$.

## Idea

The ratio of consecutive coefficients is $(\alpha - k)/(k + 1)$, which tends to $-1$. So its absolute value tends to $1$. The hypothesis on $\alpha$ makes every coefficient nonzero, so the ratio formula applies. If $\alpha$ were a natural number, the series would stop and be a polynomial.
