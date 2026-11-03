---
tag: JB2FETPGNZ
kind: definition
name: Expected utility hypothesis
msc: [91B16, 91B06]
defines: 8C2N37XPJ8
uses: [JGP0Q56FRY, GZZS4MTDG9, 0WQNRCNY3M]
sources:
  - url: https://en.wikipedia.org/wiki/Expected_utility_hypothesis
---

## Definition

Let $X$ be a set of outcomes.
A *lottery* on $X$ is a function $L \colon X \to [0, 1]$ with finite support and $\sum_{x \in X} L(x) = 1$, where $L(x)$ is the probability of the outcome $x$.
Let $\mathcal{L}(X)$ be the set of lotteries on $X$, and let $\succsim$ be a [[preference relation|JGP0Q56FRY]] on $\mathcal{L}(X)$.
An *expected utility representation* of $\succsim$ is a function $u \colon X \to \R$ such that, for all $L, M \in \mathcal{L}(X)$,
$$L \succsim M \iff \sum_{x \in X} L(x)\, u(x) \ge \sum_{x \in X} M(x)\, u(x).$$
The *expected utility hypothesis* for $\succsim$ is the assertion that $\succsim$ has an expected utility representation.
The function $u$ is then called a von Neumann–Morgenstern utility function, or Bernoulli utility function.

## Remarks

Let $X = \set{0, 100}$ and let $u(0) = 0$, $u(100) = 1$.
The relation defined by $L \succsim M$ when $L(100) \ge M(100)$ has the expected utility representation $u$, since $\sum_x L(x) u(x) = L(100)$.
Each lottery on this $X$ is fixed by $q = L(100)$.
The relation "$L \succsim M$ when $\abs{L(100) - 1/2} \le \abs{M(100) - 1/2}$" is a preference relation with no expected utility representation.
Indeed, a representation would make the value of a lottery equal to $u(0) + q\,(u(100) - u(0))$, an affine function of $q$.
The two sure outcomes $q = 0$ and $q = 1$ are indifferent, so this affine function would be constant, yet $q = 1/2$ is strictly preferred to $q = 0$.
The map $L \mapsto \sum_x L(x) u(x)$ is the [[expected value|0WQNRCNY3M]] of $u$ under $L$, so it is linear under mixtures of lotteries.
If $u$ is an expected utility representation, so is $a u + b$ for all $a > 0$ and $b \in \R$, and when $\succsim$ is not indifference between all lotteries, every other representation has this form.
