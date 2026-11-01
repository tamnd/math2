---
tag: B3JMY54GJF
kind: statement
role: theorem
name: Bombieri–Vinogradov theorem
msc: [11N13, 11N36]
uses: [B8AKSVBE5Z, 0NK8JTE1NN, 0DAMHCT17R, N15YK7XG1H, XEPW251A97]
about: [0GNVN3CA2P, DNKA4WBKDS]
sources:
  - url: https://en.wikipedia.org/wiki/Bombieri–Vinogradov_theorem
same_as:
  wikidata: Q2612539
  wikipedia: Bombieri–Vinogradov theorem
---

## Statement

Let $q \ge 1$ and $a$ be integers, and let $y \ge 2$ be real.
Let $\psi(y; q, a)$ be the sum of the [[von Mangoldt function|0NK8JTE1NN]] $\Lambda(n)$ over $n \le y$ with $n \equiv a \pmod q$.
Let $\varphi$ be [[Euler's totient function|0DAMHCT17R]].
For every $A > 0$ there is $B = B(A) > 0$ such that, for all $x \ge 2$ and $Q = x^{1/2} (\log x)^{-B}$,
$$\sum_{q \le Q} \; \max_{\gcd(a, q) = 1} \; \max_{2 \le y \le x} \left| \psi(y; q, a) - \frac{y}{\varphi(q)} \right| \le C_A \frac{x}{(\log x)^{A}},$$
where $C_A$ depends only on $A$.

## Remarks

The proof combines the [[large sieve|N15YK7XG1H]] inequality for Dirichlet characters with a decomposition of $\Lambda$ into bilinear sums, such as Vaughan's identity; small moduli are handled by the [[Siegel–Walfisz theorem|XEPW251A97]].
The [[generalized Riemann hypothesis|DNKA4WBKDS]] would give $\abs{\psi(y; q, a) - y/\varphi(q)} \le C\, y^{1/2} (\log y)^2$ for each $q \le y$, which yields the same bound for $Q$ up to about $x^{1/2} (\log x)^{-A-2}$.
So the theorem says that GRH holds "on average over moduli" up to $\sqrt{x}$.
One says that the primes have level of distribution $1/2$.
The Elliott–Halberstam conjecture states that the same bound holds with $Q = x^{\theta}$ for every $\theta < 1$.

## Explanations

### L1 human

Primes are expected to split evenly among the residue classes modulo $q$ that they can reach.
For a single large $q$ nobody can prove a good error bound.
This theorem proves that, for almost all $q$ up to about $\sqrt{x}$, the error is small, which is as good as what the generalized Riemann hypothesis would give on average.

### L2 human

The Bombieri–Vinogradov theorem is the usual replacement for GRH in sieve theory.
It controls the remainder terms of a sieve applied to the primes, as in the proof of [[Chen's theorem|WE0RQTR68H]].
It is also the main input of the Goldston–Pintz–Yıldırım and Maynard methods for [[bounded gaps between primes|XMXFDWYYMD]].
Zhang's proof of bounded gaps needed a variant that goes slightly beyond the level $1/2$ for smooth moduli.
Compare with the [[Siegel–Walfisz theorem|XEPW251A97]], which is uniform in each single modulus but only for $q$ up to a power of $\log x$.
