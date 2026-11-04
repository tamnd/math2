---
tag: 8VC5HCNAJF
kind: proof
name: Proof of the Brahmagupta–Fibonacci identity
msc: ["11E25"]
proves: 0K2DMACEZ4
uses: [0GYGHKX834]
sources:
  - url: https://en.wikipedia.org/wiki/Brahmagupta%E2%80%93Fibonacci_identity
---

## Proof

We expand both sides, using the laws of a [[commutative ring|0GYGHKX834]].

1. The left side is $(a^2 + b^2)(c^2 + d^2) = a^2c^2 + a^2d^2 + b^2c^2 + b^2d^2$.
2. We have $(ac - bd)^2 = a^2c^2 - 2abcd + b^2d^2$ and $(ad + bc)^2 = a^2d^2 + 2abcd + b^2c^2$.
3. Adding the two lines of step 2, the terms $\pm 2abcd$ cancel. The sum is $a^2c^2 + b^2d^2 + a^2d^2 + b^2c^2$, which is the left side by step 1.
4. Next, $(ac + bd)^2 = a^2c^2 + 2abcd + b^2d^2$ and $(ad - bc)^2 = a^2d^2 - 2abcd + b^2c^2$.
5. Adding the two lines of step 4, the terms $\pm 2abcd$ cancel again. The sum is again the left side.
6. Steps 3 and 5 prove both equalities.

## Idea

Each square on the right gives two of the four products $a^2c^2, a^2d^2, b^2c^2, b^2d^2$ and a cross term $\pm 2abcd$. The signs are chosen so that the cross terms cancel. Over the complex numbers this is $\abs{z}^2 \abs{w}^2 = \abs{zw}^2$ for $z = a + bi$ and $w = c + di$.
