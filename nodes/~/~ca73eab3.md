---
tag: ~ca73eab3
kind: concept
name: Łukasiewicz infinite-valued logic
aliases: [lukasiewicz-infinite-valued-logic, lukasiewicz-logic]
msc: ["03B50", "03B52"]
topics: [WZP584JQ06]
audience: research
uses: [DWYCKAKXZD, ~d7a9d81e, ~d80767f3]
sources:
  - url: https://en.wikipedia.org/wiki/%C5%81ukasiewicz_logic
    locator: Axioms; Real-valued semantics; General algebraic semantics; Complexity
  - url: https://plato.stanford.edu/entries/logic-fuzzy/
    locator: 3. Łukasiewicz logic
  - url: https://plato.stanford.edu/entries/lukasiewicz/
    locator: 5.3 More than Three Values; 5.4 Axioms and Definitions
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: 2.4 A continuum of truth values; 4.2 When is a logic finite-valued?
  - url: https://en.wikipedia.org/wiki/MV-algebra
    locator: Relation to Łukasiewicz logic
  - book: isbn:9780792360094
---

## Summary

*Infinite-valued Łukasiewicz logic* $\mathrm{Ł}_\infty$ is the logic of the matrix on $[0, 1]$ with $\neg x = 1 - x$, $x \to y = \min(1, 1 - x + y)$ and designated value $1$; see [[the definition|~3e406741]].
It has a Hilbert-style axiomatization with four axiom schemas and modus ponens, which is complete for the $[0, 1]$-tautologies.
Its formulas define exactly the continuous piecewise linear functions with integer coefficients, by [[McNaughton's theorem|~dde0176d]], and its algebras are the [[MV-algebras|8T4M7RN9AC]].
It is the oldest [[fuzzy logic|~b4bfdbf0]] and the only t-norm based logic whose connectives are all continuous.

## Motivation

Łukasiewicz first used three values and then allowed any number of them.
In 1922 he gave the tables on all of $[0, 1]$ with the same formulas as for three values.
A continuum of values is natural for vague predicates, where "tall" can hold to any degree.
The logic also has a clean algebraic theory: it is to MV-algebras what classical logic is to Boolean algebras.

## Notation

We write $x \oplus y = \min(1, x + y)$ and $x \odot y = \max(0, x + y - 1)$ for strong disjunction and strong conjunction.
Other texts write $\otimes$ or $\&$ for $\odot$; on the notation see [[the topic page|WZP584JQ06]].
Weak conjunction and disjunction are $\min$ and $\max$, written $\land$ and $\lor$.
$\varphi^n$ is $\varphi \odot \dots \odot \varphi$ with $n$ factors, and $n \varphi$ is $\varphi \oplus \dots \oplus \varphi$.

## Remarks

### Examples

1. [[Contraction fails|~073d94cb]]: $p \to (p \odot p)$ has value $\tfrac12$ at $p = \tfrac12$.
2. [[Disjunction is definable from implication|~fc72b1ed]]: $(p \to q) \to q$ has value $\max(p, q)$.
3. The Łukasiewicz $n$-valued logics $\mathrm{Ł}_n$ use the same tables on $\set{0, \tfrac{1}{n-1}, \dots, 1}$; [[Łukasiewicz's three-valued logic|~d7a9d81e]] is $\mathrm{Ł}_3$.
4. Double negation $\neg \neg p \leftrightarrow p$ is a tautology, since $1 - (1 - x) = x$.

### Non-examples

1. [[Double negation fails in Gödel and product logic|~0b1c57f6]], so those logics are not $\mathrm{Ł}_\infty$.
2. Classical logic is not $\mathrm{Ł}_\infty$: $p \lor \neg p$ has value $\tfrac12$ at $p = \tfrac12$.

### Basic properties

1. Completeness. A formula is a theorem of the axioms with modus ponens iff it is a $[0, 1]$-tautology.
2. For a finite set $\Gamma$, $\Gamma \models \varphi$ iff $\Gamma \vdash \varphi$, by SEP.
3. This fails for infinite $\Gamma$. Let $\Gamma = \set{\neg p \to p^n : n \ge 1}$. If $p = x < 1$, then $p^n = 0$ for large $n$, and $\neg p \to p^n = x < 1$; so $\Gamma \models p$.
4. But each finite part $\set{\neg p \to p^n : n \le N}$ has value $1$ at $p = \tfrac{N}{N+1}$, since then $p^n = \tfrac{N+1-n}{N+1} \ge \tfrac{1}{N+1} = 1 - p$. So $\Gamma \not\vdash p$.
5. The tautologies of $\mathrm{Ł}_\infty$ are contained in those of every $\mathrm{Ł}_n$, by SEP.
6. Deciding tautologies is coNP-complete, as in classical logic (Mundici 1987).

### History

Łukasiewicz gave the $[0, 1]$-valued tables in 1922, and Łukasiewicz and Tarski presented the infinite-valued logic in 1930.
SEP reports that Wajsberg proved Łukasiewicz's conjecture that the axioms are complete, but the first published proof was by Rose and Rosser in 1958.
Chang gave an algebraic proof in 1958 and 1959 with MV-algebras; see [[Chang's completeness theorem|~e7bd3b21]].
McNaughton characterized the definable functions in 1951, and Mundici proved coNP-completeness in 1987.

### Common errors

1. Using $\land$ where $\odot$ is meant. Modus ponens in degrees uses $\odot$: $x \odot (x \to y) \le y$, while $\min(x, x \to y) \le y$ fails at $x = 0.6$, $y = 0.2$.
2. Assuming strong completeness. Property 3 shows a consequence that no proof from the premises can reach.
3. Thinking that $\mathrm{Ł}_\infty$ is the union of the finite-valued logics. It is their intersection: a formula valid in every $\mathrm{Ł}_n$ is $1$ on a dense set of rational points, hence everywhere by continuity.

## Explanations

### L1 human

Truth values are all numbers from $0$ to $1$.
"Not $x$" is $1 - x$.
"If $x$ then $y$" is fully true when $x \le y$, and otherwise loses exactly the amount by which $x$ exceeds $y$.
A formula is a law when it gets the value $1$ for every choice of values.

### L2 human

The typical computation is a piecewise linear one: split $[0, 1]^n$ into regions where each $\min$ and $\max$ picks a fixed argument.
For example, $p \to (q \to p)$ has value $\min(1, 1 - x + \min(1, 1 - y + x)) = 1$, since $1 - y + x \ge x$.
A trap: the value of $p \odot p$ at $p = \tfrac12$ is $0$, not $\tfrac14$; strong conjunction is not multiplication.

### L3 human

$\mathrm{Ł}_\infty$ is algebraizable with equivalent algebraic semantics the variety of MV-algebras, generated by $[0, 1]$.
Mundici's functor $\Gamma$ identifies MV-algebras with abelian lattice-ordered groups with a strong unit.
The free MV-algebra on $n$ generators is the algebra of McNaughton functions on $[0, 1]^n$.
