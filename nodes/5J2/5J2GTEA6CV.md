---
tag: 5J2GTEA6CV
kind: definition
name: Nonlinear Schrödinger equation
msc: [35Q55, 35Q51]
defines: GEJHRXC176
uses: [GC5BDZ6QBC, EPZR6H2WJN, 0E0B6RA8K0]
sources:
  - url: https://en.wikipedia.org/wiki/Nonlinear_Schrödinger_equation
---

## Definition

Let $d \ge 1$ be an integer, let $p > 1$ be a real number, and let $\mu \in \set{1, -1}$.
The *nonlinear Schrödinger equation* with power nonlinearity is the [[partial differential equation|GC5BDZ6QBC]]
$$i \partial_t u + \Delta u = \mu \abs{u}^{p-1} u$$
for an unknown function $u \colon \R \times \R^d \to \C$, $(t, x) \mapsto u(t, x)$.
Here $\Delta$ is the [[Laplacian|0E0B6RA8K0]] in the variable $x$.
The equation is *defocusing* if $\mu = 1$ and *focusing* if $\mu = -1$.
The case $p = 3$ is the *cubic* nonlinear Schrödinger equation.

## Remarks

Example: for $A \in \C$ and $k \in \R^d$, the plane wave $u(t,x) = A e^{i(k \cdot x - \omega t)}$ is a solution when $\omega = \abs{k}^2 + \mu \abs{A}^{p-1}$.
Indeed $i \partial_t u = \omega u$, $\Delta u = -\abs{k}^2 u$ and $\abs{u}^{p-1} u = \abs{A}^{p-1} u$.

Non-example: the linear [[Schrödinger equation|EPZR6H2WJN]] $i \partial_t u + \Delta u = 0$ corresponds to $\mu = 0$, which the definition excludes.

Smooth solutions that decay at infinity conserve the mass $\int \abs{u}^2 \, dx$ and the energy
$$E(u) = \int_{\R^d} \left( \tfrac{1}{2} \abs{\nabla u}^2 + \tfrac{\mu}{p+1} \abs{u}^{p+1} \right) dx.$$
Some authors write the equation as $i \partial_t u = -\Delta u + \mu \abs{u}^{p-1} u$, which is the same equation.
