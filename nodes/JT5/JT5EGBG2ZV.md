---
tag: JT5EGBG2ZV
kind: statement
role: proposition
name: Dispersion relation of water waves
msc: [76B15]
uses: [CNCGSCVQB8, R9WC0Z7Z69]
about: [CNCGSCVQB8]
sources:
  - url: https://en.wikipedia.org/wiki/Dispersion_(water_waves)
---

## Statement

Consider the linearised water wave problem of [[Airy wave theory|CNCGSCVQB8]] for water of constant depth $h > 0$.
Let the density be $\rho > 0$, gravity $g > 0$ and surface tension $\sigma \ge 0$.
For $\sigma > 0$ the linearised dynamic condition is $\phi_t + g\eta - \frac{\sigma}{\rho}\eta_{xx} = 0$ at $z = 0$.
A wave $\eta = a\cos(kx - \omega t)$ with $a \neq 0$, wavenumber $k > 0$ and angular frequency $\omega$ is the surface of a solution if and only if
$$\omega^2 = \left(gk + \frac{\sigma k^3}{\rho}\right)\tanh(kh).$$
In particular, without surface tension, the phase speed $c = \omega / k$ and the group velocity $c_g = d\omega / dk$ satisfy:

1. $c = \sqrt{\frac{g}{k}\tanh(kh)}$.
2. $c_g = \frac{c}{2}\left(1 + \frac{2kh}{\sinh(2kh)}\right)$.

## Remarks

The proof looks for a potential of the form $\phi = A(z)\sin(kx - \omega t)$.
Laplace's equation and the bottom condition force $A(z) = B\cosh(k(z + h))$.
The two surface conditions then have a nonzero solution only under the stated relation.
In deep water, $kh \to \infty$, the relation becomes $\omega^2 = gk$, so $c = \sqrt{g/k}$ and $c_g = c/2$.
In shallow water, $kh \to 0$, it becomes $c = c_g = \sqrt{gh}$, independent of $k$, so long waves do not disperse.
With surface tension in deep water, $c^2 = g/k + \sigma k/\rho$ has a minimum at $k = \sqrt{\rho g / \sigma}$; for clean water this wavelength is about $1.7$ cm.

## Explanations

### L1 human

The speed of a water wave depends on its length.
In deep water, long waves outrun short ones: a wave four times as long goes twice as fast.
This is why swell from a distant storm arrives as long, regular waves before the shorter ones.
In very shallow water all long waves travel at the same speed $\sqrt{gh}$, which is how a tsunami crosses an ocean.

### L2 human

The relation is the basic input of linear water wave theory.
Because $c_g \neq c$, the energy of a wave group travels at a different speed from the crests, and in deep water the crests run through the group at twice its speed.
This fact explains the Kelvin wake pattern behind a ship.
The relation also controls the weakly nonlinear theories: expanding $\tanh(kh)$ for small $kh$ gives the dispersive terms of the Boussinesq and Korteweg–de Vries equations.
