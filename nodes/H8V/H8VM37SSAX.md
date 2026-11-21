---
tag: H8VM37SSAX
kind: concept
name: Ultrahomogeneous structure
aliases: [ultrahomogeneous-structure, homogeneous-structure-fraisse, ultrahomogeneity]
msc: ["03C15", "03C50"]
topics: [ZS8X8KS54R]
audience: grad
uses: [983GZBQYT4, 676H7EGTKJ, PZMGQMDN25, DSQ17TNW1C, 5FKW715RGJ, 01TQB88H4C, A22K1X8GKD, RMTZ5J64FX]
sources:
  - url: https://en.wikipedia.org/wiki/Fraïssé_limit
    locator: Fraïssé's theorem
  - url: https://en.wikipedia.org/wiki/Homogeneous_graph
  - book: isbn:9780521587136
---

## Summary

A [[structure|983GZBQYT4]] $M$ is *ultrahomogeneous* when every [[isomorphism|PZMGQMDN25]] between finitely generated [[substructures|676H7EGTKJ]] of $M$ extends to an [[automorphism|DSQ17TNW1C]] of $M$.
Many authors say *homogeneous* for the same notion, especially for relational structures.
The rational order, the Rado graph and the Henson graphs are ultrahomogeneous; the integer order is not.
By [[Fraïssé's theorem|V5CKNFP3HC]], countable ultrahomogeneous structures correspond to classes of finitely generated structures with HP, JEP and AP, through their [[ages|5FKW715RGJ]].
In a finite relational signature, a [[countable|01TQB88H4C]] structure is ultrahomogeneous exactly when its theory is [[$\aleph_0$-categorical|A22K1X8GKD]] with quantifier elimination; see [[this theorem|ZRWJZK78MD]].

## Motivation

Symmetry is measured by how much the automorphism group can move.
Ultrahomogeneity asks for the most symmetry compatible with the structure: any two finite configurations of the same isomorphism type are moved onto each other.
In $(\Q, <)$ any two increasing tuples of the same length are related by an order automorphism, and this is the reason $(\Q, <)$ is so well behaved.
For countable structures, the property is local and checkable, and it is equivalent to a one-point extension property.
That makes it the target notion of the Fraïssé construction.

## Notation

The formal definition is [[this definition|CZFGSN4JNE]].
Hodges uses "ultrahomogeneous", while Fraïssé theory texts in combinatorics usually say "homogeneous".
In model theory "homogeneous" may also mean that partial elementary maps extend; that notion is different and is treated with [[saturated models|RMTZ5J64FX]].
The automorphism group is written $\operatorname{Aut}(M)$.

## Remarks

### Examples

- $(\Q, <)$ is ultrahomogeneous; see [[this example|86YZAQ1WWC]].
- The $5$-cycle $C_5$ is a finite ultrahomogeneous graph; see [[this example|YMJY7Z9T1H]].
- The [[Rado graph|RMXR0FEF54]] and the [[Henson graphs|TZT25G2YB3]] are ultrahomogeneous.
- An infinite set in the empty signature is ultrahomogeneous, since any bijection between finite subsets extends to a permutation.
- The countable atomless Boolean algebra is ultrahomogeneous as a Boolean algebra.

### Non-examples

- $(\Z, <)$ is not ultrahomogeneous: the map $0 \mapsto 0$, $1 \mapsto 2$ preserves the order but does not extend; see [[this non-example|5JVJ0HJV34]].
- The path $P_3$ with three vertices is not: its two end vertices and its middle vertex are isomorphic one-point substructures, but no automorphism moves an end to the middle.

### Basic properties

- A countable structure $M$ is ultrahomogeneous if and only if it has the extension property: for finitely generated $A \subseteq B$ in $\operatorname{Age}(M)$, every embedding $A \to M$ extends to an embedding $B \to M$.
- The age of a countable ultrahomogeneous structure has the [[amalgamation property|XSCSX39GEZ]].
- An ultrahomogeneous structure in a finite relational signature has an oligomorphic automorphism group: finitely many orbits on $n$-tuples for each $n$.
- Ultrahomogeneity depends on the signature: $(\Z, <)$ with the successor function added is ultrahomogeneous.

### History

Fraïssé studied countable relational structures with this extension property in the early 1950s.
Finite and countable homogeneous graphs were classified later; see [[the Lachlan-Woodrow theorem|F7PA1RVBCG]].

### Common errors

- To check only single points. Vertex-transitivity is much weaker; $P_3$ fails it, and $C_6$ is vertex-transitive but not ultrahomogeneous.
- To forget the signature. Adding or removing symbols changes which maps are isomorphisms of substructures.
- To confuse with saturation-type homogeneity, where elementary maps, not isomorphisms of substructures, must extend.

## Explanations

### L1 human

A structure is ultrahomogeneous when it looks the same from every finite viewpoint.
Pick two finite pieces that look alike, with a matching between them.
Then a symmetry of the whole structure carries one piece onto the other along that matching.
The rationals have this property: any two finite increasing lists can be slid onto each other by an order-preserving map.

### L2 human

We check that $C_6$ is not ultrahomogeneous, although every vertex looks the same.

1. Label the vertices $0, \dots, 5$ in cyclic order.
2. The pairs $\set{0, 2}$ and $\set{0, 3}$ are both non-edges, so $0 \mapsto 0$, $2 \mapsto 3$ is an isomorphism of induced subgraphs.
3. In $C_6$, the vertices $0$ and $2$ have the common neighbor $1$, while $0$ and $3$ have no common neighbor.
4. An automorphism preserves common neighbors, so the map does not extend.

The typical use of ultrahomogeneity is to transfer a local fact about finite substructures to the whole structure.
A trap is to test only maps between single points.

### L3 human

For countable structures, ultrahomogeneity is equivalent to the extension property, and it makes the age a complete invariant within the class of ultrahomogeneous structures.
In a finite relational signature, it is equivalent to $\aleph_0$-categoricity plus quantifier elimination.
The automorphism group is then a closed oligomorphic subgroup of $\operatorname{Sym}(\N)$.
Its topological dynamics is governed by the age through the [[Kechris-Pestov-Todorcevic correspondence|96Q4P7PZVY]].
Its algebraic structure is studied through properties such as the [[small index property|RZAF6NVEXC]].
