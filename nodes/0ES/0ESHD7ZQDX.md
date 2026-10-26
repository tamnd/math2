---
tag: 0ESHD7ZQDX
kind: statement
role: proposition
name: Divisibility by 9
msc: [11A63]
uses: [0TPW25CBN6, 0J5VGJYYC3]
sources:
  - url: https://en.wikipedia.org/wiki/Divisibility_rule
    locator: Divisibility by 3 or 9
---

## Statement

Let $n$ be a natural number with decimal digits $d_k d_{k-1} \dots d_0$, so that $n = \sum_{i=0}^{k} d_i 10^i$.
Then $9 \mid n$ if and only if $9 \mid d_0 + d_1 + \dots + d_k$.

## Remarks

More precisely, $n \equiv d_0 + d_1 + \dots + d_k \pmod 9$, because $10^i \equiv 1 \pmod 9$ for each $i$.
For example, $9 \mid 81{,}243$, because $8 + 1 + 2 + 4 + 3 = 18$.
The congruence is the basis of [[casting out nines|0E7W0EM6J6]].

## Explanations

### L1 human

Add the digits. The number is a multiple of $9$ exactly when the sum is a multiple of $9$.
For example, $123{,}456$ has the digit sum $21$, which is not a multiple of $9$. So $9 \nmid 123{,}456$.
