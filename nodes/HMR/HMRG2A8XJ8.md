---
tag: HMRG2A8XJ8
kind: definition
name: Jordan triple system
msc: [17C50, 17A40]
defines: M13DZ6YXH1
uses: [04C5ZBG1WT, 000AYPA9AJ, 6C2MCVB8C7]
sources:
  - url: https://en.wikipedia.org/wiki/Triple_system
---

## Definition

Let $F$ be a [[field|04C5ZBG1WT]] of characteristic different from $2$, and let $V$ be a [[vector space|000AYPA9AJ]] over $F$.
A *Jordan triple system* on $V$ is a trilinear map $V \times V \times V \to V$, written $(x, y, z) \mapsto \set{x, y, z}$, such that for all $u, v, x, y, z \in V$:

1. $\set{x, y, z} = \set{z, y, x}$;
2. $\set{u, v, \set{x, y, z}} = \set{\set{u, v, x}, y, z} - \set{x, \set{v, u, y}, z} + \set{x, y, \set{u, v, z}}$.

## Remarks

Example: the real $p \times q$ matrices with $\set{x, y, z} = x y^T z + z y^T x$, where $y^T$ is the transpose.
Clause 1 holds by the form of the formula, and clause 2 follows by expanding both sides into words of the form $a b^T c\, d^T e$.

Example: a [[Jordan algebra|6C2MCVB8C7]] $J$ with $\set{x, y, z} = (xy)z + (zy)x - (zx)y$.
For $J = A^+$ with $A$ associative and $x \circ y = \frac{1}{2}(xy + yx)$, this triple product equals $\frac{1}{2}(xyz + zyx)$.

Non-example: the square matrices with $\set{x, y, z} = xyz$ fail clause 1 whenever $xyz \ne zyx$, for example for the matrix units $x = e_{12}$, $y = e_{21}$, $z = e_{11}$, where $xyz = e_{11}$ and $zyx = 0$.

Clause 2 says that for fixed $u$ and $v$, the map $D(u, v) \colon z \mapsto \set{u, v, z}$ acts on the triple product like a derivation, with $-D(v, u)$ on the middle slot.
