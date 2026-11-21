---
tag: 4RS9Y3XZ0A
kind: proof
name: Proof of the Lachlan-Woodrow theorem
msc: ["03C15", "05C63"]
topics: [ZS8X8KS54R]
audience: research
proves: F7PA1RVBCG
uses: [H8VM37SSAX, V5CKNFP3HC, RMXR0FEF54, TZT25G2YB3, 0MCYJ72VGA, 03WKB2H474, DSQ17TNW1C]
methods: [0WCP0PVET6, 0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Homogeneous_graph
    locator: Classification
---

## Proof

The proof is by [[cases|0WCP0PVET6]].
The deep primitive case is cited, not reproved.

### The listed graphs are homogeneous

1. If $G$ is homogeneous, so is its [[complement|0MCYJ72VGA]]. An isomorphism of finite induced subgraphs of one is also one for the other.
2. The Rado graph and the Henson graphs are Fraïssé limits, hence homogeneous.
3. In $m \cdot K_n$, two vertices are adjacent exactly when they lie in the same component.
4. So a finite partial isomorphism $p$ induces a partial injection between components.
5. Extend it to a bijection of the $m$ components. Inside each component, extend $p$ to a bijection of the $n$ vertices.
6. The result is an [[automorphism|DSQ17TNW1C]] extending $p$.

### Disconnected homogeneous graphs

7. Let $G$ be homogeneous and disconnected. We show each component is complete.
8. Suppose a component $C$ has non-adjacent vertices $a, c$, and pick $d$ in another component.
9. The pairs $\set{a, c}$ and $\set{a, d}$ are non-edges, so $a \mapsto a$, $c \mapsto d$ is an isomorphism.
10. An extension $\sigma$ fixes $a$, so it maps $C$ onto the component of $a$, which is $C$.
11. But $\sigma(c) = d \notin C$, a [[contradiction|0J0XBKG64S]].
12. So the components are [[complete graphs|03WKB2H474]]. One-point maps extend, so all components have the same size.
13. Hence $G \cong m \cdot K_n$ with $m \ge 2$. If the complement of $G$ is disconnected, apply this to the complement.

### The primitive case

14. Assume $G$ and its complement are both connected and $G$ is homogeneous.
15. Lachlan and Woodrow show that the age of $G$ is all finite graphs, or the $K_n$-free graphs, or their complements.
16. By the uniqueness part of [[Fraïssé's theorem|V5CKNFP3HC]], $G$ is $R$, $G_n$ or the complement of $G_n$.

## Idea

Homogeneity forces "same component" to be an equivalence relation that every automorphism respects, so a disconnected homogeneous graph is a union of equal cliques.
When neither $G$ nor its complement splits, the hard part is to show that the age is determined by the cliques or independent sets it omits.

## Variants

Gardiner's classification of finite homogeneous graphs uses the same first two steps; in the primitive finite case only $C_5$ and $K_3 \times K_3$ occur.
