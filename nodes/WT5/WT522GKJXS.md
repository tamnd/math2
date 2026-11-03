---
tag: WT522GKJXS
kind: statement
role: lemma
name: Generalized binomial coefficient at minus one half
msc: [05A10]
uses: [092GEF38YD, 01WHD9T0V6]
sources:
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_genfunction_binom-app.ptx#L30
    locator: source/s_genfunction_binom-app.ptx:30
---

## Statement

For a real number $r$ and a natural number $k$, put $\binom{r}{k} = \frac{r(r-1)\cdots(r-k+1)}{k!}$. This extends the [[binomial coefficient|092GEF38YD]] to a real upper index.

Let $k$ be a natural number. Then
$$\binom{-1/2}{k} = (-1)^k \, \frac{1}{4^k} \binom{2k}{k},$$
where $\binom{2k}{k}$ is the [[central binomial coefficient|01WHD9T0V6]].

## Remarks

For $k = 0$ both sides equal $1$. For $k = 1$ both sides equal $-\tfrac12$. For $k = 2$ both sides equal $\tfrac38$.

The product $(-\tfrac12)(-\tfrac32)\cdots(-\tfrac{2k-1}{2})$ has $k$ negative factors. Its absolute value is $\frac{1\cdot 3\cdots(2k-1)}{2^k} = \frac{(2k)!}{4^k k!}$. Dividing by $k!$ gives $\binom{2k}{k}/4^k$.
