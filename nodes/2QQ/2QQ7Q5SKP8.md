---
tag: 2QQ7Q5SKP8
kind: concept
name: Logical constants and logicality
aliases: [constant-logic, logical-constants]
msc: ["03A05", "03C80"]
topics: [H8QZY0RZXZ]
audience: research
uses: [439M8B4DY2, 1HK0VYWTV7, 983GZBQYT4, 05RWFKVTJ7, XJSQVK0G71]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_constant
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Generalized_quantifier
    locator: lead section
  - wikipedia: en:4089175@r1374183857
    locator: Logical constant
    note: adopted
    mention: wikipedia://en/4089175
    sections: [Summary]
same_as:
  wikidata: Q1782658
  wikipedia: Logical constant
inventory: [5YVX9Z8E77]
---

## Summary

A logical constant of a [[formal language|5MFZ4VNY6D]] is a symbol whose meaning is fixed by the logic and does not change from one interpretation to another.
In classical first-order logic the logical constants are the [[connectives|QS0XVAN9BG]] $\neg$, $\wedge$, $\vee$, $\to$, $\leftrightarrow$, the quantifiers $\forall$ ([[universal quantifier|0GHS47PDAQ]]) and $\exists$ ([[existential quantifier|0MSRQHCNN9]]), and usually the identity symbol $=$.
The other symbols, such as $<$, $+$ or a constant $0$, are non-logical: a [[structure|983GZBQYT4]] may interpret them in any way that fits their arity.
The problem of logicality asks for a principled criterion that says which notions are logical.
The question matters because the line between logical and non-logical symbols decides which arguments count as valid "by logic alone", and so it fixes the meaning of [[logical consequence|1HK0VYWTV7]].

## Motivation

Logical consequence is defined by form: an argument is valid when every reinterpretation of its non-logical symbols that makes the premises true also makes the conclusion true.
This definition needs a list of the symbols that may not be reinterpreted.
If $<$ on the natural numbers were logical, then "$0 < 1$" would be a logical truth; if $\wedge$ were non-logical, then "from $A \wedge B$ infer $A$" would not be valid.
So the list is not a side issue, and different lists give different logics.
Two kinds of answer exist.
Semantic criteria say that a notion is logical when it does not distinguish between individual objects.
Proof-theoretic criteria say that a symbol is logical when its meaning is given completely by rules of inference of a special balanced form.

## Notation

For a nonempty set $D$, a permutation of $D$ is a [[bijective function|0SNQEF7Z53]] $\pi \colon D \to D$.
A permutation acts on each object built from $D$: on an element $a$ it gives $\pi(a)$, on an $n$-ary relation $R \subseteq D^n$ it gives $\pi[R] = \{(\pi(a_1), \ldots, \pi(a_n)) : (a_1, \ldots, a_n) \in R\}$, and on a set $Q$ of subsets of $D$ it gives $\{\pi[X] : X \in Q\}$.
An object is permutation invariant when every permutation of $D$ maps it to itself.
The words "logical constant" and "logical operation" are used for the symbol and for its meaning respectively; this page keeps the two apart.
Some textbooks call a constant symbol of a signature a "constant"; such a symbol is non-logical, and it is not a logical constant.

## Remarks

### The permutation invariance criterion

In a lecture of 1966, published in 1986 as "What are logical notions?", Alfred Tarski proposed the following criterion.
A notion over a domain $D$ (an object, a relation, a set of relations, and so on) is logical when it is invariant under all permutations of $D$.
The idea is that logic is the most general science: it cannot tell one object from another, so its notions must survive every reshuffling of the objects.
Gila Sher extended the criterion from permutations of one domain to bijections between different domains, so that a logical operation has the same behaviour on isomorphic structures.
This form of the criterion is called isomorphism invariance, and the resulting view is the Tarski-Sher thesis.

### What the criterion gives

