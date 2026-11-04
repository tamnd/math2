---
tag: G5TFN4G1RM
kind: proof
name: Proof that the characteristic of an integral domain is zero or prime
msc: [13G05]
proves: 00758QM6JJ
uses: [09S3PFBEPM, 0P7CH1CND5, 0SN0MAEKYX, 0N3ADXHNTQ, 0894J980RK]
sources:
  - url: https://proofwiki.org/wiki/Characteristic_of_Integral_Domain_is_Zero_or_Prime
---

## Proof

1. Let $R$ be an [[integral domain|09S3PFBEPM]] and let $n$ be its [[characteristic|0P7CH1CND5]]. For a positive integer $k$, write $k \cdot 1$ for the sum of $k$ copies of $1$ in $R$.
2. If $n = 0$, there is nothing to prove. So assume $n > 0$. Then $n \cdot 1 = 0$, and $k \cdot 1 \neq 0$ for $0 < k < n$.
3. Since $1 \cdot 1 = 1 \neq 0$ in an integral domain, $n \neq 1$. So $n \ge 2$.
4. We argue by contradiction. Suppose that $n$ is not a [[prime number|0SN0MAEKYX]]. Then $n$ is [[composite|0N3ADXHNTQ]], so it has a positive divisor $a$ with $a \neq 1$ and $a \neq n$.
5. Put $b = n / a$. Then $1 < a < n$ and $1 < b < n$.
6. For positive integers $a$ and $b$, $(a \cdot 1)(b \cdot 1) = (a b) \cdot 1$. Indeed, by the distributive laws of the [[ring|0894J980RK]] $R$, the product is a sum of $a b$ terms, each equal to $1 \cdot 1 = 1$.
7. So $(a \cdot 1)(b \cdot 1) = n \cdot 1 = 0$.
8. Since $R$ is an integral domain, $a \cdot 1 = 0$ or $b \cdot 1 = 0$.
9. Both $a$ and $b$ are positive and less than $n$. So step 8 contradicts the minimality of $n$ in step 2.
10. Hence $n$ is a prime number. So the characteristic of $R$ is $0$ or a prime number.

## Idea

If the characteristic $n$ factors as $a b$ with smaller factors, then $(a \cdot 1)(b \cdot 1) = 0$. In an integral domain, one of the two factors must be $0$. That contradicts the choice of $n$ as the least positive integer with $n \cdot 1 = 0$.
