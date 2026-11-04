---
tag: TAYT68QGQ8
kind: proof
name: Proof that a composite number has a prime factor at most its square root
msc: [11A51]
proves: 0EB6BBMQMC
uses: [0N3ADXHNTQ, 0SN0MAEKYX, 0SPBEDVNW1, 096PW7Q014]
sources:
  - url: https://proofwiki.org/wiki/Composite_Number_has_Prime_Factor_not_Greater_Than_its_Square_Root
---

## Proof

1. Let $n$ be a [[composite number|0N3ADXHNTQ]]. Then $n > 1$ and $n$ is not a [[prime number|0SN0MAEKYX]].
2. So $n$ has a positive [[divisor|096PW7Q014]] $a$ with $a \neq 1$ and $a \neq n$. Write $n = a b$ with an integer $b$.
3. Since $n > 0$ and $a > 0$, $b \ge 1$, so $a \le n$. Hence $1 < a < n$.
4. Then $b = n / a$ satisfies $1 < b < n$. If $b = 1$ then $a = n$, and if $b = n$ then $a = 1$; both are excluded.
5. By swapping $a$ and $b$ if needed, we may assume $a \le b$. Then $a^2 \le a b = n$.
6. By the [[existence of a prime divisor|0SPBEDVNW1]], since $a \ge 2$, there is a prime $p$ with $p \mid a$.
7. Since $p$ is a positive divisor of the positive integer $a$, $p \le a$. So $p^2 \le a^2 \le n$.
8. Since $p \mid a$ and $a \mid n$, $p \mid n$. So $p$ is a prime factor of $n$ with $p^2 \le n$, that is, $p \le \sqrt{n}$.

## Idea

A composite number splits as $n = ab$ with two factors larger than $1$. The smaller factor is at most $\sqrt{n}$, since otherwise the product would exceed $n$. Any prime factor of this smaller factor works.
