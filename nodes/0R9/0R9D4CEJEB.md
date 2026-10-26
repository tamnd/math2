---
tag: 0R9D4CEJEB
kind: statement
role: proposition
name: Divisibility by 3
msc: [11A63]
uses: [0TPW25CBN6, 0J5VGJYYC3]
sources:
  - url: https://en.wikipedia.org/wiki/Divisibility_rule
    locator: Divisibility by 3 or 9
---

## Statement

Let $n$ be a natural number with decimal digits $d_k d_{k-1} \dots d_0$, so that $n = \sum_{i=0}^{k} d_i 10^i$.
Then $3 \mid n$ if and only if $3 \mid d_0 + d_1 + \dots + d_k$.

## Remarks

More precisely, $n \equiv d_0 + d_1 + \dots + d_k \pmod 3$. This holds because $10 \equiv 1 \pmod 3$, so $10^i \equiv 1 \pmod 3$ by [[compatibility with powers|0J5VGJYYC3]].
For example, $3 \mid 7{,}341$, because $7 + 3 + 4 + 1 = 15$ and $3 \mid 15$.
The rule for [[divisibility by 9|0ESHD7ZQDX]] has the same proof.

## Explanations

### L1 human

Add the digits of the number. If the sum is a multiple of $3$, the number is a multiple of $3$, and if not, it is not.
You can repeat: for $987{,}654$ the sum is $39$, and $3 + 9 = 12$ is a multiple of $3$. So $3 \mid 987{,}654$.
