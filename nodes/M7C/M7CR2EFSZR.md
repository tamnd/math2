---
tag: M7CR2EFSZR
kind: definition
name: Homomorphic encryption
msc: [94A60, 68P25]
defines: RPBJMCCYY9
uses: [01E9MNJYEX, K99S0Q0814, SQXNFGVADX, FXBNZNG7X3, 9K50KFCY6S]
sources:
  - url: https://en.wikipedia.org/wiki/Homomorphic_encryption
---

## Definition

Let $(\mathsf{Gen}, \mathsf{Enc}, \mathsf{Dec})$ be a [[public-key|01E9MNJYEX]] encryption scheme whose algorithms run in polynomial time in the security parameter $\lambda$.
Let $\mathcal{F}$ be a class of functions on messages.
The scheme is *homomorphic* for $\mathcal{F}$ if there is a [[probabilistic|K99S0Q0814]] polynomial-time algorithm $\mathsf{Eval}$ with the following property.
For each $(pk, sk)$ output by $\mathsf{Gen}(1^\lambda)$, each $f \in \mathcal{F}$ with $k$ arguments, and all messages $m_1, \dots, m_k$ with ciphertexts $c_i = \mathsf{Enc}(pk, m_i)$:
$$\mathsf{Dec}\big(sk, \mathsf{Eval}(pk, f, c_1, \dots, c_k)\big) = f(m_1, \dots, m_k).$$
The scheme is *fully homomorphic* if $\mathcal{F}$ contains all [[Boolean circuits|SQXNFGVADX]] on bits.
It must then also be compact: the length of the output of $\mathsf{Eval}$ is bounded by a polynomial in $\lambda$ alone.

## Remarks

Example: [[ElGamal encryption|FXBNZNG7X3]] is homomorphic for the class of products $f(m_1, m_2) = m_1 m_2$.
Let $\mathsf{Eval}$ multiply coordinatewise: $(g^{y_1}, m_1 h^{y_1}) \cdot (g^{y_2}, m_2 h^{y_2}) = (g^{y_1 + y_2}, m_1 m_2 h^{y_1 + y_2})$.
This is an encryption of $m_1 m_2$ with randomness $y_1 + y_2$, so decryption returns $m_1 m_2$.

Non-example: the trivial $\mathsf{Eval}$ that outputs $(f, c_1, \dots, c_k)$ with a decryption that decrypts each $c_i$ and then applies $f$, satisfies the displayed equation for all circuits.
It is not fully homomorphic, because its output grows with the size of $f$, so it is not compact.

Most fully homomorphic schemes in use are [[lattice-based|9K50KFCY6S]].
Gentry's first scheme used bootstrapping, in which a scheme evaluates its own decryption circuit.
