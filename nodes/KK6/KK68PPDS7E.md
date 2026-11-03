---
tag: KK68PPDS7E
kind: definition
name: Riemann–Silberstein vector
msc: [78A25, 35Q61]
defines: BPMTXYN9MV
uses: [9BWWD4QK8Y, YZ7Q9DP8RT, XRED3C547P, MTMHQQ47N3]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann%E2%80%93Silberstein_vector
---

## Definition

Let $c > 0$ be the speed of light, and let $E, B \colon \R^3 \times \R \to \R^3$ be an [[electric field|YZ7Q9DP8RT]] and a [[magnetic field|XRED3C547P]].
The *Riemann–Silberstein vector* is the complex vector field
$$F = E + i c B \colon \R^3 \times \R \to \C^3.$$

## Remarks

The pair $(E, B)$ solves the source-free [[Maxwell's equations|9BWWD4QK8Y]] exactly when
$$\nabla \cdot F = 0, \qquad i \, \partial_t F = c \, \nabla \times F.$$
Indeed, the real and imaginary parts of the second equation are $\partial_t B = -\nabla \times E$ and $\partial_t E = c^2 \nabla \times B$, and the first equation contains both Gauss laws.
A [[duality rotation|MTMHQQ47N3]] by the angle $\theta$ maps $F$ to $e^{-i\theta} F$, and $\frac{\varepsilon_0}{2} \abs{F}^2 = \frac{\varepsilon_0}{2} (\abs{E}^2 + c^2 \abs{B}^2)$ is the energy density.
Some authors use $E - icB$ or a normalizing factor such as $\sqrt{\varepsilon_0 / 2}$.

Example: for the plane wave $E = (0, E_0 \cos(kx - \omega t), 0)$, $B = (0, 0, \frac{E_0}{c} \cos(kx - \omega t))$ with $\omega = ck$, one gets $F = E_0 \cos(kx - \omega t) \, (0, 1, i)$.
With $s = \sin(kx - \omega t)$, both $i \partial_t F$ and $c \nabla \times F$ equal $(0, i \omega E_0 s, -\omega E_0 s)$, and $\nabla \cdot F = 0$.

Non-example: $F(x, y, z, t) = (-y, x, 0)$ is a Riemann–Silberstein vector, with $E = (-y, x, 0)$ and $B = 0$, but it does not come from a solution of the source-free equations, since $i \partial_t F = 0$ while $c \nabla \times F = (0, 0, 2c)$.

## Explanations

### L1 human

The definition takes the electric field as real part and $c$ times the magnetic field as imaginary part.
Maxwell's equations in empty space then say that $F$ has no sources and that its time derivative is a fixed multiple of its curl.
This first-order form looks like a Schrödinger equation, which is why it appears in the quantum theory of light.
