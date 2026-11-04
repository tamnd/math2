---
tag: 1WCYX8MCTZ
kind: proof
name: Proof that a root of an integer is an integer or irrational
msc: [11J72]
proves: 0XWCKJZRYH
uses: [080T2TXVQV, 0C4JS9RF5M, 0R64A2CVN4, 0SPBEDVNW1, 051VYKA1EX, 0SN0MAEKYX, 02WF878BH1, 096PW7Q014, 0ASJVEFA9J]
methods: [0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Irrational_number
    locator: General roots
---

## Proof

We argue by contradiction, with a prime divisor of the denominator.
Let $x$ be real, $n \ge 1$ an integer and $m$ an [[integer|0C4JS9RF5M]] with $x^n = m$. Suppose that $x$ is not an integer.

1. Suppose that $x$ is not [[irrational|080T2TXVQV]], that is, $x$ is rational.
2. By the [[existence of a fraction in lowest terms|0R64A2CVN4]], $x = a / b$ with integers $a$ and $b$, $b > 0$ and $\gcd(a, b) = 1$.
3. If $b = 1$, then $x = a$ is an integer, which is false. So $b \ge 2$.
4. By the [[existence of a prime divisor|0SPBEDVNW1]], there is a [[prime number|0SN0MAEKYX]] $p$ with $p \mid b$.
5. From $x^n = m$ we get $a^n / b^n = m$, so $a^n = m b^n$.
6. Since $n \ge 1$, $b$ [[divides|096PW7Q014]] $b^n$, and so $p$ divides $m b^n = a^n$.
7. Claim: if $p \mid a^k$ for an integer $k \ge 1$, then $p \mid a$. We use [[induction|0ASJVEFA9J]] on $k$. For $k = 1$ there is nothing to prove.
8. If $p \mid a^{k+1} = a^k \cdot a$, then [[Euclid's lemma|051VYKA1EX]] gives $p \mid a^k$ or $p \mid a$. In the first case, the hypothesis of the induction gives $p \mid a$.
9. By steps 6 to 8, $p \mid a$. Together with step 4, $p$ is a common divisor of $a$ and $b$.
10. By the definition of the [[greatest common divisor|02WF878BH1]], $\gcd(a, b) \ge p \ge 2$. This contradicts $\gcd(a, b) = 1$.
11. So $x$ is not rational. Since $x$ is real, $x$ is irrational.

## Idea

Write the rational root $a / b$ in lowest terms with $b > 1$.
Any prime that divides $b$ divides $a^n = m b^n$, and so divides $a$.
This contradicts lowest terms, so the denominator is $1$ and the root is an integer.
