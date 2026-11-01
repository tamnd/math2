---
tag: B54HPY6C5Z
kind: statement
role: theorem
name: Carleman's inequality
msc: [26D15]
uses: [0CVVKY7GY2, 0DRF0F3XC9]
about: [0CVVKY7GY2]
sources:
  - url: https://en.wikipedia.org/wiki/Carleman%27s_inequality
same_as:
  wikidata: Q378741
  wikipedia: Carleman's inequality
---

## Statement

Let $a_1, a_2, \dots$ be nonnegative real numbers.
Then
$$\sum_{n=1}^{\infty} (a_1 a_2 \cdots a_n)^{1/n} \le e \sum_{n=1}^{\infty} a_n,$$
where both [[series|0CVVKY7GY2]] take values in $[0, \infty]$.

## Remarks

Proof idea: let $c_k = (k + 1)^k / k^{k-1}$, so that $c_1 c_2 \cdots c_n = (n + 1)^n$.
By the [[AM–GM inequality|0DRF0F3XC9]],
$$(a_1 \cdots a_n)^{1/n} = \frac{(c_1 a_1 \cdots c_n a_n)^{1/n}}{n + 1} \le \frac{1}{n(n+1)} \sum_{k=1}^{n} c_k a_k.$$
Summing over $n$ and using $\sum_{n \ge k} \frac{1}{n(n+1)} = \frac{1}{k}$ gives the bound $\sum_k (1 + 1/k)^k a_k$, and $(1 + 1/k)^k < e$.

The constant $e$ cannot be replaced by a smaller number.
If $0 < \sum a_n < \infty$, the inequality is strict.

## Explanations

### L1 human

Replace each term of a series of nonnegative numbers by the geometric mean of the terms up to it.
Carleman's inequality says the new series is at most $e$ times the old one.
In particular, if the old series converges, so does the new one.

### L2 human

Carleman's inequality is a limiting case of the discrete [[Hardy's inequality|S7A8YFGG8X]].
Apply Hardy's inequality to $a_n^{1/p}$ and let $p \to \infty$: the power means tend to geometric means, and $\big(\frac{p}{p-1}\big)^p \to e$.
The direct proof above shows how a well chosen weighting makes the AM–GM inequality sharp enough.
