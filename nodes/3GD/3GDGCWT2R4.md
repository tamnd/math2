---
tag: 3GDGCWT2R4
kind: example
name: The cyclic tournament on three vertices is homogeneous
aliases: [three-cycle-tournament-homogeneous]
msc: ["03C15", "05C20"]
topics: [ZS8X8KS54R]
audience: grad
instance_of: [CWKWP7G6HB, H8VM37SSAX]
uses: [CWKWP7G6HB, H8VM37SSAX, 0R5HTV7REV, DSQ17TNW1C]
sources:
  - book: isbn:9780521587136
---

## Example

Let $C_3$ be the tournament on $\Z/3\Z$ with an arc $x \to x + 1$ for each $x$.
It is a [[directed graph|0R5HTV7REV]] in which each pair of distinct vertices carries exactly one arc.
We show that $C_3$ is [[homogeneous|H8VM37SSAX]].

1. The rotations $x \mapsto x + k$ preserve arcs, so they are [[automorphisms|DSQ17TNW1C]].
2. A one-point map $u \mapsto u'$ extends to the rotation by $u' - u$.
3. A two-point isomorphism sends an arc $u \to v$ to an arc $u' \to v'$. Then $v = u + 1$ and $v' = u' + 1$.
4. The rotation by $u' - u$ sends $u$ to $u'$ and $v$ to $v'$.
5. A three-point isomorphism is an automorphism, and the empty map extends to the identity.

## Remarks

The automorphism group is the cyclic group of order $3$, and it acts regularly on arcs.
$C_3$ is one of the two finite entries in Lachlan's list of homogeneous tournaments, the other being the one-point tournament.
The transitive tournament on $3$ vertices, the linear order $0 < 1 < 2$, is not homogeneous, since its only automorphism is the identity.

## Explanations

### L1 human

Three players each beat one other player in a circle: $0$ beats $1$, $1$ beats $2$, $2$ beats $0$.
Rotating the circle is a symmetry.
Any matching between equal-looking groups of players is such a rotation.

### L2 human

We extend the map $1 \mapsto 0$, $2 \mapsto 1$.

1. The arc $1 \to 2$ goes to the arc $0 \to 1$, so the map is an isomorphism.
2. The rotation $x \mapsto x - 1$ sends $1 \mapsto 0$, $2 \mapsto 1$, and $0 \mapsto 2$.

The typical use is as the smallest nontrivial homogeneous tournament.
A trap is to try a reflection; reflections reverse arcs and are not automorphisms of a tournament.
