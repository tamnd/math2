---
tag: 7GNMP4Q32W
kind: proof
name: Proof of the irrationality of the square root of 2 by lowest terms
msc: [11J72]
proves: 0DZGSDHD92
uses: [080T2TXVQV, 0VB8BFRABH, 0R64A2CVN4, 051VYKA1EX, 0SN0MAEKYX, 02WF878BH1, 096PW7Q014]
methods: [0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Square_root_of_2
    locator: Proof by infinite descent
---

## Proof

We argue by contradiction.
By the definition of an [[irrational number|080T2TXVQV]], it suffices to show that no fraction $a / b$ of integers with $b \neq 0$ has square $2$.
The [[square root|0VB8BFRABH]] $\sqrt{2}$ is a real number with square $2$, so this shows that $\sqrt{2}$ is irrational.

1. Suppose that $a$ and $b$ are integers with $b \neq 0$ and $(a / b)^2 = 2$.
2. By the [[existence of a fraction in lowest terms|0R64A2CVN4]], there are integers $r$ and $s$ with $s > 0$, $\gcd(r, s) = 1$ and $r / s = a / b$.
3. Then $(r / s)^2 = 2$. Multiplying by $s^2$ gives $r^2 = 2 s^2$.
4. The number $2$ is a [[prime number|0SN0MAEKYX]]: a positive divisor of $2$ is at most $2$, so it is $1$ or $2$.
5. By step 3, $2$ [[divides|096PW7Q014]] $r \cdot r$. By [[Euclid's lemma|051VYKA1EX]], $2$ divides $r$. Write $r = 2 t$ with $t$ an integer.
6. Then $4 t^2 = 2 s^2$, so $s^2 = 2 t^2$. Thus $2$ divides $s \cdot s$, and Euclid's lemma gives $2 \mid s$.
7. So $2$ is a common divisor of $r$ and $s$. Then $\gcd(r, s) \ge 2$ by the definition of the [[greatest common divisor|02WF878BH1]].
8. This contradicts $\gcd(r, s) = 1$. So there are no such $a$ and $b$, and $\sqrt{2}$ is irrational.

## Idea

Write a supposed fraction for $\sqrt{2}$ in lowest terms.
The equation $r^2 = 2 s^2$ forces $r$ to be even, and then $s$ to be even too.
So the fraction was not in lowest terms after all.
