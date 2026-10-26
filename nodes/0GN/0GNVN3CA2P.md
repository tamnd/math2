---
tag: 0GNVN3CA2P
kind: statement
role: theorem
name: Dirichlet's theorem on arithmetic progressions
aliases: [dirichlet-prime-number-theorem]
msc: [11N13]
uses: [0SN0MAEKYX, 0GFKP8F8AG]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet%27s_theorem_on_arithmetic_progressions
    locator: lead section
same_as:
  wikidata: Q550402
  wikipedia: Dirichlet's theorem on arithmetic progressions
---

## Statement

Let $a$ and $d$ be positive integers that are [[coprime|0GFKP8F8AG]].
Then there are infinitely many [[prime numbers|0SN0MAEKYX]] of the form $a + n d$, with $n$ a natural number.
That is, there are infinitely many primes $p$ with $p \equiv a \pmod{d}$.

## Remarks

The hypothesis $\gcd(a, d) = 1$ is necessary. Each term of $a + n d$ is a multiple of $\gcd(a, d)$, so at most one term can be prime when $\gcd(a, d) > 1$.
For $d = 4$, the theorem gives infinitely many primes $p \equiv 1 \pmod 4$ and infinitely many primes $p \equiv 3 \pmod 4$.
A special case with an elementary proof is that there are [[infinitely many primes congruent to 1 modulo n|0T1BSD7H3M]].
The primes are in fact equally distributed among the $\varphi(d)$ possible classes, where $\varphi$ is [[Euler's totient function|0VV04M41AN]].

## History

Dirichlet proved the theorem in 1837. His proof introduced Dirichlet characters and Dirichlet $L$-functions.

## Explanations

### L1 human

The sequence $3, 7, 11, 15, 19, 23, \dots$ adds $4$ at each step. It contains infinitely many primes.
In general, a sequence $a, a + d, a + 2d, \dots$ contains infinitely many primes, unless $a$ and $d$ have a common factor that blocks them all.
