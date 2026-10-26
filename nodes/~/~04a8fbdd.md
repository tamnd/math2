---
tag: ~04a8fbdd
kind: definition
name: Discrete random variable
msc: ["60E05"]
defines: ~d3097315
uses: [~89528024, 0ZG61TFBES]
sources:
  - url: https://en.wikipedia.org/wiki/Probability_distribution
    locator: Discrete probability distribution
---

## Definition

Let $X$ be a real [[random variable|~89528024]] on a probability space $(\Omega, \mathcal{F}, P)$.
$X$ is discrete if there is a [[countable set|0ZG61TFBES]] $S \subseteq \mathbb{R}$ with $P(X \in S) = 1$.
A distribution $\mu$ on $\mathbb{R}$ is discrete if $\mu(S) = 1$ for some countable set $S$.

## Remarks

Then $P(X \in B) = \sum_{x \in B \cap S} P(X = x)$ for each Borel set $B$. So the [[probability mass function|~301be016]] $x \mapsto P(X = x)$ determines the law of $X$.
The cumulative distribution function of a discrete random variable is a step function when the set of values has no limit points. It jumps by $P(X = x)$ at each value $x$.
The Bernoulli, binomial, geometric and Poisson distributions are discrete.

## Explanations

### L1 human

A discrete random variable takes values that you can list, such as $0, 1, 2, \dots$.
The number of heads in ten coin tosses and the number of calls in an hour are discrete random variables.
