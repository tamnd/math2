---
tag: DGB4ZFX265
kind: definition
name: Complex potential
msc: [76B99, 76M40]
defines: Q4DVPTBHEE
uses: [84K7TEWZ2Z, 470A1RJWBP, E66111XRRA, 0NAHXR1FRH]
sources:
  - url: https://en.wikipedia.org/wiki/Potential_flow
---

## Definition

Let $\Omega \subseteq \C$ be a simply connected open set, with $z = x + i y$.
Let $(u, v)$ be a $C^1$ velocity field on $\Omega$ that is incompressible, $u_x + v_y = 0$, and irrotational, $v_x - u_y = 0$.
Then there are a [[velocity potential|470A1RJWBP]] $\varphi$ and a [[stream function|E66111XRRA]] $\psi$ on $\Omega$ with
$$u = \varphi_x = \psi_y, \qquad v = \varphi_y = -\psi_x.$$
The *complex potential* of the flow is the function $w = \varphi + i \psi \colon \Omega \to \C$.
It is [[holomorphic|0NAHXR1FRH]], and its derivative is the complex conjugate of the velocity:
$$w'(z) = u - i v.$$

## Remarks

The equations $\varphi_x = \psi_y$ and $\varphi_y = -\psi_x$ are the Cauchy–Riemann equations, which is why $w$ is holomorphic.
Then $w' = \varphi_x + i \psi_x = u - i v$.
Conversely, every holomorphic $w$ on $\Omega$ is the complex potential of a plane incompressible irrotational flow, with velocity $\overline{w'(z)}$.
The potentials are determined up to additive constants.

Example: $w(z) = z^2/2$ has $\varphi = (x^2 - y^2)/2$ and $\psi = x y$.
Then $w'(z) = x + i y$, so $(u, v) = (x, -y)$, the stagnation point flow, and indeed $u_x + v_y = 0$ and $v_x - u_y = 0$.

Non-example: the rigid rotation $(u, v) = (-y, x)$ has $v_x - u_y = 2 \ne 0$, so it has no complex potential.
Indeed $u - i v = -y - i x = -i \bar z$, which is not a holomorphic function of $z$.

On a domain that is not simply connected, such as $\C \setminus \set{0}$, the complex potential can be multivalued; the point vortex has $w = \frac{\Gamma}{2 \pi i} \log z$.
