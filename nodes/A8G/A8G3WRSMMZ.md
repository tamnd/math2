---
tag: A8G3WRSMMZ
kind: definition
name: Momentum operator
msc: ["81Q10", "47B25"]
defines: 5WG6YTAA6J
uses: [SASP14MA1Z, DPVM34ADZV, DF5RN297GE, 0NEGN5CRSC, CG9JEATW3Q, 7XAKGQQWTP]
sources:
  - url: https://en.wikipedia.org/wiki/Momentum_operator
---

## Definition

Let $\hbar > 0$, and let $\mathcal{F}$ be the unitary [[Fourier transform|DPVM34ADZV]] on [[$L^2(\R)$|SASP14MA1Z]], given for integrable $\psi$ by
$$(\mathcal{F}\psi)(k) = \hat\psi(k) = \frac{1}{\sqrt{2\pi}} \int_\R \psi(x) e^{-ikx}\, dx.$$
The *momentum operator* $P$ is the operator with domain
$$D(P) = \set{\psi \in L^2(\R) : \int_\R k^2 \abs{\hat\psi(k)}^2 \, dk < \infty}$$
given by $P\psi = \mathcal{F}^{-1}\big(\hbar k\, \hat\psi(k)\big)$.

## Remarks

For $\psi$ in the [[Schwartz space|CG9JEATW3Q]] $\mathcal{S}(\R)$, $\widehat{\psi'}(k) = ik\hat\psi(k)$, so $P\psi = -i\hbar\, \psi'$.
More generally $D(P)$ is the Sobolev space $H^1(\R)$ and $P\psi = -i\hbar\, \psi'$ with the weak derivative.
Since $\mathcal{F}$ is unitary, $P = \mathcal{F}^{-1} (\hbar \hat X) \mathcal{F}$, where $\hat X$ is the [[position operator|7XAKGQQWTP]] in the variable $k$.
So $P$ is [[self-adjoint|0NEGN5CRSC]], an [[observable|DF5RN297GE]], with spectrum $\R$ and no eigenvalues.
In $\R^n$, $P_j = -i\hbar\, \partial/\partial x_j$ is defined in the same way with $k_j$.

Example: $\psi(x) = \pi^{-1/4} e^{-x^2/2}$ is a Schwartz function, and $P\psi = -i\hbar \psi' = i\hbar x\psi$.
So $\ip{\psi}{P\psi} = i\hbar \int x \pi^{-1/2} e^{-x^2}\, dx = 0$.

Non-example: the indicator $\psi = \mathbf{1}_{[0, 1]}$ is in $L^2(\R)$, with $\hat\psi(k) = (1 - e^{-ik})/(ik\sqrt{2\pi})$ for $k \ne 0$.
Then $k^2 \abs{\hat\psi(k)}^2 = \abs{1 - e^{-ik}}^2/(2\pi) = (1 - \cos k)/\pi$, which is not integrable over $\R$, so $\psi \notin D(P)$.
