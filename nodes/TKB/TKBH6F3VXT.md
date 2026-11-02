---
tag: TKBH6F3VXT
kind: definition
name: Integral transforms of tempered distributions
msc: [46F12, 44A05]
defines: QD1MCREE5A
uses: [GE020MY43M, 8TK1JNG87X, YCK709QB06, 0R0T1VWH5X, 6V59T5KJBX]
sources:
  - url: https://en.wikipedia.org/wiki/Distribution_(mathematical_analysis)
---

## Definition

Let $\mathcal{S}(\R^n)$ be the [[Schwartz space|GE020MY43M]] and $\mathcal{S}'(\R^n)$ the space of [[tempered distributions|8TK1JNG87X]], with pairing $\langle u, \varphi \rangle$.
Let $K \colon \R^n \times \R^n \to \C$ be a measurable kernel and let $T$ be the [[integral transform|YCK709QB06]] $(T\varphi)(x) = \int_{\R^n} K(x, y)\, \varphi(y)\, dy$.
Let $T^t$ be the transform with the transposed kernel, $(T^t\varphi)(y) = \int_{\R^n} K(x, y)\, \varphi(x)\, dx$.
Assume that $T$ and $T^t$ map $\mathcal{S}(\R^n)$ continuously into $\mathcal{S}(\R^n)$.
The *transform* of $u \in \mathcal{S}'(\R^n)$ is the tempered distribution $Tu$ given by
$$\langle Tu, \varphi \rangle = \langle u, T^t \varphi \rangle \quad (\varphi \in \mathcal{S}(\R^n)).$$

## Remarks

The definition agrees with the integral on Schwartz functions: for $f, \varphi \in \mathcal{S}(\R^n)$, [[Fubini's theorem|0R0T1VWH5X]] gives $\int (Tf)\varphi = \iint K(x, y) f(y) \varphi(x)\, dy\, dx = \int f\, (T^t\varphi)$, when the double integral converges absolutely.
Example: the [[Fourier transform|6V59T5KJBX]] has the symmetric kernel $K(x, y) = e^{-2\pi i x \cdot y}$, so $T^t = T$ maps $\mathcal{S}$ onto $\mathcal{S}$.
For the Dirac delta $\delta$ at $0$, $\langle T\delta, \varphi \rangle = (T\varphi)(0) = \int \varphi$, so $T\delta = 1$.
Non-example: the kernel $K(x, y) = e^{xy}$ on $\R$ does not qualify, since for the Schwartz function $\varphi(y) = e^{-\sqrt{1 + y^2}}$ the integral $\int_\R e^{2y} \varphi(y)\, dy$ diverges, so $T\varphi$ is not defined at $x = 2$.
