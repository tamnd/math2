---
tag: Q7XAMPJRWG
kind: definition
name: Anharmonic oscillator
msc: [70K25, 70K30, 34C15]
defines: 4Z5EQ17Q60
uses: [0YG0ZJPTWG, 0NT64JV96A, 0SHPXM2HWH, SGQQGP261M]
sources:
  - url: https://en.wikipedia.org/wiki/Anharmonicity
---

## Definition

Let $I$ be an open interval containing $0$, let $m > 0$, and let $V \colon I \to \R$ be a smooth function with $V(0) = 0$, $V'(0) = 0$ and $V''(0) = k > 0$.
The oscillator with mass $m$ and potential $V$ is the [[ordinary differential equation|0NT64JV96A]]
$$m \, x''(t) = - V'(x(t))$$
for the displacement $x(t) \in I$.
It is *anharmonic* if $V$ is not the quadratic function $x \mapsto \frac{k}{2} x^2$ on $I$, that is, if the restoring force $-V'(x)$ is not linear in $x$.

## Remarks

The [[pendulum equation|0SHPXM2HWH]] $\theta'' + \frac{g}{\ell} \sin \theta = 0$ is anharmonic: here $m = 1$ and $V(\theta) = \frac{g}{\ell} (1 - \cos \theta)$ on $I = (-\pi, \pi)$, which is not quadratic since $V(\theta) = \frac{g}{2\ell} \theta^2 - \frac{g}{24 \ell} \theta^4 + O(\theta^6)$.
The undamped, unforced [[Duffing equation|SGQQGP261M]] $x'' + \alpha x + \beta x^3 = 0$ with $\alpha > 0$ and $\beta \neq 0$ is anharmonic too, with $V(x) = \frac{\alpha}{2} x^2 + \frac{\beta}{4} x^4$.
The [[harmonic oscillator|0YG0ZJPTWG]] $m x'' + k x = 0$ is not anharmonic: its potential is exactly $\frac{k}{2} x^2$.

The terms of order three and higher in the Taylor expansion of $V$ at $0$ are called the anharmonic terms.
Solutions of small amplitude oscillate with angular frequency close to $\sqrt{k/m}$, and in general the period depends on the amplitude.

## Explanations

### L1 human

An anharmonic oscillator is a mass moving back and forth in a potential well that is not exactly a parabola.
Near the bottom of the well it behaves almost like a spring, but for larger swings it does not.
