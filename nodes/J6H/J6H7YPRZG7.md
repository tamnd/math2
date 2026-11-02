---
tag: J6H7YPRZG7
kind: definition
name: Sine and cosine series
msc: [42A16, 42A20]
defines: Y6EPBG6S8G
uses: [X7GTF3D98F, FZK2M8KGXQ, G12KXDHPPS]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_series
---

## Definition

Let $f \colon [0, \pi] \to \R$ be Lebesgue [[integrable|X7GTF3D98F]].
For $n \ge 0$ put
$$a_n = \frac{2}{\pi} \int_0^\pi f(x) \cos nx \, dx, \qquad b_n = \frac{2}{\pi} \int_0^\pi f(x) \sin nx \, dx.$$
The *Fourier cosine series* of $f$ is the [[trigonometric series|FZK2M8KGXQ]] $\frac{a_0}{2} + \sum_{n=1}^{\infty} a_n \cos nx$.
The *Fourier sine series* of $f$ is the trigonometric series $\sum_{n=1}^{\infty} b_n \sin nx$.

## Remarks

The cosine series is the [[Fourier series|G12KXDHPPS]] of the even $2\pi$-periodic function equal to $f$ on $[0, \pi]$.
The sine series is the Fourier series of the odd $2\pi$-periodic function equal to $f$ on $(0, \pi)$.
Example: for $f(x) = x$ on $[0, \pi]$, integration by parts gives $b_n = \frac{2(-1)^{n+1}}{n}$, so the sine series is $2 \sum_{n \ge 1} \frac{(-1)^{n+1}}{n} \sin nx$.
For the same $f$, $a_0 = \pi$, $a_n = 0$ for even $n \ge 2$ and $a_n = -\frac{4}{\pi n^2}$ for odd $n$.
Non-example: $f(x) = 1/x$ on $(0, \pi]$ is not integrable on $[0, \pi]$, so its sine and cosine coefficients are not defined.
