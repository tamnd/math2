---
tag: Y2S28SPR3R
kind: example
name: The second-order induction axiom is not the first-order induction schema
msc: ["03F30", "03H15"]
topics: [QHCRN4JVG0]
audience: grad
not_instance_of:
  - target: HACXBCM7SS
    note: the second-order Peano axioms have only the standard model up to isomorphism, while Peano arithmetic has a non-standard model by compactness
  - target: 1QD0KDDGYJ
    note: the second-order axiom quantifies over all subsets, and it fails in a non-standard model of the first-order schema
uses: [0QFT7Z76N5, 1NR3HAWG9D, 1QWN5CV4CG, Z8YDBW2857, DC60FYCSPM]
sources:
  - url: https://en.wikipedia.org/wiki/Peano_axioms
    locator: Nonstandard models
  - url: https://en.wikipedia.org/wiki/Non-standard_model_of_arithmetic
    locator: lead section
  - book: isbn:9780122384523
---

## Example

The second-order [[Peano axioms|0QFT7Z76N5]] state induction as one axiom with a set variable $X$:
$$\forall X\, \Bigl( \bigl( X(0) \land \forall x\,(X(x) \to X(S x)) \bigr) \to \forall x\, X(x) \Bigr).$$
In a structure with domain $M$, the variable $X$ ranges over all subsets of $M$.
By Dedekind's theorem, every structure that satisfies the second-order axioms is isomorphic to $\N$.
We show that first-order [[Peano arithmetic|Z8YDBW2857]] does not have this property, so the axiom and the schema differ in strength.

1. Add a new constant symbol $c$ to $L_A$, and let $T = \mathsf{PA} \cup \set{c \ne \overline{n} : n \in \N}$.
2. Let $T_0 \subseteq T$ be finite, and let $k$ be larger than every $n$ with $c \ne \overline{n}$ in $T_0$.
3. The standard model $\mathfrak{N}$, with $c$ interpreted as $k$, satisfies $T_0$: it satisfies $\mathsf{PA}$, and $k \ne n$ for these $n$.
4. By the [[compactness theorem|1NR3HAWG9D]], $T$ has a model $\mathfrak{M}$, and its reduct to $L_A$ is a model of $\mathsf{PA}$.
5. The element $c^{\mathfrak{M}}$ differs from the value $\overline{n}^{\mathfrak{M}}$ of every numeral.
6. Suppose $h : \mathfrak{N} \to \mathfrak{M}$ is an isomorphism. Then $h(n) = \overline{n}^{\mathfrak{M}}$ for every $n$, since $h$ preserves $0$ and $S$.
7. So $h$ is onto only if every element of $M$ is the value of a numeral, and step 5 rules this out. Hence $\mathfrak{M}$ is not isomorphic to $\mathfrak{N}$.
8. Let $A \subseteq M$ be the set of values of numerals. Then $0^{\mathfrak{M}} \in A$, and $A$ is closed under $S^{\mathfrak{M}}$, since $S^{\mathfrak{M}}(\overline{n}^{\mathfrak{M}}) = \overline{n + 1}^{\mathfrak{M}}$.
9. But $A \ne M$, by step 5. So the second-order induction axiom fails in $\mathfrak{M}$ for $X = A$.
10. Every instance of the first-order schema holds in $\mathfrak{M}$. So no formula with parameters defines $A$ in $\mathfrak{M}$.

## Remarks

The example shows the exact difference: the schema speaks only about definable subsets, and the axiom speaks about all subsets.
A counting argument gives the same picture in $\N$: there are countably many formulas, so countably many definable sets, but uncountably many subsets of $\N$.
The model $\mathfrak{M}$ is a [[non-standard model of arithmetic|1QWN5CV4CG]], and its elements outside $A$ are the non-standard numbers.
The price of categoricity is the logic: second-order logic with full semantics has no complete proof system.
In [[second-order arithmetic|DC60FYCSPM]] with Henkin semantics, the induction axiom is a single sentence, but non-standard models return.

## Explanations

### L1 human

The second-order induction axiom says: every set of numbers that contains $0$ and is closed under "next" contains all numbers.
The first-order schema says this only for sets that a formula can describe.
Compactness gives a model of the schema with an extra number $c$ beyond all the usual numbers.
In that model, the set of usual numbers contains $0$ and is closed under "next", but it misses $c$.
So the second-order axiom fails there, while every first-order instance holds.

### L2 human

We check step 3 for $T_0 = \set{\text{finitely many axioms of } \mathsf{PA}, c \ne \overline{0}, c \ne \overline{5}, c \ne \overline{17}}$.

1. Take $k = 18$, larger than $0$, $5$ and $17$.
2. In $\mathfrak{N}$ with $c = 18$, the sentences $c \ne \overline{0}$, $c \ne \overline{5}$ and $c \ne \overline{17}$ hold.
3. The axioms of $\mathsf{PA}$ in $T_0$ hold in $\mathfrak{N}$, and they do not mention $c$.
4. So $\mathfrak{N}$ with $c = 18$ is a model of $T_0$.

The typical use of this example is to explain why first-order arithmetic has non-standard models.
A trap is to think that $\mathfrak{M}$ violates the schema; it satisfies every instance, and only the set $A$, which no formula defines, escapes induction.
