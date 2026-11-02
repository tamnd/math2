---
tag: F5YG34FAY1
kind: statement
role: theorem
name: Asymptotics of Bessel functions
msc: [33C10, 41A60]
uses: [CZCMRDWDYW, GRSNDJG363, 0H5SYBSED9, 0QR92XBV6H]
about: [CZCMRDWDYW, GRSNDJG363]
sources:
  - url: https://en.wikipedia.org/wiki/Bessel_function
---

## Statement

Let $\nu$ be a real number, and let $J_\nu$ and $Y_\nu$ be the [[Bessel functions of the first kind|CZCMRDWDYW]] and of the [[second kind|GRSNDJG363]].
Let $\Gamma$ be the [[gamma function|0H5SYBSED9]], and let $\sim$ denote [[asymptotic equivalence|0QR92XBV6H]].

1. (Large argument.) As $x \to +\infty$,
$$J_\nu(x) = \sqrt{\frac{2}{\pi x}} \left( \cos\left( x - \frac{\nu\pi}{2} - \frac{\pi}{4} \right) + O\left( \frac{1}{x} \right) \right),$$
$$Y_\nu(x) = \sqrt{\frac{2}{\pi x}} \left( \sin\left( x - \frac{\nu\pi}{2} - \frac{\pi}{4} \right) + O\left( \frac{1}{x} \right) \right).$$
2. (Small argument.) As $x \to 0^+$, if $\nu$ is not a negative integer then $J_\nu(x) \sim \frac{1}{\Gamma(\nu + 1)} \left( \frac{x}{2} \right)^\nu$; if $\nu > 0$ then $Y_\nu(x) \sim -\frac{\Gamma(\nu)}{\pi} \left( \frac{2}{x} \right)^\nu$; and $Y_0(x) \sim \frac{2}{\pi} \ln x$.

## Remarks

The small-argument forms are the leading terms of the power series of $J_\nu$ and of the series of $Y_\nu$ obtained from its definition.
The large-argument forms come from an integral representation of the Hankel functions $H^{(1)}_\nu = J_\nu + iY_\nu$ and the stationary-phase method.
They are the first terms of full asymptotic expansions in powers of $\frac{1}{x}$.
Example: for $\nu = \frac{1}{2}$, $J_{1/2}(x) = \sqrt{\frac{2}{\pi x}} \sin x$ exactly, and indeed $\cos\left( x - \frac{\pi}{2} \right) = \sin x$, with no error term.
The large-argument form holds for fixed $\nu$; it fails when $\nu$ grows with $x$, for instance when $\nu$ is close to $x$, where the transition is described by Airy functions.

## Explanations

### L1 human

Far from the origin a Bessel function looks like a cosine wave whose amplitude shrinks like $\frac{1}{\sqrt{x}}$.
The order $\nu$ only shifts the phase of the wave.
Near the origin $J_\nu$ behaves like the power $x^\nu$, while $Y_\nu$ blows up like $x^{-\nu}$ or like $\ln x$.

### L2 human

The large-argument form explains why the positive zeros of $J_\nu$ are eventually spaced by about $\pi$.
The amplitude $\frac{1}{\sqrt{x}}$ reflects conservation of energy for cylindrical waves, whose wavefronts have length proportional to $x$.
The small-argument forms decide which solution is allowed in a boundary value problem on a disc: regularity at the centre excludes $Y_\nu$.
For modified Bessel functions the analogues are $I_\nu(x) \sim \frac{e^x}{\sqrt{2\pi x}}$ and $K_\nu(x) \sim \sqrt{\frac{\pi}{2x}}\, e^{-x}$.
