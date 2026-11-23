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

Logical constants are the words, such as "and", "not" and "all", whose meaning stays fixed when we test an argument for validity; every other word may be reinterpreted.
Where that line is drawn decides which arguments are valid by logic alone, and the problem of logicality asks for a principled way to draw it.

Compare two inferences about a relation $<$.
"From $x < y \wedge y < z$ infer $x < y$" stays valid however $<$ is read, because its force comes from $\wedge$.
"From $x < y \wedge y < z$ infer $x < z$" holds when $<$ is an order and fails when $<$ is read as "differs from", so it is valid only if $<$ itself counts as logical.

In exact terms, a logical constant of a [[formal language|5MFZ4VNY6D]] is a symbol whose interpretation is the same in every interpretation of the language.
In classical first-order logic the logical constants are the [[connectives|QS0XVAN9BG]] $\neg$, $\wedge$, $\vee$, $\to$, $\leftrightarrow$, the quantifiers $\forall$ ([[universal quantifier|0GHS47PDAQ]]) and $\exists$ ([[existential quantifier|0MSRQHCNN9]]), and usually the identity symbol $=$.
The other symbols, such as $<$, $+$ or $0$, are non-logical, and a [[structure|983GZBQYT4]] may interpret them in any way that fits their arity.

## Motivation

[[Logical consequence|1HK0VYWTV7]] is defined by form: an argument is valid when every reinterpretation of its non-logical symbols that makes the premises true also makes the conclusion true.
That definition needs a list of the symbols that may not be reinterpreted.
If $<$ on the natural numbers were logical, "$0 < 1$" would be a logical truth.
If $\wedge$ were non-logical, "from $A \wedge B$ infer $A$" would not be valid.
So different lists give different logics, and the list needs a reason.

Two kinds of reason have been proposed.
Semantic criteria call a notion logical when it cannot tell one object from another.
Proof-theoretic criteria call a symbol logical when rules of inference of a special balanced form give its whole meaning.

## Notation

For a nonempty set $D$, a permutation of $D$ is a [[bijective function|0SNQEF7Z53]] $\pi \colon D \to D$.
A permutation acts on every object built from $D$.
On an element $a$ it gives $\pi(a)$, and on an $n$-ary relation $R \subseteq D^n$ it gives $\pi[R] = \{(\pi(a_1), \ldots, \pi(a_n)) : (a_1, \ldots, a_n) \in R\}$.
On a set $Q$ of subsets of $D$, that is, a unary quantifier, it gives $\{\pi[X] : X \in Q\}$.
An object is permutation invariant when every permutation of $D$ maps it to itself.

"Logical constant" names a symbol, and "logical notion" or "logical operation" names its meaning on a domain.
A constant symbol of a signature, such as $0$ in arithmetic, is non-logical: "constant" there means "names one object", not "has a fixed meaning".

## Remarks

### The permutation criterion

In a lecture of 1966, published in 1986 as "What are logical notions?", Alfred Tarski proposed that a notion over a domain $D$ is logical when it is invariant under all permutations of $D$.
Logic, on this view, is the most general science: it cannot tell one object from another, so its notions survive every reshuffling of the objects.
Gila Sher extended the criterion from permutations of one domain to bijections between different domains, so that a logical operation behaves the same way on isomorphic structures.
This form is called isomorphism invariance, and the resulting view is often called the thesis of Tarski and Sher.

### What the criterion counts as logical

On a domain with at least two elements no single object is logical, because some permutation moves it.
Exactly four binary relations are invariant: the empty relation, [[identity|CX9MEPJF9D]], diversity and the full relation $D \times D$.
A unary quantifier is invariant exactly when its truth for a set $X$ depends only on the cardinalities of $X$ and of $D \setminus X$, as [[cardinality quantifiers are permutation invariant|HPA3BKNZE1]] shows.
So $\forall$ ($D \setminus X$ is empty), $\exists$ ($X$ is nonempty), "at least two", "infinitely many" and "more than half" all pass.
The truth-functional connectives pass at once, because they act on truth values and not on objects.

Every relation definable in pure first-order logic with identity is invariant, by induction on the formula.
The converse fails on infinite domains: "infinitely many" is invariant, but by the [[compactness theorem|1NR3HAWG9D]] no first-order formula expresses it.

### What the criterion rules out

[[The order of the natural numbers|9WVJK3DWAN]] is not logical, because the permutation that swaps $0$ and $1$ sends the pair $(0, 1)$ in $<$ to $(1, 0)$, which is not in $<$.
The membership relation $\in$ on a domain of sets is not logical either, because a permutation of the sets can break it.
On this view set theory is a theory with its own subject matter, not a part of logic.
A quantifier such as "$X$ contains the number $1$" fails as well: the swap of $1$ and $2$ sends $\{1\}$ to $\{2\}$.

### McGee's theorem

Vann McGee proved in 1996 that an operation is invariant under all bijections between domains if and only if it is definable by a formula of the [[infinitary logic|PQG7VAZ1R2]] $L_{\infty\infty}$ that uses identity and no non-logical symbols.
$L_{\infty\infty}$ allows conjunctions and disjunctions of any set of formulas and quantification over any set of variables.
So isomorphism invariance makes logic much larger than first-order logic: every cardinality quantifier counts as logical, and with them much of the theory of cardinal numbers.

