---
tag: EW8NFTDRYW
kind: example
name: Particle in a box
msc: [81Q05, 81U15, 35J10]
illustrates: [J0S11FEEWK, 3XZFX39KH9]
uses: [VXDEQB46GV, EPZR6H2WJN, J0S11FEEWK, 3XZFX39KH9, 0S9GGTR0EX]
sources:
  - url: https://en.wikipedia.org/wiki/Particle_in_a_box
same_as:
  wikidata: Q909221
  wikipedia: Particle in a box
---

## Example

Let $m > 0$ be the mass of a particle, $L > 0$ the length of the box and $\hbar$ the reduced Planck constant.
The particle moves on the interval $(0, L)$ between infinitely high walls.
The state space is $L^2(0, L)$, and the [[Hamiltonian|VXDEQB46GV]] is
$$H = -\frac{\hbar^2}{2m} \frac{d^2}{dx^2}$$
with the Dirichlet boundary conditions $\psi(0) = \psi(L) = 0$.
Its eigenfunctions, the [[stationary states|J0S11FEEWK]], are
$$\psi_n(x) = \sqrt{\frac{2}{L}} \sin\left(\frac{n \pi x}{L}\right), \qquad E_n = \frac{n^2 \pi^2 \hbar^2}{2 m L^2}, \qquad n = 1, 2, 3, \dots$$

Check: $\psi_n'' = -(n\pi/L)^2 \psi_n$, so $H \psi_n = \frac{\hbar^2}{2m}(n\pi/L)^2 \psi_n = E_n \psi_n$.
Both boundary conditions hold, since $\sin 0 = \sin(n\pi) = 0$.
The normalisation holds, since $\int_0^L \frac{2}{L}\sin^2(n\pi x/L)\, dx = 1$.
These are all eigenfunctions, and they form an [[orthonormal basis|0S9GGTR0EX]] of $L^2(0, L)$, the Fourier sine basis.

So the energy is quantised, every state is a [[bound state|3XZFX39KH9]], and the lowest energy $E_1$ is strictly positive.
A general solution of the [[Schrödinger equation|EPZR6H2WJN]] is $\psi(x, t) = \sum_n c_n \psi_n(x) e^{-i E_n t/\hbar}$ with $\sum_n \abs{c_n}^2 = 1$.
Since $E_n t / \hbar = 2\pi n^2$ at $t = 4 m L^2/(\pi \hbar)$, every state returns to itself at that time.

## Explanations

### L1 human

A particle trapped between two perfectly hard walls can only have certain energies, unlike a classical ball, which can move at any speed.
The allowed wave functions are standing waves that fit an integer number of half wavelengths into the box, like the modes of a guitar string.
The energies grow like $n^2$, and they are larger for a smaller box.
Even the lowest state has positive energy: the particle can never be fully at rest.
