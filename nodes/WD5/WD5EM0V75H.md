---
tag: WD5EM0V75H
kind: definition
name: Brane
msc: [81T30, "83E30"]
defines: DJAATX710N
uses: [BY4QYYS788, VKFW27WXEZ]
sources:
  - url: https://en.wikipedia.org/wiki/Brane
---

## Definition

Let $(M, g)$ be a $D$-dimensional [[Lorentzian manifold|BY4QYYS788]] and let $0 \le p \le D - 1$.
A *$p$-brane* in $M$ is an extended object whose history is a $(p+1)$-dimensional [[submanifold|VKFW27WXEZ]] $W \subset M$, its worldvolume, on which the induced metric $h = g|_W$ is Lorentzian.
In the simplest case its dynamics is given by the Nambu–Goto–Dirac action
$$S[W] = -T_p \int_W \sqrt{-\det h_{\alpha\beta}} \; d^{p+1}\sigma.$$
Here $\sigma^\alpha$ are coordinates on $W$, $h_{\alpha\beta}$ are the components of $h$, and $T_p > 0$ is a constant, the tension of the brane.

## Remarks

The action is $-T_p$ times the $(p+1)$-volume of $W$, so the classical worldvolumes are those of stationary volume.
Example: for $p = 0$, $W$ is a timelike curve and $S$ is $-T_0$ times its proper time.
This is the action of a free relativistic particle of mass $T_0$, in units $c = 1$.
For $p = 1$ one gets the Nambu–Goto action of a string.
Non-example: a spacelike surface in $M$ is not the worldvolume of a brane, since its induced metric is not Lorentzian.
A D$p$-brane in string theory is a $p$-brane on which open strings can end, with Dirichlet boundary conditions in the normal directions.
Its action, the Dirac–Born–Infeld action, also contains a gauge field on $W$.
