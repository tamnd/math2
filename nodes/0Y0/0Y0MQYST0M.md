---
tag: 0Y0MQYST0M
kind: concept
name: Modus ponens
aliases: [implication-elimination]
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
uses: [0NMG7W7Q11, QPD3X471Q1, 05RSK4Q657]
sources:
  - url: https://en.wikipedia.org/wiki/Modus_ponens
    locator: lead section
  - url: https://en.wikipedia.org/wiki/What_the_Tortoise_Said_to_Achilles
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 1.1
  - book: isbn:9781482237726
    locator: Chapter 1
same_as:
  wikidata: Q655742
  wikipedia: Modus ponens
---

## Summary

"If a number ends in $0$, then it is even; $30$ ends in $0$; so $30$ is even."
This step is modus ponens, and almost every step of a proof has this form.

Modus ponens is the [[rule of inference|QPD3X471Q1]] that derives $\psi$ from the two premises $\varphi$ and $\varphi \to \psi$, for any formulas $\varphi$ and $\psi$:
$$\frac{\varphi \qquad \varphi \to \psi}{\psi}$$
The premise $\varphi \to \psi$ is a [[material implication|0NMG7W7Q11]], and the premise $\varphi$ is its antecedent.
The rule is valid: under every valuation that makes both premises true, the conclusion $\psi$ is true.
In a [[Hilbert system|1MGMQX43B8]] it is often the only rule of inference.

## Motivation

A theorem usually has the form "if $P$, then $Q$".
To use it on a particular object, we check that the object satisfies $P$, and we conclude that it satisfies $Q$.
This is modus ponens, and a proof is a chain of such steps, so a precise account of proofs must start with this rule.

## Notation

The rule is written as a fraction, with the premises above the line and the conclusion below it, or as $\varphi,\ \varphi \to \psi \vdash \psi$.
Other names are implication elimination ($\to$E) in [[natural deduction|6KT3BJZ7D1]], the rule of detachment, and affirming the antecedent.
The arrow is also written $\supset$ or $\Rightarrow$.
In Lean, if `h : p → q` and `hp : p`, then the application `h hp` has type `q`, so modus ponens is function application.

## Remarks

### Checking the rule by a truth table

Let $p$ be "the number ends in $0$" and $q$ be "the number is even".
The [[truth table|05RSK4Q657]] marks the rows where both premises are true.

| $p$ | $q$ | $p \to q$ | premises both true |
|---|---|---|---|
| T | T | T | yes |
| T | F | F | no |
| F | T | T | no |
| F | F | T | no |

Only the row TT makes both premises true, and in that row $q$ is true.
Equivalently, the formula $(p \land (p \to q)) \to q$ is a [[tautology|05006AJ7DZ]].
The rule is valid in [[intuitionistic logic|Q11N8X99FK]] as well, since a proof of $p \to q$ is a method that turns a proof of $p$ into a proof of $q$.

### Worked examples

[[Modus ponens applied to a divisibility theorem|3DJDNG0ZC9]] derives "$3$ divides $312$" from "if $6$ divides $n$, then $3$ divides $n$" and "$6$ divides $312$".
[[A Hilbert system proof that every formula implies itself|SD7R5BDA6N]] uses two axioms and two steps of modus ponens to derive $p \to p$.
From "$x^2$ is differentiable at $1$" and the theorem that [[differentiable functions are continuous|07ZMX4ANJS]], we derive that $x^2$ is continuous at $1$.
The antecedent can be any formula: from $p \land q$ and $(p \land q) \to r$ we derive $r$.
From $\neg q$ and $\neg q \to \neg p$ we derive $\neg p$, which is the core of [[modus tollens|32AQPJQQAM]].

### What is not modus ponens

From $p \to (q \to r)$ and $q$ we cannot derive $r$, as shown in [[detaching an inner conditional|T850KJAMS5]].
From $q$ and $p \to q$ we cannot derive $p$, which is the fallacy of [[affirming the consequent|J7KFCFQRBT]], treated in [[affirming the consequent is not a valid deduction|2XXTDXK1ZC]].
From $\neg p$ and $p \to q$ we cannot derive $\neg q$, which is [[denying the antecedent|6FH1TVDXGS]].

### What the rule gives you

