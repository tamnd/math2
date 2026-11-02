---
tag: ZS5TMX4G8P
kind: definition
name: Horn clause
msc: ["03B05", "03B70", "08C15"]
defines: QR92EZDTKF
uses: [0B3D4C8YF2]
sources:
  - url: https://en.wikipedia.org/wiki/Horn_clause
---

## Definition

A *literal* is an atomic formula or the negation of an atomic formula; it is *positive* in the first case and *negative* in the second.
A *clause* is a finite disjunction $L_1 \vee \cdots \vee L_k$ of literals, as in a [[conjunctive normal form|0B3D4C8YF2]].
A *Horn clause* is a clause in which at most one literal is positive.

## Remarks

A Horn clause with exactly one positive literal is a *definite clause*; one with no positive literal is a *goal clause*.
A definite clause $\neg p_1 \vee \cdots \vee \neg p_n \vee q$ is equivalent to the implication $p_1 \wedge \cdots \wedge p_n \rightarrow q$; for $n = 0$ it is the fact $q$.

Example: $\neg p \vee \neg q \vee r$ is a Horn clause, since only $r$ is positive.

Non-example: $p \vee q$ is not a Horn clause, since it has two positive literals.
No conjunction of Horn clauses is equivalent to it.
The satisfying assignments of a conjunction of Horn clauses are closed under the coordinatewise "and".
But $(1, 0)$ and $(0, 1)$ satisfy $p \vee q$, while $(0, 0)$ does not.

In first-order logic, the atoms may be any atomic formulas, and the clause is read as universally quantified over its variables.
