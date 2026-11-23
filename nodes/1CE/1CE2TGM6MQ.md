---
tag: 1CE2TGM6MQ
kind: concept
name: Łukasiewicz three-valued logic
aliases: [l3, lukasiewicz-three-valued-logic]
msc: ["03B50"]
topics: [WZP584JQ06]
audience: grad
uses: [DWYCKAKXZD, 66NMTCQNQV, 0Y0MQYST0M]
sources:
  - url: https://en.wikipedia.org/wiki/%C5%81ukasiewicz_logic
    locator: Three-valued logic
  - url: https://plato.stanford.edu/entries/lukasiewicz/
    locator: 5.1 Possibility and the Third Value; 5.2 Indeterminism and the Third Value; 5.4 Axioms and Definitions
  - url: https://en.wikipedia.org/wiki/Three-valued_logic
    locator: Łukasiewicz logic
---

## Summary

Here is the implication of Łukasiewicz's three-valued logic, with the row for $x$ and the column for $y$.

| $x \to y$ | $y = 0$ | $y = \tfrac12$ | $y = 1$ |
|---|---|---|---|
| $x = 0$ | $1$ | $1$ | $1$ |
| $x = \tfrac12$ | $\tfrac12$ | $1$ | $1$ |
| $x = 1$ | $0$ | $\tfrac12$ | $1$ |

The corners are the classical table, and the new entries follow one rule: $x \to y$ is fully true when $x \le y$, and otherwise it loses as much truth as $x$ exceeds $y$.
So $\tfrac12 \to \tfrac12 = 1$, and that single entry makes $p \to p$ a law even when $p$ is undecided.

Exactly, as in [[the definition|F9NDCFY3GS]], $\mathrm{Ł}_3$ is the [[many-valued logic|DWYCKAKXZD]] of the matrix with values $\{0, \tfrac12, 1\}$, designated set $\{1\}$ and the two operations below.
$$\neg x = 1 - x, \qquad x \to y = \min(1, 1 - x + y)$$
Disjunction and conjunction are derived, and they take the values $\max$ and $\min$.
$\mathrm{Ł}_3$ is the first many-valued logic, and it starts the family that leads to [[infinite-valued Łukasiewicz logic|NFCEM44XYH]] and to [[MV-algebras|8T4M7RN9AC]].

## Motivation

Łukasiewicz wanted a logic for an open future.
In his view a sentence about a contingent future event, such as "there will be a sea battle tomorrow", is neither true nor false today.
He gave such sentences the third value $\tfrac12$, read "possible", and kept the classical tables for the values $0$ and $1$.

The result is a logic with a real implication: modus ponens holds, many classical laws survive, and the third value blocks exactly the laws that seem to decide the future in advance, such as $p \lor \neg p$.
Kleene's three-valued logic has the same tables for $\neg$, $\land$ and $\lor$, and the comparison below shows how much one entry of a table can change.
Mundici later found a second reading of $\mathrm{Ł}_3$, as the logic of a guessing game in which one answer may be a lie, as [[the Rényi-Ulam game|402GXME26B]] explains.

## Notation

$\mathrm{Ł}_3$ is also written $\mathrm{L}_3$ or $\text{Ł}3$.
Łukasiewicz wrote formulas in Polish notation, with $C$ for implication and $N$ for negation, so $CpCqp$ means $p \to (q \to p)$.
The middle value is written $\tfrac12$, $I$ or $U$.
The strong connectives are $x \oplus y = \neg x \to y = \min(1, x + y)$ and $x \odot y = \neg(x \to \neg y) = \max(0, x + y - 1)$.

## Remarks

### Laws that survive and laws that fail

Since $\min(1, 1 - x + x) = 1$, the law $p \to p$ holds.
Excluded middle fails: at $p = \tfrac12$ the value is $\max(\tfrac12, \tfrac12) = \tfrac12$, as [[the worked case|6S872VHF67]] shows.
Contraposition holds, because $\neg y \to \neg x = \min(1, 1 - (1 - y) + (1 - x))$, which is $\min(1, 1 - x + y)$ again.
Contraction fails: at $p = \tfrac12$ and $q = 0$ the formula $(p \to (p \to q)) \to (p \to q)$ has the value below.
$$\bigl(\tfrac12 \to \tfrac12\bigr) \to \tfrac12 = 1 \to \tfrac12 = \tfrac12$$
Wajsberg's axiom $((p \to \neg p) \to p) \to p$ holds, as [[the definition|F9NDCFY3GS]] checks row by row.

### Three logics on three values

