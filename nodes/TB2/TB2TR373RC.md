---
tag: TB2TR373RC
kind: example
name: Square wave
msc: [42A16, 42A20]
illustrates: [G12KXDHPPS, VMF169AT67]
uses: [75ZQW12WY0, 004FH91BN5]
sources:
  - url: https://en.wikipedia.org/wiki/Square_wave_(waveform)
same_as:
  wikidata: Q1136640
  wikipedia: Square wave (waveform)
---

## Example

The *square wave* is the $2\pi$-periodic function $f$ with $f(x) = 1$ for $0 < x < \pi$, $f(x) = -1$ for $-\pi < x < 0$, and $f(0) = f(\pi) = 0$.
It is odd, so its cosine coefficients vanish, and for $n \ge 1$
$$b_n = \frac{2}{\pi} \int_0^\pi \sin nx \, dx = \frac{2 (1 - (-1)^n)}{\pi n},$$
which is $\frac{4}{\pi n}$ for odd $n$ and $0$ for even $n$.
So its Fourier series is
$$\frac{4}{\pi} \left( \sin x + \frac{\sin 3x}{3} + \frac{\sin 5x}{5} + \cdots \right).$$
The function is of bounded variation, so by the [[Dirichlet conditions|75ZQW12WY0]] the series converges at every $x$ to $\frac{1}{2}(f(x^+) + f(x^-))$.
This is $f(x)$ at every $x$, including the points of [[jump discontinuity|004FH91BN5]] $x \in \pi\Z$, where both sides are $0$.

## Remarks

At $x = \pi/2$ the series gives $1 = \frac{4}{\pi}(1 - \frac{1}{3} + \frac{1}{5} - \cdots)$, which is the Leibniz formula for $\pi/4$.
The coefficients decay only like $1/n$, because of the jumps, so the series does not converge absolutely.
The convergence is uniform on every closed interval that avoids $\pi\Z$, but not on $\R$, since the limit is discontinuous.
Near each jump the partial sums overshoot: their maximum just to the right of $0$ tends to $\frac{2}{\pi} \int_0^\pi \frac{\sin t}{t} \, dt \approx 1.179$, the [[Gibbs phenomenon|VMF169AT67]].

## Explanations

### L1 human

The square wave switches between $-1$ and $1$ every half period, like an ideal on-off signal.
It is built from the odd harmonics only, with amplitudes $1, \frac{1}{3}, \frac{1}{5}, \dots$ times $\frac{4}{\pi}$.
Adding more harmonics makes the flat parts flatter and the jumps steeper, but a small spike of about $9\%$ of the jump remains near each jump.
