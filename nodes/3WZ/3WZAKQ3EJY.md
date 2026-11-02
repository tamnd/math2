---
tag: 3WZAKQ3EJY
kind: definition
name: Perspectivity
msc: [51A05, 51N15]
defines: QTZWZR1KWQ
uses: [DANFNN8C4Y]
sources:
  - url: https://en.wikipedia.org/wiki/Perspectivity
---

## Definition

Let $\ell$ and $m$ be two distinct lines of a [[projective plane|DANFNN8C4Y]], and let $O$ be a point that lies on neither of them.
The *perspectivity* from $\ell$ to $m$ with centre $O$ sends each point $X$ of $\ell$ to the common point of the lines $OX$ and $m$.

## Remarks

The map is a bijection from the points of $\ell$ to the points of $m$; its inverse is the perspectivity from $m$ to $\ell$ with the same centre.
It fixes the common point of $\ell$ and $m$.
A composition of finitely many perspectivities is a *projectivity*.
Dually, let $A$ and $B$ be points and $a$ a line through neither.
The perspectivity with axis $a$ sends each line $x$ through $A$ to the line through $B$ and the point $x \cap a$.

Example: in the real affine plane, completed to $\mathbb{P}^2(\R)$, let $\ell$ be $y = 1$, let $m$ be $y = 2$, and let $O = (0, 0)$.
The perspectivity sends $(t, 1)$ to $(2t, 2)$.
Check: the line through $O$ and $(t, 1)$ is $\set{(st, s)}$, and it meets $y = 2$ at $s = 2$.
The common point of $\ell$ and $m$ is their point at infinity, which is fixed.

Non-example: if the centre $O$ lies on $\ell$, the rule fails at $X = O$, since there is no line $OX$ for $X = O$.
