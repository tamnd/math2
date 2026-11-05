---
tag: ASN2MPH5V8
kind: statement
role: proposition
name: The Erdős–Turán–Koksma inequality
sources:
  - wikipedia: en:478601@r1369498188
    locator: Low-discrepancy sequence, section The Erdős–Turán–Koksma inequality
    note: adopted
    mention: wikipedia://en/478601#4XGH
    sections: [Statement]
inventory: [2GE5YTXFQV]
---

## Statement

It is computationally hard to find the exact value of the discrepancy of large point sets. The Erdős–Turán–Koksma inequality provides an upper bound.

Let $x_1,\ldots,x_N$ be points in $I^s$ and $H$ be an arbitrary positive integer. Then

$$D_{N}^{*}(x_1,\ldots,x_N)\leq \left(\frac{3}{2}\right)^s \left( \frac{2}{H+1}+ \sum_{0<\|h\|_{\infty}\leq H}\frac{1}{r(h)} \left| \frac{1}{N} \sum_{n=1}^{N} e^{2\pi i\langle h,x_n\rangle} \right| \right)$$

where

$$r(h) = \prod_{i=1}^s\max\{1,|h_i|\}\quad\text{for}\quad h=(h_1,\ldots,h_s)\in\mathbb{Z}^s.$$
