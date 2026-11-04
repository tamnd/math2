---
tag: N10HP9QWX7
kind: proof
name: Proof of the factorial formula for binomial coefficients by induction
msc: [05A10]
proves: 033KTKKRV6
uses: [092GEF38YD, 0WFCGVMRRC, 0YRG241HQQ]
methods: [0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/Binomial_coefficient
    locator: Factorial formula
---

## Proof

We use the recursive definition of the [[binomial coefficient|092GEF38YD]] and the [[factorial|0WFCGVMRRC]], and argue by induction on $n$. We prove the division-free form $k!\,(n-k)!\,\binom{n}{k} = n!$.

1. Lemma: for every natural number $n$, $\binom{n}{n} = 1$, and $\binom{n}{j} = 0$ for all $j > n$. We prove it by induction on $n$.
2. For $n = 0$, the definition gives $\binom{0}{0} = 1$ and $\binom{0}{j} = 0$ for $j \ge 1$.
3. Suppose the lemma holds for $n$. Let $j > n + 1$, and write $j = i + 1$ with $i > n$. By [[Pascal's rule|0YRG241HQQ]], $\binom{n+1}{i+1} = \binom{n}{i} + \binom{n}{i+1} = 0 + 0 = 0$.
4. Also $\binom{n+1}{n+1} = \binom{n}{n} + \binom{n}{n+1} = 1 + 0 = 1$. This proves the lemma.
5. Main claim: for every $n$ and every $k \le n$, $k!\,(n-k)!\,\binom{n}{k} = n!$. We argue by induction on $n$.
6. For $n = 0$, only $k = 0$ occurs, and $0!\,0!\,\binom{0}{0} = 1 = 0!$.
7. Suppose the claim holds for $n$, and let $k \le n + 1$. If $k = 0$, then $0!\,(n+1)!\,\binom{n+1}{0} = (n+1)!$, since $\binom{n+1}{0} = 1$.
8. If $k = n + 1$, then $(n+1)!\,0!\,\binom{n+1}{n+1} = (n+1)!$ by the lemma.
9. Otherwise $1 \le k \le n$. Write $k = j + 1$ with $0 \le j \le n - 1$. Then $n + 1 - k = n - j$, and Pascal's rule gives $\binom{n+1}{k} = \binom{n}{j} + \binom{n}{j+1}$.
10. For the first term, $(j+1)! = (j+1) \cdot j!$. By the induction hypothesis for $j$, $(j+1)!\,(n-j)!\,\binom{n}{j} = (j+1) \cdot n!$.
11. For the second term, $n - j \ge 1$, so $(n-j)! = (n-j) \cdot (n-j-1)!$. By the induction hypothesis for $j + 1 \le n$, $(j+1)!\,(n-j)!\,\binom{n}{j+1} = (n-j) \cdot n!$.
12. Adding steps 10 and 11 gives $k!\,(n+1-k)!\,\binom{n+1}{k} = (j + 1 + n - j) \cdot n! = (n+1) \cdot n! = (n+1)!$.
13. This completes the induction. So $k!\,(n-k)!\,\binom{n}{k} = n!$ whenever $k \le n$.
14. Every factorial is at least $1$, since $0! = 1$ and $(m+1)! = (m+1) \cdot m!$. So $k!\,(n-k)! \ne 0$.
15. Dividing by $k!\,(n-k)!$ gives $\binom{n}{k} = \dfrac{n!}{k!\,(n-k)!}$.

## Idea

Both sides obey the same recursion. Pascal's rule splits $\binom{n+1}{k}$ into two terms.
After multiplying by $k!\,(n+1-k)!$, the two terms become $k \cdot n!$ and $(n+1-k) \cdot n!$, and these add up to $(n+1)!$.
