---
tag: Z6MCGB0ZFX
kind: concept
name: Tarskian hierarchy
aliases: [hierarchy-of-languages, typed-truth-hierarchy]
msc: ["03A05", "03B10"]
topics: [6Q4JJ2MMV8]
audience: grad
uses: [8FBF0EFFC9, D9G8M42GKC, YRV6SYK2BY, WP27CABPA4]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section T
    note: adopted
    mention: wikipedia://en/76765067#GAEI
    sections: [Summary]
  - url: https://plato.stanford.edu/entries/liar-paradox/
    locator: "Liar Paradox, 4.3.1 Typed restrictionist approaches"
  - url: https://en.wikipedia.org/wiki/Semantic_theory_of_truth
    locator: Motivation
inventory: [59V8G2NC68]
---

## Summary

A *Tarskian hierarchy* over the [[language of arithmetic|D8SD54M5PN]] $\mathcal{L}_0$ is the sequence of languages $\mathcal{L}_{n+1} := \mathcal{L}_n \cup \{T_n\}$, where $T_n$ is a new unary predicate.
In the intended model $\mathcal{N}_{n+1}$, the predicate $T_n$ holds of exactly the codes of the sentences of $\mathcal{L}_n$ that are true in $\mathcal{N}_n$.
The typed axioms are the T-sentences $T_k(\ulcorner \varphi \urcorner) \leftrightarrow \varphi$ for every $k$ and every sentence $\varphi$ of $\mathcal{L}_k$.
Each language has a truth predicate for the languages below it, and no language has a truth predicate for itself.
The hierarchy is the classical way to keep Convention T and avoid the [[liar paradox|KBYY281V8T]].

## Motivation

