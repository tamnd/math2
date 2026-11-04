---
tag: T7F6HM7GN0
kind: proof
name: Proof of the converse of Wilson's theorem
msc: [11A51]
proves: 06WRV8HFDY
uses: [0SN0MAEKYX, 0TPW25CBN6, 096PW7Q014]
methods: [0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Wilson%27s_theorem
    locator: Composite modulus
---

## Proof

We argue by contradiction.

1. Let $n > 1$ be an integer with $(n - 1)! \equiv -1 \pmod n$. Suppose that $n$ is not a [[prime number|0SN0MAEKYX]].
2. Since $n > 1$ is not prime, $n$ has a positive [[divisor|096PW7Q014]] $a$ other than $1$ and $n$. So $1 < a < n$.
3. Since $1 < a \le n - 1$, the number $a$ is one of the factors of $(n - 1)! = 1 \cdot 2 \cdots (n - 1)$. So $a$ divides $(n - 1)!$.
4. By the definition of [[congruence|0TPW25CBN6]], $n$ divides $(n - 1)! - (-1) = (n - 1)! + 1$. Since $a \mid n$, also $a$ divides $(n - 1)! + 1$.
5. By steps 3 and 4, $a$ divides $\big( (n - 1)! + 1 \big) - (n - 1)! = 1$.
6. This is impossible, since $a > 1$. So $n$ is prime.

## Idea

A proper divisor $a$ of $n$ appears as a factor in $(n - 1)!$. It also divides $(n - 1)! + 1$, so it would divide $1$, which cannot happen.
