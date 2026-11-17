---
tag: 0F72FK8EKB
kind: concept
name: Disjunction
aliases: [logical-or, inclusive-or]
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
uses: [0ZGC7ZESYN, 029JBBF693]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_disjunction
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.1
  - book: isbn:9781108439534
    locator: Section 3.5
same_as:
  wikidata: Q1651704
  wikipedia: Logical disjunction
---

## Summary

The disjunction of two [[propositions|0ZGC7ZESYN]] $p$ and $q$ is the proposition $p \lor q$, read "$p$ or $q$", which is true when at least one of $p$ and $q$ is true and false when both are false.
This "or" is inclusive: $p \lor q$ is true also when $p$ and $q$ are both true.
Disjunction is a [[logical connective|QS0XVAN9BG]] with two inputs; the precise definition and the truth table are on the page [[disjunction (definition)|0H5GKDTB01]].
To prove $p \lor q$, it is enough to prove one of $p$ and $q$; to use a hypothesis $p \lor q$, we argue by cases.
Disjunction expresses alternatives, so it appears in every case analysis, in the solutions of equations and in the union of sets.

## Motivation

Many facts of mathematics offer alternatives without saying which one holds.
Every integer is even or odd.
If $ab = 0$ for real numbers $a$ and $b$, then $a = 0$ or $b = 0$.
Each real number $x$ satisfies $x \geq 0$ or $x \leq 0$, and $x = 0$ satisfies both.
The last example shows why mathematics chose the inclusive reading: an alternative that allows both cases is common, and excluding the overlap would make such statements false.
The connective $\lor$ fixes this meaning, and its elimination rule is the method of proof by cases.

## Notation

This sub-area writes $p \lor q$.
Some books on Boolean algebra write $p + q$; in this sub-area $+$ is avoided, because $p + q$ modulo $2$ is the [[exclusive or|PTMR3P9J6C]].
In programming, disjunction is often written `p || q`.
In English, disjunction is expressed by "or", "either ... or" and, in many texts, "unless"; see [[translating statements into logical form|WGZX7GV3PP]].
In Lean's Mathlib, the disjunction of `a` and `b` is `Or a b`, written `a ∨ b`.

## Remarks

### Examples

1. [[Proof by cases: $n^2$ leaves remainder $0$ or $1$ on division by $4$|T6KQTVF2Q8]]: a disjunction is used by cases and proved by one of its parts.
2. [["$x \leq 3$ or $x \geq 2$" is true for every real $x$|BX9T7YS4B8]]: for $x$ from $2$ to $3$ both parts are true.
3. [[The inclusive "or" in "$n$ is even or $n$ is a multiple of $3$"|CER1EHMKW6]]: the statement is true for $n = 6$.
4. "$2$ is even or $2$ is prime" is true. Both parts are true, and the inclusive "or" accepts this.
5. "$x^2 = 4$" is equivalent to "$x = 2$ or $x = -2$"; see [[the condition $x^2 = 4$ is a disjunction, not a conjunction|7HZCKQQNKD]].

### Non-examples

1. [[The "or" of "the meal comes with soup or salad" is exclusive|XBS0DS337X]]: the restaurant's claim is false when the meal comes with both, so it is not a disjunction.
2. The [[exclusive or|PTMR3P9J6C]] $p \oplus q$ is not a disjunction: it is false when $p$ and $q$ are both true.
3. "Is $n$ even or odd?" is a question, not a proposition, so it is not a disjunction, although it contains "or".

### Inclusive and exclusive "or"

In daily speech, "or" is often exclusive: "tea or coffee" on a menu means one of the two, not both.
In mathematics, "or" is always inclusive unless the text says "but not both", "exactly one of" or "either ... or ..., but not both".
When the two parts cannot both be true, as in "$x < 0$ or $x \geq 0$", the two readings give the same truth value.
They differ only in the row where both parts are true.
The page [[connectives in mathematical language|12QQ51VK01]] treats the reading of "or" in mathematical English.

### Rules of inference for disjunction

In [[natural deduction|6KT3BJZ7D1]], disjunction has two introduction rules and one elimination rule.

1. Disjunction introduction (left): from $p$, conclude $p \lor q$. In Mathlib this rule is `Or.inl`.
2. Disjunction introduction (right): from $q$, conclude $p \lor q$. In Mathlib this rule is `Or.inr`.
3. [[Disjunction elimination|FTH70E7K1D]]: from $p \lor q$, from a derivation of $r$ under the assumption $p$, and from a derivation of $r$ under the assumption $q$, conclude $r$. In Mathlib this rule is `Or.elim`.

