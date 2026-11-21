---
tag: YMJY7Z9T1H
kind: example
name: The five-cycle is an ultrahomogeneous graph
aliases: [five-cycle-ultrahomogeneous]
msc: ["03C15", "05C63"]
topics: [ZS8X8KS54R]
audience: grad
instance_of: [H8VM37SSAX]
uses: [H8VM37SSAX, CZFGSN4JNE, 0QQ0F12962, 0EREPBVG2G, 0MCYJ72VGA, DSQ17TNW1C]
sources:
  - url: https://en.wikipedia.org/wiki/Homogeneous_graph
    locator: Classification
  - book: isbn:9780521587136
---

## Example

Let $C_5$ be the [[cycle graph|0QQ0F12962]] on $\Z/5\Z$, with $x \sim y$ when $x - y = \pm 1$.
Its automorphism group is the dihedral group $D_5$ of order $10$, made of the maps $x \mapsto \pm x + k$.
We show that $C_5$ is [[ultrahomogeneous|H8VM37SSAX]].
Let $p \colon A \to B$ be an isomorphism of [[induced subgraphs|0EREPBVG2G]]; we sort by $\lvert A \rvert$.

1. Size $0$ or $1$: rotations act transitively on vertices.
2. Size $2$: $D_5$ has $10$ elements, and it acts transitively on the $10$ ordered edges, so it acts regularly on them. The $5$ non-edges form the [[complement|0MCYJ72VGA]], which is again a $5$-cycle, so $D_5$ acts regularly on ordered non-edges too.
3. Size $3$: a $3$-set induces either a path, such as $\set{0, 1, 2}$, or an edge plus a point, such as $\set{0, 1, 3}$. Rotations move each type transitively. The reflection $x \mapsto 2 - x$ swaps the ends of $\set{0, 1, 2}$, and $x \mapsto 1 - x$ swaps $0$ and $1$ and fixes $3$. Each induced graph has exactly $2$ automorphisms, so all of them are realized.
4. Size $4$: a $4$-set is the complement of one vertex $v$ and induces a path of length $3$. The reflection fixing $v$ reverses that path.
5. Size $5$: $p$ is itself an [[automorphism|DSQ17TNW1C]].

In every case $p$ extends to an element of $D_5$.

## Remarks

The graph $C_5$ is isomorphic to its complement, which explains why edges and non-edges behave in the same way.
Gardiner's classification of finite homogeneous graphs lists $C_5$, the rook's graph $K_3 \times K_3$, disjoint unions $m \cdot K_n$, and their complements.
The cycle $C_6$ is not ultrahomogeneous, so $C_5$ is a special case.

## Explanations

### L1 human

The five-cycle looks the same from every corner and from every pair of corners.
Whatever small piece one picks, and however one matches it with a piece of the same shape, a rotation or a flip of the pentagon does the matching.

### L2 human

We extend the map $p(0) = 2$, $p(2) = 4$.

1. The pairs $\set{0, 2}$ and $\set{2, 4}$ are non-edges, so $p$ is an isomorphism.
2. Try the rotation $x \mapsto x + 2$: it sends $0 \mapsto 2$ and $2 \mapsto 4$.
3. So the rotation extends $p$.

The typical use is as the smallest nontrivial finite homogeneous graph.
A trap is to stop after checking vertices and edges; the $3$-sets and $4$-sets also need checking.
