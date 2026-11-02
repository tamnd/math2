---
tag: 3MDPTW005V
kind: definition
name: Linear congruential generator
msc: [65C10, 11K45]
defines: Q0K15AWV8H
uses: [C5FG6ARWVV, 03BR7SAX0Q, 03VFZ2WETT]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_congruential_generator
---

## Definition

Let $m \ge 2$ be an integer, the modulus, and let $a$, $c$ and $X_0$ be integers with $0 < a < m$, $0 \le c < m$ and $0 \le X_0 < m$.
The *linear congruential generator* with multiplier $a$, increment $c$ and seed $X_0$ is a [[pseudorandom number generator|C5FG6ARWVV]].
Its state space is $\set{0, \ldots, m-1}$ and its states are
$$X_{n+1} = (a X_n + c) \bmod m, \qquad n \ge 0,$$
where $\bmod$ is the [[modulo operation|03BR7SAX0Q]].
Its outputs are the numbers $u_n = X_n / m \in [0, 1)$.
If $c = 0$ it is called a *multiplicative* congruential generator, or Lehmer generator.

## Remarks

Example: $m = 8$, $a = 5$, $c = 1$, $X_0 = 0$.
The states are $0, 1, 6, 7, 4, 5, 2, 3, 0, \ldots$, for instance $5 \cdot 7 + 1 = 36 \equiv 4 \pmod 8$; all $8$ residues appear, so the period is $m$.
Non-example: $X_{n+1} = X_n^2 \bmod m$ is not a linear congruential generator, because the map $x \mapsto x^2$ is not of the form $x \mapsto ax + c$.
The map $x \mapsto ax + c$ is an affine map of the ring of [[integers modulo $m$|03VFZ2WETT]], so the period is at most $m$.
The Hull–Dobell theorem treats $c \ne 0$.
The period equals $m$ for every seed if and only if three conditions hold.
They are: $c$ and $m$ are coprime, every prime factor of $m$ divides $a - 1$, and $4$ divides $a - 1$ if $4$ divides $m$.
In the example, $\gcd(1, 8) = 1$ and $a - 1 = 4$, so the conditions hold.
