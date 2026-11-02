---
tag: BRXKAGYEFQ
kind: definition
name: Linear canonical transformation
msc: [44A15, 42A38, 81S30]
defines: 74BXAPVSW8
uses: [0V9PMN0RBH, DPVM34ADZV, SASP14MA1Z, MM0EJ2GDE4]
sources:
  - url: https://en.wikipedia.org/wiki/Linear_canonical_transformation
---

## Definition

Let $M = \begin{pmatrix} a & b \\ c & d \end{pmatrix}$ be a real matrix with $ad - bc = 1$, an element of the [[special linear group|0V9PMN0RBH]] $SL(2, \R)$, and assume $b \ne 0$.
Fix a square root $\sqrt{1/(ib)}$ of the complex number $1/(ib)$.
The *linear canonical transformation* with matrix $M$ sends an integrable function $f \colon \R \to \C$ to the function
$$L_M f(u) = \sqrt{\frac{1}{i b}}\; e^{i\pi \frac{d}{b} u^2} \int_\R e^{-2\pi i \frac{u t}{b}}\, e^{i\pi \frac{a}{b} t^2} f(t)\, dt, \qquad u \in \R.$$

## Remarks

The map $L_M$ is the composite of a multiplication by the chirp $e^{i\pi a t^2 / b}$, a [[Fourier transform|DPVM34ADZV]] rescaled by $1/b$, a multiplication by $e^{i\pi d u^2 / b}$, and the factor $\sqrt{1/(ib)}$ of modulus $\abs{b}^{-1/2}$.
The rescaled Fourier transform multiplies the $L^2$ norm by $\abs{b}^{1/2}$, the factor divides it by the same amount, and the chirps do not change it.
So $L_M$ preserves the $L^2$ norm, and $L_M$ extends to a [[unitary operator|MM0EJ2GDE4]] of $L^2(\R)$, the [[$L^2$ space|SASP14MA1Z]].
For $b = 0$ the transform is defined by $L_M f(u) = \sqrt{d}\, e^{i\pi c d u^2} f(du)$, a scaling followed by a chirp multiplication.
For two matrices one has $L_{M_1} L_{M_2} = \pm L_{M_1 M_2}$; the sign ambiguity comes from the choice of square roots.

Example: $M = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}$, which has determinant $0 \cdot 0 - 1 \cdot (-1) = 1$.
Here $a = d = 0$ and $b = 1$, so $L_M f(u) = \sqrt{1/i} \int_\R e^{-2\pi i u t} f(t)\, dt$.
With $\sqrt{1/i} = e^{-i\pi/4}$, this is $e^{-i\pi/4} \hat f(u)$, the Fourier transform up to a constant phase.
The matrices $\begin{pmatrix} \cos\alpha & \sin\alpha \\ -\sin\alpha & \cos\alpha \end{pmatrix}$ give the fractional Fourier transforms, in the normalization with the kernel $e^{-2\pi i u t}$, up to a constant phase.

Non-example: $M = \begin{pmatrix} 1 & 1 \\ 0 & 2 \end{pmatrix}$ has determinant $2$, so it is not in $SL(2, \R)$ and has no linear canonical transformation.
The formula above does not use $c$, and with $a = 1$, $b = 1$, $d = 2$ it gives the transform of $\begin{pmatrix} 1 & 1 \\ 1 & 2 \end{pmatrix}$, the only matrix of determinant $1$ with these entries $a$, $b$, $d$.
