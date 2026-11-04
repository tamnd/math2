---
tag: 28FB6V6JNV
kind: proof
name: Proof of the gcd formula for Fibonacci numbers by the Euclidean algorithm
msc: [11B39]
proves: 0R9F850CTH
uses: [0GA9K57A39, 02WF878BH1, 00CN2F997Q, 0D3PFXEAKF, 03BAREW1Z5, 0GFKP8F8AG, 0KMVFSHFGZ, 0TRNT4X7J0]
sources:
  - url: https://proofwiki.org/wiki/GCD_of_Fibonacci_Numbers
---

## Proof

We show that $\gcd(F_a, F_b)$ obeys the subtraction step of the [[Euclidean algorithm|0TRNT4X7J0]], and argue by [[strong induction|0KMVFSHFGZ]].

1. Let $F_k$ be the [[Fibonacci numbers|0GA9K57A39]]. They are natural numbers. Two pairs of integers with the same common divisors have the same [[greatest common divisor|02WF878BH1]].
2. For integers $x, y, t$, the pairs $(x, y)$ and $(x, y + t x)$ have the same common divisors. Indeed, $d \mid x$ and $d \mid y$ imply $d \mid y + tx$, and conversely $d \mid x$ and $d \mid y + tx$ imply $d \mid y$.
3. Let $x, y, c$ be integers with $\gcd(x, y) = 1$. We claim that $(x, yc)$ and $(x, c)$ have the same common divisors.
4. A common divisor of $x$ and $c$ divides $yc$. Conversely, let $d \mid x$ and $d \mid yc$. A common divisor of $d$ and $y$ divides $x$ and $y$, so it is $\pm 1$. Also $d$ and $y$ are not both $0$, since otherwise $x = 0 = y$ and $\gcd(x, y) = 0$. Thus $d$ and $y$ are [[coprime|0GFKP8F8AG]].
5. By the [[generalized Euclid's lemma|03BAREW1Z5]], $d \mid c$. This proves the claim of step 3.
6. Let $a \ge 1$ and $c \ge 0$. The [[addition formula|00CN2F997Q]] with $m = a - 1$ and $n = c$ gives $F_{a+c} = F_{a-1} F_c + F_a F_{c+1}$.
7. By step 2 with $t = -F_{c+1}$, $\gcd(F_a, F_{a+c}) = \gcd(F_a, F_{a-1} F_c)$.
8. By [[consecutive Fibonacci numbers are coprime|0D3PFXEAKF]], $\gcd(F_a, F_{a-1}) = 1$. By step 3, $\gcd(F_a, F_{a-1} F_c) = \gcd(F_a, F_c)$.
9. So $\gcd(F_a, F_b) = \gcd(F_a, F_{b-a})$ whenever $1 \le a \le b$, and also $\gcd(a, b) = \gcd(a, b - a)$ by step 2.
10. For a natural number $x$, $\gcd(x, 0) = x$. For $x > 0$ the largest divisor of $x$ is $x$, and $\gcd(0, 0) = 0$ by convention.
11. Let $Q(s)$ be the claim that $\gcd(F_a, F_b) = F_{\gcd(a, b)}$ for all natural numbers $a, b$ with $a + b = s$. We prove $Q(s)$ for all $s$ by strong induction.
12. Fix $s$ and assume $Q(s')$ for all $s' < s$. Let $a + b = s$.
13. If $a = 0$, then by step 10, $\gcd(F_0, F_b) = \gcd(0, F_b) = F_b = F_{\gcd(0, b)}$. The case $b = 0$ is the same with the roles exchanged.
14. If $1 \le a \le b$, then $a + (b - a) = b < s$. By step 9 and $Q(b)$, $\gcd(F_a, F_b) = \gcd(F_a, F_{b-a}) = F_{\gcd(a, b-a)} = F_{\gcd(a, b)}$.
15. If $1 \le b < a$, the same argument with $a$ and $b$ exchanged applies, since $\gcd$ is symmetric in its two arguments.
16. So $Q(s)$ holds. By strong induction, $\gcd(F_m, F_n) = F_{\gcd(m, n)}$ for all natural numbers $m$ and $n$.

## Idea

The addition formula writes $F_{a+c}$ as $F_{a-1} F_c$ plus a multiple of $F_a$. Since $F_{a-1}$ and $F_a$ are coprime, $\gcd(F_a, F_{a+c}) = \gcd(F_a, F_c)$. So the indices follow the Euclidean algorithm, which ends at $\gcd(m, n)$.
