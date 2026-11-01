---
tag: WE0RQTR68H
kind: statement
role: theorem
name: Chen's theorem
msc: [11P32, 11N36]
uses: [01826KMG2H, 0KXQKES075, B3JMY54GJF, M4G4RXASTY]
about: [063JNBSMJ0, 0FER36N8SB]
sources:
  - url: https://en.wikipedia.org/wiki/Chen's_theorem
same_as:
  wikidata: Q1317350
  wikipedia: Chen's theorem
---

## Statement

Call a positive integer a *$P_2$ number* if it is a [[prime|01826KMG2H]] or a product of two primes.
Equivalently, its [[number of prime factors counted with multiplicity|0KXQKES075]] is $1$ or $2$.

1. There is an integer $N_0$ such that every even integer $N > N_0$ can be written as $N = p + m$ with $p$ prime and $m$ a $P_2$ number.
2. There are infinitely many primes $p$ such that $p + 2$ is a $P_2$ number.

## Remarks

Both parts are due to Chen Jingrun.
The proof is a weighted sieve argument.
A lower bound sieve counts the $m = N - p$ with no small prime factor, and an upper bound sieve removes those with three or more prime factors.
The [[Bombieri–Vinogradov theorem|B3JMY54GJF]] controls the remainder terms on average over the moduli.
A switching argument, which counts the same configurations with the roles of the factors exchanged, is the key new step.
Example: $100 = 3 + 97 = 7 + 93$, where $97$ is prime and $93 = 3 \cdot 31$ is a $P_2$ number.
Part 1 is a weak form of [[Goldbach's conjecture|063JNBSMJ0]], and part 2 a weak form of the [[twin prime conjecture|0FER36N8SB]].

## Explanations

### L1 human

Goldbach's conjecture says that every even number larger than $2$ is a sum of two primes.
Chen proved the next best thing: every large even number is a prime plus a number that is either prime or the product of two primes.
In the same way, he proved that there are infinitely many primes $p$ for which $p + 2$ is "almost prime".

### L2 human

Sieve methods cannot by themselves separate numbers with an odd number of prime factors from those with an even number; this is the parity problem.
So a sieve can at best reach products of two primes, and Chen's theorem reaches exactly that limit.
Earlier sieve results of the same kind, starting with the [[Brun sieve|M4G4RXASTY]], allowed more prime factors on both sides.
