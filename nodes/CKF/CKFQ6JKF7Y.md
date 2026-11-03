---
tag: CKFQ6JKF7Y
kind: definition
name: Mutually unbiased bases
msc: [81P55, 81P18, 05B25]
defines: 769RHWS4WK
uses: [0S9GGTR0EX, XAQCW3D4QQ]
sources:
  - url: https://en.wikipedia.org/wiki/Mutually_unbiased_bases
---

## Definition

Let $d \ge 2$ and let $\C^d$ carry its standard inner product $\ip{\cdot}{\cdot}$.
Two [[orthonormal bases|0S9GGTR0EX]] $(e_1, \dots, e_d)$ and $(f_1, \dots, f_d)$ of $\C^d$ are *mutually unbiased* if
$$\abs{\ip{e_j}{f_k}}^2 = \frac1d \quad \text{for all } j, k \in \set{1, \dots, d}.$$
A family of orthonormal bases of $\C^d$ is a family of *mutually unbiased bases* if any two distinct bases in it are mutually unbiased.

## Remarks

Example: in $\C^2$, take the standard basis $(\lvert 0 \rangle, \lvert 1 \rangle)$, the basis $(\lvert 0 \rangle \pm \lvert 1 \rangle)/\sqrt2$ and the basis $(\lvert 0 \rangle \pm i\lvert 1 \rangle)/\sqrt2$.
These are the eigenbases of the [[Pauli matrices|XAQCW3D4QQ]] $Z$, $X$ and $Y$.
Each inner product between vectors of different bases has modulus $1/\sqrt2$, so its square is $1/2 = 1/d$.

Non-example: the standard basis and the basis $(\cos t\, \lvert 0 \rangle + \sin t\, \lvert 1 \rangle, -\sin t\, \lvert 0 \rangle + \cos t\, \lvert 1 \rangle)$ with $t = \pi/6$.
Here $\abs{\langle 0 \vert (\cos t\, \lvert 0 \rangle + \sin t\, \lvert 1 \rangle)}^2 = \cos^2 t = 3/4 \ne 1/2$.

In $\C^d$ the standard basis and the Fourier basis $f_k = d^{-1/2}\sum_j e^{2\pi i jk/d} e_j$ are mutually unbiased.
A family of mutually unbiased bases of $\C^d$ has at most $d + 1$ members.
When $d$ is a prime power, a family of $d + 1$ members exists.
For other $d$, such as $d = 6$, the largest size is unknown.
