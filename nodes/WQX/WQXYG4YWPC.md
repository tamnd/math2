---
tag: WQXYG4YWPC
kind: concept
name: Rijndael MixColumns
aliases: [rijndael-mix-column, rijndael-mix-columns]
sources:
  - wikipedia: en:2105621@r1354370362
    locator: Rijndael MixColumns
    note: adopted
    mention: wikipedia://en/2105621
    sections: [Summary]
same_as:
  wikidata: Q2152944
  wikipedia: Rijndael MixColumns
inventory: [SXTDPPJ6MQ]
---

## Summary

The **MixColumns** operation performed by the Rijndael cipher or Advanced Encryption Standard is, along with the ShiftRows step, its primary source of diffusion. Each column of bytes is treated as a four-term polynomial $b(x) = b_3 x^3 + b_2 x^2 + b_1 x + b_0$, each byte representing an element in the Galois field $\operatorname{GF}(2^8)$. The coefficients are elements within the prime [[sub-field|0EQWVHF3W5]] $\operatorname{GF}(2)$.
