---
tag: 0225QPWRRE
kind: definition
name: Taylor series
msc: [41A58]
defines: 0Z49YH6ZWY
uses: [0BE3QDH73A, 0VP56B4EMX, 0HFSFVMWQB]
sources:
  - url: https://en.wikipedia.org/wiki/Taylor_series
    locator: Definition
---

## Definition

Let $I$ be an open interval, let $a \in I$, and let $f \colon I \to \mathbb{R}$ be [[smooth|0BE3QDH73A]].
The Taylor series of $f$ at $a$ is the [[power series|0VP56B4EMX]]
$$\sum_{n=0}^{\infty} \frac{f^{(n)}(a)}{n!} (x - a)^n.$$

## Remarks

Its partial sums are the [[Taylor polynomials|0HFSFVMWQB]] of $f$ at $a$.
The Taylor series may diverge for each $x \ne a$. It may also converge to a function other than $f$, as for the [[smooth non-analytic function|09RTYYHXKA]].
The Taylor series converges to $f$ near $a$ exactly when $f$ is [[analytic|0JD5ZNW0F4]] at $a$.
For $a = 0$ it is the [[Maclaurin series|043SJ5RF59]].

## Explanations

### L1 human

The Taylor series is the Taylor polynomial of infinite degree.
It uses all the derivatives of $f$ at one point.
