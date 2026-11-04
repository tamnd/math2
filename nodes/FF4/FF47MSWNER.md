---
tag: FF47MSWNER
kind: proof
name: Proof of Vandermonde's identity by induction
msc: [05A19]
proves: 01JADB9VW5
uses: [092GEF38YD, 0YRG241HQQ]
methods: [0ASJVEFA9J]
sources:
  - url: https://courses.csail.mit.edu/6.042/past-devel/archive/spring00/archive/lectures/L16.pdf
    locator: Theorem 1.7
---

## Proof

We argue by induction on $n$. The claim for $n$ is that the identity holds for this $n$, every natural number $m$ and every natural number $r$.

1. Let $n = 0$. By the definition of the [[binomial coefficient|092GEF38YD]], $\binom{0}{0} = 1$ and $\binom{0}{j} = 0$ for $j \ge 1$.
2. So in $\sum_{k=0}^{r} \binom{m}{k} \binom{0}{r-k}$ only the term $k = r$ is nonzero. The sum equals $\binom{m}{r} = \binom{m+0}{r}$.
3. Suppose the claim holds for $n$. Fix $m$ and $r$. We prove $\binom{m+n+1}{r} = \sum_{k=0}^{r} \binom{m}{k} \binom{n+1}{r-k}$.
4. If $r = 0$, both sides equal $1$, because $\binom{a}{0} = 1$ for every $a$.
5. Otherwise $r = s + 1$ for a natural number $s$. By [[Pascal's rule|0YRG241HQQ]], $\binom{m+n+1}{s+1} = \binom{m+n}{s} + \binom{m+n}{s+1}$.
6. By the induction hypothesis for $n$, with $r = s$ and with $r = s + 1$, the left side is $L_1 + L_2$. Here $L_1 = \sum_{k=0}^{s} \binom{m}{k} \binom{n}{s-k}$ and $L_2 = \sum_{k=0}^{s+1} \binom{m}{k} \binom{n}{s+1-k}$.
7. In the right side $\sum_{k=0}^{s+1} \binom{m}{k} \binom{n+1}{s+1-k}$, the term $k = s + 1$ is $\binom{m}{s+1} \binom{n+1}{0} = \binom{m}{s+1} \binom{n}{0}$, since both coefficients $\binom{\cdot}{0}$ equal $1$.
8. For $k \le s$, write $s + 1 - k = (s - k) + 1$. Pascal's rule gives $\binom{n+1}{s+1-k} = \binom{n}{s-k} + \binom{n}{s+1-k}$.
9. So the right side equals $\sum_{k=0}^{s} \binom{m}{k} \binom{n}{s-k} + \sum_{k=0}^{s} \binom{m}{k} \binom{n}{s+1-k} + \binom{m}{s+1} \binom{n}{0}$.
10. The first sum is $L_1$. The last two parts together are $L_2$, whose term $k = s + 1$ is $\binom{m}{s+1} \binom{n}{0}$.
11. Hence the right side equals $L_1 + L_2$, which is the left side by step 6. This completes the induction.

## Idea

Pascal's rule splits every binomial coefficient with top entry $n + 1$ into two with top entry $n$.
Applying it on both sides reduces the identity for $n + 1$ to two instances of the identity for $n$.
The induction hypothesis must cover all $r$, because the step uses it for $r - 1$ and for $r$.
