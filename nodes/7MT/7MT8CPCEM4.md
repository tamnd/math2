---
tag: 7MT8CPCEM4
kind: concept
name: Hypothetical syllogism
aliases: [chain-argument, conditional-syllogism, transitivity-of-implication]
msc: ["03B05"]
topics: [PM1AYWABA7]
audience: school
uses: [0NMG7W7Q11, 0Y0MQYST0M, QPD3X471Q1]
sources:
  - wikipedia: en:177633@r1356009065
    locator: Hypothetical syllogism
    note: adopted
    mention: wikipedia://en/177633
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Hypothetical_syllogism
    locator: lead section
  - book: isbn:9781482237726
    locator: Chapter 1
same_as:
  wikidata: Q1641477
  wikipedia: Hypothetical syllogism
inventory: [6E1JVBEK1Z]
---

## Summary

"If it rains, the street is wet" and "if the street is wet, cars drive slowly" give "if it rains, cars drive slowly".
This step is hypothetical syllogism: two implications that share a middle part join into one.

Hypothetical syllogism is the [[rule of inference|QPD3X471Q1]] that derives $\varphi \to \chi$ from the two premises $\varphi \to \psi$ and $\psi \to \chi$, for any formulas $\varphi$, $\psi$ and $\chi$:
$$\frac{\varphi \to \psi \qquad \psi \to \chi}{\varphi \to \chi}$$
Both premises and the conclusion are [[material implications|0NMG7W7Q11]], and the consequent of the first premise is the antecedent of the second.
The rule is valid: under every valuation that makes both premises true, the conclusion is true.
It says that implication is transitive, and every chain of implications in a proof uses it.

## Motivation

A long proof often runs through a chain: from the hypothesis we reach a first fact, from it a second, and so on to the conclusion.
Each link is an implication, and the whole proof is the implication from the first statement to the last.
For example, "$f$ is differentiable" gives "$f$ is continuous", and "$f$ is continuous on $[a, b]$" gives "$f$ is Riemann integrable on $[a, b]$".
Hypothetical syllogism joins two links into one, so that a theorem can be stated without its intermediate steps.

## Notation

The rule is written as a fraction, or as $\varphi \to \psi,\ \psi \to \chi \vdash \varphi \to \chi$.
The corresponding tautology is $((p \to q) \land (q \to r)) \to (p \to r)$.
In proofs, a chain is often written $P \Rightarrow Q \Rightarrow R$, meaning $P \Rightarrow Q$ and $Q \Rightarrow R$, with the conclusion $P \Rightarrow R$.
This chain notation does not mean $P \Rightarrow (Q \Rightarrow R)$, which is a different formula.
Other names are chain argument and transitivity of implication.

## Remarks

### Checking the rule by a truth table

Let $p$ be "it rains", $q$ be "the street is wet" and $r$ be "cars drive slowly".
The [[truth table|05RSK4Q657]] has eight rows.

| $p$ | $q$ | $r$ | $p \to q$ | $q \to r$ | $p \to r$ |
|---|---|---|---|---|---|
| T | T | T | T | T | T |
| T | T | F | T | F | F |
| T | F | T | F | T | T |
| T | F | F | F | T | F |
| F | T | T | T | T | T |
| F | T | F | T | F | T |
| F | F | T | T | T | T |
| F | F | F | T | T | T |

Both premises are true in the rows TTT, FTT, FFT and FFF, and $p \to r$ is true in each of them.

### Why it holds intuitionistically

Assume $p \to q$, $q \to r$ and $p$.
Two uses of [[modus ponens|0Y0MQYST0M]] give $q$ and then $r$, so $p \to r$ follows by implication introduction.
This argument uses no excluded middle, so the rule is valid in [[intuitionistic logic|Q11N8X99FK]].
In Lean the proof is composition of functions: from `f : p → q` and `g : q → r` the term `fun h => g (f h)` has type `p → r`.

### Worked examples

