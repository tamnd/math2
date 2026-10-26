---
tag: 0JQE130DHW
kind: statement
role: theorem
name: Weierstrass approximation theorem
msc: [41A10]
uses: [0C4VWBFY73, 0W0TZDRF9C, 08FPABDQ4C]
sources:
  - url: https://en.wikipedia.org/wiki/Stone%E2%80%93Weierstrass_theorem
    locator: Weierstrass approximation theorem
---

## Statement

Let $a < b$ and let $f \colon [a, b] \to \mathbb{R}$ be continuous.
Then for every $\varepsilon > 0$ there is a polynomial $p$ with $|f(x) - p(x)| < \varepsilon$ for all $x \in [a, b]$.

## Remarks

Equivalently, there is a sequence of polynomials that converges [[uniformly|08FPABDQ4C]] to $f$ on $[a, b]$.
One proof uses the [[Bernstein polynomials|0C4VWBFY73]] on $[0, 1]$, together with [[uniform continuity|0W0TZDRF9C]] of $f$.
The Stone–Weierstrass theorem generalizes the result to compact spaces. Mathlib states the theorem as `polynomialFunctions_closure_eq_top`.

## History

Karl Weierstrass proved the theorem in 1885.

## Explanations

### L1 human

Every continuous function on a closed bounded interval is uniformly close to a polynomial.
So polynomials can imitate any continuous graph as closely as we like.
