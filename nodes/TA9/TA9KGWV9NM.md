---
tag: TA9KGWV9NM
kind: statement
role: theorem
name: Hrushovski's extension property for finite graphs
aliases: [hrushovski-extension-property, eppa-for-graphs, extension-property-for-partial-automorphisms]
msc: ["03C15", "05C25", "20B25"]
topics: [ZS8X8KS54R]
audience: research
about: [00C0BR7D7H, RMXR0FEF54]
uses: [00C0BR7D7H, 0EREPBVG2G, 0F7QKGJS6B, DSQ17TNW1C, RMXR0FEF54, H8VM37SSAX]
sources:
  - url: https://en.wikipedia.org/wiki/Rado_graph
    locator: Symmetry group
  - book: isbn:9780521587136
---

## Statement

For every finite [[graph|00C0BR7D7H]] $G$ there is a finite graph $H$ that contains $G$ as an [[induced subgraph|0EREPBVG2G]] and has the following property.
Every [[isomorphism|0F7QKGJS6B]] between induced subgraphs of $G$ extends to an [[automorphism|DSQ17TNW1C]] of $H$.

In words, the class of finite graphs has the extension property for partial automorphisms (EPPA).

## Remarks

### Why each hypothesis is needed

- Finiteness of $H$ is the content. The [[Rado graph|RMXR0FEF54]] contains $G$ and is [[ultrahomogeneous|H8VM37SSAX]], so an infinite $H$ always exists.
- The class matters. For finite linear orders the analogue fails: every finite linear order is rigid, so the one-point map between the two points of $0 < 1$ extends in no finite linear order.

### Consequences

- If $G$ has $n$ vertices, $H$ can be chosen with $n 2^{n-1}$ vertices, by the construction in the [[proof|1Q99SE2FDY]].
- Hodges, Hodkinson, Lascar and Shelah used EPPA to prove that the automorphism group of the Rado graph has the [[small index property|RZAF6NVEXC]].

### Converse

The statement is not an equivalence with homogeneity.
A finite graph in which every partial isomorphism of the graph itself extends is a finite homogeneous graph, and such graphs are rare by Gardiner's classification.
EPPA only asks this for the partial isomorphisms of the smaller graph $G$.

### Generalizations

Herwig extended EPPA to all finite structures in a finite relational signature.
Herwig and Lascar extended it to classes defined by forbidden homomorphic images, which include the $K_n$-free graphs.
EPPA fails for finite linear orders, and for finite tournaments it is a well-known open problem.

## History

Hrushovski proved the statement in 1992.

## Explanations

### L1 human

Inside a finite graph, two small pieces may look alike without a symmetry of the graph matching them.
Hrushovski showed that one can always enlarge the graph, keeping it finite, so that every such matching becomes a symmetry of the larger graph.

### L2 human

We take $G$ to be the path $a - b - c$.

1. The map $a \mapsto b$ is an isomorphism of one-point subgraphs.
2. No automorphism of $G$ does it, since $a$ has degree $1$ and $b$ has degree $2$.
3. The $4$-cycle $a - b - c - d - a$ contains $G$ as an induced subgraph, and its rotation $a \mapsto b \mapsto c \mapsto d \mapsto a$ extends the map.
4. A full $H$ must handle every partial isomorphism of $G$ at once, which the construction in the proof does.

The typical use is to approximate the automorphism group of a Fraïssé limit by finite groups.
A trap is to extend each partial isomorphism in a different $H$; the statement asks for one $H$.

### L3 human

EPPA for a Fraïssé class makes the automorphism group of its limit approximable by finite groups in a strong sense.
That approximation is the input to proofs of the small index property and of related automatic continuity results.
