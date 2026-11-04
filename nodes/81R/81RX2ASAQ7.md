---
tag: 81RX2ASAQ7
kind: proof
name: Proof that exp(2 pi i/n) is a primitive root of unity
msc: [11R18]
proves: 0CF0XGYHNJ
uses: [0J817RTVG6, 04R3CY41VJ, 0WB57D9488, 03MTBVG3VE, 0P4NQD746K, 05V7J4WD1C, 0ZZRSX91QR, 0SQSQP748R]
sources:
  - url: https://en.wikipedia.org/wiki/Root_of_unity
    locator: Trigonometric expression
---

## Proof

We show that $\zeta = e^{2 \pi i / n}$ is a primitive $n$th root of unity.

1. Let $n \ge 1$ and $\zeta = e^{2 \pi i / n}$. For real arguments the power series of $\cos$ and $\sin$ are the real [[sine and cosine|0WB57D9488]].
So [[Euler's formula|04R3CY41VJ]] gives $\zeta = \cos \frac{2 \pi}{n} + i \sin \frac{2 \pi}{n}$.
2. For each integer $k \ge 1$, [[de Moivre's formula|03MTBVG3VE]] gives $\zeta^k = \cos t_k + i \sin t_k$ with $t_k = 2 \pi k / n$.
3. For $k = n$ we get $t_n = 2 \pi$. Since $\sin$ and $\cos$ are [[$2\pi$-periodic|0P4NQD746K]], $\cos 2 \pi = \cos 0 = 1$ and $\sin 2 \pi = \sin 0 = 0$.
So $\zeta^n = 1$.
4. Now let $1 \le k < n$, so $0 < t_k < 2 \pi$. Assume, for a contradiction, that $\zeta^k = 1$.
5. By [[equality of complex numbers|05V7J4WD1C]], $\cos t_k = 1$ and $\sin t_k = 0$.
6. Let $t = t_k$ if $t_k \le \pi$, and $t = t_k - 2 \pi$ if $t_k > \pi$. In both cases $-\pi < t \le \pi$ and $t \neq 0$.
7. By periodicity, $\cos t = 1$ and $\sin t = 0$. So $1 = 1 \cdot (\cos t + i \sin t)$, and $t$ is an [[argument|0ZZRSX91QR]] of $1$, since $|1| = 1$.
8. Also $0$ is an argument of $1$ in $(-\pi, \pi]$, since $\cos 0 = 1$ and $\sin 0 = 0$.
9. The [[principal value of the argument|0SQSQP748R]] is unique, so $t = 0$. This contradicts step 6.
10. So $\zeta^k \neq 1$ for $1 \le k < n$, and $\zeta^n = 1$ by step 3.
By the definition of a [[primitive root of unity|0J817RTVG6]], $\zeta$ is a primitive $n$th root of unity.

## Idea

The powers $\zeta^k$ are the points of the unit circle at angles $2 \pi k / n$.
For $1 \le k < n$ the angle lies strictly between $0$ and $2 \pi$, so the point is not $1$.
The first power that returns to $1$ is the $n$th.
