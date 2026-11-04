---
tag: FATHK2VGE6
kind: proof
name: Proof that a prime is a Gaussian prime if and only if it is 3 modulo 4
msc: [11R11]
proves: 0WMJSEFYFE
uses: [0GTEHJQRFK, 0SN0MAEKYX, 0B268GVX95, 00HPT88ZX0, 06RH4XAGRY, 043B3ENSTY, 0PHBS78HKT, 01J8AMV9RS, 0DQVHMYAGA]
sources:
  - url: https://en.wikipedia.org/wiki/Gaussian_integer
    locator: Gaussian primes
---

## Proof

Write $N(\gamma) = \gamma\bar\gamma$ for the [[norm|00HPT88ZX0]] of a [[Gaussian integer|0B268GVX95]] $\gamma$. Then $N(\gamma\delta) = N(\gamma) N(\delta)$, since complex conjugation is multiplicative.

1. A [[prime number|0SN0MAEKYX]] $p$ is either $2$, or odd with $p \equiv 1 \pmod 4$, or odd with $p \equiv 3 \pmod 4$. We treat the three cases.
2. Case $p = 2$. We have $2 = (1 + i)(1 - i)$, so $2$ divides $(1 + i)(1 - i)$ in $\mathbb{Z}[i]$.
3. But $2 \nmid 1 + i$ and $2 \nmid 1 - i$, because $(1 \pm i)/2$ has non-integer real part. So $2$ is not a [[Gaussian prime|0GTEHJQRFK]].
4. Case $p \equiv 1 \pmod 4$. By [[Fermat's theorem on sums of two squares|043B3ENSTY]], $p = a^2 + b^2$ with integers $a$, $b$. So $p = (a + bi)(a - bi)$.
5. If $p \mid a + bi$ in $\mathbb{Z}[i]$, then $p \mid a$ and $p \mid b$ in $\Z$, so $p^2 \mid a^2 + b^2 = p$. This is false. Likewise $p \nmid a - bi$.
6. So $p$ divides $(a + bi)(a - bi)$ but neither factor, and $p$ is not a Gaussian prime.
7. Case $p \equiv 3 \pmod 4$. First, $p \ne 0$, and $p$ is not a unit, since the [[units|06RH4XAGRY]] of $\mathbb{Z}[i]$ are $\pm 1$ and $\pm i$.
8. By the [[first supplement to quadratic reciprocity|0PHBS78HKT]], the [[Legendre symbol|01J8AMV9RS]] of $-1$ is $(-1)^{(p-1)/2} = -1$. So $-1$ is not a square modulo $p$.
9. Claim: if $a$, $b$ are integers with $p \mid a^2 + b^2$, then $p \mid a$ and $p \mid b$. Suppose $p \nmid b$. By [[Bézout's identity|0DQVHMYAGA]], there is an integer $c$ with $bc \equiv 1 \pmod p$.
10. Multiplying $a^2 + b^2 \equiv 0$ by $c^2$ gives $(ac)^2 \equiv -1 \pmod p$, against step 8. So $p \mid b$, and then $p \mid a^2$, so $p \mid a$ since $p$ is prime.
11. Now let $\alpha = a + bi$ and $\beta$ be Gaussian integers with $p \mid \alpha\beta$ and $p \nmid \alpha$. We show $p \mid \beta$.
12. Since $p \nmid \alpha$, $p$ does not divide both $a$ and $b$. By the claim, $p \nmid N(\alpha) = a^2 + b^2$.
13. As $p$ is prime, $\gcd(N(\alpha), p) = 1$. By Bézout's identity, $u N(\alpha) + v p = 1$ for some integers $u$, $v$.
14. Then $\beta = u N(\alpha) \beta + v p \beta = u \bar\alpha (\alpha\beta) + v p \beta$. Both terms are divisible by $p$ in $\mathbb{Z}[i]$, so $p \mid \beta$.
15. By steps 7 and 14, $p$ is a Gaussian prime when $p \equiv 3 \pmod 4$.
16. By steps 3, 6 and 15, $p$ is a Gaussian prime if and only if $p \equiv 3 \pmod 4$.

## Idea

For $p = 2$ and $p \equiv 1 \pmod 4$, the prime is a product $(a + bi)(a - bi)$ and divides this product without dividing either factor.
For $p \equiv 3 \pmod 4$, the fact that $-1$ is not a square mod $p$ makes $N(\alpha)$ prime to $p$ whenever $p \nmid \alpha$.
Then a Bézout relation lets us cancel $\alpha$ from $p \mid \alpha\beta$, as for ordinary primes.
