---
tag: 60MZVF9TJN
kind: example
name: Sinusoidal plane-wave solutions
msc: [78A40, 35Q61]
instance_of: [NM024G378A]
uses: [9BWWD4QK8Y, FSDEQM9SCV, NM024G378A, YZ7Q9DP8RT, XRED3C547P]
sources:
  - url: https://en.wikipedia.org/wiki/Sinusoidal_plane-wave_solutions_of_the_electromagnetic_wave_equation
same_as:
  wikidata: Q7525226
  wikipedia: Sinusoidal plane-wave solutions of the electromagnetic wave equation
---

## Example

Let $c$ be the speed of light, let $k \in \R^3$ be a nonzero wave vector, and put $\omega = c \abs{k}$.
Let $E_0 \in \C^3$ be a complex amplitude with $k \cdot E_0 = 0$.
Define the [[electric field|YZ7Q9DP8RT]] and the [[magnetic field|XRED3C547P]]
$$E(x, t) = \mathrm{Re}\big( E_0 \, e^{i(k \cdot x - \omega t)} \big), \qquad B(x, t) = \frac{1}{\omega} \, k \times E(x, t).$$
These are [[sinusoidal plane waves|NM024G378A]] that solve the source-free [[Maxwell's equations|9BWWD4QK8Y]].

Check, writing $e = e^{i(k \cdot x - \omega t)}$:

1. $\nabla \cdot E = \mathrm{Re}(i \, k \cdot E_0 \, e) = 0$ and $\nabla \cdot B = 0$, because $k \cdot (k \times E) = 0$.
2. $\nabla \times E = \mathrm{Re}(i \, k \times E_0 \, e)$, and $-\partial_t B = -\frac{1}{\omega} k \times \mathrm{Re}(-i \omega E_0 e) = \mathrm{Re}(i \, k \times E_0 \, e)$.
3. $\nabla \times B = \frac{1}{\omega} \mathrm{Re}\big(i \, k \times (k \times E_0) \, e\big) = -\frac{\abs{k}^2}{\omega} \mathrm{Re}(i E_0 e)$, using $k \times (k \times E_0) = k (k \cdot E_0) - \abs{k}^2 E_0$; and $\frac{1}{c^2} \partial_t E = -\frac{\omega}{c^2} \mathrm{Re}(i E_0 e)$, which is the same since $\omega = c \abs{k}$.

So each component solves the [[electromagnetic wave equation|FSDEQM9SCV]], and $E$, $B$ and $k$ are mutually orthogonal with $\abs{B} = \abs{E} / c$.

## Remarks

The direction of $E_0$ is the polarization.
If $k = (0, 0, \abs{k})$, then $E_0 = (1, 0, 0)$ gives linear polarization and $E_0 = (1, i, 0)$ gives circular polarization: at a fixed point, $E$ then has constant length and turns in the $xy$-plane.
The condition $k \cdot E_0 = 0$ is needed: with $E_0$ parallel to $k$, the field $E$ solves the wave equation but $\nabla \cdot E \neq 0$, so it is not a source-free Maxwell field.

## Explanations

### L1 human

The simplest light wave has flat wavefronts and a single frequency.
Its electric field, its magnetic field and its direction of travel are at right angles to each other.
The magnetic field is the electric field turned by a right angle about the direction of travel and divided by $c$.
