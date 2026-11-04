---
tag: BQ2M6MND3X
kind: proof
name: Proof that every positive integer is a square times a square-free integer
msc: [11A51]
proves: 080Q3RPKY6
uses: [004JW7A2N5, 096PW7Q014, 0SN0MAEKYX]
sources:
  - url: https://en.wikipedia.org/wiki/Square-free_integer
    locator: Square-free factors of integers
---

## Proof

We take $a$ as large as possible.

1. Let $n$ be a positive integer. Let $A$ be the set of positive integers $a$ such that $a^2$ [[divides|096PW7Q014]] $n$.
2. The set $A$ is nonempty, because $1^2 = 1$ divides $n$.
3. The set $A$ is bounded. If $a \in A$, then $a^2$ is a positive divisor of the positive integer $n$, so $a \le a^2 \le n$.
4. So $A$ is a nonempty finite set, and it has a largest element $a$.
5. Write $n = a^2 b$ with an integer $b$. Since $n > 0$ and $a^2 > 0$, $b$ is a positive integer.
6. Suppose that $b$ is not [[square-free|004JW7A2N5]]. Then there is a [[prime number|0SN0MAEKYX]] $p$ with $p^2 \mid b$. Write $b = p^2 c$ with an integer $c$.
7. Then $n = a^2 p^2 c = (a p)^2 c$, so $a p \in A$.
8. Since $p \ge 2$, $a p > a$. This contradicts the choice of $a$ as the largest element of $A$.
9. So $b$ is square-free, and $n = a^2 b$ with positive integers $a$ and $b$.

## Idea

Take the largest square that divides $n$ and divide it out. If the quotient still had a factor $p^2$, a larger square would divide $n$. So the quotient is square-free.
