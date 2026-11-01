---
tag: S8X2N1DW8P
kind: statement
role: theorem
name: Chebyshev's sum inequality
msc: [26D15]
uses: [0KN22AAW5R]
about: [0KN22AAW5R]
sources:
  - url: https://en.wikipedia.org/wiki/Chebyshev%27s_sum_inequality
same_as:
  wikidata: Q1428736
  wikipedia: Chebyshev's sum inequality
---

## Statement

Let $a_1 \ge a_2 \ge \dots \ge a_n$ and $b_1 \ge b_2 \ge \dots \ge b_n$ be real numbers.
Then
$$\frac{1}{n} \sum_{i=1}^{n} a_i b_i \ge \Big( \frac{1}{n} \sum_{i=1}^{n} a_i \Big) \Big( \frac{1}{n} \sum_{i=1}^{n} b_i \Big).$$

## Remarks

Proof idea: expand to get the identity
$$n \sum_{i=1}^{n} a_i b_i - \sum_{i=1}^{n} a_i \sum_{j=1}^{n} b_j = \frac{1}{2} \sum_{i=1}^{n} \sum_{j=1}^{n} (a_i - a_j)(b_i - b_j).$$
Each term on the right is $\ge 0$, because $a_i - a_j$ and $b_i - b_j$ have the same sign for [[monotone sequences|0KN22AAW5R]] ordered the same way.

If one sequence decreases and the other increases, the inequality is reversed.
The common ordering is needed: for $a = (1, 0)$ and $b = (0, 1)$, the left side is $0$ and the right side is $1/4$.

Example: taking $b = a$ gives $n \sum a_i^2 \ge (\sum a_i)^2$, which holds for every real sequence after sorting.

Mathlib states a form as `Monovary.sum_mul_sum_le_card_mul_sum`.

## Explanations

### L1 human

If two lists are sorted in the same order, the average of their products is at least the product of their averages.
Large values meet large values, so the products are pushed up.
For lists sorted in opposite orders the reverse holds.

### L2 human

The inequality follows from the [[rearrangement inequality|6E9TAF8HCY]] by summing over the $n$ cyclic shifts of the second sequence.
It has an integral form: if $f$ and $g$ are both increasing on $[0, 1]$, then $\int_0^1 f g \ge \int_0^1 f \int_0^1 g$.
In probability it says that two increasing functions of the same random variable have nonnegative covariance.
