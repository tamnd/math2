---
tag: NC1THAZVY9
kind: proof
name: Proof that the modulus of the conjugate equals the modulus
msc: [30A99]
proves: 00KRCVE7CK
uses: [0KW2X0TFBX, 0BJV24C4SY, 02ZE6JHJ7G]
sources:
  - url: https://en.wikipedia.org/wiki/Complex_conjugate
    locator: Properties
---

## Proof

1. Let $z = a + b i$ with $a$ and $b$ real.
2. By the definition of the [[complex conjugate|0BJV24C4SY]], $\bar{z} = a + (-b) i$.
So $\operatorname{Re} \bar{z} = a$ and $\operatorname{Im} \bar{z} = -b$, by the definition of the [[real and imaginary parts|02ZE6JHJ7G]].
3. By the definition of the [[modulus|0KW2X0TFBX]], $|\bar{z}| = \sqrt{a^2 + (-b)^2}$.
4. Since $(-b)^2 = b^2$, this is $\sqrt{a^2 + b^2}$, which is $|z|$ by the same definition.
So $|\bar{z}| = |z|$.

## Idea

Conjugation changes the sign of the imaginary part only.
The modulus depends on the square of that part, so the sign does not matter.
