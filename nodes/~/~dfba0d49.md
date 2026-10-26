---
tag: ~dfba0d49
kind: statement
role: proposition
name: Multiplicativity of the Möbius function
msc: [11A25]
uses: [~23b71668, ~d4940324]
sources:
  - url: https://en.wikipedia.org/wiki/M%C3%B6bius_function
    locator: Properties
---

## Statement

The [[Möbius function|~23b71668]] $\mu$ is a [[multiplicative function|~d4940324]].
That is, $\mu(1) = 1$ and $\mu(mn) = \mu(m) \mu(n)$ for all coprime positive integers $m$ and $n$.

## Remarks

The function $\mu$ is not completely multiplicative: $\mu(4) = 0$, but $\mu(2)^2 = 1$.
The proof: for coprime $m$ and $n$, the product $mn$ is squarefree exactly when $m$ and $n$ are both squarefree. Then $\omega(mn) = \omega(m) + \omega(n)$.

## Explanations

### L1 human

For example, $\mu(5) = -1$ and $\mu(6) = 1$, and $\mu(30) = -1 = \mu(5) \mu(6)$.
When $m$ and $n$ have no common prime, their prime factors just combine, so the signs multiply.
