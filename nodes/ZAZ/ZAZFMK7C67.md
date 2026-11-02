---
tag: ZAZFMK7C67
kind: definition
name: Steiner conic
msc: ["51A30", "51N15"]
defines: J2KM2VYA3J
uses: [DANFNN8C4Y, QTZWZR1KWQ, ZT9A6JK8QF]
sources:
  - url: https://en.wikipedia.org/wiki/Steiner_conic
---

## Definition

Let $\Pi$ be a [[projective plane|DANFNN8C4Y]].
For a point $U$, let $B(U)$ be the pencil of all lines through $U$.
For a line $g$, let $R(g)$ be the range of all points on $g$.
For a point $U$ and a line $g$ not through $U$, the maps $B(U) \to R(g)$, $m \mapsto m \cap g$, and its inverse $R(g) \to B(U)$, $P \mapsto PU$, are [[perspectivities|QTZWZR1KWQ]].
A *projectivity* $B(U) \to B(V)$ is a composition of finitely many such perspectivities.
Let $U$ and $V$ be distinct points and let $\pi \colon B(U) \to B(V)$ be a projectivity with $\pi(UV) \ne UV$.
The *Steiner conic* of $\pi$ is the set of points
$$C = \set{m \cap \pi(m) : m \in B(U)}.$$

## Remarks

The condition $\pi(UV) \ne UV$ makes $m$ and $\pi(m)$ distinct lines for every $m$, so each intersection is a single point.
The points $U$ and $V$ lie on $C$: $UV \cap \pi(UV) = V$, and the line $m$ with $\pi(m) = UV$ gives $m \cap UV = U$.

Example: in the [[projective plane|ZT9A6JK8QF]] over a field $F$, let $U = [1 : 0 : 0]$ and $V = [0 : 0 : 1]$.
The lines through $U$ are $by + cz = 0$ and the lines through $V$ are $ax + by = 0$, with $(b, c)$ and $(a, b)$ up to scaling.
Let $\pi$ send $by + cz = 0$ to $bx + cy = 0$; this map is linear in the parameters, and over a field such maps are projectivities.
The line $UV$ is $y = 0$, and $\pi$ sends it to $x = 0$, so $\pi(UV) \ne UV$.
Solving $by + cz = 0$ and $bx + cy = 0$ with $t = -c/b$ gives the points $[t^2 : t : 1]$, and $b = 0$ gives $U$.
So $C$ is the conic $xz = y^2$.

Non-example: let $a$ be a line through neither $U$ nor $V$, and let $\pi(m)$ be the line joining $V$ to $m \cap a$.
Then $\pi(UV) = UV$, so the condition fails.
For $m \ne UV$ the point $m \cap \pi(m)$ is $m \cap a$, so these points are the points of the line $a$ other than $a \cap UV$, not a conic.

In a plane over a field, Steiner's theorem says that the Steiner conics are exactly the non-degenerate [[projective conics|R3TMVHTP3A]].
