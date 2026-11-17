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

Modus ponens is the [[rule of inference|QPD3X471Q1]] that derives the formula $\psi$ from the two premises $\varphi$ and $\varphi \to \psi$, for any formulas $\varphi$ and $\psi$:
$$\frac{\varphi \qquad \varphi \to \psi}{\psi}$$
The premise $\varphi \to \psi$ is a [[material implication|0NMG7W7Q11]], and the premise $\varphi$ is its antecedent.
The rule is valid: under every valuation that makes both premises true, the conclusion $\psi$ is true.
Modus ponens is the basic step of almost every proof, and in a [[Hilbert system|1MGMQX43B8]] it is often the only rule of inference.

## Motivation

A theorem usually has the form "if $P$, then $Q$".
To use the theorem on a particular object, we check that the object satisfies $P$, and we conclude that it satisfies $Q$.
This step is modus ponens: from $P$ and $P \to Q$, we get $Q$.
A proof is a chain of such steps, so a precise account of proofs must start with this rule.

## Notation

The rule is written as a fraction, with the premises above the line and the conclusion below it, or as $\varphi,\ \varphi \to \psi \vdash \psi$.
Other names are "implication elimination" ($\to$E) in [[natural deduction|6KT3BJZ7D1]], "rule of detachment" and "affirming the antecedent".
The arrow is also written $\supset$ or $\Rightarrow$.
In Lean, if `h : p → q` and `hp : p`, then the application `h hp` has type `q`; modus ponens is function application.

## Remarks

### Examples

1. [[Modus ponens applied to a divisibility theorem|3DJDNG0ZC9]]: from "if $6$ divides $n$, then $3$ divides $n$" and "$6$ divides $312$", we derive "$3$ divides $312$".
2. [[A proof of $p \to p$ in a Hilbert system|SD7R5BDA6N]]: two axioms and two uses of modus ponens give the formula $p \to p$.
3. From "if $f$ is differentiable at $1$, then $f$ is continuous at $1$" and "$f(x) = x^2$ is differentiable at $1$", we derive that $x^2$ is continuous at $1$. The first premise is an instance of the theorem that [[differentiable functions are continuous|07ZMX4ANJS]].
4. From $p \land q$ and $(p \land q) \to r$ we derive $r$. The antecedent can be any formula, here a conjunction.
5. From $\neg q$ and $\neg q \to \neg p$ we derive $\neg p$. This is modus ponens on the contrapositive, and it is the core of [[modus tollens|32AQPJQQAM]].

### Non-examples

1. [[Detaching an inner conditional without its outer antecedent is not modus ponens|T850KJAMS5]]: from $p \to (q \to r)$ and $q$ we cannot derive $r$.
2. From $q$ and $p \to q$ we cannot derive $p$. This is the fallacy of [[affirming the consequent|J7KFCFQRBT]], treated in the example [[affirming the consequent is not a valid deduction|2XXTDXK1ZC]].
3. From $\neg p$ and $p \to q$ we cannot derive $\neg q$. This is [[denying the antecedent|6FH1TVDXGS]].

### Basic properties

1. Validity by [[truth table|05RSK4Q657]]. In the table below, the only row in which both premises $p$ and $p \to q$ are true is the row TT, and in that row $q$ is true.

| $p$ | $q$ | $p \to q$ | premises both true |
|---|---|---|---|
| T | T | T | yes |
| T | F | F | no |
| F | T | T | no |
| F | F | T | no |

2. Equivalently, the formula $(p \land (p \to q)) \to q$ is a [[tautology|05006AJ7DZ]].
3. Modus ponens preserves truth, so a proof whose steps use it and whose premises are true has a true conclusion. This is the base of the [[soundness|4A84VHDTHV]] of proof systems.
4. The rule is valid in [[intuitionistic logic|Q11N8X99FK]] as well as in classical logic.
5. The [[deduction theorem|9X08XK5RV2]] is a partial converse: if $\psi$ can be derived from the hypothesis $\varphi$, then $\varphi \to \psi$ can be derived with no hypothesis. Modus ponens goes back: from $\vdash \varphi \to \psi$ and the hypothesis $\varphi$ we get $\psi$.
6. Other rules can be derived from modus ponens and suitable axioms, for example [[modus tollens|32AQPJQQAM]] and [[hypothetical syllogism|7MT8CPCEM4]].

