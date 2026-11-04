---
tag: 67KN8TZJ5C
kind: proof
name: Proof that a complex number times its conjugate is the square of its modulus
msc: [30A99]
proves: 0ZB7J071WQ
uses: [09FTAET5Z4, 0BJV24C4SY, 0KW2X0TFBX, 068BZBXE0C, 05V7J4WD1C]
sources:
  - url: https://en.wikipedia.org/wiki/Complex_conjugate
    locator: Properties
---

## Proof

1. Let $z = a + b i$ be a [[complex number|09FTAET5Z4]], with $a$ and $b$ real.
2. Its [[conjugate|0BJV24C4SY]] is $\bar{z} = a + (-b) i$.
3. By the rule for multiplying complex numbers,
$$z \bar{z} = \bigl(a \cdot a - b \cdot (-b)\bigr) + \bigl(a \cdot (-b) + b \cdot a\bigr) i = (a^2 + b^2) + 0 i.$$
4. By the definition of the [[modulus|0KW2X0TFBX]], $|z| = \sqrt{a^2 + b^2}$.
Here $\sqrt{a^2 + b^2}$ is the nonnegative real number whose square is $a^2 + b^2$, by [[existence of square roots|068BZBXE0C]].
5. So $|z|^2 = a^2 + b^2$. With step 3 and [[equality of complex numbers|05V7J4WD1C]], this gives $z \bar{z} = |z|^2$.
6. Since $a^2 \ge 0$ and $b^2 \ge 0$, the number $z \bar{z} = a^2 + b^2$ is a nonnegative real number.

## Idea

The product $(a + b i)(a - b i)$ is a difference of squares, $a^2 - (b i)^2 = a^2 + b^2$.
The imaginary parts cancel, and what remains is the square of the distance from $z$ to $0$.
