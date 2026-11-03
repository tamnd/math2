---
tag: PKXX6NQQVA
kind: definition
name: Concatenated code
msc: [94B05, 94B60]
defines: ECFMHV9A8W
uses: [E85KREWV60, M2X88AXM17, 0ZXZ82FTX2]
sources:
  - url: https://en.wikipedia.org/wiki/Concatenated_error_correction_code
---

## Definition

Let $q$ be a prime power and $k \ge 1$, and fix an $\F_q$-linear bijection $\phi \colon \F_{q^k} \to \F_q^k$, given by a basis of $\F_{q^k}$ over $\F_q$.
Let $C_{\mathrm{out}}$ be a [[linear code|E85KREWV60]] over $\F_{q^k}$ with parameters $[N, K, D]$, the outer code.
Let $C_{\mathrm{in}}$ be a linear code over $\F_q$ with parameters $[n, k, d]$ and an injective linear encoding map $E \colon \F_q^k \to \F_q^n$ with image $C_{\mathrm{in}}$, the inner code.
The *concatenated code* $C_{\mathrm{out}} \circ C_{\mathrm{in}}$ is
$$\set{\big(E(\phi(c_1)), E(\phi(c_2)), \dots, E(\phi(c_N))\big) : (c_1, \dots, c_N) \in C_{\mathrm{out}}} \subseteq \F_q^{Nn}.$$

## Remarks

The concatenated code is a linear code over $\F_q$ of length $Nn$ and dimension $Kk$.
Its [[minimum distance|M2X88AXM17]] is at least $Dd$: a nonzero outer codeword has at least $D$ nonzero symbols, and each nonzero symbol gives an inner block of weight at least $d$.

Example: take $q = 2$, $k = 2$, the outer code the $[3, 1, 3]$ repetition code over $\F_4$, and the inner code the $[3, 2, 2]$ even-weight code over $\F_2$.
The concatenated code is a binary $[9, 2, \ge 6]$ code; for instance, the outer word $(a, a, a)$ with $\phi(a) = (1, 0)$ and $E(1, 0) = (1, 0, 1)$ gives $(1, 0, 1, 1, 0, 1, 1, 0, 1)$, of weight $6$.

Non-example: an outer code over $\F_8$ and an inner code of dimension $2$ over $\F_2$ do not concatenate, since an element of $\F_8$ corresponds to $3$ bits, not $2$.
Variants allow a different inner code for each outer position, as in [[Justesen codes|FM4SW5DB8T]].
