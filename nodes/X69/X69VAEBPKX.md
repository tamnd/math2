---
tag: X69VAEBPKX
kind: proof
name: Proof of the existence of a prime divisor
msc: [11A41]
proves: 0SPBEDVNW1
uses: [0SN0MAEKYX, 096PW7Q014, 01BX15HSRR]
sources:
  - url: https://proofwiki.org/wiki/Positive_Integer_Greater_than_1_has_Prime_Divisor
---

## Proof

We show that the least divisor of $n$ greater than $1$ is prime.

1. Let $n$ be a natural number with $n \ge 2$.
2. Let $D$ be the set of natural numbers $d \ge 2$ with $d \mid n$, in the sense of [[divisibility|096PW7Q014]]. Since $n \mid n$ and $n \ge 2$, $n \in D$.
3. By the [[well-ordering principle|01BX15HSRR]], $D$ has a least element $p$. Then $p \ge 2$ and $p \mid n$.
4. Let $e$ be a positive divisor of $p$ with $e \neq 1$. Write $p = e f$ with an integer $f$. Since $p > 0$ and $e > 0$, $f \ge 1$, so $e \le p$.
5. Since $e \neq 1$ and $e \ge 1$, we have $e \ge 2$.
6. Write $n = p g$ with an integer $g$. Then $n = e (f g)$, so $e \mid n$. With step 5, this gives $e \in D$.
7. Since $p$ is the least element of $D$, $e \ge p$. With step 4, $e = p$.
8. So the only positive divisors of $p$ are $1$ and $p$, and $p > 1$. Hence $p$ is a [[prime number|0SN0MAEKYX]], and $p \mid n$.

## Idea

Look at the smallest divisor of $n$ that is larger than $1$. Any divisor of it that is larger than $1$ also divides $n$, so it cannot be smaller. Hence this smallest divisor has no proper divisors, and it is prime.
