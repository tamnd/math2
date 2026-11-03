---
tag: GYTX4BNRA5
kind: definition
name: Uniquely decodable code
msc: [94A45, 68P30]
defines: MWBRNBXW1Y
uses: [BACPE6MVPZ, 1P6EP01HZF, RABRP2KG81]
sources:
  - url: https://en.wikipedia.org/wiki/Variable-length_encoding
---

## Definition

Let $\Sigma$ be a finite [[alphabet|RABRP2KG81]] and let $\Sigma^*$ be the set of finite [[strings|1P6EP01HZF]] over $\Sigma$.
Let $C \subseteq \Sigma^*$ be a [[variable-length code|BACPE6MVPZ]] whose codewords are non-empty.
The code $C$ is *uniquely decodable* if, for all codewords $c_1, \dots, c_m$ and $c'_1, \dots, c'_k$ in $C$,
$$c_1 c_2 \cdots c_m = c'_1 c'_2 \cdots c'_k$$
implies $m = k$ and $c_i = c'_i$ for every $i$.

## Remarks

Equivalently, the monoid homomorphism from the free monoid on the set $C$ to $\Sigma^*$ that sends each generator $c$ to the string $c$ is injective.
Example: $C = \set{0, 01, 11}$ is uniquely decodable.
Reversing all codewords gives $\set{0, 10, 11}$, in which no word is a prefix of another.
So a concatenation of codewords of $C$ splits uniquely when read from the right end.
Non-example: $C = \set{0, 1, 01}$ is not uniquely decodable, since $0 \cdot 1 = 01$ gives two different factorizations of the same string.
For a finite code, the Sardinas–Patterson algorithm decides whether the code is uniquely decodable.
