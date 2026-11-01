---
tag: 6E9TAF8HCY
kind: statement
role: theorem
name: Rearrangement inequality
msc: [26D15]
uses: [0BQMWCNS8S]
about: [0BQMWCNS8S]
sources:
  - url: https://en.wikipedia.org/wiki/Rearrangement_inequality
same_as:
  wikidata: Q1149189
  wikipedia: Rearrangement inequality
---

## Statement

Let $x_1 \le x_2 \le \dots \le x_n$ and $y_1 \le y_2 \le \dots \le y_n$ be real numbers, and let $\sigma$ be a [[permutation|0BQMWCNS8S]] of $\set{1, \dots, n}$.
Then
$$\sum_{i=1}^{n} x_i y_{n+1-i} \le \sum_{i=1}^{n} x_i y_{\sigma(i)} \le \sum_{i=1}^{n} x_i y_i.$$

## Remarks

Proof idea: suppose $i < j$ but $y_{\sigma(i)} > y_{\sigma(j)}$.
Swapping the two values changes the sum by $(x_j - x_i)(y_{\sigma(i)} - y_{\sigma(j)}) \ge 0$.
Repeated swaps sort $\sigma$ into the identity without decreasing the sum, which gives the upper bound.
The lower bound follows by applying the upper bound to $-y_n \le \dots \le -y_1$.

Example: with $x = (1, 2, 3)$ and $y = (4, 5, 6)$, the sums range from $1 \cdot 6 + 2 \cdot 5 + 3 \cdot 4 = 28$ to $1 \cdot 4 + 2 \cdot 5 + 3 \cdot 6 = 32$.

Mathlib states a form as `Monovary.sum_smul_comp_perm_le_sum_smul`.

## Explanations

### L1 human

You have $n$ boxes of banknotes and may take some number of notes from each box, with the counts given in advance.
To get the most money, take the most notes from the box with the largest bills.
To get the least, take the most notes from the box with the smallest bills.
The rearrangement inequality says exactly this: matching large with large maximises a sum of products.

### L2 human

The rearrangement inequality gives quick proofs of several classical inequalities.
Averaging it over the cyclic shifts of $y$ gives [[Chebyshev's sum inequality|S8X2N1DW8P]].
Applied to suitable sequences it also gives the [[AM–GM inequality|0DRF0F3XC9]] and the [[Cauchy–Schwarz inequality|0RFWW56Y22]] in special cases.
