---
tag: ~fe69b7ef
kind: definition
name: Analytic function
aliases: [real-analytic-function]
msc: ["26E05"]
defines: ~f59812f7
uses: [~9b386670]
sources:
  - url: https://en.wikipedia.org/wiki/Analytic_function
    locator: Definitions
---

## Definition

Let $I$ be an open interval and let $f \colon I \to \mathbb{R}$.
The function $f$ is analytic at $a \in I$ if there are $r > 0$ and a [[power series|~9b386670]] $\sum c_n (x - a)^n$ that converges to $f(x)$ for all $x$ with $|x - a| < r$.
It is analytic on $I$ if it is analytic at each point of $I$.

## Remarks

An analytic function is [[smooth|~61ef95c0]], and its power series at $a$ is its [[Taylor series|~3da7ac56]] at $a$.
Polynomials, the exponential function, sine, and cosine are analytic on $\mathbb{R}$.
A smooth function need not be analytic. See the [[smooth non-analytic function|~e21a0b09]].
Mathlib defines analyticity at a point as `AnalyticAt`.

## Explanations

### L1 human

An analytic function equals a convergent power series near each point.
So it is determined near a point by its derivatives at that point.
