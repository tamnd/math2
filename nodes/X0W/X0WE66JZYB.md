---
tag: X0WE66JZYB
kind: definition
name: Twistor theory
msc: ["32L25", "53C28", "83C60"]
defines: YVRVYE0ZWS
uses: [G49G4R1K04, 7GJ4STCNNM, CYPA882RB9, 8NJ7XY6F1S]
sources:
  - url: https://en.wikipedia.org/wiki/Twistor_theory
---

## Definition

*Twistor space* is $\mathbb{T} = \C^4$, with elements written $Z = (\omega, \pi)$ where $\omega, \pi \in \C^2$ are column vectors.
It carries the [[Hermitian form|8NJ7XY6F1S]] $\Sigma(Z) = \omega^* \pi + \pi^* \omega$, of signature $(2,2)$.
*Projective twistor space* is $\mathbb{PT} = \mathbb{CP}^3$, the [[complex projective space|7GJ4STCNNM]] of lines in $\mathbb{T}$.
Identify a point $x = (x^0, x^1, x^2, x^3)$ of complexified [[Minkowski space|G49G4R1K04]] $\C^4$ with the matrix
$$X = \begin{pmatrix} x^0 + x^3 & x^1 + i x^2 \\ x^1 - i x^2 & x^0 - x^3 \end{pmatrix},$$
so that $\det X = (x^0)^2 - (x^1)^2 - (x^2)^2 - (x^3)^2$.
A twistor $Z = (\omega, \pi)$ is *incident* with $x$ if $\omega = i X \pi$.
The *twistor correspondence* sends $x$ to the set $L_x \subseteq \mathbb{PT}$ of classes of nonzero twistors incident with $x$.
*Twistor theory* is the study of spacetime geometry and field equations through this correspondence.

## Remarks

For each $x$, the incident twistors form the 2-dimensional subspace $\set{(iX\pi, \pi) : \pi \in \C^2}$, so $L_x$ is a projective line.
This gives a bijection between complexified Minkowski space and the lines of $\mathbb{PT}$ that do not meet the line $I = \set{\pi = 0}$.
All lines of $\mathbb{PT}$ form the [[Grassmannian|CYPA882RB9]] $\mathrm{Gr}(2, 4)$, a compactification of complexified Minkowski space.
Example: if $x$ is real, then $X$ is Hermitian, and for $\omega = iX\pi$ one gets $\Sigma(Z) = -i \pi^* X \pi + i \pi^* X \pi = 0$.
So real points correspond to lines inside the real hypersurface $\mathbb{PN} = \set{\Sigma = 0}$.
Non-example: the line $I$ is not of the form $L_x$ for any point $x$ of complexified Minkowski space, since every $L_x$ contains only twistors with $\pi \ne 0$.
Two points $x, y$ are null separated exactly when $\det(X - Y) = 0$, that is, when the lines $L_x$ and $L_y$ meet.
Many texts write the incidence relation as $\omega^A = i x^{AA'} \pi_{A'}$ in two-component spinor notation, with an extra factor $1/\sqrt{2}$ in $X$.

## Explanations

### L1 human

Twistor space is a four-dimensional complex space in which each spacetime point appears as a complex line.
