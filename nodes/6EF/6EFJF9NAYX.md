---
tag: 6EFJF9NAYX
kind: concept
name: Disjunctive syllogism
aliases: [modus-tollendo-ponens, disjunction-elimination-by-negation]
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
uses: [0F72FK8EKB, 029JBBF693, QPD3X471Q1, 05RSK4Q657]
sources:
  - url: https://en.wikipedia.org/wiki/Disjunctive_syllogism
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Relevance_logic
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 3.5
---

## Summary

Disjunctive syllogism is the logic of elimination: when one of two things is true and the first is false, the second is true.
"The key is in my left pocket or in my right pocket; it is not in the left pocket; so it is in the right pocket."
Write $p$ for "the key is in the left pocket" and $q$ for "the key is in the right pocket".
The argument has the premises $p \lor q$ and $\neg p$, and the conclusion $q$.
As a [[rule of inference|QPD3X471Q1]] it is written
$$\frac{p \lor q \qquad \neg p}{q}$$
The symmetric form concludes $p$ from $p \lor q$ and $\neg q$.
The rule is valid: in every row of the [[truth table|05RSK4Q657]] where both premises are true, the conclusion is true.

## Motivation

Many arguments in mathematics reach a list of possibilities and then rule them out one by one.
The equation $x(x - 1) = 0$ gives "$x = 0$ or $x = 1$".
A prime that divides a product $ab$ divides $a$ or divides $b$.
Two real numbers $x$ and $y$ satisfy $x < y$ or $x = y$ or $x > y$.
In each case a second fact usually removes some of the possibilities, and disjunctive syllogism is the step that turns the [[disjunction|0F72FK8EKB]] and the [[negation|029JBBF693]] of one part into a definite answer.

The rule matters outside mathematics too.
A doctor who rules out every diagnosis except one, and a SAT solver that finds a clause with all literals false except one, both use it.
The rule returns in the [[formal fallacies|T5BG7Y4J0T]], where its invalid cousin "affirming a disjunct" appears, and in the study of logics that reject it.

## Notation

The fraction form puts the premises above the line and the conclusion below it.
As a consequence it reads $p \lor q, \neg p \models q$, and as one formula it is the [[tautology|05006AJ7DZ]] $((p \lor q) \land \neg p) \to q$.
The traditional Latin name is *modus tollendo ponens*, "the mode that affirms by denying".
In Lean, `Or.resolve_left` takes a proof of `a ∨ b` and a proof of `¬a` and returns a proof of `b`.
The symbols $\lor$ and $\neg$ have variants in books, listed on the pages [[disjunction|0F72FK8EKB]] and [[negation|029JBBF693]].

## Remarks

### Checking the rule with a truth table

List the four valuations of $p$ and $q$, and compute both premises in each row:

| $p$ | $q$ | $p \lor q$ | $\neg p$ | $q$ |
|---|---|---|---|---|
| T | T | T | F | T |
| T | F | T | F | F |
| F | T | T | T | T |
| F | F | F | T | F |

Only the third row makes both premises true, and in that row $q$ is true.
So no valuation makes the premises true and the conclusion false, and the rule is valid.
The same table shows why both premises are needed: the first two rows make $p \lor q$ true with $q$ false, and the fourth row makes $\neg p$ true with $q$ false.

### Worked uses

To solve $x^2 = x$ for a [[nonzero real number|CVVR1EZYHE]], factor to get $x(x - 1) = 0$, so $x = 0 \lor x = 1$.
The hypothesis $x \neq 0$ denies the first disjunct, and the rule gives $x = 1$.

