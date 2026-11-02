---
tag: FZ6KV2J5C9
kind: definition
name: Matched Z-transform method
msc: [93C62, 44A55, 94A12]
defines: C45NVCD39K
uses: [066E7PJCYE, 00GC8ZQP4Q, 5FY0JQGHYZ]
sources:
  - url: https://en.wikipedia.org/wiki/Matched_Z-transform_method
---

## Definition

Let $T > 0$ be a sampling period.
Let $H$ be a rational function of $s$ with nonzero leading constant $c$, [[zeros|00GC8ZQP4Q]] $q_1, \ldots, q_M$ and [[poles|066E7PJCYE]] $p_1, \ldots, p_N$, listed with multiplicity:
$$H(s) = c \, \frac{\prod_{i=1}^{M} (s - q_i)}{\prod_{j=1}^{N} (s - p_j)}.$$
The *matched Z-transform* of $H$ is the following rational function of $z$.
$$H_d(z) = k \, \frac{\prod_{i=1}^{M} (1 - e^{q_i T} z^{-1})}{\prod_{j=1}^{N} (1 - e^{p_j T} z^{-1})}.$$
The constant $k$ is chosen so that $H_d$ and $H$ agree at a chosen reference point.
The usual choice is $H_d(1) = H(0)$ when $H(0)$ is finite and nonzero.

## Remarks

Example: $H(s) = a/(s + a)$ with $a > 0$ has one pole $-a$ and $H(0) = 1$.
Its matched transform is $H_d(z) = k/(1 - e^{-aT} z^{-1})$, and $H_d(1) = 1$ gives $k = 1 - e^{-aT}$.
Non-example: $H(s) = e^{-s}$, a pure delay, is not a rational function, so the method does not apply to it as stated.
A pole $p$ with $\operatorname{Re} p < 0$ goes to $e^{pT}$ with $\abs{e^{pT}} < 1$, so a stable continuous filter gives a stable discrete one.
The map $a \mapsto e^{aT}$ is the relation $z = e^{sT}$ between the [[Z-transform|5FY0JQGHYZ]] of samples and the Laplace transform.
Some versions add zeros at $z = -1$ for the zeros of $H$ at infinity when $N > M$.
