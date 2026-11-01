---
tag: X6XGGH5FPW
kind: object
name: Upper half-plane
msc: [30C20, 11F06]
instance_of: [5K0N8QMV6Q]
uses: [09FTAET5Z4, 0SG74WBFA2, 0V9PMN0RBH]
sources:
  - url: https://en.wikipedia.org/wiki/Upper_half-plane
same_as:
  wikidata: Q3258885
  wikipedia: Upper half-plane
---

## Description

The upper half-plane is the set
$$\mathbb{H} = \set{\tau \in \C : \operatorname{Im} \tau > 0}$$
of [[complex numbers|09FTAET5Z4]] with positive imaginary part.
It is an open subset of $\C$, so it is a [[Riemann surface|5K0N8QMV6Q]].
The group $\mathrm{SL}_2(\R)$ acts on $\mathbb{H}$ by [[Möbius transformations|0SG74WBFA2]] $\tau \mapsto (a\tau + b)/(c\tau + d)$.

## Remarks

The action is well defined because
$$\operatorname{Im}\left(\frac{a\tau + b}{c\tau + d}\right) = \frac{(ad - bc) \operatorname{Im} \tau}{\abs{c\tau + d}^2},$$
which is positive when $ad - bc = 1$ and $\operatorname{Im} \tau > 0$.
The holomorphic bijections of $\mathbb{H}$ onto itself are exactly these Möbius transformations, and they form the group $\mathrm{PSL}_2(\R)$.
The map $\tau \mapsto (\tau - i)/(\tau + i)$ is a biholomorphic map of $\mathbb{H}$ onto the open unit disc.
With the metric $ds^2 = (dx^2 + dy^2)/y^2$, where $\tau = x + iy$, the upper half-plane is a model of the hyperbolic plane, and $\mathrm{PSL}_2(\R)$ acts by isometries.
[[Modular forms|GWKN5VG78A]] are functions on $\mathbb{H}$.

## Explanations

### L1 human

The upper half-plane is the part of the complex plane above the real axis.
It is the stage on which modular forms live.
The [[modular group|VEKV1EM77B]] moves its points around, for example by $\tau \mapsto \tau + 1$ and $\tau \mapsto -1/\tau$, and never pushes them below the axis.
With a suitable way of measuring length, it is a picture of non-Euclidean, hyperbolic geometry.
