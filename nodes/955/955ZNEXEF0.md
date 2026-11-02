---
tag: 955ZNEXEF0
kind: definition
name: Subnormal number
msc: [65G50, 65Y04]
defines: DHXXSN12JC
uses: [RTKRSC3KPH]
sources:
  - url: https://en.wikipedia.org/wiki/Subnormal_number
---

## Definition

Consider a [[floating-point|RTKRSC3KPH]] system with base $\beta$, precision $p$ and minimal exponent $e_{\min}$.
The smallest positive normalized number is $\beta^{e_{\min}}$.
A *subnormal number* of the system is a real number
$$x = \pm\, (0 . d_1 d_2 \ldots d_{p-1})_\beta \times \beta^{e_{\min}},$$
where the digits $d_i$ are integers in $\set{0, \ldots, \beta - 1}$, not all zero.
Equivalently, $x = \pm k \, \beta^{e_{\min} - p + 1}$ with $k$ an integer and $1 \le k \le \beta^{p-1} - 1$.

## Remarks

Example: in IEEE binary64, $\beta = 2$, $p = 53$ and $e_{\min} = -1022$, so the subnormal numbers are $\pm k \, 2^{-1074}$ with $1 \le k \le 2^{52} - 1$; the smallest is $2^{-1074} \approx 4.9 \times 10^{-324}$.
Non-example: $2^{-1022}$ is not subnormal in binary64; it is the smallest positive normalized number, with leading digit $1$.
All subnormal numbers are multiples of the same spacing $\beta^{e_{\min} - p + 1}$, which is also the spacing of the normalized numbers in $[\beta^{e_{\min}}, \beta^{e_{\min}+1})$.
A subnormal number has fewer than $p$ significant digits, so the relative rounding error in the subnormal range can exceed the unit roundoff.
Other names are *denormal* and *denormalized* numbers.
