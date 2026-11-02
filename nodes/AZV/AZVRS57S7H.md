---
tag: AZVRS57S7H
kind: statement
role: proposition
name: Green's function and the Riemann map
msc: [31A15, 30C35]
uses: [M36SD56MWQ, 02WHMEG5ZR, 0QW64ARSHB, 0YYT36R4YD, GYEX4BH5WM]
about: [M36SD56MWQ, 0YYT36R4YD]
sources:
  - url: https://en.wikipedia.org/wiki/Riemann_mapping_theorem
---

## Statement

Let $\Omega \subsetneq \C$ be a [[simply connected domain|0QW64ARSHB]] and let $a \in \Omega$.
Let $\varphi \colon \Omega \to \mathbb{D}$ be a [[conformal map|0YYT36R4YD]] of $\Omega$ onto the unit disc $\mathbb{D}$ with $\varphi(a) = 0$; it exists by the [[Riemann mapping theorem|02WHMEG5ZR]].
Then the [[Green's function|M36SD56MWQ]] of $\Omega$ with pole at $a$ is
$$g(z, a) = -\log\abs{\varphi(z)}, \qquad z \in \Omega \setminus \set{a}.$$

## Remarks

Proof idea: since $\varphi$ is injective, $\varphi'(a) \ne 0$, so $\varphi(z) = (z - a) k(z)$ with $k$ holomorphic and zero-free on $\Omega$.
Hence $-\log\abs{\varphi(z)} = -\log\abs{z - a} - \log\abs{k(z)}$, and $\log\abs{k}$ is harmonic on $\Omega$.
Away from $a$, $\log\abs{\varphi}$ is harmonic because $\varphi$ is holomorphic and has no zero.
A conformal map onto $\mathbb{D}$ is proper, so $\abs{\varphi(z)} \to 1$ as $z$ tends to the boundary, and $g(z, a) \to 0$ there.
These are the defining properties, and the Green's function is unique by the maximum principle.
Example: for $\Omega = \mathbb{D}$ and $\varphi(z) = (z - a)/(1 - \bar a z)$, one gets $g(z, a) = \log\abs{(1 - \bar a z)/(z - a)}$.
Near the pole, $g(z, a) = -\log\abs{z - a} + \log\big(1/\abs{\varphi'(a)}\big) + o(1)$, and $1/\abs{\varphi'(a)}$ is the [[conformal radius|GYEX4BH5WM]] of $\Omega$ at $a$.
The hypothesis $\Omega \ne \C$ is needed: the plane has no Green's function, since a positive harmonic function on $\C \setminus \set{a}$ with a logarithmic pole at $a$ does not exist.

## Explanations

### L1 human

For a simply connected region, the Green's function and the Riemann map carry the same information.
The level curves of the Green's function are the images of the circles $\abs{w} = r$ under the inverse of the Riemann map.

### L2 human

The formula can also be read backwards.
If $g^*$ is a harmonic conjugate of $g(\cdot, a)$ on $\Omega \setminus \set{a}$, then $\exp(-(g + i g^*))$ is single-valued and gives the Riemann map.
This is one classical route to the Riemann mapping theorem via potential theory, through the solution of a Dirichlet problem.
On multiply connected domains the conjugate $g^*$ has periods, so $\exp(-(g + i g^*))$ is no longer single-valued.
