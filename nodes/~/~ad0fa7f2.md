---
tag: ~ad0fa7f2
kind: concept
name: Reducts and expansions
aliases: [reduct, expansion-of-a-structure, definitional-expansion]
msc: ["03C07"]
topics: [AY09KYSW81]
audience: ug2
uses: [983GZBQYT4, WDVVEYD6AT, K7XDVK5854, CY1TXHF6KQ]
sources:
  - url: https://en.wikipedia.org/wiki/Reduct
    locator: Definition; Examples
  - book: isbn:9780387987606
    locator: Chapter 1
  - book: isbn:9780521587136
    locator: Chapter 1
---

## Summary

Let $L \subseteq L'$ be [[signatures|WDVVEYD6AT]] and let $\mathcal{M}'$ be an $L'$-[[structure|983GZBQYT4]] with domain $M$.
The *reduct* of $\mathcal{M}'$ to $L$, written $\mathcal{M}' \restriction L$, is the $L$-structure with the same domain $M$ in which each symbol of $L$ has the same interpretation as in $\mathcal{M}'$; the symbols of $L' \setminus L$ are forgotten.
If $\mathcal{M} = \mathcal{M}' \restriction L$, then $\mathcal{M}'$ is an *expansion* of $\mathcal{M}$ to $L'$.
An expansion is *definitional* when each new symbol is interpreted by a relation, function or element that is [[definable|CY1TXHF6KQ]] without parameters in $\mathcal{M}$.
Reducts and expansions let us change the language of a structure without changing its elements, and so compare what different languages can say about one set.

## Motivation

The same set often carries several structures that we want to compare.
The real numbers form the ordered field $(\R, +, \cdot, <)$, the field $(\R, +, \cdot)$, the group $(\R, +)$ and the order $(\R, <)$.
Each smaller structure forgets some of the operations of the larger one.
In proofs we also add symbols: a constant for each element, to talk about parameters, or a symbol for a defined notion, to shorten formulas.
Reducts and expansions are the names for these two moves, and the main fact is that truth of a sentence depends only on the symbols that the sentence uses.

## Notation

We write $\mathcal{M}' \restriction L$ or $\mathcal{M}'|_L$ for the reduct.
For $A \subseteq M$, $L_A$ is $L$ with a new constant symbol $c_a$ for each $a \in A$, and $\mathcal{M}_A$ is the expansion of $\mathcal{M}$ to $L_A$ with $c_a^{\mathcal{M}_A} = a$.
Many books write $a$ instead of $c_a$.
In universal algebra, a reduct is often written by listing the remaining operations, as $(\R, +)$ for a reduct of $(\R, +, \cdot)$.

## Remarks

### Examples

- The additive group $(\R, +, -, 0)$ is a reduct of the ordered field $(\R, +, -, \cdot, 0, 1, <)$, and the ordered field is an expansion of the group.
- The structure $(\Z, <, 0)$ is the expansion of $(\Z, <)$ by a constant for $0$; see [[expansion by constants|~0804090f]].
- The structure $(\N, +, <)$ is a definitional expansion of $(\N, +)$, because $x < y$ is equivalent in $\N$ to $\exists z \, (x + z = y \land \neg(z + z = z))$.
- The ordered field $(\R, +, \cdot, <)$ is a definitional expansion of $(\R, +, \cdot)$, because $x < y$ holds exactly when $\exists z \, (\neg(z + z = z) \land x + z \cdot z = y)$, and $z + z = z$ holds only for $z = 0$.
- The structures $(\Q, <)$, $(\Q, B)$ with betweenness and $(\Q, =)$ are the first members of the list of [[reducts of the rational order|~040970c9]].

### Non-examples

- $(\Z, +)$ is not a reduct of the field $(\Q, +, \cdot)$, because a reduct keeps the domain; see [[this non-example|~8dc06e57]].
- $(\Z, +, <)$ is an expansion of $(\Z, +)$ but not a definitional one: the automorphism $x \mapsto -x$ of $(\Z, +)$ does not preserve $<$.

