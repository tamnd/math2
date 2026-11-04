---
tag: JPE6JNCSQ9
kind: proof
name: Proof that the modulus is multiplicative
msc: [30A99]
proves: 0HYNZE940T
uses: [0KW2X0TFBX, 0ZB7J071WQ, 0BJV24C4SY, 0FRSR10DWF, 068BZBXE0C, 05V7J4WD1C]
sources:
  - url: https://en.wikipedia.org/wiki/Absolute_value
    locator: Complex numbers
---

## Proof

1. Let $z = a + b i$ and $w = c + d i$ with $a, b, c, d$ real.
2. We first show that the [[conjugate|0BJV24C4SY]] of $z w$ is $\bar{z} \bar{w}$.
We have $z w = (a c - b d) + (a d + b c) i$, so $\overline{z w} = (a c - b d) - (a d + b c) i$.
3. Also $\bar{z} \bar{w} = (a - b i)(c - d i) = \bigl(a c - (-b)(-d)\bigr) + \bigl(a (-d) + (-b) c\bigr) i = (a c - b d) - (a d + b c) i$.
By [[equality of complex numbers|05V7J4WD1C]], $\overline{z w} = \bar{z} \bar{w}$.
4. By [[a complex number times its conjugate|0ZB7J071WQ]] applied to $z w$, then step 3, we get $|z w|^2 = (z w)(\bar{z} \bar{w})$.
5. Multiplication in $\C$ is commutative and associative, since $\C$ is a [[field|0FRSR10DWF]]. So $(z w)(\bar{z} \bar{w}) = (z \bar{z})(w \bar{w})$.
6. Applying [[a complex number times its conjugate|0ZB7J071WQ]] to $z$ and to $w$ gives $(z \bar{z})(w \bar{w}) = |z|^2 |w|^2 = (|z| \, |w|)^2$.
7. By steps 4 to 6, the real numbers $|z w|$ and $|z| \, |w|$ have the same square.
8. Both numbers are nonnegative, since the [[modulus|0KW2X0TFBX]] is nonnegative.
A nonnegative real number has only one nonnegative square root, by [[existence of square roots|068BZBXE0C]].
So $|z w| = |z| \, |w|$.

## Idea

Squaring removes the square root in the modulus and turns $|z|^2$ into $z \bar{z}$.
Conjugation respects products, so $|z w|^2$ splits as $|z|^2 |w|^2$.
