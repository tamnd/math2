---
tag: 0XRRYF1HPE
kind: statement
role: theorem
name: Dini's theorem
msc: [40A30]
uses: [056FSKG32J, 08FPABDQ4C, 0KDJD249DT]
sources:
  - url: https://en.wikipedia.org/wiki/Dini%27s_theorem
    locator: Formal statement
same_as:
  wikidata: Q595466
  wikipedia: Dini's theorem
---

## Statement

Let $a < b$, and let $f_n \colon [a, b] \to \mathbb{R}$ be continuous functions with $f_n(x) \le f_{n+1}(x)$ for all $n$ and all $x$.
Assume that $(f_n)$ converges [[pointwise|056FSKG32J]] to a continuous function $f$ on $[a, b]$.
Then $(f_n)$ converges [[uniformly|08FPABDQ4C]] to $f$ on $[a, b]$.

## Remarks

The same holds for decreasing sequences, and for any compact space in place of $[a, b]$.
One proof uses the [[Bolzano–Weierstrass theorem|0KDJD249DT]]. Another uses the open sets $\{x : f(x) - f_n(x) < \varepsilon\}$, which increase and cover $[a, b]$.
All hypotheses are needed. The sequence $x^n$ on $[0, 1]$ is monotone, but its limit is not continuous. Mathlib states a version as `Monotone.tendstoLocallyUniformly_of_forall_tendsto`.

## History

The theorem is named after Ulisse Dini. He gave the first version in an 1878 book on real functions, printed in Pisa.

## Explanations

### L1 human

If continuous functions increase to a continuous limit on a closed bounded interval, they get close to it everywhere at once.
Monotonicity and compactness rule out the bad behavior of examples such as $x^n$.