The [[semantic conception of truth|8FBF0EFFC9]] asks for a truth definition for a language $L$ that proves every T-sentence of $L$.
[[Tarski's undefinability theorem|YRV6SYK2BY]] shows that this definition cannot be in $L$ itself when $L$ can express its own syntax.
So the definition must be in a [[metalanguage|D9G8M42GKC]] that is essentially richer than $L$.
To speak about the truth of metalanguage sentences, we need a metametalanguage, and so on.
Iterating this step gives the hierarchy.

## Notation

1. $\mathcal{L}_0$ is the object language; in this page it is the language of arithmetic $\{0, S, +, \cdot\}$.
2. $T_n$ is the truth predicate of level $n$; it applies to sentences of $\mathcal{L}_n$.
3. $\mathcal{N}_0$ is the [[standard model|WP27CABPA4]], and $\mathcal{N}_{n+1}$ expands $\mathcal{N}_n$ by the interpretation of $T_n$.
4. Some texts write $\mathrm{Tr}_n$ or $\mathrm{True}_n$, and some start the count at $1$.

## Remarks

### Examples

1. The first levels over arithmetic, with the computation of $T_1(\ulcorner T_0(\ulcorner 2 + 2 = 4 \urcorner) \urcorner)$, are in [[this example|151M7YHAQV]].
2. A liar sentence for $T_1$ exists in $\mathcal{L}_2$, but it is simply true at level $2$; see [[the liar attempt at level one|VTTMVKGK40]].
3. Tarski's own setting has two levels: an object language and a metalanguage. An instance is the definition of [[truth for arithmetic in set theory|QS0FWVFZWZ]].
4. The theory $\mathsf{PA}$ plus the typed T-sentences of all levels is consistent. The expansion of $\mathcal{N}_0$ that interprets each $T_n$ as in $\mathcal{N}_{n+1}$ satisfies every axiom.

### Non-examples

1. A language with one type-free truth predicate, as in [[Kripke's theory of truth|ES71QTSTNV]], is not a level of the hierarchy. Its truth predicate applies to sentences that contain it.
2. A pair of claims that speak about each other cannot be placed in the hierarchy; see [[the example of Jc and Michael|8CMS44DM16]].
3. A predicate "true at some level" would apply to sentences of every level, including sentences that contain it. Allowing it brings back the paradox, as the SEP entry notes.

### Basic properties

1. Each $\mathcal{N}_{n+1}$ is well defined, by induction on $n$: the interpretation of $T_n$ uses only truth in $\mathcal{N}_n$.
2. In $\mathcal{N}_{n+1}$, the predicate $T_n$ satisfies Convention T for $\mathcal{L}_n$, by its definition.
3. No $T_n$ satisfies Convention T for $\mathcal{L}_{n+1}$, by the undefinability theorem applied to $\mathcal{L}_{n+1}$.
4. The diagonal lemma holds in every $\mathcal{L}_n$, so self-referential sentences exist at every level. They are harmless because $T_k$ is not applied to sentences of level above $k$ in the axioms.
5. The hierarchy can be continued into the transfinite, with a truth predicate for the union of all earlier levels at each limit stage.

### History

The SEP entry names Tarski (1936) as the oldest typed restrictionist approach, with an object language $\mathcal{L}_0$ and a metalanguage $\mathcal{L}_1$.
It reports that Kripke (1975) criticized the hierarchy because the level of an ordinary claim is not fixed by its syntax.
Wikipedia adds that, for Kripke, the level needed by a statement can depend on empirical facts.

### Common errors

1. Thinking that the hierarchy forbids self-reference. The diagonal lemma still gives self-referential sentences at each level; the hierarchy only restricts which T-sentences hold.
2. Thinking that $T_0(\ulcorner \psi \urcorner)$ is meaningless when $\psi$ contains $T_0$. It is a sentence of $\mathcal{L}_1$, and it is false in the intended model, because $T_0$ holds only of sentences of $\mathcal{L}_0$.
3. Forgetting that one natural-language word "true" would need infinitely many indexed predicates in this approach.

## Explanations

### L1 human

Think of a building with floors.
On the ground floor we speak only about numbers, for example "$2 + 2 = 4$".
On the first floor we can also say "the ground-floor sentence $2 + 2 = 4$ is true".
On the second floor we can say that a first-floor sentence is true, and so on.
A sentence can only call sentences on lower floors true or not true.
So the sentence "this sentence is not true" cannot use its own floor's word "true", and the liar paradox does not arise.

### L2 human

1. Let $\varphi := (2 + 2 = 4)$, a sentence of $\mathcal{L}_0$. It is true in $\mathcal{N}_0$.
2. By the definition of $\mathcal{N}_1$, the sentence $T_0(\ulcorner \varphi \urcorner)$ is true in $\mathcal{N}_1$.
3. $T_0(\ulcorner \varphi \urcorner)$ is a sentence of $\mathcal{L}_1$, so by the definition of $\mathcal{N}_2$, $T_1(\ulcorner T_0(\ulcorner \varphi \urcorner) \urcorner)$ is true in $\mathcal{N}_2$.
4. But $T_0(\ulcorner T_0(\ulcorner \varphi \urcorner) \urcorner)$ is false in $\mathcal{N}_1$, since $T_0(\ulcorner \varphi \urcorner)$ is not a sentence of $\mathcal{L}_0$.

The typical use is a consistent theory of truth for arithmetic in classical logic, with a separate predicate for each level.
The trap is step 4: the lower predicate does not "see" sentences of its own level, so iterated truth needs a higher index each time.

### L3 human

The hierarchy is the semantic counterpart of the ramified hierarchy of types.
Its axiomatic form is a sequence of [[typed theories of truth|KE8ZX8KVA3]], one for each level.
The type-free theories, from [[Kripke's theory of truth|ES71QTSTNV]] to the [[Kripke-Feferman theory|VQG258JQAD]], replace the fixed syntactic levels by stages of an inductive construction.
The page on the Kripke-Feferman theory states its strength in terms of ramified analysis, which is a transfinite hierarchy of this kind.
