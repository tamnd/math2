---
tag: ZGGFKNFPCS
kind: definition
name: Turbo code
msc: [94B60, 94B35, 94B10]
defines: SGRYABP8D0
uses: [JCFC831VS2, 05RWFKVTJ7]
sources:
  - url: https://en.wikipedia.org/wiki/Turbo_code
---

## Definition

Let $K \ge 1$, and let $\pi$ be a [[permutation|05RWFKVTJ7]] of $\set{1, \dots, K}$, the interleaver.
Let $E_1$ and $E_2$ be recursive systematic rate $1/2$ binary [[convolutional encoders|JCFC831VS2]].
This means that $E_j$ has a generator matrix $(1, \ p_j(D)/r_j(D))$ with $p_j, r_j \in \F_2[D]$ and $r_j(0) = 1$.
Write $P_j(v) \in \F_2^K$ for the first $K$ parity bits that $E_j$ produces from an input $v \in \F_2^K$.
The *turbo code* with these components maps a message $u \in \F_2^K$ to the codeword
$$\big(u, \ P_1(u), \ P_2(u_\pi)\big) \in \F_2^{3K}, \quad \text{where } u_\pi = (u_{\pi(1)}, \dots, u_{\pi(K)}).$$

## Remarks

The rate is $1/3$; higher rates are obtained by puncturing, that is, by not sending some parity bits.
The map is $\F_2$-linear, so the turbo code is a binary linear block code of length $3K$ and dimension $K$.
In practice the encoders are often driven back to the zero state by a few extra tail bits.
Decoding alternates two BCJR decoders that exchange extrinsic log-likelihood ratios through $\pi$ and $\pi^{-1}$.

Example: $E_1 = E_2$ with generator $(1, (1 + D^2)/(1 + D + D^2))$.
The parity bits $p_t$ of input $v$ satisfy $p_t + p_{t-1} + p_{t-2} = v_t + v_{t-2}$, with $p_t = v_t = 0$ for $t < 1$.
For $K = 3$, $u = (1, 0, 0)$ and $\pi$ the cyclic shift with $u_\pi = (0, 0, 1)$, one gets $P_1(u) = (1, 1, 1)$ and $P_2(u_\pi) = (0, 0, 1)$, so the codeword is $(1, 0, 0, 1, 1, 1, 0, 0, 1)$.

Non-example: the pair $(u, P_1(u))$ alone is the codeword of a single recursive convolutional code; it lacks the second, interleaved parity stream, so it is not a turbo code.
