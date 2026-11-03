---
tag: FT5DFRMR3M
kind: definition
name: Rindler coordinates
msc: [83A05, 53B30]
defines: TWXJH5ZEHA
uses: [G49G4R1K04, 01PPDSDP2N]
sources:
  - url: https://en.wikipedia.org/wiki/Rindler_coordinates
---

## Definition

Let $M$ be [[Minkowski space|G49G4R1K04]] with inertial coordinates $(t, x, y, z)$ and metric $ds^2 = -c^2 dt^2 + dx^2 + dy^2 + dz^2$.
The *Rindler wedge* is the region $W = \set{(t, x, y, z) : x > \abs{ct}}$.
*Rindler coordinates* on $W$ are $(\eta, \rho, y, z)$, with $\eta \in \R$ and $\rho > 0$, given by
$$ct = \rho \sinh\eta, \qquad x = \rho \cosh\eta.$$
The coordinates $y$ and $z$ are unchanged, and $\sinh$ and $\cosh$ are the [[hyperbolic functions|01PPDSDP2N]].
In these coordinates the metric is
$$ds^2 = -\rho^2 \, d\eta^2 + d\rho^2 + dy^2 + dz^2.$$

## Remarks

Check of the metric: $c \, dt = \sinh\eta \, d\rho + \rho \cosh\eta \, d\eta$ and $dx = \cosh\eta \, d\rho + \rho \sinh\eta \, d\eta$.
Then $dx^2 - c^2 dt^2 = (\cosh^2\eta - \sinh^2\eta)(d\rho^2 - \rho^2 d\eta^2) = d\rho^2 - \rho^2 d\eta^2$, since the cross terms cancel.
The map $(\eta, \rho) \mapsto (\rho \sinh\eta, \rho \cosh\eta)$ is a bijection from $\R \times (0, \infty)$ onto the wedge $x > \abs{ct}$, with inverse $\rho = \sqrt{x^2 - c^2 t^2}$ and $\eta = \operatorname{artanh}(ct / x)$.
Non-example: the event $(t, x) = (1/c, 0)$ lies outside $W$ and has no Rindler coordinates, since $x^2 - c^2 t^2 = -1 < 0$.
The curve of fixed $\rho, y, z$ is the world line of an observer with constant proper acceleration $c^2 / \rho$, and its proper time is $\rho \eta / c$.
A common variant uses Rindler time $T = \rho_0 \eta / c$ adapted to the observer at $\rho = \rho_0$.
