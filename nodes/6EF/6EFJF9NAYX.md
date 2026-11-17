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

Disjunctive syllogism is the [[rule of inference|QPD3X471Q1]] that concludes $q$ from the two premises $p \lor q$ and $\neg p$:
$$\frac{p \lor q \qquad \neg p}{q}$$
In words: one of two statements is true, the first one is false, so the second one is true.
The rule also has the symmetric form that concludes $p$ from $p \lor q$ and $\neg q$.
The rule is valid: in every row of the [[truth table|05RSK4Q657]] where $p \lor q$ and $\neg p$ are both true, $q$ is true.
Disjunctive syllogism is the logic of elimination, and every argument that lists the possible cases and then rules out all of them except one uses it.

## Motivation

Many arguments in mathematics end with a list of possibilities.
An equation $x(x - 1) = 0$ gives "$x = 0$ or $x = 1$".
A prime $p$ that divides a product $ab$ gives "$p$ divides $a$ or $p$ divides $b$".
Two real numbers $x$ and $y$ satisfy "$x < y$ or $x = y$ or $x > y$".
In each case a second fact often rules out some of the possibilities.
Disjunctive syllogism is the step that turns the [[disjunction|0F72FK8EKB]] and the [[negation|029JBBF693]] of one part into a definite conclusion.

## Notation

The rule is written as a fraction, with the premises above the line and the conclusion below it.
As a consequence relation it reads $p \lor q, \neg p \models q$, and as a single formula it is the [[tautology|05006AJ7DZ]] $((p \lor q) \land \neg p) \to q$.
The traditional Latin name is *modus tollendo ponens*, "the mode that affirms by denying".
In Lean and Mathlib the rule is `Or.resolve_left`: from a proof of `a ∨ b` and a proof of `¬a` it gives a proof of `b`.
The connectives $\lor$ and $\neg$ have the variants listed on the pages [[disjunction|0F72FK8EKB]] and [[negation|029JBBF693]].

## Remarks

### Examples

