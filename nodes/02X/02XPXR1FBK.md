---
tag: 02XPXR1FBK
kind: definition
name: Bernoulli process
msc: [60G50]
defines: 0CQQG3DEW9
uses: [0AJN7WHBJZ, 0J97P5KZY0, 0QH5ENKZM1]
sources:
  - url: https://en.wikipedia.org/wiki/Bernoulli_process
    locator: Definition
---

## Definition

Let $p \in [0, 1]$.
A Bernoulli process with parameter $p$ is a [[stochastic process|0QH5ENKZM1]] $(X_n)_{n \ge 1}$ of [[i.i.d.|0AJN7WHBJZ]] random variables with the [[Bernoulli distribution|0J97P5KZY0]] $\operatorname{Bernoulli}(p)$:
$$P(X_n = 1) = p \quad \text{and} \quad P(X_n = 0) = 1 - p \quad \text{for each } n \ge 1.$$

## Remarks

One calls $X_n = 1$ a success and $X_n = 0$ a failure in trial $n$.
The number of successes in the first $n$ trials has the binomial distribution $\operatorname{Bin}(n, p)$.
For $0 < p \le 1$, the number of failures before the first success has the geometric distribution with parameter $p$. The times between successes are i.i.d.
The Bernoulli process is a discrete-time analogue of the Poisson process.

## Explanations

### L1 human

The Bernoulli process is the mathematical model of tossing the same coin again and again, forever.
Each toss is independent of the others, and each has the same probability $p$ of heads.
