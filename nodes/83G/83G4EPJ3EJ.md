---
tag: 83G4EPJ3EJ
kind: statement
role: theorem
name: Shor's algorithm
msc: [68Q12, 81P68, 11Y05]
uses: [VP21SFE7ZA, YPE65X5HJ4, 0WE2NHZJ7B]
about: [YPE65X5HJ4, VP21SFE7ZA]
sources:
  - url: https://en.wikipedia.org/wiki/Shor%27s_algorithm
same_as:
  wikidata: Q940334
  wikipedia: Shor's algorithm
---

## Statement

There is a quantum algorithm with the following property.
Given an integer $N \ge 2$ with $n$ binary digits, it outputs the prime factorization of $N$ with probability at least $2/3$.
Its running time is bounded by a polynomial in $n$.

In particular, the decision version of [[integer factorization|YPE65X5HJ4]] lies in [[BQP|VP21SFE7ZA]].

## Remarks

The algorithm reduces factoring to order finding.
For an odd $N$ that is not a prime power, pick a random $a$ with $\gcd(a, N) = 1$ and let $r$ be the [[order|0WE2NHZJ7B]] of $a$ modulo $N$.
With probability at least $1/2$, $r$ is even and $a^{r/2} \not\equiv -1 \pmod N$, and then $\gcd(a^{r/2} - 1, N)$ is a nontrivial factor of $N$.
The quantum part finds $r$: it prepares a superposition over exponents $x$, computes $a^x \bmod N$, applies the quantum Fourier transform, and measures.
The exponents range over $0 \le x < 2^m$ with $N^2 \le 2^m < 2N^2$.
The measured value is close to a multiple of $2^{m}/r$, and $r$ is recovered from it with continued fractions.

Example: for $N = 15$ and $a = 7$, the powers of $7$ modulo $15$ are $7, 4, 13, 1$, so $r = 4$.
Then $7^2 = 49$ and $\gcd(48, 15) = 3$, $\gcd(50, 15) = 5$, which gives $15 = 3 \cdot 5$.

With schoolbook arithmetic the algorithm uses $O(n^3)$ gates, the cost being dominated by modular exponentiation.
The same method computes discrete logarithms in polynomial time.

## Explanations

### L1 human

Multiplying two large primes is easy, but recovering them from their product seems very hard for ordinary computers.
The security of RSA encryption relies on this difficulty.
Peter Shor showed in 1994 that a quantum computer could factor numbers quickly.
It finds the period of a repeating sequence of remainders, using interference between many computations at once.

### L2 human

The classical part is elementary number theory: a period of $a^x \bmod N$ gives a square root of $1$ modulo $N$, and a nontrivial square root of $1$ yields a factor.
The quantum Fourier transform is the quantum version of the discrete Fourier transform, and it turns periodicity into peaks of probability.
The method generalizes to the hidden subgroup problem for finite abelian groups.
It breaks RSA, Diffie–Hellman and elliptic curve cryptography, which motivates post-quantum cryptography.
