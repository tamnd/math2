---
tag: 1GRHMHWK7R
kind: definition
name: Simple harmonic motion
msc: [70J30]
defines: 8C19QDA99E
uses: [0YG0ZJPTWG]
sources:
  - url: https://en.wikipedia.org/wiki/Simple_harmonic_motion
---

## Definition

A function $x \colon \R \to \R$ describes *simple harmonic motion* when there are constants $A > 0$, $\omega > 0$ and $\varphi \in \R$ such that
$$x(t) = A \cos(\omega t + \varphi) \quad \text{for all } t \in \R.$$
The number $A$ is the *amplitude*, $\omega$ is the *angular frequency*, $\varphi$ is the *phase*, and $T = 2\pi / \omega$ is the *period*.

## Remarks

Equivalently, $x$ is a nonzero solution of $\ddot x + \omega^2 x = 0$ for some $\omega > 0$, the equation of the [[harmonic oscillator|0YG0ZJPTWG]].
For a mass $m > 0$ on a spring of stiffness $k > 0$, the frequency is $\omega = \sqrt{k/m}$.

Example: $x(t) = 3 \sin(2t) = 3 \cos(2t - \pi/2)$ is simple harmonic motion with $A = 3$, $\omega = 2$ and period $\pi$.
Check: $\ddot x = -12 \sin(2t) = -4 x$.

Non-example: $x(t) = e^{-t} \cos t$ solves $\ddot x + 2 \dot x + 2 x = 0$, but its amplitude decays, so it is not of the form $A \cos(\omega t + \varphi)$ with constant $A$; it is a damped oscillation.
