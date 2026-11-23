---
tag: 06S4WGSEQA
kind: definition
name: Disjunctive normal form
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug1
defines: 0GVDFAY4KW
uses: [TT7WT5HPN9, 029JBBF693, 025YZN3VJW, 0F72FK8EKB]
sources:
  - url: https://en.wikipedia.org/wiki/Disjunctive_normal_form
    locator: Definition
  - book: isbn:9781482237726
    locator: Chapter 1
inventory: [CN2SAXWJ5G]
---

## Definition

We define the shape of formula that is an "or" of "and"s of literals.

Let $P$ be a set of propositional variables.
A literal is a variable $p \in P$ or its [[negation|029JBBF693]] $\neg p$.
A term is a [[conjunction|025YZN3VJW]] $l_1 \land \cdots \land l_k$ of $k \geq 1$ literals.
A [[propositional formula|TT7WT5HPN9]] is in disjunctive normal form (DNF) when it has the form
$$D_1 \lor D_2 \lor \cdots \lor D_m \qquad (m \geq 1),$$
where each $D_i$ is a term.
So a DNF is a [[disjunction|0F72FK8EKB]] of one or more conjunctions of one or more literals.
Let the variables of the formula be $p_1, \ldots, p_n$.
The DNF is full, or canonical, over $p_1, \ldots, p_n$ when each term contains each $p_i$ exactly once, as $p_i$ or as $\neg p_i$, and no two terms have the same literals.

## Notation

We drop the brackets inside a term and between terms, because $\land$ and $\lor$ are associative.
A term of a full DNF is a minterm.
For $a \in \{ 0, 1 \}^n$, the minterm $m_a$ contains $p_i$ when $a_i = 1$ and $\neg p_i$ when $a_i = 0$.
Terms are also called conjunctive clauses or products, and in circuit design a DNF is a "sum of products".

## Remarks

The definition is about the written shape of a formula.
Negation stands only directly in front of variables, so no negation hides a compound formula.
The only other connectives are $\land$ and $\lor$.
No $\lor$ lies inside a $\land$, so the formula splits at the top into cases, and each case is a plain list of conditions.

For example, $(p \land \neg q) \lor (q \land r) \lor \neg p$ is in DNF, with three terms.
The formula $p \land (q \lor r)$ fails the last condition, and $\neg(p \land q)$ fails the first.
A formula with one term, such as $p \land \neg q$, is in DNF and also in [[conjunctive normal form|07C4A8Y18K]].
So is a formula with one literal in each term, such as $p \lor \neg q$.
Every satisfiable formula is equivalent to a full DNF that is unique up to order, and the [[concept page|0GVDFAY4KW]] proves both facts.

## Explanations

### L1 human

A formula in disjunctive normal form is an "or" of "and"s.
Each "and" part describes one case, such as "$p$ is true and $q$ is false".
The whole formula is true when at least one of the cases holds.

### L2 human

We decide whether three formulas are in DNF.
The formula $(p \land q) \lor (\neg p \land \neg r)$ is in DNF, since it has two terms and each is a conjunction of literals.
The formula $(p \lor q) \land r$ is not, because the disjunction lies inside the conjunction; distribution gives $(p \land r) \lor (q \land r)$.
The formula $(p \land q \land \neg r) \lor (\neg p \land q \land r)$ is in DNF, and it is full over $p, q, r$, since each term contains each variable once.
Watch out: $(p \land q) \lor \neg p$ is a DNF, but it is not full over $p, q$, because its second term does not mention $q$.

### L3 human

A term with $k$ literals over $n$ variables fixes $k$ coordinates, so it describes a subcube of $\{ 0, 1 \}^n$ with $2^{n-k}$ points.
A DNF describes a set of rows as a union of subcubes, and a full DNF describes it as a union of single points.
Finding a smallest DNF means covering a set by as few subcubes as possible, which is the problem that Karnaugh maps and the [[Quine-McCluskey algorithm|W0HDZBF5FC]] solve.
