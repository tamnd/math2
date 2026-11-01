---
tag: PSR7JAN6HZ
kind: definition
name: Beurling–Ahlfors transform
msc: [42B20, 30C62, 47G10]
defines: TX32GDQ330
uses: [0V3RDQV3ZX, WMXDVF36ZT]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_integral_operators_of_convolution_type
---

## Definition

Let $f \colon \C \to \C$ be a smooth function with compact support.
Its *Beurling–Ahlfors transform* is the function $\mathcal{B} f \colon \C \to \C$ given by the [[principal value|0V3RDQV3ZX]] integral
$$\mathcal{B} f(z) = -\frac{1}{\pi} \lim_{\varepsilon \to 0} \int_{\abs{w - z} > \varepsilon} \frac{f(w)}{(z - w)^2} \, dA(w),$$
where $dA$ is the Lebesgue area measure on $\C$.
The operator $\mathcal{B}$ extends uniquely to a bounded linear operator on $L^p(\C)$ for each $p$ with $1 < p < \infty$, also called the Beurling–Ahlfors transform.

## Remarks

It is a singular integral operator of Calderón–Zygmund type, with the kernel $-\frac{1}{\pi}(z - w)^{-2}$.
The principal value is needed: the kernel has absolute value $\frac{1}{\pi}\abs{z - w}^{-2}$, which is not integrable near $w = z$ in the plane, but its integral over each circle around $z$ is $0$.
With the [[Wirtinger derivatives|WMXDVF36ZT]] $\partial$ and $\bar{\partial}$, it satisfies $\mathcal{B}(\bar{\partial}\varphi) = \partial\varphi$ for every smooth compactly supported $\varphi$.
Example: for $\varphi(z) = e^{-\abs{z}^2}$, $\bar{\partial}\varphi = -z e^{-\abs{z}^2}$ and $\partial\varphi = -\bar{z} e^{-\abs{z}^2}$, so $\mathcal{B}(z e^{-\abs{z}^2}) = \bar{z} e^{-\abs{z}^2}$.
On the Fourier transform side, $\mathcal{B}$ is multiplication by $\bar{\xi}/\xi$, where $\xi = \xi_1 + i\xi_2$ is the frequency variable; as $\abs{\bar{\xi}/\xi} = 1$, it is an isometry of $L^2(\C)$ onto itself.
The norm of $\mathcal{B}$ on $L^p(\C)$ is conjectured by Iwaniec to be $\max(p, p/(p-1)) - 1$; this is an open problem.
