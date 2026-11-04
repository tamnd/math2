---
tag: KXWTG4M4S4
kind: proof
name: Proof of the formula for the totient of a prime
msc: [11A25]
proves: 0HY1MXMEN9
uses: [0VV04M41AN, 0SN0MAEKYX, 02WF878BH1, 0GFKP8F8AG]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%27s_totient_function
    locator: Value of phi for a prime power argument
---

## Proof

1. Let $p$ be a [[prime number|0SN0MAEKYX]]. By definition, [[Euler's totient function|0VV04M41AN]] $\varphi(p)$ is the number of integers $x$ with $1 \le x \le p$ that are [[coprime|0GFKP8F8AG]] to $p$.
2. Let $x$ be an integer with $1 \le x \le p$, and let $d = \gcd(x, p)$ be the [[greatest common divisor|02WF878BH1]]. It is a positive divisor of $p$.
3. Since $p$ is prime, its only positive divisors are $1$ and $p$. So $d = 1$ or $d = p$.
4. If $x \le p - 1$, then $0 < x < p$, so $p$ does not divide $x$. Since $d$ divides $x$, $d \ne p$, and so $d = 1$.
5. If $x = p$, then $d = \gcd(p, p) = p$. Since $p > 1$, $p$ is not coprime to itself.
6. By steps 4 and 5, the integers in $\{ 1, \dots, p \}$ that are coprime to $p$ are exactly $1, 2, \dots, p - 1$.
7. Hence $\varphi(p) = p - 1$.

## Idea

A prime has no divisors other than $1$ and itself. So every positive integer below $p$ shares no factor with $p$, and only $p$ itself is left out.