Modus ponens preserves truth, so a proof whose premises are true and whose steps use it has a true conclusion.
This is the base of the [[soundness|4A84VHDTHV]] of proof systems.
The [[deduction theorem|9X08XK5RV2]] is a partial converse: if $\psi$ can be derived from the hypothesis $\varphi$, then $\varphi \to \psi$ can be derived with no hypothesis.
Other rules can be derived from modus ponens and suitable axioms, such as [[modus tollens|32AQPJQQAM]] and [[hypothetical syllogism|7MT8CPCEM4]].

### Role in Hilbert systems

A Hilbert system for propositional logic has axiom schemas and, as its only rule, modus ponens.
A usual choice of schemas for $\to$ is (A1) $\varphi \to (\psi \to \varphi)$ and (A2) $(\varphi \to (\psi \to \chi)) \to ((\varphi \to \psi) \to (\varphi \to \chi))$, with further schemas for negation.
A derivation is a finite list of formulas, each an axiom, a hypothesis, or the result of modus ponens on two earlier formulas.
So the set of theorems is the smallest set that contains the axioms and is closed under modus ponens.
The derivation of $p \to p$ in [[the Hilbert system example|SD7R5BDA6N]] is the first exercise in such a system.

### Watch out

Modus ponens needs the whole antecedent.
The [[boundedness theorem|0ATVXC3NCC]] needs a closed interval $[a, b]$, so it says nothing about $1/x$ on $(0, 1]$, which is unbounded.
A valid step gives a true conclusion only from true premises.
From "$1 = 2$" and "if $1 = 2$, then $2 = 4$" the rule validly derives the false statement $2 = 4$.

### History

The Stoic logician Chrysippus listed modus ponens as the first of his indemonstrable arguments: "if the first, then the second; the first; therefore the second".
Frege's Begriffsschrift of 1879 used modus ponens as its main rule of inference.
In 1895 Lewis Carroll published the dialogue "What the Tortoise Said to Achilles" in the journal Mind.
In it, the Tortoise accepts two premises $A$ and $B$ and the conditional "if $A$ and $B$, then $Z$", but refuses $Z$, and asks that each new conditional be added as a further premise.
The regress shows that a rule of inference cannot be replaced by one more premise, since at some point the reasoner must apply the rule.

### Try it

From "if $n$ is divisible by $9$, then $n$ is divisible by $3$" and "$9$ divides $117$", what does modus ponens give?
It gives "$3$ divides $117$", and indeed $117 = 3 \cdot 39$.

## Explanations

### L1 human

Modus ponens is the step "if this, then that; this is true; so that is true".
For example, "if a number ends in $0$, then it is even", and "$30$ ends in $0$", so "$30$ is even".
The rule never leads from true sentences to a false one.
Almost every step in a calculation or a proof has this form, even when the "if" sentence is not written out.

### L2 human

We show that $91$ is not prime, and we mark the use of modus ponens.
The definition of a [[prime number|01826KMG2H]] gives the premise "if an integer $n > 1$ has a divisor $d$ with $1 < d < n$, then $n$ is not prime".
Since $91 = 7 \cdot 13$, the number $91$ has the divisor $7$ with $1 < 7 < 91$.
The premise for $n = 91$ gives "if $91$ has a divisor $d$ with $1 < d < 91$, then $91$ is not prime".
Modus ponens with the fact about $7$ gives "$91$ is not prime".
The step to $n = 91$ is the instantiation of a universal statement, and most uses of a theorem combine it with modus ponens.
The premise cannot be used backwards: from "$n$ is not prime" alone it gives no conclusion about the divisors of $n$.

### L3 human

In the [[sequent calculus|W72CA3R9MP]], modus ponens corresponds to the rule for $\to$ on the left combined with the cut rule.
Gentzen's cut elimination shows that this combination can be removed from proofs, at the cost of longer proofs.
In a Hilbert system, by contrast, modus ponens is the only rule, and all logical content sits in the axioms.
In [[modal logic|G8VGTW9P4F]], the theorems of a normal modal logic are closed under modus ponens, and the axiom $\mathbf{K}$ makes the rule hold inside each modal operator.
In a cartesian closed category, the evaluation map $Q^P \times P \to Q$ plays the role of modus ponens.
Carroll's regress reappears in the distinction between the object language, where $\varphi \to \psi$ is a formula, and the metalanguage, where "from $\varphi$ and $\varphi \to \psi$ infer $\psi$" is a rule about formulas.
