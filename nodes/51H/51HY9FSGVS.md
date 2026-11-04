---
tag: 51HY9FSGVS
kind: proof
name: Proof of the Euclid–Euler theorem
msc: [11A25]
proves: 0WETJCKNRG
uses: [0SB7Q8SYSF, 009QCP5T3Z, 04WC36XKV6, 06GPJF9V7M, 0SN0MAEKYX, 0GFKP8F8AG, 03BAREW1Z5, 084HH1NDCB]
sources:
  - url: https://en.wikipedia.org/wiki/Euclid%E2%80%93Euler_theorem
    locator: Proof
---

## Proof

Let $\sigma$ be the [[sum of divisors|009QCP5T3Z]]. A positive integer $n$ is [[perfect|0SB7Q8SYSF]] exactly when $\sigma(n) = 2n$.

1. For $k \ge 0$, the divisors of $2^k$ are $1, 2, \dots, 2^k$, by the [[fundamental theorem of arithmetic|084HH1NDCB]]. So $\sigma(2^k) = 1 + 2 + \dots + 2^k = 2^{k+1} - 1$.
2. For a [[prime|0SN0MAEKYX]] $q$, the divisors of $q$ are $1$ and $q$, so $\sigma(q) = q + 1$.
3. An odd number and a power of $2$ have no common prime factor, so they are [[coprime|0GFKP8F8AG]]. Then [[multiplicativity of $\sigma$|04WC36XKV6]] gives $\sigma(2^k m) = \sigma(2^k) \sigma(m)$ for odd $m$.

**If $n = 2^{p-1}(2^p - 1)$ with $q = 2^p - 1$ a [[Mersenne prime|06GPJF9V7M]], then $n$ is perfect.**

4. Since $q$ is prime, $q \ge 2$, so $p \ge 2$. Also $q$ is odd.
5. By steps 1 to 3, $\sigma(n) = \sigma(2^{p-1}) \sigma(q) = (2^p - 1)(q + 1) = q \cdot 2^p = 2n$. So $n$ is perfect.

**If $n$ is an even perfect number, then $n$ has this form.**

6. Let $n$ be even and perfect. Write $n = 2^k m$ with $k \ge 1$ and $m$ odd.
7. By step 3 and step 1, $\sigma(n) = (2^{k+1} - 1)\sigma(m)$. Since $\sigma(n) = 2n$, we get $(2^{k+1} - 1)\sigma(m) = 2^{k+1} m$.
8. The numbers $2^{k+1} - 1$ and $2^{k+1}$ are coprime, since a common divisor divides their difference $1$.
9. So $2^{k+1} - 1$ divides $m$, by [[the generalized Euclid's lemma|03BAREW1Z5]]. Write $m = (2^{k+1} - 1) d$ with $d$ a positive integer.
10. Then step 7 gives $(2^{k+1} - 1)\sigma(m) = 2^{k+1}(2^{k+1} - 1) d$, so $\sigma(m) = 2^{k+1} d = m + d$.
11. Since $k \ge 1$, we have $2^{k+1} - 1 \ge 3$, so $d < m$. Thus $m$ and $d$ are two distinct divisors of $m$.
12. The sum $\sigma(m)$ of all divisors of $m$ is $m + d$. So every divisor of $m$ is $m$ or $d$, since any other divisor would add a positive term.
13. The number $1$ divides $m$, and $1 \ne m$ because $m \ge 3$. So $d = 1$, and the only divisors of $m$ are $1$ and $m$.
14. Hence $m = 2^{k+1} - 1$ is prime. Put $p = k + 1$. Then $n = 2^{p-1}(2^p - 1)$, and $2^p - 1$ is a Mersenne prime.

## Idea

The sum of divisors is multiplicative, so it splits over the power of $2$ and the odd part. For an even perfect number this forces $2^{k+1} - 1$ to divide the odd part $m$, and then $\sigma(m) = m + d$. A number whose divisors add up to only two of them must be prime.
