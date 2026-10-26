---
tag: 09YBMJTNBM
kind: statement
role: proposition
name: Divisibility by 11
msc: [11A63]
uses: [0TPW25CBN6, 0J5VGJYYC3]
sources:
  - url: https://en.wikipedia.org/wiki/Divisibility_rule
    locator: Divisibility by 11
---

## Statement

Let $n$ be a natural number with decimal digits $d_k d_{k-1} \dots d_0$, so that $n = \sum_{i=0}^{k} d_i 10^i$.
Then $11 \mid n$ if and only if $11 \mid d_0 - d_1 + d_2 - \dots + (-1)^k d_k$.

## Remarks

More precisely, $n \equiv \sum_{i=0}^{k} (-1)^i d_i \pmod{11}$. This holds because $10 \equiv -1 \pmod{11}$, so $10^i \equiv (-1)^i \pmod{11}$.
For example, $918{,}082$ gives $2 - 8 + 0 - 8 + 1 - 9 = -22$, and $11 \mid -22$. So $11 \mid 918{,}082$.

## Explanations

### L1 human

Start at the last digit, and add and subtract the digits in turn.
The number is a multiple of $11$ exactly when the result is a multiple of $11$, including $0$.
For example, $121$ gives $1 - 2 + 1 = 0$, and indeed $121 = 11 \cdot 11$.
