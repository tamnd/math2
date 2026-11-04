---
tag: TMXSM5BNVK
kind: proof
name: Proof of Euclid's theorem using n! + 1
msc: [11A41]
proves: 0292EPPPT0
uses: [0SN0MAEKYX, 0SPBEDVNW1, 096PW7Q014]
sources:
  - url: https://en.wikipedia.org/wiki/Euclid%27s_theorem
    locator: Euclid's proof, Variations
---

## Proof

We show that $n! + 1$ has a prime divisor larger than $n$.

1. Let $n$ be a natural number, and put $N = n! + 1$. Here $n! = 1 \cdot 2 \cdots n$, with $0! = 1$.
2. Since $n! \ge 1$, $N \ge 2$. By the [[existence of a prime divisor|0SPBEDVNW1]], there is a [[prime number|0SN0MAEKYX]] $p$ with $p \mid N$.
3. Suppose $p \le n$. Since $p \ge 2$, $p$ is one of the factors $1, 2, \dots, n$ of $n!$, so $p$ [[divides|096PW7Q014]] $n!$.
4. Then $p$ divides $N - n! = 1$. But $p \ge 2$, and $2$ or more cannot divide $1$. This is a contradiction.
5. So $p > n$, and in particular $p \ge n$. This proves the second form of the statement.
6. Suppose there were only finitely many primes. Let $n$ be one more than the largest of them.
7. By step 5, there is a prime $p \ge n$. Then $p$ is larger than every prime, which is impossible. So there are infinitely many primes.

## Idea

Every number from $2$ to $n$ divides $n!$, so it leaves remainder $1$ when it divides $n! + 1$. Hence every prime factor of $n! + 1$ is larger than $n$, and there is always a prime beyond any given bound.
