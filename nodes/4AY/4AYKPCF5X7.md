---
tag: 4AYKPCF5X7
kind: proof
name: Proof of the formula for the inverse of a complex number
msc: [12D99]
proves: 0FQRAV5SKH
uses: [0ZB7J071WQ, 0FRSR10DWF, 0KW2X0TFBX, 0BJV24C4SY, 05V7J4WD1C]
sources:
  - url: https://en.wikipedia.org/wiki/Complex_number
    locator: Complex conjugate, absolute value, argument and division
---

## Proof

1. Let $z = a + b i$ with $a, b$ real and $z \neq 0$. Let $\bar{z} = a - b i$ be its [[conjugate|0BJV24C4SY]] and $|z|$ its [[modulus|0KW2X0TFBX]].
2. Since $z \neq 0$, we have $a \neq 0$ or $b \neq 0$, by [[equality of complex numbers|05V7J4WD1C]].
The square of a nonzero real is positive, so $a^2 + b^2 > 0$. By the definition of the modulus, $|z|^2 = a^2 + b^2$.
So $|z|^2 > 0$, and the real number $1 / |z|^2$ exists.
3. Let $v = \dfrac{\bar{z}}{|z|^2}$, that is, the product of the real number $1/|z|^2$ and $\bar{z}$.
4. By [[a complex number times its conjugate|0ZB7J071WQ]], $z \bar{z} = |z|^2$.
5. Using commutativity and associativity of multiplication in the [[field|0FRSR10DWF]] $\C$, we get $z v = \dfrac{1}{|z|^2} (z \bar{z}) = \dfrac{|z|^2}{|z|^2} = 1$.
6. Inverses in a field are unique. Indeed, $z z^{-1} = 1$ and $z v = 1$ give $v = v (z z^{-1}) = (v z) z^{-1} = z^{-1}$.
So $z^{-1} = \bar{z} / |z|^2$.
7. In coordinates, a real number $t$ times $a - b i$ is $t a - t b i$. With $t = 1/(a^2 + b^2)$, step 6 gives
$$z^{-1} = \frac{a}{a^2 + b^2} - \frac{b}{a^2 + b^2} \, i.$$

## Idea

The product $z \bar{z}$ is the positive real number $|z|^2$.
Dividing this identity by $|z|^2$ shows that $\bar{z} / |z|^2$ undoes multiplication by $z$.
