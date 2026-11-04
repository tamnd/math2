---
tag: E0VRN67WYX
kind: proof
name: Proof of the power series of cosine
msc: [33B10, 30B10]
proves: 08W5RN375X
uses: [0WB57D9488, 0QNY6ZBXPN, 0W3K3QPEWT, 00R4MWW532, 0V2DV29EGT, 084NGSTWM7, 043SJ5RF59, 0WFCGVMRRC]
sources:
  - url: https://en.wikipedia.org/wiki/Sine_and_cosine
    locator: Series and polynomials
---

## Proof

1. Fix a real $x$. Let $v_n = \frac{(-1)^n x^{2n}}{(2n)!}$ for $n \ge 0$, where $k!$ is the [[factorial|0WFCGVMRRC]].
2. If $x = 0$, then $v_0 = 1$ and $v_n = 0$ for $n \ge 1$, so $\sum \abs{v_n}$ converges.
3. If $x \ne 0$, then $v_n \ne 0$ and $\frac{\abs{v_{n+1}}}{\abs{v_n}} = \frac{x^2}{(2n+1)(2n+2)} \to 0 < 1$.
4. By the [[ratio test|0QNY6ZBXPN]], $\sum v_n$ converges [[absolutely|0W3K3QPEWT]] in this case too.
5. By the [[definition of cosine|0WB57D9488]], $\cos x = \sum_{n=0}^{\infty} v_n = 1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots$.
6. It remains to identify this series as the Maclaurin series. By the [[derivative of sine|00R4MWW532]] and the [[derivative of cosine|0V2DV29EGT]], $\sin' = \cos$ and $\cos' = -\sin$ on $\mathbb{R}$.
7. By induction on $k$, the [[higher derivatives|084NGSTWM7]] exist for all orders: $\cos^{(4k)} = \cos$, $\cos^{(4k+1)} = -\sin$, $\cos^{(4k+2)} = -\cos$ and $\cos^{(4k+3)} = \sin$. So $\cos$ is smooth.
8. In the defining series at $0$, only the first term of the cosine series is nonzero, and every term of the sine series is zero. So $\cos 0 = 1$ and $\sin 0 = 0$.
9. By steps 7 and 8, $\cos^{(m)}(0) = 0$ for odd $m$, $\cos^{(m)}(0) = 1$ for $m = 4k$, and $\cos^{(m)}(0) = -1$ for $m = 4k + 2$.
10. So for $m = 2n$ we get $\cos^{(m)}(0) = (-1)^n$, since $n$ is even exactly when $m = 4k$.
11. The [[Maclaurin series|043SJ5RF59]] $\sum_m \frac{\cos^{(m)}(0)}{m!} x^m$ thus has zero terms for odd $m$, and the term $\frac{(-1)^n x^{2n}}{(2n)!}$ for $m = 2n$.
12. Removing the zero terms, the Maclaurin series of $\cos$ is $\sum_{n=0}^{\infty} \frac{(-1)^n x^{2n}}{(2n)!}$, the series of the statement.

## Idea

The terms shrink like $\frac{1}{(2n)!}$, which beats any power of $x$, so the ratio test gives absolute convergence. With cosine defined by this series, the equality is the definition. The derivatives of $\cos$ at $0$ cycle through $1, 0, -1, 0$, and these values give back the same coefficients.
