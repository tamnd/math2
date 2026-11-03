---
tag: S4JT06VQVZ
kind: definition
name: Semantic security
msc: [94A60, 68P25]
defines: F51ANJH2XM
uses: [K99S0Q0814, 01E9MNJYEX, ZH3TM0EVWQ]
sources:
  - url: https://en.wikipedia.org/wiki/Semantic_security
---

## Definition

Let $(\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$ be a [[public-key|01E9MNJYEX]] encryption scheme with security parameter $\lambda$, whose algorithms run in polynomial time.
The scheme is *semantically secure* if the following holds.
For each [[probabilistic|K99S0Q0814]] polynomial-time algorithm $A$ there is a probabilistic polynomial-time algorithm $S$ with this property.
Let $M$ be any distribution on messages of length $p(\lambda)$, samplable in polynomial time, and let $f, h$ be functions computable in polynomial time.
Let $m$ be drawn from $M$ and let $(pk, sk) = \mathsf{Gen}(1^\lambda)$.
Then
$$\Big| \Pr\big[A(1^\lambda, pk, \mathsf{Enc}(pk, m), h(m)) = f(m)\big] - \Pr\big[S(1^\lambda, h(m)) = f(m)\big] \Big|$$
is negligible in $\lambda$.
A function $\nu$ is negligible if $\nu(\lambda) < 1/q(\lambda)$ for every polynomial $q$ and all large $\lambda$.

## Remarks

The function $h$ is prior knowledge about $m$, and $f$ is the information that $A$ tries to learn.
The simulator $S$ sees no ciphertext, so the definition says that the ciphertext gives $A$ no real help.

A scheme is semantically secure if and only if it has [[indistinguishable encryptions|ZH3TM0EVWQ]] under chosen-plaintext attack.
So ElGamal encryption in a group where the decisional Diffie–Hellman assumption holds is semantically secure.

Non-example: a scheme with deterministic $\mathsf{Enc}$, such as textbook RSA, is not semantically secure.
Let $M$ be uniform on two fixed messages $m_0 \ne m_1$, let $h$ be constant, and let $f(m) = 1$ if $m = m_0$ and $0$ otherwise.
The algorithm $A$ that compares the ciphertext with $\mathsf{Enc}(pk, m_0)$ finds $f(m)$ always, while any $S$ is right with probability exactly $1/2$.
