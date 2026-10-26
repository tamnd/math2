---
tag: 0BW9N5CDSB
kind: definition
name: Antiderivative
aliases: [primitive-function]
msc: [26A36]
defines: 0BYWRWFT4F
uses: [0F1WR9C83K]
sources:
  - url: https://en.wikipedia.org/wiki/Antiderivative
    locator: lead section
---

## Definition

Let $I$ be an open interval and let $f \colon I \to \mathbb{R}$.
A function $F \colon I \to \mathbb{R}$ is an antiderivative of $f$ on $I$ if $F$ is differentiable on $I$ and $F'(x) = f(x)$ for all $x \in I$.

## Remarks

If $F$ is an antiderivative of $f$, then so is $F + C$ for each constant $C$.
On an interval, these are all the antiderivatives, because a function with [[zero derivative|003QDZ4T16]] is constant.
For example, $x^3/3$ is an antiderivative of $x^2$ on $\mathbb{R}$.
A function with a jump has no antiderivative on an interval, by [[Darboux's theorem|0Q5A47J48D]].

## Explanations

### L1 human

An antiderivative undoes differentiation.
We look for a function whose derivative is the given function.
