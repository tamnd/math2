---
tag: 7ZGTPQBFHC
kind: definition
name: Ciphertext indistinguishability
msc: [94A60, 68P25]
defines: ZH3TM0EVWQ
uses: [K99S0Q0814, 01E9MNJYEX, MATWVFGKTD]
sources:
  - url: https://en.wikipedia.org/wiki/Ciphertext_indistinguishability
---

## Definition

Let $(\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$ be a [[public-key|01E9MNJYEX]] encryption scheme with security parameter $\lambda$, whose algorithms run in polynomial time.
For an adversary $A$, the IND-CPA game runs as follows.

1. $\mathsf{Gen}(1^\lambda)$ outputs $(pk, sk)$, and $A$ receives $pk$.
2. $A$ outputs two messages $m_0, m_1$ of the same length.
3. A bit $b$ is chosen uniformly, and $A$ receives $c = \mathsf{Enc}(pk, m_b)$.
4. $A$ outputs a bit $b'$.

The scheme has *indistinguishable encryptions under chosen-plaintext attack* (IND-CPA) if the following holds.
For each [[probabilistic|K99S0Q0814]] polynomial-time adversary $A$, the advantage $\abs{\Pr[b' = b] - 1/2}$ is negligible in $\lambda$.
A function $\nu$ is negligible if $\nu(\lambda) < 1/p(\lambda)$ for every polynomial $p$ and all large $\lambda$.

## Remarks

Example: in the symmetric setting with one challenge, the [[one-time pad|MATWVFGKTD]] of length $n$ gives every adversary advantage $0$.
There $A$ gets no key, and $c = m_b \oplus k$ with $k$ uniform is uniform on $\set{0,1}^n$ whatever $b$ is, so $c$ carries no information on $b$.

Non-example: no scheme with deterministic $\mathsf{Enc}$ is IND-CPA secure.
The adversary computes $\mathsf{Enc}(pk, m_0)$ itself and outputs $b' = 0$ exactly when it equals $c$, which gives $\Pr[b' = b] = 1$.

In IND-CCA1 the adversary may also query a decryption oracle before step 3, and in IND-CCA2 also after it, except on $c$ itself.
