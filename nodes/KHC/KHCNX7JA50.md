---
tag: KHCNX7JA50
kind: definition
name: Mutual information
msc: [94A17, 62B10]
defines: A83CYGDXFG
uses: [0X2J0VY6DN, 0DR81R1F2B, PQBW43X5RE, Y86E072V0V, F3ZNDD6GG7, DZWEWHZ20N]
sources:
  - url: https://en.wikipedia.org/wiki/Mutual_information
---

## Definition

Let $X$ and $Y$ be [[discrete random variables|0X2J0VY6DN]] on a common probability space, with values in countable sets $\mathcal{X}$ and $\mathcal{Y}$.
Let $p(x, y)$ be their [[joint mass function|0DR81R1F2B]], and let $p(x) = \sum_y p(x, y)$ and $p(y) = \sum_x p(x, y)$ be the marginal mass functions.
The *mutual information* of $X$ and $Y$ is
$$I(X; Y) = \sum_{x, y \,:\, p(x, y) > 0} p(x, y) \log \frac{p(x, y)}{p(x) \, p(y)} \in [0, \infty].$$

## Remarks

Equivalently, $I(X; Y) = D(P_{(X, Y)} \,\|\, P_X \otimes P_Y)$, the [[Kullback–Leibler divergence|PQBW43X5RE]] of the joint law from the product of the marginal laws.
This form defines $I(X; Y)$ for arbitrary random variables, not only discrete ones.
It is symmetric, $I(X; Y) = I(Y; X)$, and non-negative, with $I(X; Y) = 0$ exactly when $X$ and $Y$ are independent.
If $H(X)$ and $H(Y)$ are finite, then $I(X; Y) = H(X) - H(X \mid Y) = H(X) + H(Y) - H(X, Y)$, with the [[Shannon entropy|Y86E072V0V]], the [[conditional entropy|F3ZNDD6GG7]] and the [[joint entropy|DZWEWHZ20N]].
In particular $I(X; X) = H(X)$.

Example: let $X$ be a fair bit and $Y = X$.
The two terms with $p(x, y) > 0$ are $(0, 0)$ and $(1, 1)$, each equal to $\frac12 \log_2 \frac{1/2}{1/4} = \frac12$, so $I(X; Y) = 1$ bit.

Non-example: the covariance of $X$ and $Y$ is not the mutual information; for $X$ uniform on $\set{-1, 0, 1}$ and $Y = X^2$ the covariance is $0$, but $I(X; Y) = H(Y) = H_b(\frac13) > 0$.

## Explanations

### L1 human

Mutual information compares the true joint law of $X$ and $Y$ with the law they would have if they were independent.
The larger the difference, the more the two variables tell about each other.