### Role in Hilbert systems

A Hilbert system for propositional logic has axiom schemas and, as its only rule, modus ponens.
A usual choice of schemas for $\to$ is (A1) $\varphi \to (\psi \to \varphi)$ and (A2) $(\varphi \to (\psi \to \chi)) \to ((\varphi \to \psi) \to (\varphi \to \chi))$, with further schemas for negation.
A derivation is a finite list of formulas, each an axiom, a hypothesis, or the result of modus ponens on two earlier formulas.
So the set of theorems of the system is the smallest set that contains the axioms and is closed under modus ponens.
The derivation of $p \to p$ in [[example 2|SD7R5BDA6N]] is the first exercise in such a system.

### History

The Stoic logician Chrysippus listed modus ponens as the first of his indemonstrable arguments: "if the first, then the second; the first; therefore the second".
Frege's Begriffsschrift of 1879 used modus ponens as its main rule of inference.
In 1895 Lewis Carroll published the dialogue "What the Tortoise Said to Achilles".
In it, the Tortoise accepts two premises $A$ and $B$ and also the conditional "if $A$ and $B$, then $Z$", but refuses $Z$, and asks that each new conditional be added as a further premise.
The regress shows that a rule of inference cannot be replaced by one more premise: at some point the reasoner must apply the rule.

### Common errors

1. A student applies the implication in the wrong direction, which is [[affirming the consequent|J7KFCFQRBT]].
2. A student applies a theorem without checking all of its hypotheses. Modus ponens needs the whole antecedent: the [[boundedness theorem|0ATVXC3NCC]] needs a closed interval $[a, b]$, so it says nothing about $1/x$ on $(0, 1]$, which is unbounded.
3. A student believes that a valid step makes its conclusion true. Modus ponens gives a true conclusion only from true premises: from "$1 = 2$" and "if $1 = 2$, then $2 = 4$" it validly derives the false statement $2 = 4$.

## Explanations

### L1 human

Modus ponens is the step "if this, then that; this is true; so that is true".
For example: "if a number ends in $0$, then it is even", and "$30$ ends in $0$", so "$30$ is even".
The rule never leads from true sentences to a false one.
Almost every step in a calculation or a proof has this form, even when the "if" sentence is not written out.

### L2 human

We show that $91$ is not prime, and we mark each use of modus ponens.

1. Premise: if an integer $n > 1$ has a divisor $d$ with $1 < d < n$, then $n$ is not prime. This is the definition of a [[prime number|01826KMG2H]], read as an implication.
2. Fact: $91 = 7 \cdot 13$, so $91$ has the divisor $7$ with $1 < 7 < 91$.
3. Step 1 applied to $n = 91$ gives the implication "if $91$ has a divisor $d$ with $1 < d < 91$, then $91$ is not prime".
4. Modus ponens with steps 2 and 3 gives "$91$ is not prime".

Step 3 is the instantiation of a universal statement, and step 4 is modus ponens; most uses of a theorem combine the two.
A trap is to use step 1 backwards: from the statement "$n$ is not prime" alone, step 1 gives no conclusion about the divisors of $n$.

### L3 human

In the [[sequent calculus|W72CA3R9MP]], modus ponens corresponds to a combination of the rule for $\to$ on the left with the cut rule.
Gentzen's cut elimination shows that this combination can be removed from proofs, at the cost of longer proofs.
In a Hilbert system, by contrast, modus ponens is the only rule, and all logical content sits in the axioms.
In [[modal logic|G8VGTW9P4F]], the set of theorems of a normal modal logic is closed under modus ponens, and the axiom $\mathbf{K}$ makes the rule hold inside each modal operator.
In a cartesian closed category, the evaluation map $Q^P \times P \to Q$ plays the role of modus ponens; the type-theoretic reading of this map belongs to the area of type theory.
Carroll's regress reappears in the distinction between the object language, where $\varphi \to \psi$ is a formula, and the metalanguage, where "from $\varphi$ and $\varphi \to \psi$ infer $\psi$" is a rule about formulas.