1. [[Solving $x^2 = x$ for a nonzero real number|CVVR1EZYHE]]: the equation gives $x = 0 \lor x = 1$, the hypothesis $x \neq 0$ denies the first part, so $x = 1$.
2. [[From $7 \mid 3n$ to $7 \mid n$|1GABWKBKPD]]: [[Euclid's lemma|051VYKA1EX]] gives $7 \mid 3 \lor 7 \mid n$, and $7 \nmid 3$, so $7 \mid n$.
3. For real numbers $x$ and $y$, [[trichotomy|1APZE11YEF]] gives $x < y \lor x = y \lor x > y$. If $x \not< y$ and $x \neq y$, two uses of the rule give $x > y$.
4. A digit $d$ of a puzzle is $1$, $5$ or $9$. If the rules exclude $1$ and $9$, then two uses of the rule give $d = 5$.
5. In clause logic, the clause $p \lor q$ and the unit clause $\neg p$ give the clause $q$. This is the simplest case of the resolution rule, discussed below.

### Non-examples

1. [[Affirming a disjunct|3X34TM3SRT]]: from $p \lor q$ and $p$ conclude $\neg q$. The second premise affirms a disjunct instead of denying it, and the row $p = q = \mathrm{T}$ refutes the form.
2. From $p \lor q$ and $\neg r$ conclude $q$, where $r$ is not one of the disjuncts. The negated statement must be a disjunct; the row $p = \mathrm{T}$, $q = \mathrm{F}$, $r = \mathrm{F}$ refutes the form.
3. "Every real $x$ satisfies $x < 0$ or $x > 0$; $x$ is not negative; so $x > 0$." The form is valid, but the first premise is false at $x = 0$, so the argument is not sound. The disjunction must list every case.

### Basic properties

1. The rule is valid. The table below lists the four valuations in the standard order.

| $p$ | $q$ | $p \lor q$ | $\neg p$ | $q$ |
|---|---|---|---|---|
| T | T | T | F | T |
| T | F | T | F | F |
| F | T | T | T | T |
| F | F | F | T | F |

Only the third row makes both premises true, and in that row $q$ is true.
So $((p \lor q) \land \neg p) \to q$ is a tautology.

2. Classically, $p \lor q$ is [[logically equivalent|0JMR2HM2N2]] to $\neg p \to q$, by the law `imp_iff_not_or` applied to $\neg p$ and the [[double negation law|0NFAGWH84K]]. With this equivalence, disjunctive syllogism is [[modus ponens|0Y0MQYST0M]] applied to $\neg p \to q$ and $\neg p$.
3. The rule generalizes to $n$ disjuncts: from $p_1 \lor \dots \lor p_n$ and $\neg p_1, \dots, \neg p_{n-1}$, conclude $p_n$. The proof applies the rule $n - 1$ times.
4. The rule is valid in [[intuitionistic logic|Q11N8X99FK]]. A proof by cases on $p \lor q$ works: in the case $p$, the premise $\neg p$ gives a contradiction, and [[explosion|TTKZGJEEK7]] gives $q$; in the case $q$, there is nothing to do.
5. The proof in property 4 needs explosion. In minimal logic, which has no explosion rule, disjunctive syllogism cannot be derived.
6. Conversely, disjunctive syllogism gives explosion. From $p$ and $\neg p$, the rule of disjunction introduction gives $p \lor q$, and disjunctive syllogism with $\neg p$ gives $q$.
7. The resolution rule concludes $q \lor r$ from $p \lor q$ and $\neg p \lor r$. Disjunctive syllogism is the case where the second clause is the single literal $\neg p$.

### Rejection in relevance logic

Property 6 shows that a logic with disjunction introduction and disjunctive syllogism has explosion.
Relevance logics, developed by Alan Ross Anderson and Nuel Belnap, require that the premises of a valid inference be relevant to its conclusion.
Explosion fails this requirement, because $p$ and $\neg p$ say nothing about an unrelated $q$.
These logics keep disjunction introduction, so they do not accept disjunctive syllogism as a valid inference from arbitrary premises.
A countermodel exists in the three-valued logic LP of Graham Priest, a [[paraconsistent logic|C7YWCR87QJ]] with the values T, B ("both") and F, where T and B count as true.
Take $p = \mathrm{B}$ and $q = \mathrm{F}$.
Then $\neg p = \mathrm{B}$ and $p \lor q = \mathrm{B}$, so both premises count as true, but the conclusion $q$ is false.
The topic [[substructural, linear and relevance logics|98QF5J4W16]] treats these logics.

### History

The Stoic logician Chrysippus listed disjunctive syllogism among his five indemonstrable forms of argument, together with [[modus ponens|0Y0MQYST0M]] and [[modus tollens|32AQPJQQAM]].
Anderson and Belnap rejected the rule in their work on relevance logic in the second half of the 20th century.

### Common errors

1. A student affirms a disjunct: "$n$ is even or $n$ is a multiple of $3$; $n$ is even; so $n$ is not a multiple of $3$". The number $n = 6$ refutes the conclusion, because the mathematical "or" is inclusive.
2. A student uses a disjunction that misses a case, such as "$x < 0$ or $x > 0$" for a real $x$. The rule is valid, but the conclusion is only as good as the list of cases.

## Explanations

### L1 human

A key is in the left pocket or in the right pocket.
I look in the left pocket, and the key is not there.
So the key is in the right pocket.
With numbers: a secret number is $3$ or $7$, and it is not $3$, so it is $7$.
This step is called disjunctive syllogism.
It works only when the list of possibilities is complete and one possibility is ruled out.

### L2 human

We find the real numbers $x$ with $x^2 - 5x + 6 = 0$ and $x > 2.5$.

1. Factor: $x^2 - 5x + 6 = (x - 2)(x - 3)$, so $(x - 2)(x - 3) = 0$.
2. A product of two real numbers is $0$ only when one factor is $0$. So $x = 2 \lor x = 3$.
3. The hypothesis $x > 2.5$ gives $x \neq 2$. This is the negation of the first disjunct.
4. Disjunctive syllogism gives $x = 3$.
5. Check: $9 - 15 + 6 = 0$ and $3 > 2.5$.

The typical use of the rule is at the end of a [[proof by cases|0WCP0PVET6]] in which all cases except one are impossible.
A trap is the everyday exclusive "or".
The rule allows us to deny a disjunct and conclude the other one, and it never allows us to affirm a disjunct and deny the other one.
Only with an [[exclusive or|PTMR3P9J6C]] does the second form hold.

### L3 human

In a [[Heyting algebra|NG943XNQWH]], and so in every [[Boolean algebra|0XADJKM699]], the rule is the inequality $(a \lor b) \land \neg a \le b$.
The proof uses distributivity and $a \land \neg a = 0$: we have $(a \lor b) \land \neg a = (a \land \neg a) \lor (b \land \neg a) = b \land \neg a \le b$.
The relevance and paraconsistent logics use algebras in which $a \land \neg a$ need not be the least element, and there the inequality fails, as the LP countermodel shows.
So the status of disjunctive syllogism measures how a logic treats contradictions.

The rule is the unit case of resolution, the single rule of the resolution method for propositional and first-order logic.
SAT solvers apply it many times as unit propagation: a clause with all literals false except one forces the last literal.
In type theory, a proof of $p \lor q$ is a tagged proof of one side, and `Or.resolve_left` inspects the tag: the tag "left" is impossible because of $\neg p$, so the tag is "right".
With the instantiation rule of the [[universal quantifier|0GHS47PDAQ]], the rule extends to first-order logic: $\forall x \, (P(x) \lor Q(x))$ and $\neg P(a)$ give $Q(a)$.
