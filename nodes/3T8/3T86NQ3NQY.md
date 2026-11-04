---
tag: 3T86NQ3NQY
kind: proof
name: Proof of the irrationality of the square root of a prime
msc: [11J72]
proves: 0YHFMXJJAZ
uses: [080T2TXVQV, 0VB8BFRABH, 0R64A2CVN4, 051VYKA1EX, 0SN0MAEKYX, 02WF878BH1, 096PW7Q014]
methods: [0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Square_root_of_2
    locator: Proof by infinite descent
---

## Proof

We argue by contradiction, as in the proof for $\sqrt{2}$.
Let $p$ be a [[prime number|0SN0MAEKYX]]. Since $p > 0$, the [[square root|0VB8BFRABH]] $\sqrt{p}$ is a real number with $(\sqrt{p})^2 = p$.

1. Suppose that $\sqrt{p}$ is not [[irrational|080T2TXVQV]], that is, $\sqrt{p}$ is rational.
2. By the [[existence of a fraction in lowest terms|0R64A2CVN4]], $\sqrt{p} = a / b$ with integers $a$ and $b$, $b > 0$ and $\gcd(a, b) = 1$.
3. Squaring gives $a^2 / b^2 = p$. Multiplying by $b^2$ gives $a^2 = p b^2$.
4. So $p$ [[divides|096PW7Q014]] $a \cdot a$. By [[Euclid's lemma|051VYKA1EX]], $p$ divides $a$. Write $a = p c$ with $c$ an integer.
5. Then $p^2 c^2 = p b^2$. Since $p \neq 0$, dividing by $p$ gives $b^2 = p c^2$.
6. So $p$ divides $b \cdot b$, and Euclid's lemma gives $p \mid b$.
7. Thus $p$ is a common divisor of $a$ and $b$. By the definition of the [[greatest common divisor|02WF878BH1]], $\gcd(a, b) \ge p \ge 2$.
8. This contradicts $\gcd(a, b) = 1$. So $\sqrt{p}$ is irrational.

## Idea

If $\sqrt{p} = a / b$ in lowest terms, then $a^2 = p b^2$.
Because $p$ is prime, $p$ must divide $a$, and then $p$ must divide $b$ as well.
This contradicts the choice of lowest terms.
