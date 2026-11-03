---
tag: F03RHFMPKC
kind: example
name: Landau levels
msc: [81Q05, 81V70, 81Q10]
illustrates: [VXDEQB46GV]
uses: [VXDEQB46GV, F7194XX840, XRED3C547P]
sources:
  - url: https://en.wikipedia.org/wiki/Landau_levels
same_as:
  wikidata: Q277967
  wikipedia: Landau levels
---

## Example

Let a particle of mass $m > 0$ and charge $q > 0$ move in the plane $\R^2$.
It feels a uniform [[magnetic field|XRED3C547P]] of strength $B > 0$ perpendicular to the plane.
In the Landau gauge the vector potential is $A(x, y) = (0, Bx)$, and the [[Hamiltonian|VXDEQB46GV]] on $L^2(\R^2)$ is
$$H = \frac{1}{2m} \left( p_x^2 + (p_y - qBx)^2 \right), \qquad p_x = -i\hbar \partial_x, \quad p_y = -i\hbar \partial_y.$$
The spectrum of $H$ consists of the *Landau levels*
$$E_n = \hbar \omega_c \left( n + \tfrac12 \right), \qquad n = 0, 1, 2, \ldots, \qquad \omega_c = \frac{qB}{m},$$
and each level is an eigenvalue of infinite multiplicity.

Check: try $\psi(x, y) = e^{iky} f(x)$ with $k \in \R$.
Then $p_y$ acts as $\hbar k$, and with $x_k = \hbar k/(qB)$,
$$H\psi = e^{iky} \left( -\frac{\hbar^2}{2m} f'' + \frac12 m \omega_c^2 (x - x_k)^2 f \right).$$
This is the [[quantum harmonic oscillator|F7194XX840]] centred at $x_k$, so $f$ can be its $n$-th eigenfunction with energy $E_n$, for every $k$.
Wave packets in $k$ of these functions give square-integrable eigenfunctions, and since $k$ is free each level is infinitely degenerate.

## Remarks

On a large region of area $S$, the number of states in one level is approximately $qBS/(2\pi\hbar)$, that is, one state per flux quantum $2\pi\hbar/q$.
The levels and their degeneracy are the starting point of the theory of the quantum Hall effect.

## Explanations

### L1 human

A charged particle in a magnetic field moves in circles.
In quantum mechanics the circular motion is quantised, and the allowed energies form a ladder with equal steps $\hbar qB/m$, exactly like a spring.
Each rung of the ladder holds a huge number of states, one for each possible centre of the circle, so the levels are highly degenerate.
