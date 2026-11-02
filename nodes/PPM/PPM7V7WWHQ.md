---
tag: PPM7V7WWHQ
kind: definition
name: Cole–Hopf transformation
msc: [35Q35, 35K05, 35A22]
defines: VBMQ9SJ3DH
uses: [NEGHXN8RE1, VP2HN86VAG, 09EGC6F8PT]
sources:
  - url: https://en.wikipedia.org/wiki/Cole%E2%80%93Hopf_transformation
---

## Definition

Let $\nu > 0$, let $I \subseteq \R$ be an open interval, and let $T > 0$.
Let $\varphi \colon I \times (0, T) \to (0, \infty)$ be a positive function with continuous [[partial derivatives|09EGC6F8PT]] $\varphi_t$, $\varphi_x$, $\varphi_{xx}$.
The *Cole–Hopf transformation* of $\varphi$ is the function
$$u = -2\nu\, \frac{\varphi_x}{\varphi} = -2\nu\, \partial_x \log \varphi.$$
Its basic property: if $\varphi$ solves the [[heat equation|VP2HN86VAG]] $\varphi_t = \nu \varphi_{xx}$, then $u$ solves the viscous [[Burgers' equation|NEGHXN8RE1]] $u_t + u u_x = \nu u_{xx}$.

## Remarks

Proof of the basic property: put $\psi = \log \varphi$, so $u = -2\nu \psi_x$.
The heat equation for $\varphi$ becomes $\psi_t = \nu \psi_{xx} + \nu \psi_x^2$.
Differentiating in $x$ and multiplying by $-2\nu$ gives $u_t = \nu u_{xx} - u u_x$.

Inverse direction: given initial values $u_0$, take $\varphi_0(x) = \exp\left(-\frac{1}{2\nu} \int_0^x u_0(y)\, dy\right)$.
Solving the heat equation with data $\varphi_0$ and transforming gives the solution of Burgers' equation with data $u_0$, for bounded continuous $u_0$ on $I = \R$.

Example: $\varphi(x, t) = 1 + e^{-k(x - \nu k t)}$ with $k > 0$ solves $\varphi_t = \nu \varphi_{xx}$, since both sides equal $\nu k^2 e^{-k(x - \nu k t)}$.
Its transformation is $u = \nu k \left(1 - \tanh\left(\tfrac{k}{2}(x - \nu k t)\right)\right)$.
This is a [[traveling wave|M37M411KP7]] of speed $\nu k$ from $2\nu k$ to $0$.

Non-example: $\varphi(x, t) = \sin x$ is not allowed on $\R$, since it is not positive.
Its transformation $-2\nu \cot x$ is undefined at the zeros of $\sin x$.

## Explanations

### L1 human

The transformation takes the logarithmic derivative of a solution of the heat equation.
This one formula converts a linear equation into a nonlinear one.
Read backwards, it solves a nonlinear equation with the tools of a linear one.
