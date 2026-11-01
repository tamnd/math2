---
tag: XMHQCDWZW1
kind: statement
role: theorem
name: AKS primality test
msc: [11Y11, 11A51, 68Q25]
uses: [01826KMG2H, 02RRHJ7R98, 0DAMHCT17R, 0SDC934R52, 0076HWHGHQ, 0M25PRN3WQ, 0396VGFA78, 0SZCSYHW60]
about: [0EGJZHZ02C, 01826KMG2H]
sources:
  - url: https://en.wikipedia.org/wiki/AKS_primality_test
same_as:
  wikidata: Q294284
  wikipedia: AKS primality test
---

## Statement

Let $n \ge 2$ be an integer and let $r \ge 2$ be an integer.
Assume that $n$ has no [[prime|01826KMG2H]] factor $p \le r$.
Then $\gcd(n, r) = 1$, so the [[multiplicative order|02RRHJ7R98]] $\ord_r(n)$ of $n$ modulo $r$ is defined.
Assume also that $\ord_r(n) > (\log_2 n)^2$.
Let $\varphi$ be [[Euler's totient function|0DAMHCT17R]] and let $\ell = \floor{\sqrt{\varphi(r)} \log_2 n}$.
Then the following hold.

1. The integer $n$ is prime if and only if $n$ is not a perfect power and
$$(X + a)^n \equiv X^n + a \pmod{X^r - 1,\ n}$$
for every integer $a$ with $1 \le a \le \ell$.
Here the congruence is an equality in the [[quotient ring|0076HWHGHQ]] $\Z[X]/(X^r - 1, n)$ of the [[polynomial ring|0SDC934R52]] $\Z[X]$.
A perfect power is an integer $m^k$ with integers $m, k \ge 2$.
2. For every $n \ge 2$ there is an integer $r \le \max\set{3, \ceil{(\log_2 n)^5}}$ with $\ord_r(n) > (\log_2 n)^2$ or $\gcd(n, r) > 1$.
3. Hence a deterministic algorithm decides whether $n$ is prime with a number of bit operations polynomial in $\log n$.

## Remarks

The algorithm is due to Manindra Agrawal, Neeraj Kayal and Nitin Saxena, in the paper "PRIMES is in P".
It starts from a simple fact: for $\gcd(a, n) = 1$, the integer $n$ is prime if and only if $(X + a)^n \equiv X^n + a \pmod n$ in $\Z[X]$.
The direct check of this identity costs about $n$ operations, so the test reduces it modulo $X^r - 1$ for a small $r$.
If $n$ is composite with a prime factor $p$, the congruences for all $a \le \ell$ give a group of polynomials modulo $p$.
This group is forced to be both small and large at once, unless $n$ is a power of $p$.
The algorithm finds the smallest suitable $r$, checks $\gcd(a, n)$ for $a \le r$, tests for perfect powers, and then checks the $\ell$ congruences.

For $n$ prime, part 1 holds by [[Fermat's little theorem|0M25PRN3WQ]] and the [[freshman's dream|0396VGFA78]] $(X + a)^p = X^p + a^p$ in characteristic $p$.
The test needs no unproved hypothesis and is never wrong, unlike the [[Miller–Rabin primality test|0SZCSYHW60]], which is randomised.

## Explanations

### L1 human

The AKS test decides whether a whole number is prime, and it is always right.
Its running time grows only like a power of the number of digits of $n$, not like $n$ itself.
Before it, no known test was at the same time deterministic, free of unproved conjectures and polynomial in the number of digits.
It answered the old question whether primality can be decided in polynomial time.

### L2 human

The test turns the binomial identity $(X + a)^p = X^p + a$ modulo $p$ into a criterion that is cheap to check.
The working ring $\Z[X]/(X^r - 1, n)$ has elements of size about $r \log n$ bits, and $r$ is polynomial in $\log n$ by part 2.
The proof uses only elementary algebra of finite fields and cyclotomic polynomials, together with a bound on the least common multiple of $1, \ldots, m$.
In practice the test is slower than the [[Miller–Rabin primality test|0SZCSYHW60]] or elliptic curve methods, so its importance is mainly theoretical.
It is a [[primality test|0EGJZHZ02C]], and it does not find factors; the [[integer factorization|YPE65X5HJ4]] problem is believed to be much harder.
