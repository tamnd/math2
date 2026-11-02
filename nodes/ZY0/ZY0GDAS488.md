---
tag: ZY0GDAS488
kind: definition
name: Bäcklund transform
msc: [37K35, 35Q51, 35Q53]
defines: SS62J715AZ
uses: [GC5BDZ6QBC, 09EGC6F8PT]
sources:
  - url: https://en.wikipedia.org/wiki/B%C3%A4cklund_transform
---

## Definition

Let $E_1$ and $E_2$ be two [[partial differential equations|GC5BDZ6QBC]] for real functions of two variables $(x, y)$.
A *Bäcklund transform* between $E_1$ and $E_2$ is a system of first-order equations
$$v_x = F(x, y, u, v, u_x, u_y), \qquad v_y = G(x, y, u, v, u_x, u_y)$$
with these two properties.

1. The compatibility condition $(v_x)_y = (v_y)_x$ of the system, for an unknown $v$, holds exactly when $u$ satisfies $E_1$.
2. Each pair $(u, v)$ of solutions of the system has $v$ solving $E_2$.

When $E_1 = E_2$, it is called an *auto-Bäcklund transform*.

## Remarks

Example: the Cauchy–Riemann system $v_x = -u_y$, $v_y = u_x$ is an auto-Bäcklund transform of Laplace's equation $u_{xx} + u_{yy} = 0$.
Indeed $(v_x)_y = -u_{yy}$ and $(v_y)_x = u_{xx}$, so the system is compatible exactly when $u_{xx} + u_{yy} = 0$.
Then $v_{xx} + v_{yy} = -u_{yx} + u_{xy} = 0$ for $C^2$ functions, so $v$ is harmonic too.

Example: for a constant $a \ne 0$, the system
$$\Big(\frac{v - u}{2}\Big)_x = a \sin\frac{u + v}{2}, \qquad \Big(\frac{u + v}{2}\Big)_y = \frac{1}{a} \sin\frac{v - u}{2}$$
is an auto-Bäcklund transform of the [[sine-Gordon equation|802QSF9NM3]] $\varphi_{xy} = \sin \varphi$.
With $s = (u + v)/2$ and $d = (v - u)/2$, one gets $d_{xy} = \cos s \sin d$ and $s_{xy} = \cos d \sin s$, so $u_{xy} = \sin(s - d) = \sin u$ and $v_{xy} = \sin(s + d) = \sin v$.

Non-example: the system $v_x = u_x$, $v_y = u_y$ is compatible for every $C^2$ function $u$.
So it imposes no equation on $u$, and it is not a Bäcklund transform between two equations.

## Explanations

### L1 human

A Bäcklund transform is a pair of first-order equations that ties a new function $v$ to a known function $u$.
It can only be solved when $u$ solves a given equation, and then $v$ solves a given equation as well.
