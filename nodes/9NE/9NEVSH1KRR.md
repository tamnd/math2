---
tag: 9NEVSH1KRR
kind: definition
name: Feistel cipher
msc: [94A60, 68P25]
defines: JWVE27832R
uses: [7YNRCX56CM, 0EPAT51DXQ, 05RWFKVTJ7]
sources:
  - url: https://en.wikipedia.org/wiki/Feistel_cipher
---

## Definition

Let $n \ge 1$ and $r \ge 1$ be integers.
Let $F_1, \dots, F_r \colon \set{0,1}^n \to \set{0,1}^n$ be [[functions|0EPAT51DXQ]], the round functions; in a cipher, $F_i$ depends on the $i$-th round key.
Write $\oplus$ for addition modulo $2$ in each coordinate.
The *Feistel network* with round functions $F_1, \dots, F_r$ maps $(L_0, R_0) \in \set{0,1}^n \times \set{0,1}^n$ to $(L_r, R_r)$, where for $i = 1, \dots, r$:
$$L_i = R_{i-1}, \qquad R_i = L_{i-1} \oplus F_i(R_{i-1}).$$
A *Feistel cipher* is a block [[cryptosystem|7YNRCX56CM]] on $\set{0,1}^{2n}$ whose encryption functions are Feistel networks.

## Remarks

Every Feistel network is a [[permutation|05RWFKVTJ7]] of $\set{0,1}^{2n}$.
Its inverse undoes the rounds in reverse order with $R_{i-1} = L_i$ and $L_{i-1} = R_i \oplus F_i(L_i)$.

Example: $n = 1$, $r = 1$ and $F_1(x) = 1$ for both $x$.
The map is $(L, R) \mapsto (R, L \oplus 1)$, which sends $00, 01, 10, 11$ to $01, 11, 00, 10$, a bijection as claimed.

Non-example: the map $(L, R) \mapsto (R, F(R))$ is not a Feistel round, since the old left half is not added.
For a constant $F$ it sends $(0, R)$ and $(1, R)$ to the same output, so it is not invertible.

Many descriptions swap the two halves after the last round, so that decryption uses the same network with the round functions in reverse order.
