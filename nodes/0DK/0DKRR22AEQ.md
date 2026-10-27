---
tag: 0DKRR22AEQ
kind: definition
name: Random variable
msc: [60A05]
defines: 0PNRKMRC55
uses: [0ZYBZ34RT2, 04WSW8T3SY, 0BVHZXWKCD, 0XHDTE5YMZ, 0FGCFY1AZX]
sources:
  - url: https://en.wikipedia.org/wiki/Random_variable
    locator: Measure-theoretic definition
inventory: [7S5969T1EZ]
---

## Definition

Let $(\Omega, \mathcal{F}, P)$ be a [[probability space|0ZYBZ34RT2]] and let $(E, \mathcal{E})$ be a set $E$ with a [[σ-algebra|04WSW8T3SY]] $\mathcal{E}$.
A random variable with values in $E$ is a [[function|0XHDTE5YMZ]] $X \colon \Omega \to E$ such that the [[preimage|0FGCFY1AZX]] $X^{-1}(B) = \{\omega \in \Omega : X(\omega) \in B\}$ is in $\mathcal{F}$ for each $B \in \mathcal{E}$.
A real random variable is a random variable with values in $\mathbb{R}$, with the [[Borel σ-algebra|0BVHZXWKCD]] on $\mathbb{R}$.

## Remarks

The condition says that $X$ is a measurable function. It makes $\{X \in B\}$ an event, so $P(X \in B)$ is defined.
A real function $X$ on $\Omega$ is a random variable if and only if $\{X \le x\} \in \mathcal{F}$ for each $x \in \mathbb{R}$.
For two rolls of a die, $\Omega = \{1, \dots, 6\}^2$ and the sum $X(a, b) = a + b$ is a random variable.
Sums, products and continuous functions of real random variables are random variables.

## Explanations

### L1 human

A random variable is a number that you read off from the result of the experiment.
For two rolls of a die, the sum of the two numbers is a random variable.
It is $7$ for the result $(3, 4)$ and $12$ for the result $(6, 6)$.
