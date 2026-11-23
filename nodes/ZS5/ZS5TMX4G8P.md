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

We define the clauses that allow at most one positive conclusion.

A literal is a propositional variable $p$, a positive literal, or its negation $\neg p$, a negative literal.
A [[clause|T3SXVH3ZZC]] is a finite set of literals, read as their disjunction.

1. A *Horn clause* is a clause that contains at most one positive literal.
2. A *definite clause* is a clause that contains exactly one positive literal.
   A definite clause $\{ q \}$ with no negative literal is a *fact*.
3. A *goal clause* is a clause that contains no positive literal.
4. A *Horn formula* is a finite set of Horn clauses, read as their conjunction.

In first-order logic the literals are atomic formulas and their negations, a clause is read as universally quantified over its free variables, and the definitions 1 to 4 are the same.

## Notation

The definite clause $\{ \neg p_1, \ldots, \neg p_n, q \}$ is written in implicative form as $p_1 \land \cdots \land p_n \to q$.
Logic programming writes it as $q \leftarrow p_1, \ldots, p_n$, with head $q$ and body $p_1, \ldots, p_n$.
The goal clause $\{ \neg p_1, \ldots, \neg p_n \}$ is written $\neg(p_1 \land \cdots \land p_n)$ or $\leftarrow p_1, \ldots, p_n$.

## Remarks

The single condition, at most one positive literal, is what turns a clause into a rule.
With one positive literal $q$, the clause says that the negative literals together force $q$.
With none, it says that the negative literals cannot all be true.
With two or more, it would leave a choice between conclusions, and forward reasoning could no longer proceed without guessing.

So every Horn clause is either a definite clause or a goal clause.
The clause $\{ \neg p, \neg q, r \}$ is a definite clause with implicative form $p \land q \to r$.
The empty clause $\square$ has no positive literal, so it is a goal clause and a Horn clause.
The clause $\{ p, q \}$, that is, $p \lor q$, is not a Horn clause, since it has two positive literals.

The concept page [[Horn clause|QR92EZDTKF]] proves that the models of a Horn formula are closed under intersection and that every set of definite clauses has a least model.
It also gives the linear-time marking algorithm for satisfiability.

## Explanations

### L1 human

A Horn clause is a rule "if all of these are true, then this one is true", or a ban "these are not all true".
"If it rains and I go out, I take an umbrella" is a rule of this kind.
"It rains or it snows" is not, since it offers two possible outcomes.

### L2 human

We sort four clauses.
The clause $\{ \neg p, q \}$ has one positive literal, $q$, so it is the definite clause $p \to q$.
The clause $\{ r \}$ has one positive literal and no negative one, so it is a fact.
The clause $\{ \neg p, \neg r \}$ has no positive literal, so it is the goal clause $\neg(p \land r)$.
The clause $\{ p, \neg q, r \}$ has two positive literals, so it is not a Horn clause.
Watch out: a Horn clause may have many negative literals, because the condition limits only the positive ones.