### Proof-theoretic criteria

Gerhard Gentzen remarked that the introduction rules of [[natural deduction|6KT3BJZ7D1]] can be read as definitions of the connectives, with the elimination rules as their consequences.
On this view a symbol is logical when its introduction and elimination rules fix its meaning and are in [[harmony|XJSQVK0G71]]: the elimination rules give back exactly what the introduction rules put in.

Arthur Prior's connective [[tonk|QSVQ1KPNBX]] of 1960 shows that some such condition is needed.
It has the introduction rule of $\vee$, "from $A$ infer $A \text{ tonk } B$", and the elimination rule of $\wedge$, "from $A \text{ tonk } B$ infer $B$", so every $B$ follows from every $A$.
Nuel Belnap answered in 1962 that a new connective must give a [[conservative extension|N238J43XNE]]: it may not create new consequences among formulas that do not contain it.
Harmony is tied to the normalization theorems of [[structural proof theory|R10RMQCJQX]].

The standard rules for the intuitionistic connectives and quantifiers are harmonious.
Classical negation is not, in the usual single-conclusion natural deduction, because double negation elimination is not justified by the introduction rule of $\neg$.
It passes only in reformulated systems, such as calculi with several conclusions.

### Watch out

Permutation invariance is a property of a notion over a domain, not of a symbol.
A symbol is logical when its meaning on every domain is invariant.
Passing the criterion does not make a notion first-order: "infinitely many" passes, and first-order logic cannot express it.
Testing one permutation is not enough, since a relation can be fixed by some permutations and moved by others.
The two criteria disagree: the semantic one admits "infinitely many", the proof-theoretic one has no rules for it.

### History

Bolzano saw that what follows from what depends on which ideas are held fixed.
Tarski, in his paper of 1936 on logical consequence, made the same point about logical constants and left the choice open.
His lecture of 1966 gave the permutation criterion, and it was published in 1986.
Sher developed the isomorphism criterion in *The Bounds of Logic* (1991), and McGee's theorem appeared in 1996.
Prior's "tonk" (1960) and Belnap's reply (1962) started the proof-theoretic line.

### Try it

On $D = \{1, 2\}$, which subsets of $D$, viewed as unary relations, are permutation invariant?
Only $\varnothing$ and $D$: the swap of $1$ and $2$ sends $\{1\}$ to $\{2\}$.

On a domain with $n$ elements, how many invariant unary quantifiers are there?
A quantifier is fixed by the set of sizes $|X| \in \{0, 1, \ldots, n\}$ for which it holds, so there are $2^{n+1}$ of them.

## Explanations

### L1 human

Some words in an argument carry the logic, and other words carry the content.
In "all cats are animals, Tom is a cat, so Tom is an animal", the words "all" and "is" carry the logic.
If we replace "cat" by "dog" and "animal" by "mammal", the argument stays correct, so those words carry only content.
The question of logical constants is which words belong to the first kind.
One answer says that a word is logical when it cannot tell objects apart.
The word "all" does not care which objects there are, but the word "cat" picks out some objects and not others.

### L2 human

We check the permutation criterion for two binary relations on $D = \{1, 2, 3\}$, using the permutation $\pi$ with $\pi(1) = 2$, $\pi(2) = 1$ and $\pi(3) = 3$.

1. The relation $<$ on $D$ is $\{(1, 2), (1, 3), (2, 3)\}$.
2. Applying $\pi$ to each pair gives $(2, 1)$, $(2, 3)$ and $(1, 3)$.
3. So $\pi[<]$ contains $(2, 1)$ and differs from $<$, and $<$ is not logical by the criterion.
4. The identity relation is $\{(1, 1), (2, 2), (3, 3)\}$.
5. Applying $\pi$ gives $(2, 2)$, $(1, 1)$ and $(3, 3)$, the same set.
6. The same holds for each of the $6$ permutations of $D$, because a pair $(a, a)$ always goes to a pair $(\pi(a), \pi(a))$.
7. So identity is logical by the criterion.

The criterion is a quick test for a proposed new quantifier or connective, such as a generalized quantifier from linguistics.
The trap is to stop after one permutation: one failure refutes invariance, but a success proves it only when it covers every permutation.

### L3 human

Tarski presented permutation invariance as the end point of Felix Klein's Erlangen program, the case in which the transformation group is as large as possible.
Geometry studies the invariants of the Euclidean group, topology those of the homeomorphisms, and logic those of all bijections.
By McGee's theorem the invariants of all bijections are the notions definable in $L_{\infty\infty}$ from identity alone, a Galois-type correspondence between groups and definable notions of the kind model theory studies for automorphism groups.

The two criteria give different logics.
The semantic criterion admits all cardinality quantifiers, so it leans toward [[second-order logic and its extensions|MDHDYV8QZW]].
The proof-theoretic criterion fits first-order logic and fits [[intuitionistic logic|Q11N8X99FK]] even better, since all its constants have harmonious rules.
Lindström's theorem characterizes first-order logic as the strongest logic with compactness and the downward Löwenheim-Skolem property, which gives a third, model-theoretic answer to "why first-order logic?".
The philosophical side, whether logic is topic-neutral and what that means, belongs to the [[philosophy of mathematics|NTJ5XW0PVD]].
