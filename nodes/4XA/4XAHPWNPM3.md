---
tag: 4XAHPWNPM3
kind: proof
name: Proof of the sum of two squares theorem
msc: ["11E25"]
proves: 04NPWJMA6H
uses: [043B3ENSTY, 0K2DMACEZ4, 04VCPS30ZE, 0850JJMJYZ, 0PHBS78HKT, 01J8AMV9RS, 0SQDB87Z3T, 00GXTQMY8Z, 0DQVHMYAGA, 051VYKA1EX, 080Q3RPKY6, 004JW7A2N5, 020K0X7HVR, 0ASJVEFA9J]
sources:
  - url: https://wstein.org/ent/ent.pdf
    locator: Section 5.7, Theorem 5.7.1
---

## Proof

Let $\nu_p$ be the [[p-adic valuation|04VCPS30ZE]]. Call $n$ a sum of two squares if $n = x^2 + y^2$ with integers $x, y$.

**Lemma.** Let $p \equiv 3 \pmod 4$ be prime with $p \mid x^2 + y^2$. Then $p \mid x$ and $p \mid y$.

1. Suppose $p \nmid y$. Then $\gcd(y, p) = 1$, and [[Bézout's identity|0DQVHMYAGA]] gives a [[modular inverse|00GXTQMY8Z]] $w$ with $yw \equiv 1 \pmod p$.
2. Multiplying $x^2 + y^2 \equiv 0$ by $w^2$ gives $(xw)^2 \equiv -1 \pmod p$. So $-1$ is a [[quadratic residue|0SQDB87Z3T]] modulo $p$, and $\left(\frac{-1}{p}\right) = 1$ as a [[Legendre symbol|01J8AMV9RS]].
3. But $(p - 1)/2$ is odd, so the [[first supplement|0PHBS78HKT]] gives $\left(\frac{-1}{p}\right) = -1$. This contradiction shows $p \mid y$.
4. Then $p \mid x^2$, and $p \mid x$ by [[Euclid's lemma|051VYKA1EX]].

**If $n$ is a sum of two squares, then $\nu_p(n)$ is even for each prime $p \equiv 3 \pmod 4$.**

5. Fix such a prime $p$. We use strong [[induction|0ASJVEFA9J]] on $n \ge 1$. Let $n = x^2 + y^2$.
6. If $p \nmid n$, then $\nu_p(n) = 0$, which is even.
7. If $p \mid n$, the lemma gives $x = px'$ and $y = py'$ with integers $x', y'$. Then $n = p^2 n'$ with $n' = x'^2 + y'^2$, and $1 \le n' < n$.
8. By the induction hypothesis, $\nu_p(n')$ is even. By the [[valuation of a product|0850JJMJYZ]], $\nu_p(n) = 2 + \nu_p(n')$ is even.

**If $\nu_p(n)$ is even for each prime $p \equiv 3 \pmod 4$, then $n$ is a sum of two squares.**

9. By [[the square times square-free decomposition|080Q3RPKY6]], $n = a^2 b$ with positive integers $a$, $b$ and $b$ [[square-free|004JW7A2N5]].
10. Let $p \equiv 3 \pmod 4$ be a prime. If $p \mid b$, then $\nu_p(b) = 1$, as $p^2 \nmid b$. Then $\nu_p(n) = 2\nu_p(a) + 1$ is odd, which is excluded. So $p \nmid b$.
11. By [[existence of prime factorization|020K0X7HVR]], $b = q_1 \cdots q_r$ with primes $q_i$, where $r \ge 0$. By step 10, each $q_i$ is $2$ or a prime $q_i \equiv 1 \pmod 4$.
12. Each $q_i$ is a sum of two squares: $2 = 1^2 + 1^2$, and the others by [[Fermat's theorem on sums of two squares|043B3ENSTY]].
13. By the [[Brahmagupta–Fibonacci identity|0K2DMACEZ4]], a product of two sums of two squares is a sum of two squares. By induction on $r$, $b$ is a sum of two squares. For $r = 0$, $b = 1 = 1^2 + 0^2$.
14. Write $b = u^2 + v^2$. Then $n = a^2 b = (au)^2 + (av)^2$, a sum of two squares.

## Idea

A prime $p \equiv 3 \pmod 4$ cannot divide $x^2 + y^2$ without dividing both $x$ and $y$, because $-1$ is not a square modulo $p$. So such primes come off in pairs. Conversely, the remaining primes are sums of two squares, and the Brahmagupta–Fibonacci identity multiplies them together.
