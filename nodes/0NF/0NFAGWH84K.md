---
tag: 0NFAGWH84K
kind: statement
role: theorem
name: Double negation law
aliases: [double-negation-elimination]
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
about: [029JBBF693, 0JMR2HM2N2]
uses: [029JBBF693, 0JMR2HM2N2, 05RSK4Q657]
sources:
  - url: https://en.wikipedia.org/wiki/Double_negation
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.2
  - book: isbn:9780122384523
    locator: Section 1.2
same_as:
  wikidata: Q5300067
  wikipedia: Double negation
---

## Statement

The double negation law says that two negations cancel: denying a denial gives back the original statement.
"It is not true that the door is not locked" means "the door is locked".

Let $p$ be a propositional variable, and let $\neg$ be [[negation|029JBBF693]].
In classical propositional logic,
$$\neg\neg p \equiv p,$$
that is, $\neg\neg p$ and $p$ are [[logically equivalent|0JMR2HM2N2]].
The law has two directions.

1. Double negation introduction: $p \to \neg\neg p$ is a tautology, and it is also provable in [[intuitionistic logic|Q11N8X99FK]].
2. Double negation elimination: $\neg\neg p \to p$ is a tautology, and it is not provable in intuitionistic logic.

By substitution, $\neg\neg\varphi \equiv \varphi$ for every formula $\varphi$.
In Mathlib the law is `Classical.not_not`, with the statement `¬¬a ↔ a`; the prefix `Classical` marks the use of a classical axiom.
The [[proof by a truth table|A35WJBK3PW]] gives the classical law, and the [[proof by natural deduction|D3S30V9ZZ2]] shows which direction needs the [[law of excluded middle|0RYYK8PG4S]].

## Remarks

### Two swaps bring you back

Let $p$ be "the door is locked", and suppose it is true.
Then "the door is not locked", $\neg p$, is false, and "it is not true that the door is not locked", $\neg\neg p$, is true again.
If $p$ is false, the same two swaps give F, T, F.

| $p$ | $\neg p$ | $\neg\neg p$ |
|---|---|---|
| T | F | T |
| F | T | F |

The first and the last columns agree, so $\neg\neg p \equiv p$ classically.
One negation alone is far from neutral: $\neg p$ and $p$ differ in every row.

### Where intuitionistic logic differs

In intuitionistic logic, $\neg p$ means "$p$ leads to a contradiction", and a proof of $\neg\neg p$ only shows that $\neg p$ is impossible.
Introduction is still fine: if you hold a proof of $p$, any refutation of $p$ yields a contradiction, so $p \to \neg\neg p$.
Elimination is not: knowing that $p$ cannot be refuted does not give a proof of $p$.
A [[Kripke model|NGHWZ9Y7ZV]] with two worlds refutes $\neg\neg p \to p$, as the Variants of the natural deduction proof show.

Elimination does hold intuitionistically for negated formulas: $\neg\neg\neg p \to \neg p$ is provable.
So three negations reduce to one in both logics, while two negations reduce to none only classically.
The failure is a feature of intuitionistic logic, not of every logic with more than two values.
In Kleene's three-valued logic, with $\neg \mathrm{U} = \mathrm{U}$, the formulas $\neg\neg p$ and $p$ still have the same value in every row.

### The law in proofs by contradiction

To prove $p$ by [[proof by contradiction|0J0XBKG64S]], you assume $\neg p$ and derive a contradiction.
That argument proves $\neg\neg p$, with no classical step at all.
Elimination then turns $\neg\neg p$ into $p$, and this is the only classical step.
In Lean, a proof by contradiction of `p` produces a proof of `¬¬p`, and `Classical.not_not` turns it into a proof of `p`.

The backward direction of the [[contrapositive|04T1CT7212]] runs the same way.
From $\neg q \to \neg p$ and $p$, the assumption $\neg q$ gives $\neg p$ and a contradiction, so $\neg\neg q$, and elimination gives $q$.

### What else the law gives you

