---
tag: 0WCZH4AFMT
kind: definition
name: Rational function
msc: [26A09]
defines: 0XDK9CGYKJ
uses: [0GR2APWTAC, 0C5TP6RYSV]
sources:
  - url: https://en.wikipedia.org/wiki/Rational_function
    locator: Definitions
---

## Definition

Let $p$ and $q$ be real polynomials, with $q$ not the zero polynomial.
Let $D = \{ x \in \mathbb{R} : q(x) \ne 0 \}$.
The function $f \colon D \to \mathbb{R}$ given by $f(x) = p(x)/q(x)$ is a rational function.

## Remarks

A nonzero polynomial has only finitely many roots, so $D$ is $\mathbb{R}$ minus a finite set.
Each rational function is continuous on $D$, since [[polynomials are continuous|0C5TP6RYSV]] and [[quotients of continuous functions are continuous|0GR2APWTAC]].
For example, $1/x$ and $(x^2 + 1)/(x - 2)$ are rational functions.

## Explanations

### L1 human

A rational function is a quotient of two polynomials.
It is defined everywhere except at the zeros of the denominator.
