---
tag: 06S4WGSEQA
kind: definition
name: Disjunctive normal form
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug1
defines: 0GVDFAY4KW
uses: [~7139c138, 029JBBF693, 025YZN3VJW, 0F72FK8EKB]
sources:
  - url: https://en.wikipedia.org/wiki/Disjunctive_normal_form
    locator: Definition
  - book: isbn:9781482237726
    locator: Chapter 1
inventory: [CN2SAXWJ5G]
---

## Definition

Let $P$ be a set of propositional variables.
A literal is a variable $p \in P$ or its [[negation|029JBBF693]] $\neg p$.
A term is a [[conjunction|025YZN3VJW]] $l_1 \land \cdots \land l_k$ of $k \geq 1$ literals.
A [[propositional formula|~7139c138]] is in disjunctive normal form (DNF) when it has the form
$$D_1 \lor D_2 \lor \cdots \lor D_m \quad (m \geq 1),$$
where each $D_i$ is a term.
So a DNF is a [[disjunction|0F72FK8EKB]] of one or more conjunctions of one or more literals.
Let the variables of the formula be $p_1, \ldots, p_n$.
The DNF is full (or canonical) over $p_1, \ldots, p_n$ when each term contains each $p_i$ exactly once, as $p_i$ or as $\neg p_i$, and no two terms have the same literals.

## Notation

Brackets inside a term and between terms are dropped, because $\land$ and $\lor$ are associative.
A term of a full DNF is a minterm; for $a \in \set{0,1}^n$, the minterm $m_a$ contains $p_i$ if $a_i = 1$ and $\neg p_i$ if $a_i = 0$.
Other names: terms are also called conjunctive clauses or products, and a DNF is a "sum of products" in circuit design.

## Remarks

The definition is purely syntactic: negation stands only directly in front of variables, the only other connectives are $\land$ and $\lor$, and no $\lor$ lies inside a $\land$.
So $(p \land \neg q) \lor (q \land r) \lor \neg p$ is in DNF, but $p \land (q \lor r)$ and $\neg(p \land q)$ are not.
A formula with one term, such as $p \land \neg q$, is both in DNF and in [[conjunctive normal form|0B3D4C8YF2]].
A formula with one literal in each term, such as $p \lor \neg q$, is also in both forms.
Every satisfiable formula is logically equivalent to a full DNF, which is unique up to order; the [[concept page|0GVDFAY4KW]] proves both facts.

## Explanations

### L1 human

A formula in disjunctive normal form is an "or" of "and"s.
Each "and" part describes one case, such as "$p$ is true and $q$ is false".
The whole formula is true when at least one of the cases holds.

### L2 human

We decide whether three formulas are in DNF.

1. $(p \land q) \lor (\neg p \land \neg r)$: two terms, each a conjunction of literals, so yes.
2. $(p \lor q) \land r$: the disjunction lies inside the conjunction, so no. By distributivity it is equivalent to $(p \land r) \lor (q \land r)$.
3. $(p \land q \land \neg r) \lor (\neg p \land q \land r)$: yes, and it is a full DNF over $p, q, r$, since each term contains each variable once.

A trap: $(p \land q) \lor \neg p$ is a DNF, but not a full DNF over $p, q$, because its second term does not contain $q$.

### L3 human

The DNFs over $n$ variables describe subsets of $\set{0,1}^n$ as unions of subcubes: a term with $k$ literals fixes $k$ coordinates and describes a subcube with $2^{n-k}$ points.
A full DNF is the description of a set as a union of single points.
Minimizing a DNF means covering a set by as few subcubes as possible, which is the problem solved by Karnaugh maps and the [[Quine-McCluskey algorithm|W0HDZBF5FC]].
