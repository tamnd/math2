---
tag: JAKSE2A1D4
kind: definition
name: Herbrand structure
msc: ["03B10"]
topics: [NJDME6F845]
audience: ug2
defines: HKW429DSDK
uses: [JKP0XNXRPB, Y6C40MHZZC, CWQV9PTCB3]
sources:
  - url: https://en.wikipedia.org/wiki/Herbrand_structure
    locator: lead section
---

## Definition

Let $L$ be a signature with at least one constant symbol, and let $H(L)$ and $B(L)$ be its [[Herbrand universe and Herbrand base|JKP0XNXRPB]].
A Herbrand structure for $L$ is an $L$-[[structure|Y6C40MHZZC]] $\mathcal{H}$ such that:

1. the domain of $\mathcal{H}$ is $H(L)$;
2. $c^{\mathcal{H}} = c$ for every constant symbol $c$;
3. $f^{\mathcal{H}}(t_1, \ldots, t_n) = f(t_1, \ldots, t_n)$ for every $n$-ary function symbol $f$ and all $t_1, \ldots, t_n \in H(L)$.

The relation symbols $R$ may have any interpretation $R^{\mathcal{H}} \subseteq H(L)^n$.
For $I \subseteq B(L)$, the Herbrand structure $\mathcal{H}_I$ has $R^{\mathcal{H}_I} = \set{(t_1, \ldots, t_n) : R(t_1, \ldots, t_n) \in I}$.
A Herbrand model of a set $\Sigma$ of $L$-sentences is a Herbrand structure that is a [[model|CWQV9PTCB3]] of $\Sigma$.

## Notation

The set $I$ is called a Herbrand interpretation.
The map $I \mapsto \mathcal{H}_I$ is a bijection from the subsets of $B(L)$ to the Herbrand structures for $L$.

## Remarks

Clauses 2 and 3 fix the interpretation of all constant and function symbols, so two Herbrand structures for $L$ differ only in their relations.
The equality symbol is interpreted as identity, as in every structure, so distinct closed terms are never equal in a Herbrand structure.
The concept page [[Herbrand structure|HKW429DSDK]] gives examples and the main theorem.

## Explanations

### L1 human

Take all the names that the language can form as the objects, let each name stand for itself, and then choose which basic facts about the names are true.

### L2 human

We check the definition on $L = \set{a, b, P}$ with two constants and one unary relation symbol.

1. $H(L) = \set{a, b}$, because there are no function symbols, and $B(L) = \set{P(a), P(b)}$.
2. Clauses 2 and 3 force $a^{\mathcal{H}} = a$ and $b^{\mathcal{H}} = b$, and there is nothing else to fix.
3. $P^{\mathcal{H}}$ can be any of the $4$ subsets of $\set{a, b}$, so there are $4$ Herbrand structures, one for each $I \subseteq B(L)$.
4. The structure $\mathcal{H}_I$ with $I = \set{P(a)}$ is a Herbrand model of $\set{P(a), \neg P(b)}$, and it is the only one.

The typical use is to look for models of a set of clauses among the subsets of $B(L)$.
A trap is to let $a$ and $b$ denote the same element; then the structure has one element and is not a Herbrand structure.
