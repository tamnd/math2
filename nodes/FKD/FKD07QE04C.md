---
tag: FKD07QE04C
kind: proof
name: Proof that exp z = 1 iff z is an integer multiple of 2πi
msc: [33B10]
proves: 013AHC4DRT
uses: [054VXHMCA3, 0C4JS9RF5M, 0WM7DJCM6G, 04R3CY41VJ, 08W5RN375X, 02KTRHQMHN, 06JZGMYTYD, 0P9BNBW2W3, 0KN2V7840E, 0KW2X0TFBX, 0HYNZE940T, 03H7WZ4T3K, 0P4NQD746K, 028XEQCE88]
sources:
  - url: https://en.wikipedia.org/wiki/Exponential_function
    locator: Complex exponential
---

## Proof

We split $z$ into real and imaginary parts and use the periods of sine and cosine.

1. Write $z = x + iy$ with $x, y$ real. By the [[product of exponentials|0WM7DJCM6G]], $e^z = e^x e^{iy}$, where $e^w$ is the [[complex exponential|054VXHMCA3]].
2. At the real number $x$, the exponential series sums to the [[real exponential|06JZGMYTYD]]. So $e^x$ is a [[positive real number|0P9BNBW2W3]].
3. By [[Euler's formula|04R3CY41VJ]], $e^{iy} = \cos y + i \sin y$. At real $y$, these are the real [[cosine|08W5RN375X]] and [[sine|02KTRHQMHN]]. So $\cos y$ and $\sin y$ are the real and imaginary parts of $e^{iy}$.
4. By the [[definition of the modulus|0KW2X0TFBX]] and the [[Pythagorean identity|03H7WZ4T3K]], $\abs{e^{iy}} = \sqrt{\cos^2 y + \sin^2 y} = 1$.
5. Let $k$ be an [[integer|0C4JS9RF5M]]. Applying the [[periodicity of sine and cosine|0P4NQD746K]] $\abs{k}$ times gives $\cos(2\pi k) = \cos 0 = 1$ and $\sin(2 \pi k) = \sin 0 = 0$.
6. So if $z = 2 \pi i k$, then $e^z = e^{i (2\pi k)} = \cos(2\pi k) + i \sin(2\pi k) = 1$ by step 3. This proves one direction.
7. Conversely, assume $e^z = 1$. The [[modulus is multiplicative|0HYNZE940T]], so $1 = \abs{e^z} = \abs{e^x} \abs{e^{iy}} = e^x$ by steps 2 and 4.
8. The real exponential is [[strictly increasing|0KN2V7840E]] and $e^0 = 1$. So $e^x = 1$ forces $x = 0$.
9. Then $1 = e^{iy} = \cos y + i \sin y$. Comparing real and imaginary parts, $\cos y = 1$ and $\sin y = 0$.
10. Let $k = \floor{y / (2\pi)}$, an integer, and $t = y - 2\pi k$. Then $0 \le t < 2\pi$.
11. By periodicity, as in step 5, $\cos t = \cos y = 1$ and $\sin t = \sin y = 0$.
12. Suppose that $t > 0$. For each real $s$, the [[angle addition formula|028XEQCE88]] gives $\sin(s + t) = \sin s \cos t + \cos s \sin t = \sin s$.
13. So $t$ is a positive period of $\sin$ with $t < 2\pi$. This contradicts the fact that $2\pi$ is the smallest positive period of $\sin$. Hence $t = 0$.
14. So $y = 2 \pi k$ and $z = x + iy = 2 \pi i k$ with $k$ an integer.

## Idea

The modulus of $e^{x + iy}$ is $e^x$ and its angle is $y$. So $e^z = 1$ forces the modulus $e^x$ to be $1$ and the angle $y$ to be a full number of turns. The minimality of the period $2\pi$ rules out any other angle.