[[Strong Kleene logic|SZHA10A9X7]] uses the same values, negation, $\min$ and $\max$, with implication $\max(1 - x, y)$.
That table differs from Łukasiewicz's only at $\tfrac12 \to \tfrac12$, where it gives $\tfrac12$, so [[Ł3 is not strong Kleene logic|61J1PFA9CW]]: $p \to p$ is a law of one and not of the other.
The difference is not a choice of notation, because [[no Kleene formula defines Łukasiewicz implication|729J1FD1GZ]].
[[One formula in all three logics|XZ2NRGZ69N]] adds weak Kleene logic to the comparison.

### The rules you can use

Every tautology of $\mathrm{Ł}_3$ is a classical tautology, since the tables restrict to the classical ones on $\{0, 1\}$.
[[Modus ponens|0Y0MQYST0M]] is valid: at $x = 1$ the table gives $1 \to y = y$, so a designated $p \to q$ forces $q = 1$.
Conjunction and disjunction are definable, with $x \lor y = (x \to y) \to y$ and $x \land y = \neg(\neg x \lor \neg y)$.
Wajsberg's four axioms with modus ponens give exactly the tautologies.

### What it is not

[[The four-valued Łukasiewicz logic refutes Wajsberg's axiom|BK6EPGABW8]], so $\mathrm{Ł}_4$ is not a model of $\mathrm{Ł}_3$, although the two use the same formulas for $\neg$ and $\to$.
The connectives of $\mathrm{Ł}_3$ are [[not functionally complete|TCVVFJ46VR]], because they map classical inputs to classical outputs and so never define the constant $\tfrac12$.
Classical logic is not $\mathrm{Ł}_3$ either, since $p \lor \neg p$ separates them.

### Watch out

The classical deduction theorem fails.
We have $p \land \neg p \models q$, because $\min(x, 1 - x) \le \tfrac12$ and the premise is never designated.
But $(p \land \neg p) \to q$ has the value $\tfrac12 \to 0 = \tfrac12$ at $p = \tfrac12$, $q = 0$, so it is not a tautology.
A second trap is to define disjunction by $\neg x \to y$.
That gives the strong disjunction $\min(1, x + y)$, which is $1$ at $x = y = \tfrac12$, while $\max(\tfrac12, \tfrac12) = \tfrac12$.

### History

Łukasiewicz published his three-valued logic in 1920, with future contingents as his motivation.
The joint paper of Łukasiewicz and Tarski of 1930 presents the $n$-valued and infinite-valued generalizations.
Wajsberg axiomatized $\mathrm{Ł}_3$ in 1931, with four axioms in implication and negation and modus ponens as the rule.

### Try it

First, is $p \to (q \to p)$ a tautology of $\mathrm{Ł}_3$?
Yes: $q \to p \ge p$ for all values, and $x \to z = 1$ whenever $x \le z$.

Second, find the value of $(p \to q) \lor (q \to p)$ at $p = \tfrac12$, $q = 0$.
It is $\max(\tfrac12, 1) = 1$; in fact this formula is always $1$, since one of $x \le y$ and $y \le x$ holds.

## Explanations

### L1 human

Łukasiewicz added a third truth value, "possible", written $\tfrac12$.
"Not" turns $\tfrac12$ into $\tfrac12$.
"If $x$ then $y$" is fully true when the condition is no truer than the conclusion.
So "if $p$ then $p$" is always fully true, even when $p$ is only possible.
But "$p$ or not $p$" is only $\tfrac12$ when $p$ is $\tfrac12$, so it is not a law.

### L2 human

We test the classical law $\neg p \to (p \to q)$, "a false statement implies anything".
Start with the inner implication and then the outer one:
$$\neg x \to (x \to y) = \min\bigl(1, x + \min(1, 1 - x + y)\bigr) = \min(1, 1 + x, 1 + y) = 1.$$
So the law holds in $\mathrm{Ł}_3$ for every row.
Check: at $x = \tfrac12$ and $y = 0$ we get $\tfrac12 \to \tfrac12 = 1$.
This row-by-row test, or its algebraic short form, is the typical way to decide which classical laws survive.
Watch out: a law can survive while its usual proof does not, because the proof may use contraction, which fails here.

### L3 human

The algebra of $\mathrm{Ł}_3$ is the three-element [[MV-algebra|8T4M7RN9AC]].
It satisfies $x \oplus x \oplus x = x \oplus x$, which fails at $x = \tfrac13$ in $[0, 1]$, so the variety it generates is a proper subvariety of all MV-algebras.
The finite-valued logics $\mathrm{Ł}_n$ come from the subalgebras $\{0, \tfrac{1}{n-1}, \dots, 1\}$ of $[0, 1]$, and the common tautologies of all of them are those of [[Łukasiewicz logic|NFCEM44XYH]].
Through [[Mundici's model of the Rényi-Ulam game|402GXME26B]], $\mathrm{Ł}_3$ is also the logic of searching with one lie.
