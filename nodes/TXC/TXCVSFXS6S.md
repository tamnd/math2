---
tag: TXCVSFXS6S
kind: definition
name: Love numbers
msc: [86A30, 74B05]
defines: C8HCN8NEQP
uses: [2E2KCFNMHE, 3F32Y21HP4, 6W00ZECYT0]
sources:
  - url: https://en.wikipedia.org/wiki/Love_number
---

## Definition

Let a planet be a spherically symmetric, non-rotating, [[linearly elastic|6W00ZECYT0]] and isotropic body of radius $R$ with surface gravity $g$.
Let an external potential act on it, for example a term of the [[tide-generating potential|2E2KCFNMHE]].
Assume its value on the surface $r = R$ is $W_n$, a [[spherical harmonic|3F32Y21HP4]] of degree $n \ge 2$.
By linearity and symmetry, the static response at the surface has the form

1. radial displacement $u_r = h_n\, W_n / g$;
2. horizontal displacement $u_H = (l_n / g)\, R\, \nabla_H W_n$, where $\nabla_H$ is the horizontal gradient;
3. additional potential, due to the deformation, equal to $k_n W_n$ on the surface;

for constants $h_n, l_n, k_n$ that depend only on $n$ and the internal structure.
These constants are the *Love numbers* of degree $n$; $l_n$ is also called the Shida number.

## Remarks

Example: for a perfectly rigid body nothing moves and no mass is redistributed, so $h_n = l_n = k_n = 0$ for all $n$.
For the Earth, $h_2 \approx 0.6$, $k_2 \approx 0.3$ and $l_2 \approx 0.08$.
Non-example: a body with a laterally varying interior does not have Love numbers in this sense, because its response to $W_n$ contains harmonics of other degrees and orders.
The combination $1 + k_2 - h_2 \approx 0.7$ reduces the ocean tide relative to the sea floor, and $1 + k_2$ is the factor by which the Earth's own deformation increases the tidal change of gravity potential.
Load Love numbers, written $h_n'$, $l_n'$, $k_n'$, describe the response to a surface load instead of an external potential.
