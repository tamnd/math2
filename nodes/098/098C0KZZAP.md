---
tag: 098C0KZZAP
kind: statement
role: theorem
name: Intermediate value theorem for connected spaces
aliases: [intermediate-value-theorem]
msc: [54D05]
uses: [0EPD87YVG8, 0B9ZQFMQNV, 0SY9ECQ19Q]
sources:
  - url: https://en.wikipedia.org/wiki/Intermediate_value_theorem
    locator: General metric and topological spaces
  - url: https://en.wikipedia.org/wiki/Intermediate_value_theorem
    locator: Theorem
---

## Statement

Let $X$ be a [[connected space|0D939CMME7]], let $f \colon X \to \mathbb{R}$ be [[continuous|0SY9ECQ19Q]], and let $a, b \in X$.
Then for each real $c$ between $f(a)$ and $f(b)$ there is $x \in X$ with $f(x) = c$.

## Remarks

Proof: $f(X)$ is connected, by [[continuous image of a connected set is connected|0EPD87YVG8]]. Thus it is an interval, by [[connected subsets of the real line are intervals|0B9ZQFMQNV]], and it contains $c$.
For $X = [a, b]$, this is the intermediate value theorem of calculus: a continuous $f \colon [a, b] \to \mathbb{R}$ takes each value between $f(a)$ and $f(b)$.
For example, each polynomial of odd degree with real coefficients has a real root.

## Explanations

### L1 human

A continuous real function on a connected space cannot jump over a value. To get from $f(a)$ to $f(b)$, it passes through all values in between.
