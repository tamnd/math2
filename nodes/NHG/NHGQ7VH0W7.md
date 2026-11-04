---
tag: NHGQ7VH0W7
kind: proof
name: Proof of the hockey-stick identity by induction
msc: [05A19]
proves: 04JHQNNBFE
uses: [092GEF38YD, 0YRG241HQQ, 033KTKKRV6]
methods: [0ASJVEFA9J]
sources:
  - url: https://proofwiki.org/wiki/Rising_Sum_of_Binomial_Coefficients
---

## Proof

Fix $r$. We argue by induction on $n \ge r$.

1. Let $n = r$. The left side is the single term $\binom{r}{r}$.
2. By the [[factorial formula|033KTKKRV6]], $\binom{r}{r} = \frac{r!}{r!\,0!} = 1$ and $\binom{r+1}{r+1} = 1$. So both sides equal $1$.
3. Suppose $\sum_{i=r}^{n} \binom{i}{r} = \binom{n+1}{r+1}$ for some $n \ge r$.
4. Then $\sum_{i=r}^{n+1} \binom{i}{r} = \binom{n+1}{r+1} + \binom{n+1}{r}$, by adding the term $i = n + 1$.
5. By [[Pascal's rule|0YRG241HQQ]] with $n + 1$ and $r$, $\binom{n+1}{r} + \binom{n+1}{r+1} = \binom{n+2}{r+1}$.
6. So $\sum_{i=r}^{n+1} \binom{i}{r} = \binom{(n+1)+1}{r+1}$. This completes the induction.

## Idea

Adding one more term to the diagonal sum adds $\binom{n+1}{r}$ to $\binom{n+1}{r+1}$.
Pascal's rule turns this pair into the next entry $\binom{n+2}{r+1}$, so the formula moves one row down.
