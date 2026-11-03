---
tag: KJCJSAPV1P
kind: concept
name: Goppa code
msc: [94B05, 11T71]
specializes: [E85KREWV60]
sources:
  - url: https://en.wikipedia.org/wiki/Binary_Goppa_code
---

## Summary

A Goppa code is a [[linear code|E85KREWV60]] over $\F_q$ defined by a polynomial $g$ over an extension field $\F_{q^m}$.
Its positions are labelled by field elements that are not roots of $g$.
A word belongs to the code when a certain sum of simple fractions is zero modulo $g$.
If $g$ has degree $t$, the code has dimension at least $n - mt$ and distance at least $t + 1$.
Binary Goppa codes with a squarefree $g$ have distance at least $2t + 1$.
Binary Goppa codes are the codes of the [[McEliece cryptosystem|RF9TDRQ2P4]].

## Explanations

### L1 human

Each position $i$ of a codeword is tied to a field element $\alpha_i$.
A word $c$ is a codeword when the rational function $\sum_i c_i / (x - \alpha_i)$, reduced modulo $g$, vanishes.
This is a list of linear conditions on $c$, so the code is linear, and the conditions are strong enough to keep codewords far apart.
For example, over $\F_2$ with $g(x) = x^2 + x + 1$ and all $8$ elements of $\F_8$ as the $\alpha_i$, one gets a binary code of length $8$ with minimum distance at least $5$.
Without knowledge of $g$, a binary Goppa code is believed to be hard to tell apart from a random linear code, which is the reason for its use in cryptography.
