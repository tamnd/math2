---
tag: MNXKTXJ35G
kind: concept
name: Helmholtz equation
msc: [35J05]
specializes: [GC5BDZ6QBC]
sources:
  - url: https://en.wikipedia.org/wiki/Helmholtz_equation
same_as:
  wikidata: Q860615
  wikipedia: Helmholtz equation
---

## Summary

The Helmholtz equation is the equation $\Delta u + k^2 u = 0$, where $\Delta$ is the [[Laplacian|0E0B6RA8K0]] and $k$ is a constant called the wave number.
It describes waves of a single frequency, and it arises when the time variable is separated in the [[wave equation|5EHD2XBQDG]].
It appears in acoustics, electromagnetism, quantum mechanics and scattering theory.
For $k = 0$ it becomes Laplace's equation.

## Explanations

### L1 human

Think of a drum or an organ pipe that vibrates at one fixed pitch.
At each point the motion goes up and down in time like $\cos(\omega t)$, and only the amplitude $u(x)$ changes from place to place.
The amplitude then satisfies the Helmholtz equation, with $k$ proportional to the frequency.
On a line, $u(x) = \sin(kx)$ is a solution: its second derivative is $-k^2 \sin(kx)$, which cancels $k^2 u$.
