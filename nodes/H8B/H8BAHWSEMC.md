---
tag: H8BAHWSEMC
kind: statement
role: theorem
name: Green–Tao theorem
msc: [11N13, 11B25, 11B30]
uses: [01826KMG2H]
about: [01826KMG2H, B23B0QEMN5]
sources:
  - url: https://en.wikipedia.org/wiki/Green%E2%80%93Tao_theorem
same_as:
  wikidata: Q922012
  wikipedia: Green–Tao theorem
---

## Statement

For every integer $k \ge 1$, there are positive integers $a$ and $d$ such that the $k$ numbers $a, a + d, a + 2d, \dots, a + (k-1)d$ are all [[prime numbers|01826KMG2H]].

## Remarks

Green and Tao proved more: every subset $A$ of the set $\mathcal{P}$ of primes with
$$\limsup_{N \to \infty} \frac{\abs{A \cap \set{1, \dots, N}}}{\abs{\mathcal{P} \cap \set{1, \dots, N}}} > 0$$
contains arithmetic progressions of every length.
[[Szemerédi's theorem|B23B0QEMN5]] does not apply directly, because the primes have density zero by the [[prime number theorem|0EHBY5Y84N]].
The proof is a transference principle.
A relative Szemerédi theorem holds for dense subsets of a pseudorandom set.
The primes sit densely inside such a set, built from sieve weights of Goldston and Yıldırım.
For example, $5, 11, 17, 23, 29$ is a progression of five primes with difference $6$.
The primes contain no infinite arithmetic progression: for $a \ge 2$ the term $a + ad = a(1 + d)$ is composite, and for $a = 1$ the first term is not prime.

## Explanations

### L1 human

You can find evenly spaced prime numbers in long rows, as long as you like.
For example, $3, 5, 7$ is a row of three and $5, 11, 17, 23, 29$ is a row of five.
The theorem says rows of every length exist, even though primes get rarer.

### L2 human

The Green–Tao theorem combines [[additive combinatorics|3NM362A2JG]] with analytic number theory.
Its idea is that Szemerédi's theorem survives inside sparse but random-looking sets.
It is a special case of the open [[Erdős conjecture on arithmetic progressions|FN978TDX67]], since the sum of the reciprocals of the primes diverges.
