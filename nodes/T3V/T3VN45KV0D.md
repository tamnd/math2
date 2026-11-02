---
tag: T3VN45KV0D
kind: statement
role: theorem
name: Alexander's theorem on proper self-maps of the ball
msc: [32H35, 32H02]
uses: [TM528Q96ZD, PDQ9KW9FAP, FX92PP3HZR]
about: [TM528Q96ZD, PDQ9KW9FAP]
sources:
  - url: https://en.wikipedia.org/wiki/Biholomorphism
---

## Statement

Let $n \ge 2$ and let $B \subset \C^n$ be the [[unit ball|PDQ9KW9FAP]].
Every [[proper holomorphic map|TM528Q96ZD]] $F \colon B \to B$ is a [[biholomorphism|FX92PP3HZR]] of $B$ onto itself.

## Remarks

A proper holomorphic self-map of $B$ is a finite branched covering.
One proof shows that it has no branching: near a suitable boundary point $F$ is a local biholomorphism that maps a piece of the sphere $\partial B$ into $\partial B$.
Such a local map is the restriction of an automorphism of $B$, a rigidity property of the sphere that goes back to Poincaré.
By the identity theorem, $F$ itself is that automorphism.

The hypothesis $n \ge 2$ is necessary.
For $n = 1$ the map $z \mapsto z^2$ is a proper holomorphic self-map of the unit disc that is not injective.

The shape of the ball matters too.
The map $(z_1, z_2) \mapsto (z_1, z_2^2)$ is a proper holomorphic self-map of the unit polydisc in $\C^2$ that is not injective.

The target dimension matters as well: the map $(z_1, z_2) \mapsto (z_1^2, \sqrt{2}\, z_1 z_2, z_2^2)$ sends the unit ball of $\C^2$ properly into the unit ball of $\C^3$.
Check: $\abs{z_1}^4 + 2\abs{z_1 z_2}^2 + \abs{z_2}^4 = (\abs{z_1}^2 + \abs{z_2}^2)^2$, which tends to $1$ exactly when $\abs{z_1}^2 + \abs{z_2}^2$ does.

## Explanations

### L1 human

In one variable the unit disc has many maps onto itself that wrap it several times, such as $z \mapsto z^2$.
Alexander's theorem says that the ball in two or more complex variables has none.
Any holomorphic map from the ball to itself that sends the boundary to the boundary is a symmetry of the ball, one to one and onto.

### L2 human

The theorem is a basic example of rigidity in several complex variables.
Combined with the description of the automorphisms of $B$, it lists all proper self-maps of the ball.
They are the maps $z \mapsto U \varphi_a(z)$, with $U$ unitary and $\varphi_a$ the automorphism exchanging $a$ and $0$.
It started the study of proper holomorphic maps between balls of different dimensions, where, as the example above shows, many non-trivial maps exist.
