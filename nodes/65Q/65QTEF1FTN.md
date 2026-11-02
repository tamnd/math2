---
tag: 65QTEF1FTN
kind: definition
name: Discrete-time Fourier transform
msc: ["42A16", "94A12", "42A38"]
defines: RXFJ47VYGX
uses: [SASP14MA1Z, 07GJV36896, G12KXDHPPS]
sources:
  - url: https://en.wikipedia.org/wiki/Discrete-time_Fourier_transform
---

## Definition

Let $x = (x_n)_{n \in \Z}$ be an absolutely summable sequence of complex numbers, that is, $x \in \ell^1(\Z)$, a case of the [[$L^p$ spaces|SASP14MA1Z]].
The *discrete-time Fourier transform* of $x$ is the function $X \colon \R \to \C$ given by
$$X(\omega) = \sum_{n \in \Z} x_n\, e^{-i \omega n}, \qquad \omega \in \R,$$
where $e^{-i\omega n}$ is the [[complex exponential|07GJV36896]].

## Remarks

The series converges absolutely and uniformly in $\omega$, so $X$ is continuous and $2\pi$-periodic, with $\abs{X(\omega)} \le \sum_n \abs{x_n}$.
The sequence is recovered by
$$x_n = \frac{1}{2\pi} \int_{-\pi}^{\pi} X(\omega)\, e^{i \omega n}\, d\omega,$$
so $x_{-n}$ is the $n$-th coefficient of the [[Fourier series|G12KXDHPPS]] of $X$.

Example: for $\abs{a} < 1$, let $x_n = a^n$ for $n \ge 0$ and $x_n = 0$ for $n < 0$.
Then $\sum_n \abs{x_n} = 1/(1 - \abs{a}) < \infty$, and the geometric series gives $X(\omega) = \sum_{n \ge 0} (a e^{-i\omega})^n = \frac{1}{1 - a e^{-i\omega}}$.

Non-example: the constant sequence $x_n = 1$ is not absolutely summable, and $\sum_n e^{-i\omega n}$ diverges for every $\omega$ because its terms do not tend to $0$.
As a distribution its transform is a Dirac comb of period $2\pi$, scaled by $2\pi$.

By the Riesz–Fischer and Parseval theorems the transform extends to an isometry, up to the factor $2\pi$, from $\ell^2(\Z)$ onto $L^2$ of a period, with the series converging in $L^2$.
Some authors use the frequency $f = \omega / (2\pi)$, which gives period $1$.