With [[De Morgan's laws (logic)|09PKJKA6J0]], the law pushes negations inward: each formula in $\neg$, $\land$ and $\lor$ is equivalent to one where $\neg$ stands only directly before variables, as in [[negating mathematical statements|K930V33BSC]].
Over intuitionistic logic, double negation elimination for all formulas is equivalent to the law of excluded middle for all formulas.
Part 3 of the [[natural deduction proof|D3S30V9ZZ2]] gives one direction, and the law of excluded middle gives the other.

### The converse and generalizations

The law is an equivalence, so its converse is the law itself, and the real question is the status of each direction.
Introduction holds in both logics.
Elimination holds classically, and intuitionistically only for special formulas, such as negated formulas and formulas $p$ for which $p \lor \neg p$ is provable.

In a [[Boolean algebra|0XADJKM699]], negation is an involution, $\neg\neg a = a$; for sets, $(A^c)^c = A$, where $A^c$ is the [[complement|0RKF1ZT5JJ]].
In a [[Heyting algebra|NG943XNQWH]], only $a \le \neg\neg a$ and $\neg\neg\neg a = \neg a$ hold.
The elements with $\neg\neg a = a$ are called regular, and they form a Boolean algebra.

### Watch out

The law applies to logical negation, not to every negative word.
"Not unhappy" is weaker than "happy", because "unhappy" is an opposite of "happy", not its negation, and a neutral mood is neither.
In the same way "$x$ is not negative" is not the same as "$x$ is positive": for $x = 0$ the first is true and the second is false, because "negative" is not the negation of "positive".

### Try it

Simplify $\neg\neg(p \land \neg\neg q)$ classically.
Two applications of the law give $p \land q$.

Which part of $\neg\neg\neg p \leftrightarrow \neg p$ needs no work beyond double negation introduction?
The direction $\neg p \to \neg\neg\neg p$ is introduction applied to $\neg p$.

## History

In George Boole's algebra of logic of 1854, "not $x$" is written $1 - x$, and the law becomes $1 - (1 - x) = x$.
Luitzen Egbertus Jan Brouwer rejected the law of excluded middle in his intuitionism, and with it double negation elimination.
Glivenko's theorem later showed that a propositional formula is a classical tautology exactly when its double negation is provable intuitionistically.

## Explanations

### L1 human

"It is not true that the door is not locked" means "the door is locked".
Negation swaps true and false, and two swaps bring back the first value.
Ordinary speech needs care here.
"Not unhappy" is weaker than "happy", because "unhappy" is an opposite of "happy", not its negation, so "not unhappy" can describe a neutral mood.

### L2 human

Here is the law inside a familiar proof: if $n^2$ is even, then $n$ is even, for an integer $n$.
Assume that $n^2$ is even, and let $p$ be "$n$ is even".
Now assume $\neg p$, so $n = 2k + 1$ for an integer $k$, and compute
$$n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1,$$
which is odd.
That contradicts the hypothesis, so $\neg p$ is false, which gives $\neg\neg p$.
Double negation elimination now gives $p$: $n$ is even.
Every step except the last is valid in every logic, and the last is the classical one.
Here it is harmless, because "$n$ is even or not" can be decided by division by $2$.
Many proofs by contradiction have this exact shape, with the law as their final line.

### L3 human

In a Heyting algebra, $a \mapsto \neg\neg a$ is a closure operator, and its fixed points form a Boolean algebra.
By Glivenko's theorem, the classical propositional tautologies are exactly the formulas whose double negations are intuitionistic theorems.
For first-order logic the [[double-negation translation|HGJVM49PA4]] does the same job, with $\neg\neg$ placed in front of atomic formulas, disjunctions and existential quantifiers.

Under the [[Curry-Howard correspondence|A77FER1Q5H]], a proof of $\neg\neg p$ is a program that takes a continuation of type $p \to \bot$ and returns $\bot$.
Introduction is the program that passes a value to the continuation.
Elimination has no such program in pure type theory, which is why Lean needs a classical axiom for `Classical.not_not`.
