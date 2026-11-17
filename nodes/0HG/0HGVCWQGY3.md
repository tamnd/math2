---
tag: 0HGVCWQGY3
kind: statement
role: theorem
name: Pigeonhole principle
aliases: [dirichlet-box-principle]
msc: ["05A05", "00A35"]
topics: [GB14W4SYPK]
audience: school
about: [0EPAT51DXQ, 09NWETVTNY, 05099E1NMJ]
uses: [05099E1NMJ, 0EPAT51DXQ, 09NWETVTNY]
formal:
  - system: lean4
    library: mathlib
    decl: Finset.exists_ne_map_eq_of_card_lt_of_maps_to
    match: exact
history:
  first_stated: "Jean Leurechon, 1622, in the form that two people have the same number of hairs"
  notes: "Dirichlet used the principle in number theory in the nineteenth century, and German texts call it the Schubfachprinzip (drawer principle)."
sources:
  - url: https://en.wikipedia.org/wiki/Pigeonhole_principle
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Pigeonhole_principle
    locator: History
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_basics_pigeonhole.ptx#L6
    locator: source/s_basics_pigeonhole.ptx:6
same_as:
  wikidata: Q188276
  wikipedia: Pigeonhole principle
---

## Statement

Let $A$ and $B$ be [[finite sets|070R982G4B]], and let $|A|$ and $|B|$ be their numbers of elements, as in [[cardinality of a finite set|05099E1NMJ]].
Let $f : A \to B$ be a [[function|0EPAT51DXQ]].
Assume that $|A| > |B|$.
Then there are elements $a$ and $a'$ of $A$ with $a \neq a'$ and $f(a) = f(a')$.
In other words, $f$ is not [[injective|09NWETVTNY]].

The usual special case: if $n + 1$ objects go into $n$ boxes, then some box receives at least two objects.
Here $A$ is the set of objects, $B$ is the set of boxes, and $f(a)$ is the box of the object $a$.
The [[proof|E0R6P2FMCM]] is short.

## Remarks

The principle is also called Dirichlet's box principle, the drawer principle, or the Schubfachprinzip.
All these names denote the same statement.
In an application, the hard part is the choice of the boxes: the objects and the map $f$ must be defined so that two objects in one box give the desired conclusion.
The page [[applications of the pigeonhole principle|~f5e5f57d]] shows four such choices.

### Why each hypothesis is needed

- The inequality $|A| > |B|$ is needed. For $A = B = \set{1, 2}$, the identity map is injective, so no box holds two objects.
- The sets must be finite when "more elements" is read as "a proper superset". The set $\N$ of natural numbers is larger than the set $E$ of even numbers in this sense, but $n \mapsto 2n$ is an injective map from $\N$ to $E$, as in [[Hilbert's hotel|0N3Y8G340X]].
- The map $f$ must be defined on all of $A$: each object must go into some box. If only $2$ of $3$ objects are placed in $2$ boxes, the two placed objects can go into different boxes.

### Consequences

- The [[generalized pigeonhole principle|0BY7GN3449]] gives a box with more than $n$ objects when there are more than $n \cdot |B|$ objects.
- There is no injection from a set of size $m$ to a set of size $n < m$. So the [[number of injections|0X0N833FF8]] from $A$ to $B$ is $0$ when $|A| > |B|$.
- For finite sets with $|A| = |B|$, a map $f : A \to B$ is injective if and only if it is surjective. This fact proves that [[a finite integral domain is a field|0EBE031B8E]].
- [[Dirichlet's approximation theorem|04JAY9DGB7]] and the [[Erdős-Szekeres theorem|0SNJM8HSD3]] have proofs by the pigeonhole principle, in [[this proof|Q4PTS4BYNG]] and [[this proof|22G1VPJW6Y]].

### Converse

The converse is true for finite sets: if every function $f : A \to B$ fails to be injective, then $|A| > |B|$.
Indeed, if $|A| \le |B|$, we number $A = \set{a_1, \dots, a_m}$ and $B = \set{b_1, \dots, b_n}$ with $m \le n$, and the map $a_i \mapsto b_i$ is injective.
The other reading of the converse is false: a single non-injective map does not show $|A| > |B|$.
The constant map from $\set{1, 2}$ to $\set{1, 2}$ is not injective, and $|A| = |B|$.

### Generalizations

- The [[generalized pigeonhole principle|0BY7GN3449]]: if $|A| > n \cdot |B|$, some fibre of $f$ has more than $n$ elements.
- The [[infinite pigeonhole principle|0FS3RHF6KE]]: an infinite set in finitely many boxes gives an infinite box.
- For infinite cardinals, $|A| > |B|$ means by definition that there is no injection $A \to B$, so the statement holds by definition. The work moves into the comparison of the two cardinals.
- A measure version: if measurable subsets $S_1, \dots, S_k$ of a set of measure $1$ have measures with sum greater than $1$, then two of them meet in a set of positive measure. [[Blichfeldt's theorem|A3FTHW4NES]] is a statement of this kind.

## History

Jean Leurechon stated a form of the principle in 1622: two people have the same number of hairs on their heads.
Peter Gustav Lejeune Dirichlet used the principle in number theory in the nineteenth century, and the name "Dirichlet's box principle" comes from his use.
German texts call it the Schubfachprinzip, the drawer principle.

## Explanations

### L1 human

If there are more letters than mailboxes, and every letter goes into a mailbox, then some mailbox gets two letters.
The reason is simple counting: if each mailbox had at most one letter, there would be at most as many letters as mailboxes.
For example, among any $13$ people, two have their birthdays in the same month, because there are only $12$ months.
The principle tells us that two such people exist.
It does not tell us which two people they are.

### L2 human

We prove: among any $5$ points in a square of side $2$, two points are at distance at most $\sqrt{2}$.

1. We cut the square into $4$ squares of side $1$ by the two lines through its centre. These $4$ small squares are the boxes.
2. We put each point into a small square that contains it. A point on a cutting line lies in two small squares, and we choose one of them.
3. There are $5$ points and $4$ boxes, and $5 > 4$. By the pigeonhole principle, two points $P$ and $Q$ lie in the same small square.
4. Two points of a closed square of side $1$ are at distance at most the length of its diagonal, which is $\sqrt{1^2 + 1^2} = \sqrt{2}$.
5. So the distance from $P$ to $Q$ is at most $\sqrt{2}$.

The typical use of the principle follows these steps: find the objects, find fewer boxes, and show that two objects in one box give the conclusion.
A trap is a choice of boxes that is too coarse or too fine.
With $2$ boxes (two rectangles of size $1 \times 2$), two points share a box, but the diagonal of a box is $\sqrt{5}$, which gives a weaker bound.
The bound $\sqrt{2}$ is best possible: the $4$ corners and the centre are $5$ points with all distances at least $\sqrt{2}$.

### L3 human

In the language of functions, the principle says that there is no injection from a finite set to a smaller one.
For finite sets this is the content of the statement that the number of elements of a finite set is well defined.
In Mathlib the statement for finite sets is `Finset.exists_ne_map_eq_of_card_lt_of_maps_to`, and there is a version for finite types, `Fintype.exists_ne_map_eq_of_card_lt`.

The principle is the start of Ramsey theory: a large structure, split into a few classes, has a class with a lot of structure, as in the [[theorem on friends and strangers|0NYM0ZGAK9]] and [[Ramsey's theorem|00TQV3F5S4]].
In number theory it gives [[Dirichlet's approximation theorem|04JAY9DGB7]] and Thue's lemma, and in transcendence theory it gives Siegel's lemma on [[auxiliary functions|X01V173DZD]].
The [[generalized|0BY7GN3449]] and the [[infinite|0FS3RHF6KE]] forms, and the other methods of [[counting, invariant and extremal arguments|GB14W4SYPK]], such as [[double counting|0F8YBHF2W3]] and the [[averaging argument|~f5987d03]], are refinements of the same count.