- No individual object is logical when $D$ has at least two elements, because a permutation can move it.
- On a domain with at least two elements, exactly four binary relations are permutation invariant: the empty relation, [[identity|CX9MEPJF9D]], diversity and the full relation.
- The invariant sets of subsets of $D$, that is, the invariant unary quantifiers, are exactly those whose truth for a set $X$ depends only on the cardinalities of $X$ and of $D \setminus X$. See [[cardinality quantifiers are permutation invariant|HPA3BKNZE1]].
- So $\forall$ (the complement of $X$ is empty), $\exists$ ($X$ is nonempty), "there are at least two", "there are infinitely many" and "most" are logical by the criterion.
- The truth-functional connectives are logical, because they act on truth values and not on objects.

### McGee's theorem

Vann McGee proved in 1996 an exact description of the operations that pass the isomorphism criterion.
An operation is invariant under all bijections between domains if and only if it is definable by a formula of the [[infinitary logic|PQG7VAZ1R2]] $L_{\infty\infty}$ that uses only identity and no non-logical symbols.
The language $L_{\infty\infty}$ allows conjunctions and disjunctions of any set of formulas and quantification over any set of variables.
So the criterion makes logic much larger than first-order logic: it counts all cardinality quantifiers, and with them much of the theory of cardinal numbers, as logic.

### Proof-theoretic criteria

Gerhard Gentzen remarked that the introduction rules of [[natural deduction|6KT3BJZ7D1]] can be seen as definitions of the connectives, and that the elimination rules are consequences of them.
On this view a symbol is logical when its meaning is fixed by its introduction and elimination rules, and the rules are in [[harmony|XJSQVK0G71]]: the elimination rules give back exactly what the introduction rules put in.
Arthur Prior's connective "tonk" of 1960 shows why some condition is needed.
Its introduction rule is that of $\vee$ ("from $A$ infer $A \text{ tonk } B$") and its elimination rule is that of $\wedge$ ("from $A \text{ tonk } B$ infer $B$"), so any $B$ follows from any $A$.
See [[tonk|QSVQ1KPNBX]].
Nuel Belnap answered in 1962 that a new connective must give a conservative extension of the old system: it may not create new consequences between formulas without it.
This links logicality with [[conservative extensions|N238J43XNE]] and with the normalization theorems of [[structural proof theory|R10RMQCJQX]].

### Examples

- The identity relation is logical in Tarski's sense: every permutation maps a pair $(a, a)$ to a pair $(\pi(a), \pi(a))$, see [[the identity relation is permutation invariant|CX9MEPJF9D]].
- The quantifier "there are infinitely many" is logical in Tarski's sense, because a permutation preserves the cardinality of each set, see [[cardinality quantifiers are permutation invariant|HPA3BKNZE1]].
- Conjunction is logical in the proof-theoretic sense: its introduction rule and its two elimination rules are in harmony.
- The relation "$x$ and $y$ are different" is logical, because it is the complement of identity.

### Non-examples

- The order $<$ on the natural numbers is not logical: the permutation that swaps $0$ and $1$ maps the pair $(0, 1)$ in $<$ to the pair $(1, 0)$, which is not in $<$, see [[the order of the natural numbers is not a logical notion|9WVJK3DWAN]].
- The membership relation $\in$ of set theory is not logical by the criterion, because a permutation of the sets can break it; this is why set theory is a theory and not part of logic on this view.
- Prior's "tonk" is not logical in the proof-theoretic sense, because its rules are not in harmony.

### Basic properties

- The permutation invariant objects over $D$ are closed under the Boolean operations, under composition of relations and under the operations of first-order logic, because each permutation commutes with these operations.
- Every relation that is definable in pure first-order logic with identity is permutation invariant, by induction on the formula.
- The converse fails on infinite domains: "infinitely many" is invariant but not definable in first-order logic, by the [[compactness theorem|1NR3HAWG9D]].
- The logical constants of classical first-order logic pass both the semantic criterion and the proof-theoretic criterion.

