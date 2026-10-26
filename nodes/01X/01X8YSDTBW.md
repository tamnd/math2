---
tag: 01X8YSDTBW
kind: definition
name: Identically distributed random variables
msc: ["60E05"]
defines: 08ZDW5SA3B
uses: [0TST4MHA3A]
sources:
  - url: https://en.wikipedia.org/wiki/Independent_and_identically_distributed_random_variables
    locator: Definition for two random variables
---

## Definition

Let $(E, \mathcal{E})$ be a set with a σ-algebra.
Let $X$ be a random variable on a probability space $(\Omega, \mathcal{F}, P)$ with values in $E$.
Let $Y$ be a random variable on a probability space $(\Omega', \mathcal{F}', P')$ with values in $E$.
$X$ and $Y$ are identically distributed if they have the same [[law|0TST4MHA3A]]: $P(X \in B) = P'(Y \in B)$ for each $B \in \mathcal{E}$.
One writes $X \overset{d}{=} Y$.

## Remarks

For real random variables, this holds if and only if $X$ and $Y$ have the same cumulative distribution function.
Identically distributed random variables need not be equal. For a fair coin, the indicator $X$ of heads and the indicator $1 - X$ of tails are identically distributed, but they are never equal.
If $X \overset{d}{=} Y$ and $g$ is a measurable function, then $g(X) \overset{d}{=} g(Y)$.

## Explanations

### L1 human

Two random variables are identically distributed when they behave the same way statistically.
The results of two different fair dice are identically distributed, although the dice show different numbers in most throws.
