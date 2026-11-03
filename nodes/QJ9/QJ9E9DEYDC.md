---
tag: QJ9E9DEYDC
kind: definition
name: Malcev algebra
msc: [17D10]
defines: 9G3TWHYBH9
uses: [CCZ0W5WGWX, 5JJYBJ6A8K, N8K9SSVMRN]
sources:
  - url: https://en.wikipedia.org/wiki/Malcev_algebra
---

## Definition

Let $k$ be a field of characteristic not $2$.
A *Malcev algebra* over $k$ is a vector space $A$ over $k$ with a bilinear product $(x, y) \mapsto xy$ such that:

1. $xx = 0$ for all $x \in A$ (the product is [[anticommutative|CCZ0W5WGWX]]);
2. $(xy)(xz) = ((xy)z)x + ((yz)x)x + ((zx)x)y$ for all $x, y, z \in A$ (Malcev identity).

## Remarks

With the Jacobian $J(x, y, z) = (xy)z + (yz)x + (zx)y$, the Malcev identity is equivalent, for anticommutative products, to $J(x, y, xz) = J(x, y, z)\, x$.

Example: every [[Lie algebra|5JJYBJ6A8K]] is a Malcev algebra, since $J = 0$ makes both sides of $J(x, y, xz) = J(x, y, z)\, x$ vanish.
If $A$ is an [[alternative algebra|N8K9SSVMRN]], then $A$ with the commutator $[x, y] = xy - yx$ is a Malcev algebra.

Non-example: let $A$ have basis $x, y, z$ with $xy = y$, $yx = -y$, $yz = x$, $zy = -x$, and all other products of basis vectors zero.
This product is anticommutative, and $J(x, y, z) = yz + xx + 0 = x$.
In the form $J(u, v, uw) = J(u, v, w)\, u$, take $u = y$, $v = z$, $w = x$.
The left side is $J(y, z, yx) = -J(y, z, y) = 0$, since $J$ is alternating.
The right side is $J(y, z, x)\, y = J(x, y, z)\, y = xy = y \neq 0$.
So the Malcev identity fails.
