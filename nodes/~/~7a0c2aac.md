---
tag: ~7a0c2aac
kind: statement
role: proposition
name: Divergence part of the ratio test
msc: [40A05]
uses: [~a39ef3d8, ~b65556fc]
sources:
  - url: https://en.wikipedia.org/wiki/Ratio_test
    locator: The test
---

## Statement

Let $(a_n)$ be a real sequence with $a_n \ne 0$ for all $n$.
Assume that $|a_{n+1}| / |a_n| \to L$ as $n \to \infty$, for a real number $L$ with $L > 1$.
Then the series $\sum a_n$ diverges.

## Remarks

For large $n$ we have $|a_{n+1}| > |a_n|$. So $|a_n|$ is eventually increasing and positive, and $a_n$ does not tend to $0$. The [[term test|~b65556fc]] gives divergence.
The same proof works when $|a_{n+1}| / |a_n| \to +\infty$.
For example, $\sum 2^n / n$ diverges, since the ratio is $2n/(n+1) \to 2$.

## Explanations

### L1 human

If each term is eventually bigger than the term before, the terms cannot shrink to $0$.
Then the series cannot converge.
