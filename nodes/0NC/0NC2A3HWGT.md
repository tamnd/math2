---
tag: 0NC2A3HWGT
kind: statement
role: corollary
name: The integral of a continuous function is an antiderivative
msc: [26A36]
uses: [063H5KJC69, 0BW9N5CDSB, 06SESV7GQY]
sources:
  - url: https://en.wikipedia.org/wiki/Fundamental_theorem_of_calculus
    locator: First part
---

## Statement

Let $I$ be an open interval, let $f \colon I \to \mathbb{R}$ be continuous, and let $a \in I$.
Then $F(x) = \int_a^x f(t) \, dt$ is an [[antiderivative|0BW9N5CDSB]] of $f$ on $I$.

## Remarks

The integral exists, since [[continuous functions are integrable|06SESV7GQY]]. The [[first fundamental theorem|063H5KJC69]] applies at each point of $I$.
So every continuous function on an open interval has an antiderivative.
Mathlib states the derivative as `Continuous.deriv_integral`.

## Explanations

### L1 human

Every continuous function has an antiderivative.
The area function from a fixed starting point is one.
