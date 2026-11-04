---
tag: 8Y4GQYMHVW
kind: proof
name: Proof of the equality of complex numbers
msc: [30A99]
proves: 05V7J4WD1C
uses: [09FTAET5Z4, 0CBAB9QQ9X, 0JQWWFCS9R, 02ZE6JHJ7G, 0ESCX36MMC]
sources:
  - url: https://en.wikipedia.org/wiki/Complex_number
    locator: Definition and basic operations
---

## Proof

We use the [[construction of the complex numbers as pairs of reals|0CBAB9QQ9X]].

1. In this construction, a [[complex number|09FTAET5Z4]] is an [[ordered pair|0JQWWFCS9R]] $(a, b)$ of real numbers.
Addition is $(a, b) + (c, d) = (a + c, b + d)$, and multiplication is $(a, b)(c, d) = (a c - b d, a d + b c)$.
2. A real number $a$ is the pair $(a, 0)$, and the [[imaginary unit|0ESCX36MMC]] is $i = (0, 1)$.
3. Let $a$ and $b$ be real. Then $b i = (b, 0)(0, 1) = (b \cdot 0 - 0 \cdot 1, \, b \cdot 1 + 0 \cdot 0) = (0, b)$.
So $a + b i = (a, 0) + (0, b) = (a, b)$.
4. By step 3 and the definition of the [[real and imaginary parts|02ZE6JHJ7G]], the pair $z = (a, b)$ has $\operatorname{Re} z = a$ and $\operatorname{Im} z = b$.
These parts are well defined. If also $z = a' + b' i$ with $a', b'$ real, then $(a, b) = (a', b')$ by step 3, so $a = a'$ and $b = b'$.
5. Let $z = (a, b)$ and $w = (c, d)$. By step 4, $\operatorname{Re} z = a$, $\operatorname{Im} z = b$, $\operatorname{Re} w = c$ and $\operatorname{Im} w = d$.
6. By the defining property of ordered pairs, $(a, b) = (c, d)$ holds if and only if $a = c$ and $b = d$.
7. By steps 5 and 6, $z = w$ if and only if $\operatorname{Re} z = \operatorname{Re} w$ and $\operatorname{Im} z = \operatorname{Im} w$.

## Idea

A complex number is nothing more than its pair of real coordinates $(a, b)$.
Two pairs are equal exactly when their first entries agree and their second entries agree.
