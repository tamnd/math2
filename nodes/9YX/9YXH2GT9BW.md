---
tag: 9YXH2GT9BW
kind: definition
name: Quantum key distribution
msc: [81P94, 94A60]
defines: 31HDBNPAH4
uses: [10VZYJ4552, V1JTB52E8C, SQ3J7AVMKM, 2Q85WTJ07A, 769RHWS4WK]
sources:
  - url: https://en.wikipedia.org/wiki/Quantum_key_distribution
---

## Definition

A *quantum key distribution protocol* is a protocol between two parties, Alice and Bob.
They are linked by a [[quantum channel|10VZYJ4552]] and by an authenticated public classical channel.
Authenticated means that others can read its messages but cannot alter them.
A third party, Eve, may act arbitrarily on the quantum channel and may read the classical channel.
At the end the protocol either aborts or outputs bit strings $K_A$ to Alice and $K_B$ to Bob, of a fixed length $\ell$.
Let $p$ be the probability that the protocol does not abort.
Let $\rho_{K_A E}$ be the joint [[state|V1JTB52E8C]] of Alice's key and Eve's system, given no abort.
Let $\varepsilon \ge 0$.
The protocol is *$\varepsilon$-secure* if, for every strategy of Eve, the following two conditions hold.

1. Correctness: the probability that the protocol does not abort and $K_A \ne K_B$ is at most $\varepsilon$.
2. Secrecy: $p \cdot \frac12 \norm{\rho_{K_A E} - \omega_\ell \otimes \rho_E}_1 \le \varepsilon$.

Here $\rho_E$ is the [[partial trace|SQ3J7AVMKM]] of $\rho_{K_A E}$ over the key, and $\omega_\ell = 2^{-\ell} \sum_{k \in \set{0,1}^\ell} \lvert k \rangle \langle k \rvert$ is the uniform distribution on keys.

## Remarks

The secrecy clause says that the key is $\varepsilon$-close in [[trace distance|2Q85WTJ07A]] to a uniform key independent of Eve.
This form of security is composable: the key can be used in a later protocol, such as a one-time pad, at an added error of at most $\varepsilon$.

Example: in the BB84 protocol, Alice sends each bit in one of two [[mutually unbiased bases|769RHWS4WK]] of a qubit, chosen at random, and Bob measures in a random basis.
They keep the rounds where the bases agree, estimate the error rate on a sample, abort if it is too high, and then apply error correction and privacy amplification.
For every $\varepsilon > 0$, BB84 with suitable parameters is $\varepsilon$-secure.
The key length then depends on $\varepsilon$, on the number of rounds and on the observed error rate.

Non-example: a protocol that sends the key bits in a single fixed basis fails the secrecy clause.
Eve can measure each qubit in that basis, learn the bit, and resend it without causing any error.
