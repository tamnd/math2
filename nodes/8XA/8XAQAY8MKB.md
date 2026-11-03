---
tag: 8XAQAY8MKB
kind: definition
name: Lie algebra extension
msc: [17B05, 17B56]
defines: 8264A9XM74
uses: [5JJYBJ6A8K, H5D71JE8TA, KJKNJMGKZZ]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_algebra_extension
---

## Definition

Let $\mathfrak a$ and $\mathfrak g$ be [[Lie algebras|5JJYBJ6A8K]] over a field $k$.
Let $\mathfrak e$ be a Lie algebra, and let $i \colon \mathfrak a \to \mathfrak e$ and $p \colon \mathfrak e \to \mathfrak g$ be [[Lie algebra homomorphisms|H5D71JE8TA]].
The triple $(\mathfrak e, i, p)$ is an *extension* of $\mathfrak g$ by $\mathfrak a$ if
$$0 \longrightarrow \mathfrak a \xrightarrow{\ i\ } \mathfrak e \xrightarrow{\ p\ } \mathfrak g \longrightarrow 0$$
is a [[short exact sequence|KJKNJMGKZZ]]: $i$ is injective, $p$ is surjective and $\im i = \ker p$.

## Remarks

The image $i(\mathfrak a)$ is then an ideal of $\mathfrak e$, and $p$ induces an isomorphism $\mathfrak e / i(\mathfrak a) \cong \mathfrak g$.
The extension is *central* if $i(\mathfrak a)$ lies in the center of $\mathfrak e$.
It is *split* if there is a Lie algebra homomorphism $s \colon \mathfrak g \to \mathfrak e$ with $p \circ s = \id$; then $\mathfrak e$ is a [[semidirect product|T9WAK2FH31]] of $i(\mathfrak a)$ and $s(\mathfrak g)$.

Example: let $\mathfrak e$ be the Heisenberg algebra with basis $x, y, z$ and $[x, y] = z$, the other brackets being $0$.
Let $\mathfrak a = k$ with $i(1) = z$, and let $\mathfrak g = k^2$ abelian with $p(ax + by + cz) = (a, b)$.
Then $p$ is a homomorphism because it kills every bracket and $\mathfrak g$ is abelian, and $\ker p = k z = \im i$.
This is a central extension that does not split.
Any elements of $\mathfrak e$ mapping to $(1, 0)$ and $(0, 1)$ have the form $x + cz$ and $y + c'z$, and their bracket is $z \ne 0$, while a splitting needs bracket $0$.

Non-example: the inclusion $k z \to \mathfrak e$ followed by the zero map $\mathfrak e \to k^2$ is not an extension, since the zero map is not surjective and its kernel is not $k z$.
