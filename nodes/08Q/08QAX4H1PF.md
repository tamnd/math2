---
tag: 08QAX4H1PF
kind: example
name: The sequence 1/n tends to zero
msc: [40A05]
instance_of: [0W4CN9E2W5]
uses: [0XKWSSY8P2, 09G6KHS6GY]
sources:
  - url: https://en.wikipedia.org/wiki/Limit_of_a_sequence
    locator: Examples
---

## Example

Let $a_n = 1/n$ for each integer $n \ge 1$.
Then $a_n \to 0$ as $n \to \infty$.
Let $\varepsilon > 0$. By the Archimedean property of $\mathbb{R}$, there is a natural number $N$ with $N > 1/\varepsilon$.
For each $n \ge N$ we get $|a_n - 0| = 1/n \le 1/N < \varepsilon$.
By the [[epsilon-N definition|09G6KHS6GY]], this shows $1/n \to 0$.

## Remarks

The proof uses the Archimedean property, which says that the natural numbers are not bounded above in $\mathbb{R}$.
With the [[algebra of limits|07XBM3A9J5]], it gives many more limits, for example $1/n^2 \to 0$ and $(n + 1)/n \to 1$.
Mathlib states it for $1/n$ over $\mathbb{R}$ as `tendsto_one_div_atTop_nhds_zero_nat`.

## Explanations

### L1 human

The numbers $1, 1/2, 1/3, 1/4, \dots$ get smaller and smaller, and they approach $0$.
To get $1/n$ below $0.001$, it is enough to take $n > 1000$.
