---
tag: Z9C8ZPT1N2
kind: definition
name: McEliece cryptosystem
msc: [94A60, 94B05, 11T71]
defines: RF9TDRQ2P4
uses: [E85KREWV60, KJCJSAPV1P, K8ZHAQAK2B, 0VD9ZSWWJG, 01E9MNJYEX]
sources:
  - url: https://en.wikipedia.org/wiki/McEliece_cryptosystem
---

## Definition

Let $C$ be a binary [[linear code|E85KREWV60]] of length $n$ and dimension $k$ with a $k \times n$ generator [[matrix|0VD9ZSWWJG]] $G$ over $\F_2$.
Suppose $C$ has an efficient decoding algorithm that corrects every error vector of [[Hamming weight|K8ZHAQAK2B]] at most $t$.
The *McEliece cryptosystem* is the [[public-key|01E9MNJYEX]] scheme with the following algorithms.

1. Key generation: choose a uniformly random invertible $k \times k$ matrix $S$ and a uniformly random $n \times n$ permutation matrix $P$ over $\F_2$. The public key is $(\hat G, t)$ with $\hat G = S G P$; the private key is $(S, G, P)$ with the decoder of $C$.
2. Encryption of $m \in \F_2^k$: choose $e \in \F_2^n$ uniformly among the vectors of weight $t$, and output $c = m \hat G + e$.
3. Decryption of $c$: compute $c P^{-1}$, decode it in $C$ to a codeword $m' G$, and output $m = m' S^{-1}$.

In McEliece's original proposal, $C$ is a binary [[Goppa code|KJCJSAPV1P]] chosen at random.

## Remarks

Decryption is correct: $c P^{-1} = (m S) G + e P^{-1}$, and $e P^{-1}$ still has weight $t$, since $P$ only permutes coordinates.
So the decoder returns the codeword $(m S) G$, which gives $m' = m S$, and then $m' S^{-1} = m$.

Example: a toy instance uses the binary Hamming code of length $7$ and dimension $4$, which corrects $t = 1$ error.
A ciphertext is $m \hat G$ with one bit flipped, and decryption recovers $m$ as above; the instance is far too small to be secure.

Non-example: if the error $e$ had weight larger than $t$, clause 2 would fail, and the decoder might return a wrong codeword.
