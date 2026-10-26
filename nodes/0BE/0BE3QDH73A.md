---
tag: 0BE3QDH73A
kind: definition
name: Smooth function
msc: ["26E10"]
defines: 0V33BNKZ9S
uses: [06SKCHDQT5]
sources:
  - url: https://en.wikipedia.org/wiki/Smoothness
    locator: Differentiability classes
---

## Definition

Let $I$ be an open interval and let $f \colon I \to \mathbb{R}$.
The function $f$ is smooth, or of class $C^{\infty}$, if it is of [[class $C^k$|06SKCHDQT5]] for each natural number $k$.

## Remarks

So a smooth function has derivatives of all orders.
Polynomials, the exponential function, and the sine are smooth on $\mathbb{R}$.
A smooth function need not be [[analytic|0JD5ZNW0F4]]. See the [[smooth non-analytic function|09RTYYHXKA]].
Mathlib uses `ContDiff ℝ ⊤ f`.

## Explanations

### L1 human

A smooth function can be differentiated as many times as we like.
All its derivatives exist and are continuous.