### History

Bolzano and later Tarski, in his paper of 1936 on logical consequence, saw that consequence depends on the choice of logical constants, and Tarski left the choice open there.
Tarski's lecture of 1966 gave the permutation criterion, and the lecture was published in 1986.
Sher developed the isomorphism criterion in her book *The Bounds of Logic* (1991), and McGee's theorem appeared in 1996.
Prior's "tonk" (1960) and Belnap's reply (1962) started the proof-theoretic line.

### Common errors

- A "constant symbol" of a signature, such as $0$ in the language of arithmetic, is a non-logical symbol. The word "constant" there means "names one object", not "has a fixed meaning".
- Permutation invariance is a property of a notion over a domain, not of a symbol. A symbol is logical when its meaning on every domain is invariant.
- Passing the criterion does not make a notion first-order. "There are infinitely many" passes the criterion, and first-order logic cannot express it.

## Explanations

### L1 human

Some words in an argument carry the logic, and other words carry the content.
In "all cats are animals, Tom is a cat, so Tom is an animal", the words "all", "are" and "so" carry the logic.
If we replace "cat" by "dog" and "animal" by "mammal", the argument stays correct, so these words carry only content.
The question of logical constants is which words belong to the first kind.
One answer says: a word is logical when it cannot tell objects apart.
The word "all" does not care which objects there are, but the word "cat" picks out some objects and not others.

### L2 human

We check the permutation criterion for a binary relation on a small domain.
Let $D = \{1, 2, 3\}$, and let $\pi$ be the permutation with $\pi(1) = 2$, $\pi(2) = 1$ and $\pi(3) = 3$.

1. Take the relation $<$ on $D$, that is, $\{(1, 2), (1, 3), (2, 3)\}$.
2. Apply $\pi$ to each pair: $(1, 2) \mapsto (2, 1)$, $(1, 3) \mapsto (2, 3)$, $(2, 3) \mapsto (1, 3)$.
3. So $\pi[<] = \{(2, 1), (2, 3), (1, 3)\}$, which contains $(2, 1)$ and is not equal to $<$.
4. So $<$ is not permutation invariant, and it is not logical by the criterion.
5. Take the identity relation $\{(1, 1), (2, 2), (3, 3)\}$.
6. Apply $\pi$: $(1, 1) \mapsto (2, 2)$, $(2, 2) \mapsto (1, 1)$, $(3, 3) \mapsto (3, 3)$, so the image is the same set.
7. The same happens for each of the $6$ permutations of $D$, because each pair $(a, a)$ goes to a pair $(\pi(a), \pi(a))$.
8. So identity is permutation invariant, and it is logical by the criterion.

The typical use of the criterion is to test a proposed new quantifier or connective, for example a generalized quantifier from linguistics.
A trap is to test only one permutation: a relation can be fixed by some permutations and moved by others, and invariance needs all of them.

### L3 human

Permutation invariance is the case of Felix Klein's Erlangen program in which the transformation group is as large as possible.
Geometry studies the invariants of the Euclidean group, topology those of the homeomorphisms, and logic those of all bijections.
By McGee's theorem the invariants of all bijections are the notions definable in $L_{\infty\infty}$ from identity, which is a Galois-type correspondence between groups and definable notions, of the kind studied in model theory for automorphism groups of structures.

The two criteria give different logics.
The semantic criterion admits all cardinality quantifiers, and so it leans toward [[second-order logic and its extensions|MDHDYV8QZW]]; the proof-theoretic criterion fits first-order logic and also [[intuitionistic logic|Q11N8X99FK]], whose constants have harmonious rules.
Lindström's theorem, which characterizes first-order logic by compactness and the Löwenheim-Skolem property, gives a third, model-theoretic answer to the question "why first-order logic?".
The philosophical side of the question, whether logic is topic-neutral and what that means, belongs to the [[philosophy of mathematics|NTJ5XW0PVD]].
