---
tag: PSNW0ZQ0E9
kind: definition
name: IEEE 754 standard
msc: [65Y04, 65G50]
defines: GNDWPYYFW4
uses: [RTKRSC3KPH, 5NPVX29Y0C, DHXXSN12JC]
sources:
  - url: https://en.wikipedia.org/wiki/IEEE_754
---

## Definition

The *IEEE 754 standard* is the technical standard for [[floating-point arithmetic|RTKRSC3KPH]] of the Institute of Electrical and Electronics Engineers.
Its main requirements are the following.

1. Formats: a format has a base $\beta \in \set{2, 10}$, a precision $p$ and an exponent range $[e_{\min}, e_{\max}]$ with $e_{\min} = 1 - e_{\max}$. The formats binary32 and binary64 have $(p, e_{\max}) = (24, 127)$ and $(53, 1023)$.
2. Special values: each format contains $+0$ and $-0$, $+\infty$ and $-\infty$, NaN ("not a number") values, and [[subnormal numbers|DHXXSN12JC]].
3. Encoding: a binary64 number has $1$ sign bit, $11$ bits of biased exponent (bias $1023$) and $52$ bits of fraction. The leading significand bit of a normalized number is implicit.
4. Correct rounding: the operations $+$, $-$, $\times$, $/$, square root and fused multiply-add must return the exact result [[rounded|5NPVX29Y0C]] by the current rounding mode.
5. Rounding modes: the default is round to nearest with ties to even. The other modes are ties away from zero and directed rounding toward $0$, $+\infty$ and $-\infty$.

## Remarks

Example: the decimal number $1$ in binary64 has sign bit $0$, biased exponent $0 + 1023 = 1023$ and fraction bits all $0$.
Non-example: an arithmetic that always computes $x + y$ by chopping the extra digits does not meet clause 4, since in the default mode the result must be rounded to nearest.
In binary64 the largest finite number is $(2 - 2^{-52}) \times 2^{1023} \approx 1.8 \times 10^{308}$, and the smallest positive normalized number is $2^{-1022}$.
An overflowing result is rounded to $\pm\infty$ under round to nearest, and an invalid operation such as $0/0$ or $\sqrt{-1}$ returns NaN.
