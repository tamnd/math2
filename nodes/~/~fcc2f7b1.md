---
tag: ~fcc2f7b1
kind: statement
role: theorem
name: Multiplicativity of the totient function
msc: [11A25]
uses: [~97075527, ~8f403547, ~d3d0b9ad]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%27s_totient_function
    locator: Phi is a multiplicative function
---

## Statement

Let $m$ and $n$ be positive integers that are [[coprime|~8f403547]].
Then $\varphi(m n) = \varphi(m) \varphi(n)$, where $\varphi$ is [[Euler's totient function|~97075527]].

## Remarks

The proof uses the [[Chinese remainder theorem|~d3d0b9ad]]. It gives a bijection between the residues modulo $m n$ and the pairs of residues modulo $m$ and modulo $n$. A residue is coprime to $m n$ if and only if both parts are coprime to their moduli.
The hypothesis is necessary: $\varphi(4) = 2$, but $\varphi(2) \varphi(2) = 1$.
So $\varphi$ is a [[multiplicative function|~d4940324]].
For example, $\varphi(36) = \varphi(4) \varphi(9) = 2 \cdot 6 = 12$.

## Explanations

### L1 human

When $m$ and $n$ have no common factor, a number is coprime to $m n$ exactly when it is coprime to $m$ and to $n$.
The two conditions are independent, so the counts multiply.
For example, $\varphi(15) = \varphi(3) \varphi(5) = 2 \cdot 4 = 8$.