For an integer $n$ with $7 \mid 3n$, [[Euclid's lemma|051VYKA1EX]] gives $7 \mid 3 \lor 7 \mid n$.
Since $0 < 3 < 7$, the number $7$ does not divide $3$, so the rule gives $7 \mid n$; the example [[from $7 \mid 3n$ to $7 \mid n$|1GABWKBKPD]] writes this out.

With more cases you apply the rule several times.
[[Trichotomy|1APZE11YEF]] gives $x < y \lor x = y \lor x > y$.
If $x \not< y$, one step leaves $x = y \lor x > y$, and if also $x \neq y$, a second step leaves $x > y$.

### What the rule does not allow

[[Affirming a disjunct|3X34TM3SRT]] concludes $\neg q$ from $p \lor q$ and $p$.
That form is invalid, because the mathematical "or" is inclusive: the row $p = q = \mathrm{T}$ makes both premises true and $\neg q$ false.
For a concrete case, $6$ is even or a multiple of $3$, and $6$ is even, but $6$ is still a multiple of $3$.

The statement that you deny must be one of the disjuncts.
From $p \lor q$ and $\neg r$ nothing follows about $q$: the row $p = \mathrm{T}$, $q = \mathrm{F}$, $r = \mathrm{F}$ makes both premises true and $q$ false.

### How it connects to other rules

Classically, $p \lor q$ is [[logically equivalent|0JMR2HM2N2]] to $\neg p \to q$.
With this equivalence, disjunctive syllogism is [[modus ponens|0Y0MQYST0M]] applied to $\neg p \to q$ and $\neg p$.

The rule is also valid in [[intuitionistic logic|Q11N8X99FK]], by a proof by cases on $p \lor q$.
In the case $p$, the premise $\neg p$ gives a contradiction, and [[explosion|TTKZGJEEK7]] gives $q$.
In the case $q$, there is nothing to do.
That proof needs explosion, and in minimal logic, which has no explosion rule, the rule cannot be derived.

Conversely, the rule gives explosion.
From $p$, disjunction introduction gives $p \lor q$, and then $\neg p$ and the rule give $q$, for any $q$ at all.
In clause logic, the resolution rule concludes $q \lor r$ from $p \lor q$ and $\neg p \lor r$, and disjunctive syllogism is the case where the second clause is the single literal $\neg p$.

### Relevance logic rejects it

The last argument shows that disjunction introduction and disjunctive syllogism together give explosion.
Relevance logics, developed by Alan Ross Anderson and Nuel Belnap, demand that the premises of a valid inference be relevant to its conclusion, and explosion fails that demand.
These logics keep disjunction introduction, so they give up disjunctive syllogism for arbitrary premises.

A countermodel lives in Graham Priest's three-valued logic LP, a [[paraconsistent logic|C7YWCR87QJ]] with the values T, B ("both") and F, where T and B count as true.
Take $p = \mathrm{B}$ and $q = \mathrm{F}$.
Then $\neg p = \mathrm{B}$ and $p \lor q = \mathrm{B}$, so both premises count as true, but the conclusion $q$ is false.
The topic [[substructural, linear and relevance logics|98QF5J4W16]] treats these logics.

### Watch out

The rule is valid, but its conclusion is only as good as the disjunction you start from.
"Every real $x$ satisfies $x < 0$ or $x > 0$; this $x$ is not negative; so $x > 0$" has a valid form and a false first premise, because $x = 0$ satisfies neither part.
Before you eliminate cases, check that your list of cases is complete.

### History

The Stoic logician Chrysippus listed this form among his five indemonstrable arguments, together with [[modus ponens|0Y0MQYST0M]] and [[modus tollens|32AQPJQQAM]].
The Stoics read "or" in this form as exclusive.
In the twentieth century, Anderson and Belnap rejected the rule in their work on relevance logic.

### Try it

A digit $d$ is $1$, $5$ or $9$, and $d$ is neither $1$ nor $9$; what is $d$?
Two applications of the rule give $d = 5$.

From "$n$ is prime or $n$ is odd" and "$n$ is prime", may you conclude that $n$ is not odd?
No: that is affirming a disjunct, and $n = 3$ makes both premises true and the conclusion false.

## Explanations

### L1 human

A secret number is $3$ or $7$.
Someone tells you it is not $3$.
Then it must be $7$.
This step is called disjunctive syllogism.
It works only when the list of possibilities is complete and one possibility is ruled out.
Being told "it is $3$" tells you nothing new about $7$, unless you also know that it cannot be both.

### L2 human

Find the real numbers $x$ with $x^2 - 5x + 6 = 0$ and $x > 2.5$.
First factor the left side:
$$x^2 - 5x + 6 = (x - 2)(x - 3).$$
A product of two real numbers is $0$ only when one factor is $0$, so $x = 2 \lor x = 3$.
The hypothesis $x > 2.5$ gives $x \neq 2$, which denies the first disjunct, and disjunctive syllogism gives $x = 3$.
Check: $9 - 15 + 6 = 0$ and $3 > 2.5$.
This is the typical use of the rule: the last step of a [[proof by cases|0WCP0PVET6]] in which every case but one is impossible.
Watch out for the everyday exclusive "or", which tempts you to affirm one disjunct and deny the other; only with an [[exclusive or|PTMR3P9J6C]] is that step valid.

### L3 human

In a [[Heyting algebra|NG943XNQWH]], and so in every [[Boolean algebra|0XADJKM699]], the rule is the inequality $(a \lor b) \land \neg a \le b$.
Distributivity and $a \land \neg a = 0$ prove it:
$$(a \lor b) \land \neg a = (a \land \neg a) \lor (b \land \neg a) = b \land \neg a \le b.$$
Relevance and paraconsistent logics use algebras in which $a \land \neg a$ need not be the least element, and there the inequality fails, as the LP countermodel shows.
So the status of disjunctive syllogism measures how a logic treats contradictions.

The rule is the unit case of resolution, the single rule of the resolution method for propositional and first-order logic, and SAT solvers apply it many times as unit propagation.
In type theory a proof of $p \lor q$ is a tagged proof of one side, and `Or.resolve_left` inspects the tag: the tag "left" is impossible because of $\neg p$, so the tag is "right".
With the instantiation rule of the [[universal quantifier|0GHS47PDAQ]], the rule extends to first-order logic: $\forall x \, (P(x) \lor Q(x))$ and $\neg P(a)$ give $Q(a)$.
