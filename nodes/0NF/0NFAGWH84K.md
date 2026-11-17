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

Let $p$ be a propositional variable, and let $\neg$ be [[negation|029JBBF693]].
In classical propositional logic,
$$\neg\neg p \equiv p,$$
that is, $\neg\neg p$ and $p$ are [[logically equivalent|0JMR2HM2N2]].
The law has two directions.

1. Double negation introduction: $p \to \neg\neg p$ is a tautology. It is also provable in [[intuitionistic logic|Q11N8X99FK]].
2. Double negation elimination: $\neg\neg p \to p$ is a tautology. It is not provable in intuitionistic logic.

By substitution, $\neg\neg\varphi \equiv \varphi$ for every formula $\varphi$.
In Mathlib the law is `Classical.not_not`, with the statement `¬¬a ↔ a`; the prefix `Classical` marks the use of a classical axiom.

The [[proof by a truth table|A35WJBK3PW]] gives the classical law.
The [[proof by natural deduction|D3S30V9ZZ2]] shows which direction needs the [[law of excluded middle|0RYYK8PG4S]].

## Remarks

### Why each hypothesis is needed

The law has no hypotheses on $p$.
We show which close variants fail, and where the classical setting enters.

1. One negation is not neutral: $\neg p \not\equiv p$, and the two formulas differ in every row.
2. Classical logic is needed for elimination. In intuitionistic logic, $\neg\neg p \to p$ fails in a [[Kripke model|NGHWZ9Y7ZV]] with two worlds, as in the Variants of the natural deduction proof.
3. Elimination does hold intuitionistically for a negated formula: $\neg\neg\neg p \to \neg p$ is provable there. So intuitionistically three negations reduce to one, but two negations do not reduce to none.
4. In a three-valued logic with $\neg \mathrm{U} = \mathrm{U}$, such as Kleene's, the law still holds. Its failure is a feature of intuitionistic logic, not of every logic with more than two values.

### Consequences

1. [[Proof by contradiction|0J0XBKG64S]]. To prove $p$, assume $\neg p$ and derive a contradiction. This proves $\neg\neg p$ without any classical step, and elimination then gives $p$.
2. The backward direction of the [[contrapositive|04T1CT7212]]. From $\neg q \to \neg p$ and $p$, the assumption $\neg q$ gives $\neg p$ and a contradiction, so $\neg\neg q$, and elimination gives $q$.
3. Negations can be pushed inward. With [[De Morgan's laws (logic)|09PKJKA6J0]] and the double negation law, each formula in $\neg$, $\land$ and $\lor$ is equivalent to one where $\neg$ stands only directly before variables. See [[negating mathematical statements|K930V33BSC]].
4. Over intuitionistic logic, double negation elimination for all formulas is equivalent to the law of excluded middle for all formulas. Part 3 of the [[natural deduction proof|D3S30V9ZZ2]] gives one direction, and the law of excluded middle page gives the other.
5. In Lean, a proof by contradiction of `p` produces a proof of `¬¬p`, and `Classical.not_not` turns it into a proof of `p`.

### Converse

The law is an equivalence, so its converse is the law itself.
The interesting question is the status of each direction.
Introduction $p \to \neg\neg p$ holds classically and intuitionistically.
Elimination $\neg\neg p \to p$ holds classically, and intuitionistically only for special formulas, such as negated formulas and formulas $p$ for which $p \lor \neg p$ is provable.

### Generalizations

1. In a [[Boolean algebra|0XADJKM699]], negation is an involution: $\neg\neg a = a$. For sets, $(A^c)^c = A$, where $A^c$ is the [[complement|0RKF1ZT5JJ]].
2. In a [[Heyting algebra|NG943XNQWH]], only $a \le \neg\neg a$ and $\neg\neg\neg a = \neg a$ hold. The elements with $\neg\neg a = a$ are the regular elements, and they form a Boolean algebra.
3. The [[double-negation translation|HGJVM49PA4]] puts $\neg\neg$ in front of the parts of a formula, and it embeds classical logic in intuitionistic logic.

## History

In George Boole's algebra of logic of 1854, "not $x$" is written $1 - x$, and the law becomes $1 - (1 - x) = x$.
Luitzen Egbertus Jan Brouwer rejected the law of excluded middle in his intuitionism, and with it double negation elimination.
Glivenko's theorem later showed that a propositional formula is a classical tautology exactly when its double negation is provable intuitionistically.

## Explanations

### L1 human

"It is not true that the door is not locked" means "the door is locked".
Two negations cancel each other, because negation swaps true and false, and two swaps bring back the first value.
In ordinary speech, care is needed: "not unhappy" is weaker than "happy".
The word "unhappy" is an opposite of "happy", not its negation, so "not unhappy" can describe a neutral mood.

### L2 human

We prove "if $n^2$ is even, then $n$ is even" for an integer $n$, and we find the step that uses the law.

1. Assume that $n^2$ is even, and let $p$ be "$n$ is even".
2. Assume $\neg p$. Then $n = 2k + 1$ for an integer $k$, so $n^2 = 2(2k^2 + 2k) + 1$ is odd.
3. Step 2 contradicts step 1, so the assumption $\neg p$ is false. This gives $\neg\neg p$.
4. By double negation elimination, $p$ holds: $n$ is even.

Step 3 is valid in every logic, and step 4 is the classical step.
Here step 4 is harmless, because "$n$ is even or $n$ is not even" can be checked by division by $2$.
The typical use of the law is this last step of a proof by contradiction.
A trap is to apply the law to words such as "not unlikely" or "not uncommon", where the prefix "un" forms an opposite and not a negation.

### L3 human

In a Heyting algebra, $a \mapsto \neg\neg a$ is a closure operator, and its fixed points form a Boolean algebra.
By Glivenko's theorem, the classical propositional tautologies are exactly the formulas whose double negations are intuitionistic theorems.
For first-order logic the [[double-negation translation|HGJVM49PA4]] does the same job, with $\neg\neg$ placed in front of atomic formulas, disjunctions and existential quantifiers.

Under the [[Curry–Howard correspondence|A77FER1Q5H]], a proof of $\neg\neg p$ is a program that takes a continuation of type $p \to \bot$ and returns $\bot$.
Introduction $p \to \neg\neg p$ is the program that passes a value to the continuation.
Elimination has no such program in pure type theory, which is why Lean needs a classical axiom for `Classical.not_not`.
