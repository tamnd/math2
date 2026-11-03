---
tag: FM4SW5DB8T
kind: example
name: Justesen code
msc: [94B65, 94B60]
instance_of: [ECFMHV9A8W]
uses: [5VBWJ7EFTX, M2X88AXM17, GW25TGD33J, 0ZXZ82FTX2]
sources:
  - url: https://en.wikipedia.org/wiki/Justesen_code
same_as:
  wikidata: Q13640215
  wikipedia: Justesen code
---

## Example

Let $m \ge 1$, $N = 2^m - 1$ and $1 \le K \le N$, and let $\alpha_1, \dots, \alpha_N$ be the nonzero elements of $\F_{2^m}$.
The outer code is the [[Reed–Solomon code|5VBWJ7EFTX]] of length $N$ and dimension $K$ over $\F_{2^m}$ with evaluation points $\alpha_1, \dots, \alpha_N$.
For position $i$, the inner code maps $x \in \F_{2^m}$ to $(x, \alpha_i x) \in \F_{2^m}^2$, identified with a word of $2m$ bits.
The *Justesen code* is the binary code
$$\set{\big((c_1, \alpha_1 c_1), \dots, (c_N, \alpha_N c_N)\big) : (c_1, \dots, c_N) \text{ in the outer code}},$$
of length $2mN$ and dimension $mK$, so of rate $R = K/(2N)$.
It is a [[concatenated code|ECFMHV9A8W]] in the extended sense where the inner code changes with the position.

The inner codes $x \mapsto (x, \alpha x)$, for $\alpha \ne 0$, form the Wozencraft ensemble.
A nonzero word $(x, y)$ lies in at most one of them, namely for $\alpha = y/x$ when $x, y \ne 0$.
So at most a small fraction of them can have a low-weight nonzero word.
A nonzero outer codeword has at least $N - K + 1$ nonzero symbols, which use distinct inner codes.
Most of these give inner words of weight at least roughly $2m H^{-1}(1/2)$, where $H$ is the [[binary entropy function|GW25TGD33J]].
This gives, for a fixed $0 < R < 1/2$ and $m \to \infty$, a relative [[minimum distance|M2X88AXM17]] at least $(1 - 2R) H^{-1}(1/2) - o(1)$.

## Explanations

### L1 human

A good inner code is easy to find by brute force when it is short, but then the outer code must handle long blocks.
Justesen's trick is to use a different simple inner code at each position, so that almost all of them are good, without searching for any.
The result is an explicit family of binary codes whose rate and relative distance both stay bounded away from zero as the length grows, an asymptotically good family.
