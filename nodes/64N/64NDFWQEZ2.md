---
tag: 64NDFWQEZ2
kind: statement
role: theorem
name: Mundici's equivalence
aliases: [mundici-equivalence, gamma-functor-mv-algebras, mundici-gamma-functor]
msc: ["06D35", "06F20", "03B50"]
topics: [QYA4H5Y7VR]
audience: research
about: [8T4M7RN9AC, G5AN43WE9D]
uses: [QVWHWDJ5X1, G5AN43WE9D, 28NQ0KRHD3, JBVKKDXETM]
proofs: [X6RYPK2WHD]
sources:
  - url: https://en.wikipedia.org/wiki/MV-algebra
    locator: Examples of MV-algebras; Relation to functional analysis
  - book: isbn:9780792360094
---

## Statement

Let $G$ be an abelian [[lattice-ordered group|G5AN43WE9D]], and let $u \in G$ with $u \ge 0$.
Put $\Gamma(G, u) = \set{x \in G : 0 \le x \le u}$, with $x \oplus y = u \land (x + y)$, $\neg x = u - x$ and the constant $0$.
A *strong unit* is an element $u \ge 0$ such that for each $x \in G$ there is $n$ with $x \le nu$.
A *unital ℓ-group* is a pair $(G, u)$ with $u$ a strong unit; its morphisms are ℓ-group homomorphisms $h$ with $h(u) = v$.

**Theorem.**

1. $\Gamma(G, u)$ is an [[MV-algebra|QVWHWDJ5X1]] for every $u \ge 0$.
2. A morphism $h : (G, u) \to (H, v)$ restricts to an MV-homomorphism $\Gamma(h) : \Gamma(G, u) \to \Gamma(H, v)$, and $\Gamma$ is a [[functor|28NQ0KRHD3]].
3. (Mundici) $\Gamma$ is an [[equivalence of categories|JBVKKDXETM]] from unital abelian ℓ-groups to MV-algebras.

Parts 1 and 2 are proved in full below.
Part 3 is stated and cited: see Cignoli, D'Ottaviano and Mundici.

## Remarks

### Why each hypothesis is needed

1. The group must be abelian: commutativity of $\oplus$ uses $x + y = y + x$.
2. The lattice order is needed to form $u \land (x + y)$; in a partially ordered group the meet may not exist.
3. The strong unit is needed in part 3.
   In $\mathbb{Z} \times_{\mathrm{lex}} \mathbb{Z}$, the element $u = (0, 1)$ is not a strong unit, and $\Gamma$ gives $\set{(0, 0), (0, 1)}$.
   This is also $\Gamma(\mathbb{Z}, 1)$, so $\Gamma$ would identify two groups that are not isomorphic.

### Consequences

1. Every MV-algebra is $\Gamma(G, u)$ for some unital ℓ-group, unique up to isomorphism.
2. [[Chang's algebra|W7AD8Q3PMK]] is $\Gamma(\mathbb{Z} \times_{\mathrm{lex}} \mathbb{Z}, (1, 0))$, and $[0, 1] = \Gamma(\mathbb{R}, 1)$.
3. Up to isomorphism, countable MV-algebras correspond one to one to [[AF C*-algebras|4Y7VENNBVK]] whose dimension group is lattice ordered; this is a topic of operator algebras.

### Converse

The inverse functor builds from an MV-algebra $A$ a group of "good sequences" of elements of $A$; see Cignoli, D'Ottaviano and Mundici.
For an MV-chain, the earlier result of Chang gives the group directly.

### Generalizations

1. Chang's construction on totally ordered groups is the special case of MV-chains.

## History

Chang introduced MV-algebras in 1958, and he represented every MV-chain by a totally ordered abelian group.
Mundici extended the construction in 1986 to lattice-ordered abelian groups with a strong unit, and proved the categorical equivalence.

## Explanations

### L1 human

Take whole numbers from $0$ to $n$, and add with a cap at $n$.
This capped addition is an MV-algebra.
The theorem says that every MV-algebra arises in this way, from some ordered group and a top element.

### L2 human

1. In $\mathbb{Z}$ with $u = 4$, compute $3 \oplus 2 = 4 \land 5 = 4$ and $\neg 1 = 3$.
2. In $\mathbb{Z}^2$ with the pointwise order and $u = (1, 1)$, the segment is $\set{0, 1}^2$.
3. There $(1, 0) \oplus (0, 1) = (1, 1)$, and $\Gamma$ gives the four-element Boolean algebra.

The typical use: one moves a problem about MV-algebras to ordered groups, where linear algebra helps.
The trap: the order of $G$ must be a lattice order, and $u$ must be a strong unit, not only positive.

### L3 human

The equivalence makes Łukasiewicz logic a logic of ordered groups.
Free MV-algebras become algebras of piecewise linear functions, by [[McNaughton's theorem|E11A9H8Z7Q]].
Countable MV-algebras then classify certain AF C*-algebras, through their dimension groups.
