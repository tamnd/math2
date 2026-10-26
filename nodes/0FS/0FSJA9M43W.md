---
tag: 0FSJA9M43W
kind: statement
role: theorem
name: Multiplicativity of the totient function
msc: [11A25]
uses: [0VV04M41AN, 0GFKP8F8AG, 0FNN9B4W64]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%27s_totient_function
    locator: Phi is a multiplicative function
---

## Statement

Let $m$ and $n$ be positive integers that are [[coprime|0GFKP8F8AG]].
Then $\varphi(m n) = \varphi(m) \varphi(n)$, where $\varphi$ is [[Euler's totient function|0VV04M41AN]].

## Remarks

The proof uses the [[Chinese remainder theorem|0FNN9B4W64]]. It gives a bijection between the residues modulo $m n$ and the pairs of residues modulo $m$ and modulo $n$. A residue is coprime to $m n$ if and only if both parts are coprime to their moduli.
The hypothesis is necessary: $\varphi(4) = 2$, but $\varphi(2) \varphi(2) = 1$.
So $\varphi$ is a [[multiplicative function|0AP80TT660]].
For example, $\varphi(36) = \varphi(4) \varphi(9) = 2 \cdot 6 = 12$.

## Explanations

### L1 human

When $m$ and $n$ have no common factor, a number is coprime to $m n$ exactly when it is coprime to $m$ and to $n$.
The two conditions are independent, so the counts multiply.
For example, $\varphi(15) = \varphi(3) \varphi(5) = 2 \cdot 4 = 8$.
