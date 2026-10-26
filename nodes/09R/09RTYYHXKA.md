---
tag: 09RTYYHXKA
kind: counterexample
name: Smooth non-analytic function
msc: ["26E10"]
uses: [0BE3QDH73A, 0JD5ZNW0F4, 0225QPWRRE]
sources:
  - url: https://en.wikipedia.org/wiki/Non-analytic_smooth_function
    locator: An example function
same_as:
  wikidata: Q7048840
  wikipedia: Non-analytic smooth function
---

## Counterexample

Let $f(x) = e^{-1/x}$ for $x > 0$ and $f(x) = 0$ for $x \le 0$.
Then $f$ is [[smooth|0BE3QDH73A]] on $\mathbb{R}$, and $f^{(n)}(0) = 0$ for all $n$.
So its [[Taylor series|0225QPWRRE]] at $0$ is the zero series. But $f(x) > 0$ for $x > 0$, so $f$ is not [[analytic|0JD5ZNW0F4]] at $0$.

## Remarks

For $x > 0$, each derivative has the form $p_n(1/x) e^{-1/x}$ for a polynomial $p_n$. It tends to $0$ as $x \to 0^+$, because $e^{-1/x}$ decays faster than any power of $x$.
Such functions give smooth bump functions and smooth partitions of unity.
Mathlib defines this function as `expNegInvGlue`.

## Explanations

### L1 human

This function is so flat at $0$ that all its derivatives vanish there.
So its Taylor series sees only the zero function, but the function is not zero.
