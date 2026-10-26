---
tag: 06JYPJ4WHH
kind: definition
name: Convergence of a sequence in a metric space
msc: ["54E35"]
defines: 090AA928Y7
uses: [063W5JMY85]
sources:
  - url: https://en.wikipedia.org/wiki/Limit_of_a_sequence
    locator: Metric spaces
---

## Definition

Let $(X, d)$ be a [[metric space|063W5JMY85]], let $(x_n)_{n \ge 1}$ be a sequence of points of $X$, and let $x \in X$.
The sequence $(x_n)$ converges to $x$ when for each real $\varepsilon > 0$ there is an integer $N$ such that $d(x_n, x) < \varepsilon$ for all $n \ge N$.
Then $x$ is a limit of $(x_n)$, with the notation $x_n \to x$ or $\lim_{n \to \infty} x_n = x$.

## Remarks

Equivalently, $x_n \to x$ if and only if $d(x_n, x) \to 0$ in $\mathbb{R}$.
A sequence in a metric space has at most one limit. This follows from the triangle inequality, and also from the fact that [[limits are unique in Hausdorff spaces|0D8T984XEE]].
For $X = \mathbb{R}$ with the usual metric, this is the usual limit of a real sequence.

## Explanations

### L1 human

A sequence converges to $x$ when its terms come as close to $x$ as you want and stay close.
For each tolerance $\varepsilon$, only finitely many terms are farther than $\varepsilon$ from $x$.
