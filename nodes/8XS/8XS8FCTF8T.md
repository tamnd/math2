---
tag: 8XS8FCTF8T
kind: concept
name: Ramsey class
aliases: [ramsey-class, ramsey-property-for-classes, structural-ramsey-property]
msc: ["05D10", "05C55", "03C15"]
topics: [ZS8X8KS54R, W8Y2NKJ8CX]
audience: research
uses: [00TQV3F5S4, SCRB74SWQN, HJVRBDQSGG, XSCSX39GEZ, 0FRXBVVR03]
sources:
  - url: https://en.wikipedia.org/wiki/Structural_Ramsey_theory
    locator: The Ramsey property
  - url: https://en.wikipedia.org/wiki/Structural_Ramsey_theory
    locator: Examples
---

## Summary

Let $\mathcal{K}$ be a class of finite structures, and write $\binom{C}{A}$ for the set of [[embeddings|SCRB74SWQN]] of $A$ into $C$.
For $A, B, C \in \mathcal{K}$ and $k \ge 2$, write $C \to (B)^A_k$ if every coloring $\binom{C}{A} \to \set{1, \dots, k}$ is constant on $\set{g \circ e : e \in \binom{B}{A}}$ for some $g \in \binom{C}{B}$.
$\mathcal{K}$ has the *Ramsey property* if for all $A, B \in \mathcal{K}$ and $k \ge 2$ there is $C \in \mathcal{K}$ with $C \to (B)^A_k$.
A *Ramsey class* is a class with the Ramsey property, usually also hereditary with JEP, so a Fraïssé class.
The finite [[linear orders|0FRXBVVR03]] form a Ramsey class by [[Ramsey's theorem|00TQV3F5S4]], and finite ordered graphs form one by the Nešetřil-Rödl theorem.

## Motivation

Ramsey's theorem colors $a$-subsets of a set and finds a large homogeneous set.
Structural Ramsey theory asks the same question with subsets replaced by substructures: color copies of a small graph inside a big graph and find a copy of a medium graph whose small copies all share one color.
The answer depends on the class, and the classes where it is positive have a strong form of symmetry.
Through the Kechris-Pestov-Todorcevic correspondence, they are exactly the classes whose [[Fraïssé limits|HJVRBDQSGG]] have extremely amenable automorphism groups.

## Notation

The arrow notation $C \to (B)^A_k$ extends the Erdős-Rado arrow of Ramsey's theorem.
Some authors color copies, that is substructures, rather than embeddings; for classes of rigid structures the two versions agree.

## Remarks

### Examples

- Finite linear orders; see [[this example|X3K7KWH5BK]].
- Finite ordered graphs, with the case of vertex colorings in [[this example|6BFRDVHC63]].
- Finite ordered $K_n$-free graphs, and more generally ordered free amalgamation classes, by Nešetřil-Rödl.

### Non-examples

- Finite graphs without an order are not a Ramsey class; see [[this non-example|D5J3R1PRNQ]].
- Any class containing a structure with a nontrivial automorphism fails the Ramsey property.

### Basic properties

- Every member of a Ramsey class is rigid. If $\alpha$ moves $a$ in $A$, fix an order on $C$ and color $e$ by whether $e(a) < e(\alpha a)$; around the cycle of $a$ under $\alpha$ both colors occur in every copy of $A$.
- A hereditary class with JEP and the Ramsey property has the [[amalgamation property|XSCSX39GEZ]], by an observation of Nešetřil.
- For a Fraïssé class of ordered structures, the Ramsey property is equivalent to extreme amenability of the automorphism group of the limit; see [[the correspondence|96Q4P7PZVY]].

### History

Nešetřil and Rödl proved the Ramsey property for ordered graphs and hypergraphs, and for ordered $K_n$-free graphs, in 1977.
Abramson and Harrington proved the result for ordered relational structures independently in 1978.
Hubička and Nešetřil developed general methods in their paper "All those Ramsey classes".

### Common errors

- To forget the order. Unordered classes with nontrivial automorphisms are never Ramsey.
- To color subsets of vertices instead of embeddings or copies; for graphs the induced structure matters.
- To expect the Ramsey property from AP alone. Ordered classes with AP need not be Ramsey; some need a richer expansion.

## Explanations

### L1 human

Ramsey's theorem says that complete disorder is impossible: color the pairs of a large enough set, and some large subset has all its pairs the same color.
A Ramsey class is a family of structures where the same holds for copies of any small structure inside copies of a larger one.
Adding a linear order is often what makes a class Ramsey, because it removes the symmetries that spoil the coloring.

### L2 human

We see the rigidity obstruction for $A = $ a two-element antichain in the class of finite partial orders.

1. $A$ has the automorphism swapping its two points $a, b$.
2. Fix a linear order on any candidate $C$, and color an embedding $e$ red if $e(a) < e(b)$, blue otherwise.
3. Every copy of $A$ in $C$ is the image of one red and one blue embedding.
4. So with $B = A$ no $C$ works, and finite partial orders are not Ramsey.

The typical use is to choose the right ordered expansion of a class before looking for a Ramsey theorem.
A trap is to ignore automorphisms of the small structure $A$.

### L3 human

The Ramsey property of $\mathcal{K}$ is a statement about the dynamics of the automorphism group of its limit.
When a class is not Ramsey, one looks for a precompact expansion that is Ramsey; it then determines the universal minimal flow of the group.
Hubička and Nešetřil show that many classes defined by forbidden substructures have such expansions.
