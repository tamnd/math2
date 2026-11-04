---
tag: WG6EAWSCCP
kind: proof
name: Proof of the irrationality of square roots of non-squares
msc: [11J72]
proves: 0N10YRNNWV
uses: [084HH1NDCB, 080T2TXVQV]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_irrational_number
    locator: Square root of non-square is irrational
---

## Proof

1. Suppose first that $n$ is a perfect square, say $n = m^2$ with $m \ge 0$ an integer. Then $\sqrt{n} = m$ is rational, so it is not [[irrational|080T2TXVQV]].
2. Now suppose that $n$ is not a perfect square. Then $n \ge 2$, since $0 = 0^2$ and $1 = 1^2$. We argue by contradiction.
3. Assume $\sqrt{n} = a/b$ with integers $a$ and $b$, $b \ne 0$. Since $\sqrt{n} > 0$, we may take $a > 0$ and $b > 0$.
4. Squaring gives $a^2 = n b^2$.
5. For a prime $p$ and a positive integer $m$, let $v_p(m)$ be the exponent of $p$ in the prime factorization of $m$. It is well defined by the [[fundamental theorem of arithmetic|084HH1NDCB]].
6. Uniqueness of factorization gives $v_p(uv) = v_p(u) + v_p(v)$ for positive integers $u$ and $v$: concatenating factorizations of $u$ and $v$ gives the factorization of $uv$.
7. By steps 4 and 6, $2 v_p(a) = v_p(n) + 2 v_p(b)$ for each prime $p$. So $v_p(n) = 2(v_p(a) - v_p(b))$ is even.
8. Put $k_p = v_p(n)/2$, a natural number, and $m = \prod_p p^{k_p}$, a finite product over the primes dividing $n$.
9. Then $m^2 = \prod_p p^{v_p(n)} = n$, so $n$ is a perfect square. This contradicts step 2.
10. So $\sqrt{n}$ is irrational when $n$ is not a perfect square. With step 1, $\sqrt{n}$ is irrational if and only if $n$ is not a perfect square.

## Idea

If $\sqrt{n} = a/b$, then $n b^2 = a^2$.
In $a^2$ and in $b^2$ every prime appears to an even power, so the same holds in $n$, and then $n$ is a square.
