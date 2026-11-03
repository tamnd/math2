---
tag: CVQ0ENNXZ6
kind: statement
role: theorem
name: Sen's liberal paradox
msc: [91B14, 91B15]
uses: [JGP0Q56FRY, PW2NKAPXWA, KH8ACT22FR, JREVYHFY4T]
about: [F17C7F17PM]
sources:
  - url: https://en.wikipedia.org/wiki/Liberal_paradox
same_as:
  wikidata: Q1261223
  wikipedia: Liberal paradox
---

## Statement

Let $A$ be a finite set of alternatives and $N = \set{1, \dots, n}$ a finite set of $n \ge 2$ individuals.
Let $\mathcal{R}(A)$ be the set of [[weak orderings|PW2NKAPXWA]] of $A$.
A *social decision function* assigns to each profile $(R_1, \dots, R_n) \in \mathcal{R}(A)^n$ a reflexive and complete relation $R$ on $A$ whose strict part $P$ has no cycle $x_1 \mathrel{P} x_2 \mathrel{P} \cdots \mathrel{P} x_k \mathrel{P} x_1$.
Write $P_i$ for the strict part of $R_i$.
Consider the conditions:

1. (unrestricted domain) the function is defined on all of $\mathcal{R}(A)^n$;
2. (weak Pareto) if $x \mathrel{P_i} y$ for every $i$, then $x \mathrel{P} y$;
3. (minimal liberalism) there are distinct individuals $i, j$ and pairs $\set{x, y}$ and $\set{z, w}$ of alternatives such that $i$ is decisive over $\set{x, y}$ and $j$ over $\set{z, w}$.

Here $i$ is decisive over $\set{x, y}$ if, for every profile, $x \mathrel{P_i} y$ implies $x \mathrel{P} y$ and $y \mathrel{P_i} x$ implies $y \mathrel{P} x$.
Then no social decision function satisfies all three conditions.

## Remarks

Suppose first that the four alternatives $x, y, z, w$ are distinct.
Let individual $i$ have $w \mathrel{P_i} x \mathrel{P_i} y \mathrel{P_i} z$ and individual $j$ have $y \mathrel{P_j} z \mathrel{P_j} w \mathrel{P_j} x$, and let every other individual prefer $w$ to $x$ and $y$ to $z$.
Decisiveness gives $x \mathrel{P} y$ and $z \mathrel{P} w$, and [[weak Pareto|JREVYHFY4T]] gives $y \mathrel{P} z$ and $w \mathrel{P} x$.
This is the cycle $x \mathrel{P} y \mathrel{P} z \mathrel{P} w \mathrel{P} x$, which is not allowed.
The cases where the pairs share one alternative, or coincide, are handled in the same way with three or two alternatives.

Sen's illustration uses a book that one prude and one lewd reader may read.
The prude prefers that nobody reads it, and next that he reads it rather than the lewd one.
The lewd one prefers that the prude reads it, and next that he reads it himself.
Each person's right over his own reading, together with the Pareto principle, then produces a cycle.

## Explanations

### L1 human

Liberalism says each person should decide some matters alone, such as what they read.
The Pareto principle says that if everyone prefers one outcome to another, society should too.
Sen showed that these two mild principles can clash, even with just two people, whenever preferences are unrestricted.

### L2 human

Unlike Arrow's theorem, the result needs neither transitivity of social preference nor independence of irrelevant alternatives; acyclicity is enough.
It started a large literature on rights in social choice and on ways out, such as restricting the domain or letting individuals waive their rights.
It is often presented as a conflict between respecting individual rights and respecting unanimous preferences.
