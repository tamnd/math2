---
tag: 32AQPJQQAM
kind: concept
name: Modus tollens
aliases: [denying-the-consequent]
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
uses: [0Y0MQYST0M, 04T1CT7212, 029JBBF693]
sources:
  - url: https://en.wikipedia.org/wiki/Modus_tollens
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.5
---

## Summary

"If the butler did it, there is mud on his shoes; there is no mud; so the butler did not do it."
This step is modus tollens: a false consequence refutes the statement that implies it.

Modus tollens is the [[rule of inference|QPD3X471Q1]] that derives $\neg \varphi$ from the two premises $\varphi \to \psi$ and $\neg \psi$, for any formulas $\varphi$ and $\psi$:
$$\frac{\varphi \to \psi \qquad \neg \psi}{\neg \varphi}$$
The rule is valid: under every valuation that makes both premises true, the conclusion $\neg \varphi$ is true.
It is [[modus ponens|0Y0MQYST0M]] applied to the [[contrapositive|04T1CT7212]] $\neg \psi \to \neg \varphi$, and it holds in intuitionistic logic as well as in classical logic.
Every refutation by a consequence has this form: to show that a statement is false, derive from it a consequence that is false.

## Motivation

Some questions have the answer "no": a number is not a square, a polynomial has no rational root, a function is not continuous.
A direct way to prove such a "no" is to find a property that every "yes" case has and that the object lacks.
Every perfect square leaves remainder $0$ or $1$ on division by $4$, and $2023$ leaves remainder $3$, so $2023$ is not a perfect square.
This pattern is modus tollens.

## Notation

The rule is written as a fraction, with the premises above the line, or as $\varphi \to \psi,\ \neg \psi \vdash \neg \varphi$.
Other names are denying the consequent and the Latin modus tollendo tollens, the mode that denies by denying.
Negation is also written $\sim \varphi$, and the arrow $\supset$ or $\Rightarrow$.
In Mathlib the rule is `mt`, of type `(a → b) → ¬b → ¬a`, and it uses no classical axiom.

## Remarks

### Checking the rule by a truth table

Let $p$ be "the butler did it" and $q$ be "there is mud on his shoes".
The [[truth table|05RSK4Q657]] marks the rows where both premises are true.

| $p$ | $q$ | $p \to q$ | $\neg q$ | $\neg p$ | premises both true |
|---|---|---|---|---|---|
| T | T | T | F | F | no |
| T | F | F | T | F | no |
| F | T | T | F | T | no |
| F | F | T | T | T | yes |

Only the row FF makes both premises true, and in that row $\neg p$ is true.
Equivalently, $((p \to q) \land \neg q) \to \neg p$ is a [[tautology|05006AJ7DZ]].

### Why it holds intuitionistically

Assume $\varphi$.
Modus ponens gives $\psi$, which contradicts $\neg \psi$, so $\neg \varphi$ follows by negation introduction.
This argument uses only the reading of $\neg \psi$ as $\psi \to \bot$ and modus ponens, so it is valid in [[intuitionistic logic|Q11N8X99FK]].
It is direction (a) of the [[proof by rules of inference|QB99VRZQ4Y]] of contraposition, applied to the case at hand.

The intuitionistic rule has a limit when the antecedent is itself a negation.
From $\neg \varphi \to \psi$ and $\neg \psi$, modus tollens gives $\neg\neg \varphi$.
Passing from $\neg\neg \varphi$ to $\varphi$ needs [[double negation elimination|0NFAGWH84K]], which is a classical step.

### Worked examples

[[Modus tollens is a valid deduction|QWTTHZ9C6T]] derives "$4$ does not divide $7$" from "if $4$ divides $n$, then $n$ is even" and "$7$ is not even".
[[2023 is not a perfect square by modus tollens|ENSESQT9XB]] uses the fact that every square is congruent to $0$ or $1$ modulo $4$.
The sign function is not continuous at $0$, so by the theorem that [[differentiable functions are continuous|07ZMX4ANJS]] it is not differentiable at $0$.
A proof by [[counterexample|0ED72CTBNP]] is modus tollens: "if $\forall x\, P(x)$, then $P(a)$" and "not $P(a)$" give "not $\forall x\, P(x)$".
From $\neg r$ and $(p \land q) \to r$ we derive $\neg(p \land q)$, which is $\neg p \lor \neg q$ by [[De Morgan's laws|09PKJKA6J0]].

### What is not modus tollens

From $(p \land q) \to r$ and $\neg r$ we cannot derive $\neg p$, as shown in [[denying the consequent of a theorem with two hypotheses|M2050AJK54]].
From $p \to q$ and $\neg p$ we cannot derive $\neg q$, which is [[denying the antecedent|6FH1TVDXGS]].
From $p \to q$ and $q$ we cannot derive $p$, which is [[affirming the consequent|2XXTDXK1ZC]].

### Watch out

The second premise must deny the consequent, not the antecedent, as explained in [[affirming the consequent and denying the antecedent|J7KFCFQRBT]].
Modus tollens is not [[proof by contrapositive|0BB5TPGQ1N]]: the proof method proves an implication, while modus tollens uses an implication that is already known.

### History

The Stoic logician Chrysippus listed modus tollens as the second of his indemonstrable arguments: "if the first, then the second; not the second; therefore not the first".

### Try it

Show that $6$ does not divide $1000$.
Use the premise "if $6$ divides $n$, then $3$ divides $n$" and check the consequent for $n = 1000$.
The digit sum of $1000$ is $1$, so $3$ does not divide $1000$, and modus tollens gives that $6$ does not divide $1000$.

## Explanations

### L1 human

Modus tollens is the step "if this, then that; that is false; so this is false".
For example, "if it is a dog, then it has four legs", and "this bird has two legs", so "this bird is not a dog".
A detective uses it too: "if the butler did it, there would be mud on his shoes; there is no mud; so the butler did not do it".
The second premise must deny the "then" part, not the "if" part.

### L2 human

We use modus tollens to show that the polynomial $x^2 - 2$ has no rational root.
The [[rational root theorem|0819CQ1V8H]] says that if $p/q$ is a rational root of $x^2 - 2$ in lowest terms, then $p$ divides $2$ and $q$ divides $1$.
So "if $x^2 - 2$ has a rational root, then one of $1, -1, 2, -2$ is a root".
None of them is a root, because $1^2 - 2 = (-1)^2 - 2 = -1$ and $2^2 - 2 = (-2)^2 - 2 = 2$.
Modus tollens gives that $x^2 - 2$ has no rational root.
The rule rules out an object by a property that it lacks.
The reverse does not work: "$x^2 - 4$ has the root $2$, which is one of $\pm 1, \pm 2$" gives nothing by modus tollens, because it affirms the consequent.

### L3 human

In a [[Heyting algebra|NG943XNQWH]] modus tollens is the inequality $(a \to b) \land \neg b \le \neg a$, which holds in every Heyting algebra.
In probability and statistics there is no exact analogue.
A consequence that is unlikely under a hypothesis does not refute the hypothesis, and statistical tests replace modus tollens by a decision rule with a stated error rate.
In the philosophy of science, the refutation of a theory by a failed prediction has the form of modus tollens, while confirmation by a successful prediction has the invalid form of affirming the consequent.
