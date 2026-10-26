---
tag: 0AVY8HKBGD
kind: statement
role: proposition
name: Totient of a prime power
msc: [11A25]
uses: [0VV04M41AN, 0SN0MAEKYX]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%27s_totient_function
    locator: Value of phi for a prime power argument
---

## Statement

Let $p$ be a [[prime number|0SN0MAEKYX]] and let $k$ be a positive integer.
Then $\varphi(p^k) = p^{k-1} (p - 1) = p^k - p^{k-1}$, where $\varphi$ is [[Euler's totient function|0VV04M41AN]].

## Remarks

The proof: an integer is coprime to $p^k$ if and only if $p$ does not divide it. Among $1, \dots, p^k$, the multiples of $p$ are $p, 2p, \dots, p^{k-1} \cdot p$, so there are $p^{k-1}$ of them.
For example, $\varphi(8) = 4$ and $\varphi(27) = 18$.
With the [[multiplicativity of the totient function|0FSJA9M43W]], this formula gives $\varphi(n)$ from the prime factorization of $n$.

## Explanations

### L1 human

Among the numbers $1$ to $p^k$, exactly one in $p$ is a multiple of $p$.
Remove these numbers. The fraction $1 - 1/p$ of the numbers stays, so $\varphi(p^k) = p^k (1 - 1/p)$.
