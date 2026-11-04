---
tag: EVARG9RYTF
kind: proof
name: Proof that i squared is minus one
msc: [12D99]
proves: 07KBQCG9KV
uses: [0ESCX36MMC, 09FTAET5Z4]
sources:
  - url: https://en.wikipedia.org/wiki/Imaginary_unit
    locator: Definition
---

## Proof

1. The [[imaginary unit|0ESCX36MMC]] is the complex number $i = 0 + 1 i$, with real part $0$ and imaginary part $1$.
2. The product of [[complex numbers|09FTAET5Z4]] is $(a + b i)(c + d i) = (a c - b d) + (a d + b c) i$.
3. Take $a = c = 0$ and $b = d = 1$. Then $i^2 = (0 \cdot 0 - 1 \cdot 1) + (0 \cdot 1 + 1 \cdot 0) i = -1 + 0 i$.
4. The complex number $-1 + 0 i$ is the real number $-1$, since $\R$ sits in $\C$ as the numbers $a + 0 i$. So $i^2 = -1$.

## Idea

The rule for multiplying complex numbers is built so that the two imaginary parts multiply to a negative real number. For $i \cdot i$ this gives exactly $-1$.
