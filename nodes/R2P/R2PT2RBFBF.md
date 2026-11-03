---
tag: R2PT2RBFBF
kind: statement
role: proposition
name: Birthday attack
msc: [94A60, 60C05]
uses: [0NMWG2PHJ0, 02MY6WZXEQ, 0GQ938GDE0, XJ8F3NQMGN]
about: [XJ8F3NQMGN]
sources:
  - url: https://en.wikipedia.org/wiki/Birthday_attack
---

## Statement

Let $N \ge 1$ and $q \ge 2$ be integers.
Let $Y_1, \dots, Y_q$ be [[independent|0GQ938GDE0]] random variables, each [[uniform|02MY6WZXEQ]] on a set of $N$ elements.
Then the probability that $Y_i = Y_j$ for some $i < j$ is at least
$$1 - e^{-q(q-1)/(2N)}.$$
In particular, if $q(q-1) \ge 2N \ln 2$, a collision occurs with probability at least $1/2$.
Let $H$ be a [[hash function|XJ8F3NQMGN]] with $\ell$-bit digests whose values on random inputs are uniform.
Then about $2^{\ell/2}$ evaluations on random inputs find a collision with probability at least $1/2$.

## Remarks

The probability of no collision is $\prod_{i=1}^{q-1} (1 - i/N)$.
Each factor is at most $e^{-i/N}$, since $1 - x \le e^{-x}$, so the product is at most $e^{-q(q-1)/(2N)}$.
This is the computation of the [[birthday problem|0NMWG2PHJ0]]; with $N = 365$ and $q = 23$ the bound already exceeds $1/2$.
For a hash function whose values on random inputs are not uniform, collisions are only more likely, so the attack works for every hash function.
The attack needs no knowledge of $H$; storing and sorting the $q$ values finds the colliding pair.

## Explanations

### L1 human

Among $23$ people, two probably share a birthday, although there are $365$ days.
The same effect means that a hash function with $\ell$-bit outputs has a collision among only about $2^{\ell/2}$ random inputs, not $2^\ell$.
So a digest of $128$ bits gives only about $64$ bits of security against collisions.

### L2 human

The bound sets the length of digests in practice: collision resistance at level $2^{k}$ needs digests of at least $2k$ bits, which is why SHA-256 has $256$-bit digests.
It also limits other constructions, such as block ciphers with $n$-bit blocks in common modes of operation, which start to leak information after about $2^{n/2}$ blocks.
Memoryless variants, such as Pollard's rho method, find collisions in the same time with little storage, by iterating $H$ and detecting a cycle.
