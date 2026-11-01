---
tag: C01Z9QRGZY
kind: statement
role: theorem
name: Vinogradov's theorem
msc: [11P32, 11P55]
uses: [01826KMG2H, ZQFBEX62D0, XEPW251A97, WE0RQTR68H]
about: [063JNBSMJ0]
sources:
  - url: https://en.wikipedia.org/wiki/Vinogradov's_theorem
same_as:
  wikidata: Q1694565
  wikipedia: Vinogradov's theorem
---

## Statement

There is an integer $N_0$ such that every odd integer $N > N_0$ is a sum of three [[prime numbers|01826KMG2H]].

## Remarks

Vinogradov proved the theorem in 1937 by the [[Hardy–Littlewood circle method|ZQFBEX62D0]].
The proof gives an asymptotic formula: for every $A > 0$,
$$\sum_{p_1 + p_2 + p_3 = N} \log p_1 \log p_2 \log p_3 = \tfrac12 \mathfrak{S}(N) N^2 + O\!\left(\frac{N^2}{(\log N)^{A}}\right),$$
where
$$\mathfrak{S}(N) = \prod_{p \mid N} \left(1 - \frac{1}{(p-1)^2}\right) \prod_{p \nmid N} \left(1 + \frac{1}{(p-1)^3}\right).$$
For odd $N$ the singular series satisfies $\mathfrak{S}(N) > 0.6$, so the main term dominates for large $N$; for even $N$ the factor at $p = 2$ is $0$.
The major arcs are handled by the [[Siegel–Walfisz theorem|XEPW251A97]], and the new step was Vinogradov's bound for the exponential sum $\sum_{p \le N} \log p \; e(p\alpha)$ on the minor arcs.
The first proof gave no explicit $N_0$, because the Siegel–Walfisz constants are ineffective; later proofs made $N_0$ explicit.
In 2013 Harald Helfgott proved that every odd integer greater than $5$ is a sum of three primes.

## Explanations

### L1 human

The weak Goldbach conjecture says that every odd number greater than $5$ is a sum of three primes, as in $21 = 3 + 7 + 11$.
Vinogradov proved this for all odd numbers beyond some huge bound.
His method also counts, approximately, how many ways there are to do it.

### L2 human

The theorem is the model application of the circle method to primes.
The case of three primes works because the minor arcs can be bounded with one factor estimated pointwise and the other two in mean square, using Parseval's identity.
For two primes, which is [[Goldbach's conjecture|063JNBSMJ0]], this argument fails: the mean square alone is as large as the expected main term.
The strongest results towards Goldbach's conjecture by other means are sieve results such as [[Chen's theorem|WE0RQTR68H]].
