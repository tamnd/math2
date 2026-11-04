---
tag: VCN0MCW84M
kind: proof
name: Proof of the formula for the totient of a prime power
msc: [11A25]
proves: 0AVY8HKBGD
uses: [0VV04M41AN, 0SN0MAEKYX, 02WF878BH1, 0GFKP8F8AG, 096PW7Q014, 0SPBEDVNW1, 051VYKA1EX]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%27s_totient_function
    locator: Value of phi for a prime power argument
---

## Proof

1. Let $p$ be a [[prime number|0SN0MAEKYX]] and let $k$ be a positive integer. By definition, [[Euler's totient function|0VV04M41AN]] $\varphi(p^k)$ is the number of integers $x$ with $1 \le x \le p^k$ that are [[coprime|0GFKP8F8AG]] to $p^k$.
2. We show that an integer $x$ is coprime to $p^k$ if and only if $p$ does not [[divide|096PW7Q014]] $x$.
3. Assume $p \mid x$. Since $k \ge 1$, $p$ also divides $p^k$. So $p$ is a common divisor, and $\gcd(x, p^k) \ge p > 1$.
4. Assume $p \nmid x$, and let $d = \gcd(x, p^k)$ be the [[greatest common divisor|02WF878BH1]]. Since $p^k \ne 0$, $d$ is positive. Suppose that $d > 1$.
5. By the [[existence of a prime divisor|0SPBEDVNW1]], there is a prime $q$ with $q \mid d$. Then $q$ divides $p^k = p \cdot p \cdots p$.
6. By [[Euclid's lemma|051VYKA1EX]], applied to the $k$ factors in turn, $q$ divides $p$. Since $q > 1$ and $p$ is prime, $q = p$.
7. Then $p = q$ divides $d$, and $d$ divides $x$, so $p \mid x$. This contradicts step 4. So $d = 1$.
8. By steps 3 and 7, the integers in $\{ 1, \dots, p^k \}$ that are not coprime to $p^k$ are exactly the multiples of $p$ in this set.
9. These multiples are $p j$ with $1 \le j \le p^{k-1}$, since $1 \le p j \le p^k$ is equivalent to $1 \le j \le p^{k-1}$ for an integer $j$. So there are $p^{k-1}$ of them.
10. Hence $\varphi(p^k) = p^k - p^{k-1} = p^{k-1} (p - 1)$.

## Idea

The only prime factor of $p^k$ is $p$, so a number shares a factor with $p^k$ exactly when $p$ divides it. Among $1, \dots, p^k$, every $p$-th number is a multiple of $p$, so we remove $p^{k-1}$ of them.
