---
tag: ZS5TMX4G8P
kind: definition
name: Horn clause
msc: ["03B05", "03B70", "08C15"]
topics: [JDK63589SA]
audience: ug2
defines: QR92EZDTKF
uses: [T3SXVH3ZZC]
sources:
  - url: https://en.wikipedia.org/wiki/Horn_clause
    locator: Definition
---

## Definition

A *literal* is a propositional variable $p$, a positive literal, or its negation $\neg p$, a negative literal.
A [[clause|T3SXVH3ZZC]] is a finite set of literals, read as their disjunction.

1. A *Horn clause* is a clause that contains at most one positive literal.
2. A *definite clause* is a clause that contains exactly one positive literal. A definite clause with no negative literal, $\set{q}$, is a *fact*.
3. A *goal clause* is a clause that contains no positive literal.
4. A *Horn formula* is a finite conjunction of Horn clauses, or equivalently a finite set of Horn clauses.

In first-order logic the literals are atomic formulas and their negations, and a clause is read as universally quantified over its free variables; the definitions 1 to 4 are the same.

## Notation

The definite clause $\set{\neg p_1, \ldots, \neg p_n, q}$ is written in implicative form as $p_1 \land \cdots \land p_n \to q$, or in logic programming as $q \leftarrow p_1, \ldots, p_n$, with head $q$ and body $p_1, \ldots, p_n$.
The goal clause $\set{\neg p_1, \ldots, \neg p_n}$ is written $\neg(p_1 \land \cdots \land p_n)$ or $\leftarrow p_1, \ldots, p_n$.

## Remarks

- Every definite clause and every goal clause is a Horn clause, and every Horn clause is one of the two.
- The empty clause $\square$ is a goal clause, so it is a Horn clause.
- $\set{\neg p, \neg q, r}$ is a definite clause with implicative form $p \land q \to r$.
- $\set{p, q}$, that is, $p \lor q$, is not a Horn clause, since it has two positive literals.
- The models of a set of Horn clauses are closed under intersection, every set of definite clauses has a least model, and Horn satisfiability is decidable in linear time. The concept page [[Horn clause|QR92EZDTKF]] proves the first two facts and gives the marking algorithm.

## Explanations

### L1 human

A Horn clause is a rule "if all of these are true, then this one is true", or a ban "these are not all true".
"If it rains and I go out, I take an umbrella" is a rule of this kind.
"It rains or it snows" is not, since it offers two possible outcomes.

### L2 human

We sort four clauses.

1. $\set{\neg p, q}$ has one positive literal, $q$: it is a definite clause, $p \to q$.
2. $\set{r}$ has one positive literal and no negative one: it is a fact.
3. $\set{\neg p, \neg r}$ has no positive literal: it is a goal clause, $\neg(p \land r)$.
4. $\set{p, \neg q, r}$ has two positive literals: it is not a Horn clause.

A trap: a Horn clause may have many negative literals; the condition limits only the positive ones.