[[A chain from differentiability to integrability|6R56603Z1S]] joins "differentiable on $\mathbb{R}$ implies continuous" and "continuous implies Riemann integrable on $[0, 1]$".
[[Hypothetical syllogism as a derived rule of a Hilbert system|R01ZRGG606]] derives the rule from two axioms and three uses of modus ponens.
For an integer $n$, "if $12 \mid n$, then $6 \mid n$" and "if $6 \mid n$, then $3 \mid n$" give "if $12 \mid n$, then $3 \mid n$".
For sets, $A \subseteq B$ and $B \subseteq C$ give $A \subseteq C$, by the rule applied to "$x \in A \to x \in B$" and "$x \in B \to x \in C$" for each $x$.
Three links $p \to q$, $q \to r$ and $r \to s$ give $p \to s$ by two uses of the rule.

### What is not a hypothetical syllogism

From $p \to q$ and $r \to q$ we cannot derive $p \to r$, as shown in [[chaining two implications with the same consequent|YMSC1Q4ST1]].
From $p \to q$ and $p \to r$ we cannot derive $q \to r$, since the valuation $p$ F, $q$ T, $r$ F makes both premises true and $q \to r$ false.
From $p \to q$ and $q \to r$ we cannot derive the [[converse|09A3N7ZN5G]] $r \to p$, since the valuation $p$ F, $q$ F, $r$ T is a countermodel.

### What the rule gives you

In a [[Hilbert system|1MGMQX43B8]] the rule is not primitive, but it is derivable from the axiom schemas (A1) and (A2) and modus ponens.
By the [[deduction theorem|9X08XK5RV2]], $(p \to q) \to ((q \to r) \to (p \to r))$ is then a theorem.
Together with the theorem $p \to p$, the rule says that the relation "$\varphi \to \psi$ is provable" is a preorder on formulas.
The rule combines with the [[contrapositive|04T1CT7212]]: from $p \to q$ and $q \to r$ we also get $\neg r \to \neg p$.

### Watch out

Every link must hold as written.
"$x > 1 \Rightarrow x^2 > 1 \Rightarrow x^4 > 1$" is a correct chain, but "$x^2 > 1 \Rightarrow x > 1$" is false for $x = -2$, so it cannot be a link.

### History

The Stoic logician Chrysippus listed five indemonstrable arguments, including modus ponens and modus tollens, and hypothetical syllogism is not among them.
In modern Hilbert systems, hypothetical syllogism is a standard derived rule, proved once from the axioms and then used freely.

### Try it

Prove that for every real $x$, if $x > 2$, then $x^3 - 4x > 0$, by a chain.
If $x > 2$, then $x > 0$ and $x^2 > 4$, so $x(x^2 - 4) > 0$, and $x(x^2 - 4) = x^3 - 4x$.

## Explanations

### L1 human

Hypothetical syllogism joins two "if, then" sentences that share a middle part.
"If it rains, the street is wet" and "if the street is wet, cars drive slowly" give "if it rains, cars drive slowly".
The middle part, "the street is wet", must be the same in both sentences.
With numbers: every multiple of $12$ is a multiple of $6$, and every multiple of $6$ is a multiple of $3$, so every multiple of $12$ is a multiple of $3$.

### L2 human

We prove that for every real $x$, if $x > 2$, then $x^3 - 4x > 0$, by a chain of three links.
Link 1: if $x > 2$, then $x > 0$ and $x^2 > 4$, because $x^2 > 2x > 4$.
Link 2: if $x > 0$ and $x^2 > 4$, then $x(x^2 - 4) > 0$, because the product of two positive numbers is positive.
Link 3: if $x(x^2 - 4) > 0$, then $x^3 - 4x > 0$, because the two expressions are equal.
Hypothetical syllogism on links 1 and 2, and then on the result and link 3, gives the claim.
A written proof shows such a chain as a sequence of statements, each implied by the one before.
A link used in the wrong direction breaks the chain: "$x^2 > 4 \Rightarrow x > 2$" is false for $x = -3$.

### L3 human

Transitivity of implication makes the formulas of a logic into a preorder, and after identification of [[logically equivalent|0JMR2HM2N2]] formulas, into a partial order.
For classical logic this order is a [[Boolean algebra|0XADJKM699]], and for intuitionistic logic it is a [[Heyting algebra|NG943XNQWH]], and hypothetical syllogism is the transitivity of $\le$.
In a category whose objects are formulas and whose arrows are proofs, the rule is composition of arrows, and the theorem $p \to p$ is the identity arrow.
In a Hilbert system, the derivation of the rule from (A1) and (A2) is one of the first lemmas, and some presentations use it in the proof of the deduction theorem.
