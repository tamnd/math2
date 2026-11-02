---
tag: PW5SKE8D5R
kind: example
name: Sawtooth wave
msc: [42A16, 42A20]
illustrates: [G12KXDHPPS]
uses: [75ZQW12WY0, 004FH91BN5]
sources:
  - url: https://en.wikipedia.org/wiki/Sawtooth_wave
same_as:
  wikidata: Q1742397
  wikipedia: Sawtooth wave
---

## Example

Let $f$ be the $2\pi$-periodic function with $f(x) = \frac{\pi - x}{2}$ for $0 < x < 2\pi$ and $f(0) = 0$.
Its graph is a sawtooth: it falls linearly from $\frac{\pi}{2}$ to $-\frac{\pi}{2}$ on each period and jumps back up at the multiples of $2\pi$.
It is odd, so its cosine coefficients vanish, and integration by parts gives for $n \ge 1$
$$b_n = \frac{1}{\pi} \int_0^{2\pi} \frac{\pi - x}{2} \sin nx \, dx = \frac{1}{\pi} \cdot \frac{1}{2} \cdot \frac{2\pi}{n} = \frac{1}{n}.$$
So its [[Fourier series|G12KXDHPPS]] is
$$\sum_{n=1}^{\infty} \frac{\sin nx}{n}.$$
The function has bounded variation, so by the [[Dirichlet conditions|75ZQW12WY0]] the series converges to $\frac{\pi - x}{2}$ for $0 < x < 2\pi$, and to $0$ at the [[jumps|004FH91BN5]] $x \in 2\pi\Z$.

## Remarks

At $x = \pi/2$ the series gives $\frac{\pi}{4} = 1 - \frac{1}{3} + \frac{1}{5} - \cdots$, the Leibniz formula.
The coefficients $\frac{1}{n}$ are square summable but not summable, as expected for a function with a jump.
Integrating the series term by term from $0$ to $x$ gives $\sum_{n \ge 1} \frac{1 - \cos nx}{n^2} = \frac{\pi x}{2} - \frac{x^2}{4}$ for $0 \le x \le 2\pi$, and at $x = \pi$ this yields $\sum_{n \text{ odd}} \frac{2}{n^2} = \frac{\pi^2}{4}$.

## Explanations

### L1 human

The sawtooth wave ramps down steadily and then snaps back, like the sweep of an old television beam.
It contains every harmonic, the $n$-th one with amplitude $\frac{1}{n}$.
Because of the snap back, the amplitudes shrink slowly, and many harmonics are needed for a good picture.
