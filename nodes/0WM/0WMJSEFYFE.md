---
tag: 0WMJSEFYFE
kind: statement
role: theorem
name: A prime is a Gaussian prime if and only if it is 3 modulo 4
msc: [11R11]
uses: [0GTEHJQRFK, 0SN0MAEKYX, 043B3ENSTY]
sources:
  - url: https://en.wikipedia.org/wiki/Gaussian_integer
    locator: Gaussian primes
---

## Statement

Let $p$ be a [[prime number|0SN0MAEKYX]].
Then $p$ is a [[Gaussian prime|0GTEHJQRFK]] if and only if $p \equiv 3 \pmod 4$.

## Remarks

If $p = 2$, then $2 = (1 + i)(1 - i)$, and $1 + i$ is a Gaussian prime.
If $p \equiv 1 \pmod 4$, then $p = a^2 + b^2 = (a + bi)(a - bi)$ by [[Fermat's theorem on sums of two squares|043B3ENSTY]], and $a \pm bi$ are Gaussian primes.
If $p \equiv 3 \pmod 4$, then $p$ is not a sum of two squares. So no Gaussian integer has norm $p$, and $p$ cannot split.
For example, $3$ and $7$ are Gaussian primes, but $13 = (3 + 2i)(3 - 2i)$.

## Explanations

### L1 human

An ordinary prime stays prime among the Gaussian integers exactly when it leaves remainder $3$ on division by $4$.
The other primes factor, because they are sums of two squares.
