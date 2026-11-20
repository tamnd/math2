---
tag: 8T4M7RN9AC
kind: concept
name: MV-algebra
aliases: [mv-algebra]
msc: ["06D35", "03G20", "03B50"]
topics: [QYA4H5Y7VR]
audience: research
uses: [QVWHWDJ5X1, 0N6R902FG1, JQ713VVD0G, AJNZJD8442, DWYCKAKXZD]
sources:
  - url: https://en.wikipedia.org/wiki/MV-algebra
    locator: Definitions; Examples of MV-algebras; Relation to Łukasiewicz logic
  - url: https://plato.stanford.edu/entries/logic-fuzzy/
    locator: 7. Algebraic semantics
  - book: isbn:9780792360094
  - book: isbn:9780792352389
same_as:
  wikidata: Q6719122
  wikipedia: MV-algebra
---

## Summary

An MV-algebra is a structure $(A, \oplus, \neg, 0)$ such that $(A, \oplus, 0)$ is a commutative [[monoid|0N6R902FG1]], $\neg \neg x = x$, $x \oplus \neg 0 = \neg 0$, and $\neg(\neg x \oplus y) \oplus y = \neg(\neg y \oplus x) \oplus x$ for all $x, y$; see [[the definition|QVWHWDJ5X1]].
The model is the unit interval with $x \oplus y = \min(1, x + y)$ and $\neg x = 1 - x$, the standard MV-algebra.
MV-algebras are the algebras of [[infinite-valued Łukasiewicz logic|JQ713VVD0G]], a [[many-valued logic|DWYCKAKXZD]], as Boolean algebras are the algebras of classical logic.
They link many-valued logic to ordered groups, through [[Mundici's equivalence|~41795275]].

## Motivation

In Łukasiewicz logic, truth values are real numbers in $[0, 1]$, and the strong disjunction adds values and cuts at $1$.
One wants the class of all algebras that satisfy the same equations as $[0, 1]$, to do algebra with the logic.
A short list of identities captures this class: these are the axioms above.
That the list is complete for $[0, 1]$ is [[Chang's completeness theorem|QM0F33QE9P]].

## Notation

We write $1 = \neg 0$, $x \odot y = \neg(\neg x \oplus \neg y)$ and $x \to y = \neg x \oplus y$.
The order is $x \le y$ iff $\neg x \oplus y = 1$, and in it $x \lor y = \neg(\neg x \oplus y) \oplus y$ and $x \land y = \neg(\neg x \lor \neg y)$.
We write $nx$ for $x \oplus \dots \oplus x$ with $n$ terms.
$\text{Ł}_n$ denotes a finite subalgebra of $[0, 1]$ that is a chain.
Texts differ on the index: some take $\set{0, \tfrac{1}{n}, \dots, 1}$ with $n + 1$ elements, and others take $n$ elements.

## Remarks

### Examples

1. The standard MV-algebra $[0, 1]$; [[it satisfies the axioms|~bd015994]].
2. [[The three-element MV-algebra|~593aaada]] $\set{0, \tfrac12, 1}$, the algebra of three-valued Łukasiewicz logic.
3. Every [[Boolean algebra|0XADJKM699]], with $\oplus = \lor$; an MV-algebra is Boolean iff $x \oplus x = x$ for all $x$.
4. [[Chang's algebra $C$|~28156fb0]]: a chain with an element $\varepsilon > 0$ and $n\varepsilon < \neg \varepsilon$ for every $n$.
5. $\Gamma(G, u)$ for a unital abelian ℓ-group; for instance [[$\Gamma(\mathbb{Z}, n)$|~71202a4c]], an $(n+1)$-element chain.

### Non-examples

1. [[The Zadeh algebra on $[0, 1]$|~b5821df8]] with $x \oplus y = \max(x, y)$ and $\neg x = 1 - x$: the last axiom fails at $x = 0.6$, $y = 0.5$.
2. The integers with $+$, $-$, $0$: they fail $x \oplus \neg 0 = \neg 0$, since $1 + 0 = 1 \ne 0$.
3. The three-element [[Heyting chain|~6ca00a91]] with $\lor$ and its pseudocomplement: $\neg \neg \tfrac12 = 1$, so $\neg$ is not involutive.

### Basic properties

1. MV-algebras form a [[variety|AJNZJD8442]], and the standard MV-algebra generates it, by [[Chang's completeness theorem|QM0F33QE9P]].
2. The order is a distributive lattice order, and $\neg$ is an order-reversing involution.
3. An *ideal* is a set $I$ with $0 \in I$, $x \le y \in I \Rightarrow x \in I$, and $x, y \in I \Rightarrow x \oplus y \in I$.
   Ideals correspond one to one to congruences, by $x \equiv_I y$ iff $(x \odot \neg y) \oplus (y \odot \neg x) \in I$; see Cignoli, D'Ottaviano and Mundici.
4. Every MV-algebra is a [[subdirect product|88WN3AD2VQ]] of MV-chains; see Cignoli, D'Ottaviano and Mundici.
5. [[Mundici's equivalence|~41795275]]: MV-algebras are the unit intervals $\Gamma(G, u)$ of unital abelian ℓ-groups.

### History

Chang introduced MV-algebras in 1958 to give an algebraic proof of the completeness of Łukasiewicz logic.
Chang represented every MV-chain as a segment of a totally ordered abelian group.
Mundici extended this in 1986 to lattice-ordered abelian groups with a strong unit, and related countable MV-algebras to AF C*-algebras.

### Common errors

1. Reading $\oplus$ as $\lor$. In $[0, 1]$, $0.5 \oplus 0.5 = 1$, while $0.5 \lor 0.5 = 0.5$.
2. Assuming the lattice operations need extra axioms. They are defined from $\oplus$ and $\neg$, and the axioms make them a lattice.
3. Calling $([0, 1], \max, 1 - x)$ an MV-algebra. It is a Kleene algebra in the De Morgan sense, and it is not an MV-algebra; "Kleene algebra" also names the [[algebra of regular expressions|BK4DDS24XC]], a different notion.

## Explanations

### L1 human

In Łukasiewicz logic, a statement has a truth value between $0$ and $1$.
"Not" turns the value $x$ into $1 - x$.
A strong "or" adds the values, but never goes above $1$: $0.3$ and $0.5$ give $0.8$, while $0.7$ and $0.5$ give $1$.
An MV-algebra is any system that obeys the same rules as these two operations.
The simplest ones are the ordinary true/false logic and the three values $0$, $\tfrac12$, $1$.

### L2 human

1. In $[0, 1]$, compute $0.7 \odot 0.6 = \neg(0.3 \oplus 0.4) = \neg 0.7 = 0.3$.
2. In general $x \odot y = \max(0, x + y - 1)$, the Łukasiewicz t-norm.
3. Compute $0.7 \to 0.4 = 0.3 \oplus 0.4 = 0.7$.
4. Check residuation at $z = 0.7$: $z \odot 0.7 = 0.4 \le 0.4$, and $z \le 0.7 \to 0.4 = 0.7$.
5. So $0.7$ is the largest $z$ with $z \odot 0.7 \le 0.4$.

The typical use: an MV-algebra is a residuated lattice in which the strong conjunction and its implication behave as in $[0, 1]$.
The trap: $x \odot x$ is in general smaller than $x$; in $[0, 1]$, $0.5 \odot 0.5 = 0$.

### L3 human

MV-algebras are term equivalent to the bounded commutative BCK-algebras.
Among [[BL-algebras|~d07e9350]], they are those with $\neg \neg x = x$.
[[Mundici's equivalence|~41795275]] makes the category of MV-algebras equivalent to the category of unital abelian ℓ-groups, so MV-algebras are a finitary form of ordered groups.
Through ordered groups, countable MV-algebras classify AF C*-algebras with lattice-ordered dimension group, an application in operator algebras; see [[AF C*-algebras|4Y7VENNBVK]].
In geometry, free MV-algebras are algebras of McNaughton functions, continuous piecewise linear functions with integer coefficients; see [[McNaughton's theorem|E11A9H8Z7Q]].
