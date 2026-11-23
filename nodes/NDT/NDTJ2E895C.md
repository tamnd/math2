---
tag: NDTJ2E895C
kind: statement
role: lemma
name: Isomorphism invariance of truth
aliases: [isomorphic-structures-are-elementarily-equivalent]
msc: ["03C07"]
topics: [NJDME6F845]
audience: ug2
about: [K7XDVK5854, PZMGQMDN25]
uses: [1WTCZB4DVB, YWTERZZME5, 983GZBQYT4, K7XDVK5854]
sources:
  - book: isbn:9780122384523
    locator: Section 2.2
  - url: https://en.wikipedia.org/wiki/Elementary_equivalence
    locator: lead section
  - url: https://builds.openlogicproject.org/
    locator: Theories and Their Models
---

## Statement

Isomorphic structures make the same sentences true, because an isomorphism only renames the elements and first-order logic cannot see names.

Let $\mathcal{M}$ and $\mathcal{N}$ be $L$-[[structures|983GZBQYT4]] with domains $M$ and $N$, and let $h \colon M \to N$ be an [[isomorphism|YWTERZZME5]].
So $h$ is a bijection with $h(c^{\mathcal{M}}) = c^{\mathcal{N}}$ and $h(f^{\mathcal{M}}(a_1, \ldots, a_n)) = f^{\mathcal{N}}(h(a_1), \ldots, h(a_n))$, and with $(a_1, \ldots, a_n) \in R^{\mathcal{M}}$ if and only if $(h(a_1), \ldots, h(a_n)) \in R^{\mathcal{N}}$.

1. For every term $t$ and every assignment $s$ in $\mathcal{M}$, we have $h(t^{\mathcal{M}}[s]) = t^{\mathcal{N}}[h \circ s]$.
2. For every formula $\varphi$ and every assignment $s$ in $\mathcal{M}$, we have $\mathcal{M} \models \varphi[s]$ if and only if $\mathcal{N} \models \varphi[h \circ s]$.
3. For every sentence $\sigma$, we have $\mathcal{M} \models \sigma$ if and only if $\mathcal{N} \models \sigma$.
   So $\operatorname{Th}(\mathcal{M}) = \operatorname{Th}(\mathcal{N})$.

Here $\models$ is [[satisfaction|1WTCZB4DVB]] in parts 1 and 2, and [[truth|K7XDVK5854]] in part 3.

## Remarks

### A first check

The map $h(n) = 2n$ is an isomorphism from $(\mathbb{Z}, +)$ onto the even integers $(2\mathbb{Z}, +)$, because it is a bijection and $2(m + n) = 2m + 2n$.
Test the sentence $\sigma = \forall x \, \exists y \, (y + y = x)$, which says that every element can be halved.
In $(\mathbb{Z}, +)$ it is false: for $x = 1$, no integer $y$ has $y + y = 1$.
In $(2\mathbb{Z}, +)$ it is false as well: for $x = 2$, the only solution of $y + y = 2$ is $y = 1$, and $1$ is not in the domain.
The lemma predicted this, and the counterexample moved along $h$, from $1$ to $h(1) = 2$.

### How to use it

The lemma is mostly used backward, to prove that two structures are not isomorphic.
The same sentence $\sigma$ is true in $(\mathbb{Q}, +)$, since $x = \tfrac{x}{2} + \tfrac{x}{2}$.
So $(\mathbb{Q}, +)$ and $(\mathbb{Z}, +)$ are not isomorphic, and no clever bijection can change that.
In the same way, $\exists x \, \forall y \, \neg (y < x)$ says that there is a least element, so it separates $(\mathbb{N}, <)$ from $(\mathbb{Z}, <)$.

The lemma also says that the class of [[models|MVCH6N9SNW]] of any set of sentences is closed under isomorphism.

### Automorphisms and definable sets

Apply part 2 with $\mathcal{N} = \mathcal{M}$ and an [[automorphism|DSQ17TNW1C]] $h$ of $\mathcal{M}$.
If $\varphi(x_1, \ldots, x_n)$ has no parameters and defines $X \subseteq M^n$, then $h$ maps $X$ onto $X$.
With parameters $b_1, \ldots, b_m$, the same holds for every automorphism that fixes each $b_j$.
This is the standard tool to prove that a set is not [[definable|1DQ1M6ZWS4]].
For example, $n \mapsto -n$ is an automorphism of $(\mathbb{Z}, +)$ that moves $1$ to $-1$, so no formula without parameters defines the positive integers there.

### Why each hypothesis is needed