Disjunction elimination is the logical form of [[proof by cases|0WCP0PVET6]]: to use "$p$ or $q$", we prove the goal once assuming $p$ and once assuming $q$.
The [[disjunctive syllogism|6EFJF9NAYX]] is a derived rule: from $p \lor q$ and $\neg p$, conclude $q$; in Mathlib it is `Or.resolve_left`.
In classical logic, a common way to prove $p \lor q$ is to assume $\neg p$ and prove $q$.
This uses $(\neg p \to q) \to (p \lor q)$, which is not valid in [[intuitionistic logic|Q11N8X99FK]]; there a proof of $p \lor q$ must prove one of the two parts and say which one.

### Basic properties

The symbol $\equiv$ means [[logical equivalence|0JMR2HM2N2]], and $\top$ and $\bot$ stand for a true and a false proposition.

1. Commutativity and associativity: $p \lor q \equiv q \lor p$ and $(p \lor q) \lor r \equiv p \lor (q \lor r)$. A disjunction of many parts is true exactly when at least one part is true.
2. Idempotence: $p \lor p \equiv p$.
3. Identity and domination: $p \lor \bot \equiv p$ and $p \lor \top \equiv \top$.
4. Distributivity: $p \lor (q \land r) \equiv (p \lor q) \land (p \lor r)$ and $p \land (q \lor r) \equiv (p \land q) \lor (p \land r)$.
5. Negation: $\neg(p \lor q) \equiv \neg p \land \neg q$, by [[De Morgan's laws|09PKJKA6J0]]; in Mathlib this is `not_or`.
6. Implication: $p \to q \equiv \neg p \lor q$ in classical logic; in Mathlib this is `imp_iff_not_or`.
7. Excluded middle: $p \lor \neg p$ is a tautology; see [[law of excluded middle|0RYYK8PG4S]].
8. Sets: $x \in A \cup B$ means $x \in A \lor x \in B$, so disjunction corresponds to [[union|0X1GSWNBN1]].

The full list is on the page [[laws of propositional logic|A9CSGZNBV5]].

### History

Chrysippus and the Stoic logicians listed the disjunctive syllogism among their basic forms of argument.
George Boole, in his book of 1854, added two classes only when they had no common member, so his "or" behaved like the exclusive "or".
William Stanley Jevons argued in 1864 for the inclusive reading, and later logic and mathematics followed him.

### Common errors

1. A student reads "or" as exclusive and calls "$x \geq 0$ or $x \leq 0$" false for $x = 0$. Both parts are true for $x = 0$, so the disjunction is true.
2. In a proof by cases, a student treats only one case. Disjunction elimination needs a proof of the goal in each case.
3. A student negates "$p$ or $q$" as "not $p$ or not $q$". The negation is "not $p$ and not $q$".

## Explanations

### L1 human

A claim with "or" is true when at least one part is true.
"$7$ is even or $7$ is odd" is true, because the second part is true.
"$7$ is even or $7$ is bigger than $10$" is false, because both parts are false.
In mathematics, "or" also allows both parts to be true: "$12$ is even or $12$ is bigger than $10$" is true.
This is different from a menu, where "soup or salad" usually means only one.

### L2 human

We prove that $|x| \geq x$ for every real number $x$, where $|x| = x$ for $x \geq 0$ and $|x| = -x$ for $x < 0$.

1. For every real $x$, we have $x \geq 0$ or $x < 0$. This disjunction comes from the order of the real numbers.
2. Case $x \geq 0$: then $|x| = x$, so $|x| \geq x$.
3. Case $x < 0$: then $|x| = -x > 0 > x$, so $|x| \geq x$.
4. The goal holds in both cases, so by disjunction elimination it holds for every real $x$.

The typical use of a disjunction in a proof is this split: a known disjunction, such as "even or odd" or "$\geq 0$ or $< 0$", gives the cases.

A trap: the cases must cover all possibilities.
A split into "$x > 0$" and "$x < 0$" misses $x = 0$, because "$x > 0$ or $x < 0$" is false for $x = 0$.

### L3 human

With truth values $0$ and $1$, disjunction is the maximum of its inputs; in a [[Boolean algebra|0XADJKM699]] or a lattice it is the join, the least upper bound, and in the algebra of sets it is the union.
In hardware it is the OR [[logic gate|AMH914MF2A]].
An existential statement over a finite domain $\{a_1, \ldots, a_n\}$ is the disjunction $P(a_1) \lor \cdots \lor P(a_n)$, so the [[existential quantifier|0MSRQHCNN9]] generalizes disjunction.
In type theory, a proof of $p \lor q$ is a proof of $p$ or a proof of $q$ together with a tag that says which; Mathlib's `Or` is this sum, with constructors `Or.inl` and `Or.inr`.
The rule `Or.elim` is then the universal property of the coproduct: maps from $p$ and from $q$ to $r$ give a map from $p \lor q$ to $r$.
Intuitionistic logic has the disjunction property: if $p \lor q$ is provable with no assumptions, then $p$ is provable or $q$ is provable; classical logic fails this property, as $p \lor \neg p$ shows.
