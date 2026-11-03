---
tag: T24WGK9QG7
kind: definition
name: Phase velocity
msc: [78A40, 35L05]
defines: FMDA4DKT0M
uses: [NM024G378A, R5P8M6SBG7]
sources:
  - url: https://en.wikipedia.org/wiki/Phase_velocity
---

## Definition

Let $u(x, t) = a \cos(k \cdot x - \omega t + \phi)$ be a sinusoidal [[plane wave|NM024G378A]] in $\R^d$ with wave vector $k \neq 0$ and angular frequency $\omega$.
Its *phase velocity* is the vector
$$v_p = \frac{\omega}{\abs{k}} \, \frac{k}{\abs{k}},$$
and its *phase speed* is $\omega / \abs{k}$.
For a wave equation with [[dispersion relation|R5P8M6SBG7]] $\omega = W(k)$, the phase velocity at the wave vector $k$ is $W(k) k / \abs{k}^2$.

## Remarks

The set where the phase $k \cdot x - \omega t + \phi$ has a fixed value is a plane that moves along $k / \abs{k}$ with speed $\omega / \abs{k}$; this is what the definition measures.
In a medium with refractive index $n(\omega)$, the dispersion relation $\abs{k} = n(\omega) \omega / c$ gives the phase speed $c / n(\omega)$.

Example: for $u(x, t) = \cos(2x - 6t)$ in one dimension, $k = 2$ and $\omega = 6$, so $v_p = 3$; indeed $u(x + 3s, t + s) = u(x, t)$ for all $s$.

Non-example: the speed of a crest is not $k / \omega$: for the same wave, $k/\omega = 1/3$, and $u(x + s/3, t + s) = \cos(2x - 6t - \tfrac{16}{3} s)$, which changes with $s$.

## Explanations

### L1 human

The phase velocity is frequency divided by wave number.
It is the speed of the crests of a single sinusoidal wave.
