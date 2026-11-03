---
tag: 551BWE5QYZ
kind: definition
name: Quadratic Jordan algebra
msc: [17C10, 17C05]
defines: 7Y1GGAHADG
uses: [0310REJJY8, 0NZ8JA25WK, 6C2MCVB8C7]
sources:
  - url: https://en.wikipedia.org/wiki/Quadratic_Jordan_algebra
---

## Definition

Let $\Phi$ be a [[commutative ring|0310REJJY8]] with unit, and let $J$ be a [[module|0NZ8JA25WK]] over $\Phi$ with an element $1 \in J$.
Let $U \colon J \to \End_\Phi(J)$, $x \mapsto U_x$, be a quadratic map: $U_{\alpha x} = \alpha^2 U_x$ for $\alpha \in \Phi$, and $(x, z) \mapsto U_{x + z} - U_x - U_z$ is bilinear.
For $x, y, z \in J$ put $\set{x, y, z} = (U_{x + z} - U_x - U_z)\, y$, and let $V_{x, y}$ be the map $z \mapsto \set{x, y, z}$.
The triple $(J, U, 1)$ is a *quadratic Jordan algebra* if for all $x, y \in J$:

1. $U_1 = \id_J$;
2. $U_x V_{y, x} = V_{x, y} U_x$;
3. $U_{U_x y} = U_x U_y U_x$;
4. clauses 1 to 3 also hold after extending scalars to $J \otimes_\Phi \Omega$, for every commutative $\Phi$-algebra $\Omega$ with unit.

## Remarks

Example: a unital associative $\Phi$-algebra $A$ with $U_x y = xyx$.
Then $\set{x, y, z} = xyz + zyx$, and clause 1 holds since $1y1 = y$.
Clause 3: $U_{xyx} z = xyx\, z\, xyx = U_x U_y U_x z$.
Clause 2: both $U_x V_{y, x} z$ and $V_{x, y} U_x z$ equal $xyxzx + xzxyx$.
Clause 4 holds because $A \otimes_\Phi \Omega$ is again associative.

Non-example: any $J \ne 0$ with $U_x = 0$ for all $x$ fails clause 1.

If $\frac{1}{2} \in \Phi$, a unital [[Jordan algebra|6C2MCVB8C7]] gives a quadratic Jordan algebra with $U_x y = 2x(xy) - (xx)y$.
Conversely, the product $xy = \frac{1}{2}\set{x, 1, y}$ recovers the Jordan algebra, so the two notions agree.
Clause 3 is called the fundamental formula.