### Basic properties

- If $\varphi$ is an $L$-formula and $\bar{a}$ is a tuple in $M$, then $\mathcal{M}' \models \varphi(\bar{a})$ if and only if $\mathcal{M}' \restriction L \models \varphi(\bar{a})$, because the evaluation of $\varphi$ uses only the symbols of $\varphi$.
- So $\operatorname{Th}(\mathcal{M}' \restriction L)$ is the set of $L$-sentences in $\operatorname{Th}(\mathcal{M}')$, and elementarily equivalent structures have elementarily equivalent reducts.
- A set is definable with parameters from $A$ in $\mathcal{M}$ exactly when it is definable without parameters in $\mathcal{M}_A$.
- A definitional expansion has the same definable sets as the original structure, because each new symbol can be replaced by its defining formula; this is the semantic side of [[extension by definitions|GCK0NN60E4]].
- Each automorphism of $\mathcal{M}'$ is an automorphism of its reducts, so a reduct has at least as many automorphisms.

### History

Expansions by constants for the elements of a structure are the basis of the method of diagrams, which Abraham Robinson developed in his book of 1951.
Peter Cameron determined the reducts of $(\Q, <)$ up to interdefinability in 1976, and the classification of reducts of other homogeneous structures, such as the random graph, followed.

### Common errors

- To confuse a reduct with a substructure. A reduct keeps all elements and drops symbols; a substructure keeps all symbols and drops elements.
- To think that an expansion adds nothing new. The expansion $(\Z, +, <)$ of $(\Z, +)$ defines the set $\N$, which is not definable in $(\Z, +)$.
- To forget that a reduct "up to definability" is a different notion from a reduct in the strict sense: it allows any structure whose relations are definable in $\mathcal{M}$.

## Explanations

### L1 human

A structure is a set with some operations and relations.
A reduct keeps the same set and forgets some of the operations.
An expansion keeps the same set and adds new operations or relations.
For example, the whole numbers with addition and multiplication have the reduct "whole numbers with addition only".
Going the other way, we can add the order $<$ to the whole numbers with addition and get an expansion.

### L2 human

We show that the order of $(\N, +)$ is definable, so $(\N, +, <)$ is a definitional expansion of $(\N, +)$.

1. The element $0$ is the only $z \in \N$ with $z + z = z$, since $z + z = z$ gives $z = 0$.
2. So $\neg(z + z = z)$ says $z \ne 0$.
3. For $x, y \in \N$, $x < y$ holds exactly when $y = x + z$ for some $z \ne 0$.
4. So $\varphi(x, y) = \exists z \, (x + z = y \land \neg(z + z = z))$ defines $<$ in $(\N, +)$.

The typical use is to add a defined symbol to make formulas shorter without changing what can be said.
A trap is to try the same formula in $(\Z, +)$: there every $y$ is $x + z$ for some $z \ne 0$ when $y \ne x$, so the formula defines $\ne$, not $<$.

### L3 human

Reducts and expansions are the change-of-language operations of model theory, and the functor $\mathcal{M}' \mapsto \mathcal{M}' \restriction L$ commutes with substructures, products and ultraproducts.
Craig interpolation and Beth definability compare a theory with its reducts, and Robinson's joint consistency theorem combines expansions of a common reduct.
For a structure $\mathcal{M}$ it is often better to work "up to interdefinability": two structures on $M$ are interdefinable when they have the same $\emptyset$-definable sets.
For a countable $\aleph_0$-categorical $\mathcal{M}$, the reducts up to interdefinability correspond to the closed groups between $\operatorname{Aut}(\mathcal{M})$ and the full symmetric group; the [[reducts of the rational order|~040970c9]] are the first case.
Interpretations, treated in the sub-area on [[interpretations and imaginaries|SZRM3N6BXW]], go further and allow new domains built from definable sets.