Surjectivity is needed.
The inclusion of $(\mathbb{N}, <)$ into $(\mathbb{Z}, <)$ is injective and preserves and reflects $<$, yet the least-element sentence above is true in the first and false in the second.

Injectivity is needed.
In the empty signature, let $\mathcal{M}$ have domain $\{0, 1\}$ and $\mathcal{N}$ have domain $\{0\}$, with $h$ constant.
Then $\exists x \, \exists y \, \neg (x = y)$ is true in $\mathcal{M}$ and false in $\mathcal{N}$.

Reflection of relations is needed.
The identity map from $(\{0, 1\}, \emptyset)$ to $(\{0, 1\}, \{(0, 1)\})$ is a bijective homomorphism for one binary relation symbol $R$.
The sentence $\exists x \, \exists y \, R(x, y)$ is false in the first structure and true in the second.

### The converse

The converse of part 3 is false: structures with the same true sentences, called [[elementarily equivalent|P3B1V182N4]], need not be isomorphic.
The standard example is $(\mathbb{Q}, <)$ and $(\mathbb{R}, <)$.
Model theory shows that they satisfy the same sentences, since both are dense linear orders without endpoints, but they are not isomorphic, because $\mathbb{Q}$ is countable and $\mathbb{R}$ is not.
By the [[Löwenheim-Skolem theorem|484M0TZ1S7]], every infinite structure is elementarily equivalent to a structure of a different cardinality, so the converse fails for every infinite structure.
For finite structures in a finite signature the converse holds, because one sentence describes a finite structure up to isomorphism.

### Generalizations

An elementary embedding preserves and reflects all formulas, by definition, and an isomorphism is the same as a surjective elementary embedding.
A homomorphism preserves every positive existential formula, that is, every formula built from atomic formulas with $\wedge$, $\vee$ and $\exists$.
An embedding preserves and reflects every quantifier-free formula.

### Watch out

A bijection between the domains is not enough.
The map $n \mapsto n + 1$ is a bijection from $\mathbb{Z}$ to $\mathbb{Z}$, but it is not an isomorphism of $(\mathbb{Z}, +, 0)$, since it sends $0$ to $1$ and $0 + 0 = 0$ to $1 \neq 1 + 1$.
Before you transfer a sentence, check that the map respects every symbol of the signature, in both directions for the relation symbols.

### Try it

Show that $(\mathbb{Z}, +)$ and $(\mathbb{Z} \times \mathbb{Z}, +)$ are not isomorphic.
The sentence $\exists x \, \forall y \, \exists z \, (y = z + z \vee y = x + z + z)$ says that there are at most two classes modulo doubling; it is true in $\mathbb{Z}$ with $x = 1$, and false in $\mathbb{Z} \times \mathbb{Z}$, where there are four classes modulo $2$.

Is $n \mapsto -n$ an isomorphism from $(\mathbb{Z}, <)$ to itself?
No: it reverses the order, since $1 < 2$ but $-1 > -2$.

## History

The recursive definition of satisfaction that the proof follows is the one Tarski gave in 1933.
The lemma is proved in every textbook treatment of first-order semantics, usually right after the definition of truth.

## Explanations

### L1 human

Two structures are isomorphic when one is an exact copy of the other with the elements renamed.
Think of a chess game written in two notations: the moves are the same, only the labels differ.
A statement in the language can only talk about how the elements relate, not about their labels.
So renaming cannot change which statements are true.

### L2 human

We check part 2 for the isomorphism $h(n) = -n$ from $(\mathbb{Z}, <)$ to $(\mathbb{Z}, >)$, which is the integers with the symbol $<$ read as "greater than".
Let $\varphi = \exists y \, (x < y)$ and $s(x) = 3$.
In $(\mathbb{Z}, <)$, the witness $4$ gives $3 < 4$, so $\varphi$ is satisfied under $s$.
Under $h \circ s$, the variable $x$ has the value $-3$, and in $(\mathbb{Z}, >)$ we need some $b$ with
$$-3 > b.$$
The witness $b = -4 = h(4)$ works, so $\varphi$ is satisfied under $h \circ s$, as part 2 predicts.
Notice that the witness moved along $h$, which is exactly the quantifier step of the [[proof|X3XGDVSANT]].

### L3 human

Part 3 says that the map $\mathcal{M} \mapsto \operatorname{Th}(\mathcal{M})$ is constant on isomorphism classes.
Abstract model theory takes this property as part of the definition of a logic, so every logic in that sense satisfies it.
The automorphism consequence says that definable sets are unions of orbits of the automorphism group, though not every union of orbits is definable.
Model theory studies the finer relation of elementary equivalence and the maps that preserve all formulas, the elementary embeddings.
