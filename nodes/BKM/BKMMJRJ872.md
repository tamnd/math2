---
tag: BKMMJRJ872
kind: definition
name: Describing function
msc: [93C10, 93C80]
defines: F1Y5PYXKPS
uses: [G12KXDHPPS, 0ATF6Q0633, 0W29TBTY12]
sources:
  - url: https://en.wikipedia.org/wiki/Describing_function
---

## Definition

Let $f \colon \R \to \R$ be a function that is Riemann integrable on bounded intervals, viewed as a static nonlinear element with input $x$ and output $f(x)$.
For an amplitude $A > 0$, the input $x(\theta) = A \sin \theta$ gives the $2\pi$-[[periodic|0ATF6Q0633]] output $f(A \sin \theta)$.
Let
$$a_1(A) = \frac{1}{\pi} \int_0^{2\pi} f(A \sin \theta) \cos \theta \, d\theta, \qquad b_1(A) = \frac{1}{\pi} \int_0^{2\pi} f(A \sin \theta) \sin \theta \, d\theta$$
be its first [[Fourier coefficients|G12KXDHPPS]].
The *describing function* of $f$ is
$$N(A) = \frac{b_1(A) + i\, a_1(A)}{A}.$$

## Remarks

The first harmonic of the output is $b_1 \sin \theta + a_1 \cos \theta = \operatorname{Re}\bigl(A N(A) e^{i(\theta - \pi/2)}\bigr)$, so $N(A)$ is the complex gain from the input sinusoid to the first harmonic.
If $f$ is odd, then $a_1 = 0$ and $N(A) = b_1(A)/A$ is real.
For elements with memory, such as hysteresis, the same formula with the periodic steady-state output gives a complex $N(A)$.
Consider a loop with a linear part $G$ and the element $f$ in negative feedback.
There the harmonic balance condition $G(i\omega) = -1/N(A)$ predicts a limit cycle of amplitude about $A$ and frequency about $\omega$.

Example: for the ideal relay $f(x) = M \sgn x$ with $M > 0$, $a_1 = 0$ and $b_1 = \frac{1}{\pi} \int_0^{2\pi} M \abs{\sin \theta} \, d\theta = 4M/\pi$, so $N(A) = 4M/(\pi A)$.

Example: for $f(x) = x^3$, $\sin^3 \theta = (3 \sin \theta - \sin 3\theta)/4$ gives $b_1 = 3A^3/4$ and $N(A) = 3A^2/4$.
The term $-\frac{A^3}{4} \sin 3\theta$ of the output is the third harmonic that the describing function ignores.

Contrast: for a linear element $f(x) = kx$, the describing function is the constant $k$; it does not depend on $A$, and it is the exact gain, not an approximation.
