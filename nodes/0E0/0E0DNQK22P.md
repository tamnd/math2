---
tag: 0E0DNQK22P
kind: statement
role: theorem
name: Primitive root theorem
msc: [11A07]
uses: [0KM2CJ80G7, 04XGKK8WQW]
sources:
  - url: https://en.wikipedia.org/wiki/Primitive_root_modulo_n
    locator: Definition
---

## Statement

Let $n$ be an integer with $n \ge 2$.
There is a [[primitive root|0KM2CJ80G7]] modulo $n$ if and only if $n \in \{2, 4, p^k, 2p^k\}$.
Here $p$ is an odd prime and $k$ is a positive integer.

## Remarks

Equivalently, the group $(\mathbb{Z}/n\mathbb{Z})^\times$ is cyclic exactly for these $n$.
The case $n = p$ is the [[existence of primitive roots modulo a prime|04XGKK8WQW]].
For example, there are primitive roots modulo $9$, $18$ and $25$, but not modulo $8$, $12$ or $15$.

## History

Carl Friedrich Gauss gave the first proof.
He defined primitive roots in his Disquisitiones Arithmeticae of 1801.

## Explanations

### L1 human

Modulo $12$, the residues coprime to $12$ are $1, 5, 7, 11$, and each of them squares to $1$.
So no single residue generates all four, and there is no primitive root modulo $12$.
The theorem lists exactly the moduli for which a generator exists.
