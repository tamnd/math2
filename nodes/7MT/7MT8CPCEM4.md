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

Hypothetical syllogism is the [[rule of inference|QPD3X471Q1]] that derives $\varphi \to \chi$ from the two premises $\varphi \to \psi$ and $\psi \to \chi$, for any formulas $\varphi$, $\psi$ and $\chi$:
$$\frac{\varphi \to \psi \qquad \psi \to \chi}{\varphi \to \chi}$$
Both premises and the conclusion are [[material implications|0NMG7W7Q11]], and the consequent of the first premise is the antecedent of the second.
The rule is valid: under every valuation that makes both premises true, the conclusion is true.
It says that implication is transitive, and it is the logical form of every chain of implications in a proof.

## Motivation

A long proof often runs through a chain: from the hypothesis we reach a first fact, from it a second, and so on to the conclusion.
Each link is an implication, and the whole proof is the implication from the first statement to the last.
For example, "$f$ is differentiable" gives "$f$ is continuous", and "$f$ is continuous on $[a, b]$" gives "$f$ is Riemann integrable on $[a, b]$".
Hypothetical syllogism is the rule that joins two links into one, so that a theorem can be stated without its intermediate steps.

## Notation

The rule is written as a fraction, or as $\varphi \to \psi,\ \psi \to \chi \vdash \varphi \to \chi$.
The corresponding tautology is $((p \to q) \land (q \to r)) \to (p \to r)$.
In proofs, a chain is often written $P \Rightarrow Q \Rightarrow R$, meaning $P \Rightarrow Q$ and $Q \Rightarrow R$, with the conclusion $P \Rightarrow R$.
This chain notation does not mean $P \Rightarrow (Q \Rightarrow R)$, which is a different formula.
Other names are "chain argument" and "transitivity of implication".

## Remarks

### Examples

1. [[A chain from differentiability to integrability|~f246cd28]]: "differentiable on $\mathbb{R}$" implies "continuous on $\mathbb{R}$", which implies "Riemann integrable on $[0, 1]$".
2. [[Hypothetical syllogism as a derived rule of a Hilbert system|~8df8f1f2]]: two axioms and three uses of modus ponens derive $p \to r$ from $p \to q$ and $q \to r$.
3. For an integer $n$: "if $12 \mid n$, then $6 \mid n$" and "if $6 \mid n$, then $3 \mid n$" give "if $12 \mid n$, then $3 \mid n$".
4. For sets: if $A \subseteq B$ and $B \subseteq C$, then $A \subseteq C$. This is the rule applied to "$x \in A \to x \in B$" and "$x \in B \to x \in C$" for each $x$.
5. With three links: $p \to q$, $q \to r$ and $r \to s$ give $p \to s$, by two uses of the rule.

### Non-examples

1. [[Chaining two implications with the same consequent is not a hypothetical syllogism|~dbe58c03]]: from $p \to q$ and $r \to q$ we cannot derive $p \to r$.
2. From $p \to q$ and $p \to r$ we cannot derive $q \to r$. The valuation $p$ false, $q$ true, $r$ false makes both premises true and $q \to r$ false.
3. From $p \to q$ and $q \to r$ we cannot derive the [[converse|09A3N7ZN5G]] $r \to p$. The valuation $p$ false, $q$ false, $r$ true makes both premises true and $r \to p$ false.

### Basic properties

1. Validity by [[truth table|05RSK4Q657]]. Of the eight rows, both premises are true in rows TTT, FTT, FFT and FFF, and in each of them $p \to r$ is true.

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

2. A direct argument: assume $p \to q$, $q \to r$ and $p$. Two uses of [[modus ponens|0Y0MQYST0M]] give $q$ and then $r$. So $p \to r$, by implication introduction.
3. The argument of property 2 uses no excluded middle, so the rule is valid in [[intuitionistic logic|Q11N8X99FK]].
4. In a [[Hilbert system|1MGMQX43B8]], the rule is not primitive, but it is derivable from the axiom schemas (A1) and (A2) and modus ponens; see example 2. By the [[deduction theorem|9X08XK5RV2]], $(p \to q) \to ((q \to r) \to (p \to r))$ is then a theorem.
5. Together with the theorem $p \to p$, the rule says that the relation "$\varphi \to \psi$ is provable" is a preorder on formulas: it is reflexive and transitive.
6. The rule combines with the [[contrapositive|04T1CT7212]]: from $p \to q$ and $q \to r$ we also get $\neg r \to \neg p$.

### History

The Stoic logician Chrysippus listed five indemonstrable arguments, including modus ponens and modus tollens; hypothetical syllogism is not among them.
In the Hilbert systems of modern logic, hypothetical syllogism is a standard derived rule, proved once from the axioms and then used freely.

### Common errors

1. A student chains two implications whose middle terms do not match, as in non-example 1.
2. A student reads the chain $P \Rightarrow Q \Rightarrow R$ as a proof of $R \Rightarrow P$. The chain goes in one direction only, as in non-example 3.
3. A student breaks a chain at a link that holds only under an extra hypothesis. For example, "$x > 1 \Rightarrow x^2 > 1 \Rightarrow x^4 > 1$" is fine, but "$x^2 > 1 \Rightarrow x > 1$" is false for $x = -2$, so it cannot be a link.

## Explanations

### L1 human

Hypothetical syllogism joins two "if, then" sentences that share a middle part.
"If it rains, the street is wet" and "if the street is wet, cars drive slowly" give "if it rains, cars drive slowly".
The middle part, "the street is wet", must be the same in both sentences.
With numbers: every multiple of $12$ is a multiple of $6$, every multiple of $6$ is a multiple of $3$, so every multiple of $12$ is a multiple of $3$.

### L2 human

We prove that for every real $x$, if $x > 2$, then $x^3 - 4x > 0$, by a chain.

1. Link 1: if $x > 2$, then $x > 0$ and $x^2 > 4$. Reason: $x^2 > 2x > 4$ for $x > 2$.
2. Link 2: if $x > 0$ and $x^2 > 4$, then $x(x^2 - 4) > 0$. Reason: the product of two positive numbers is positive.
3. Link 3: if $x(x^2 - 4) > 0$, then $x^3 - 4x > 0$. Reason: $x(x^2 - 4) = x^3 - 4x$.
4. Hypothetical syllogism on links 1 and 2, and then on the result and link 3, gives the claim.

The typical use is in a written proof, where the chain is shown as a sequence of statements, each implied by the one before.
A trap is a link used in the wrong direction: "$x^2 > 4 \Rightarrow x > 2$" is false for $x = -3$, so link 1 cannot be replaced by its converse.

### L3 human

Transitivity of implication makes the formulas of a logic into a preorder, and after identification of [[logically equivalent|0JMR2HM2N2]] formulas, into a partial order.
For classical logic this order is a [[Boolean algebra|0XADJKM699]], and for intuitionistic logic it is a [[Heyting algebra|NG943XNQWH]]; hypothetical syllogism is the transitivity of the order $\le$.
In a category whose objects are formulas and whose arrows are proofs, the rule is composition of arrows, and the theorem $p \to p$ is the identity arrow.
In a Hilbert system, the derivation of the rule from the axioms (A1) and (A2) is one of the first lemmas, and it is a step in the proof of the deduction theorem in some presentations.
