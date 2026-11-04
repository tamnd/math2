---
kind: statement
msc:
- 05A10
name: Half-integer binomial coefficient formula
role: lemma
sources:
- locator: source/s_recurrence_rubots.ptx:40
  url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_recurrence_rubots.ptx#L40
tag: 2WXZAJSBKV
uses:
- 01WHD9T0V6
- 0SJNCJCCQG
---

## Statement

For a real number $r$ and a natural number $k$, let $\binom{r}{k}$ be the generalized binomial coefficient $\frac{r(r-1)\cdots(r-k+1)}{k!}$, that is, the [[falling factorial|0SJNCJCCQG]] of $r$ of length $k$ divided by $k!$.

Let $k \ge 1$ be an integer. Then
$$\binom{1/2}{k} = \frac{(-1)^{k-1}}{k} \cdot \frac{\binom{2k-2}{k-1}}{2^{2k-1}}.$$

## Remarks

The number $\binom{2k-2}{k-1}$ is the $(k-1)$-th [[central binomial coefficient|01WHD9T0V6]].

Example: for $k = 1$ the right side is $\frac{1}{1} \cdot \frac{1}{2} = \frac{1}{2}$. For $k = 2$ it is $-\frac{1}{2} \cdot \frac{2}{8} = -\frac{1}{8}$. Both agree with the left side.
