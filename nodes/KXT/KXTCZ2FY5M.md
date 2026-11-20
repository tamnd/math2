---
tag: KXTCZ2FY5M
kind: concept
name: Relevance logic
aliases: [relevant-logic, relevance-logic]
msc: ["03B47", "03B53"]
topics: [98QF5J4W16]
audience: research
uses: [ZZKTJY5J4T, 09K9MWD2QQ, 3T7ZJFC9QF, 6EFJF9NAYX, C7YWCR87QJ]
sources:
  - url: https://plato.stanford.edu/entries/logic-relevance/
    locator: introduction; 4 Proof Theory; 5 Some Systems of Relevance Logic; 6 Systems Closely Related to Mainstream Relevance Logic
    note: Mares, Relevance Logic, Stanford Encyclopedia of Philosophy, revision of 2020-11-13
  - url: https://en.wikipedia.org/wiki/Relevance_logic
    locator: lead; History; Axioms
  - book: isbn:9780691071923
    note: Anderson and Belnap, Entailment, The Logic of Relevance and Necessity, volume 1
  - book: isbn:9780415215343
    note: Restall, An Introduction to Substructural Logics
---

## Summary

A *relevance logic*, also called a *relevant logic*, is a logic in which the antecedent and the consequent of a provable implication must be relevantly related.
The formal test is the *variable sharing principle*: if $A \rightarrow B$ is provable, then $A$ and $B$ have a propositional variable in common.
The main systems are $\mathbf{R}$ (relevant implication), $\mathbf{E}$ (entailment), $\mathbf{T}$ (ticket entailment) and the weak base system $\mathbf{B}$.
In sequent form, relevance logics drop the weakening rule, so they are [[substructural logics|ZZKTJY5J4T]].

## Motivation

The material implication of [[classical propositional logic|09K9MWD2QQ]] proves the [[paradoxes of material implication|3T7ZJFC9QF]].
Examples are $(p \wedge \neg p) \rightarrow q$ and $p \rightarrow (q \rightarrow q)$, in which the antecedent has no connection with the consequent.
Relevance logicians want an implication that holds only when the antecedent is really used to get the consequent.
The variable sharing principle is the formal form of this requirement.

## Notation

We write $\rightarrow$ for relevant implication, and $\wedge$, $\vee$, $\neg$ for conjunction, disjunction and negation.
The SEP entry writes $\mathbin{\&}$ for conjunction; we write $\wedge$.
The Wikipedia article axiomatizes $\mathbf{B}$ with nine axioms, including $A \rightarrow A$ and $\neg\neg A \rightarrow A$, and five rules, including modus ponens.
It lists twelve further axioms, numbered 1 to 12, and builds the stronger systems from them:

1. $\mathbf{T}$ adds axioms 1 to 7 and 11, for example suffixing $(A \rightarrow B) \rightarrow ((B \rightarrow C) \rightarrow (A \rightarrow C))$ and contraction $(A \rightarrow (A \rightarrow B)) \rightarrow (A \rightarrow B)$.
2. $\mathbf{R}$ adds axioms 1 to 11, which include assertion $A \rightarrow ((A \rightarrow B) \rightarrow B)$ and excluded middle $A \vee \neg A$.
3. $\mathbf{E}$ adds axioms 1 to 7, 10 and 11, and two further axioms.
4. $\mathbf{RM}$ (R-mingle) adds all twelve, the last being $A \rightarrow (A \rightarrow A)$.

## Remarks

### Examples

1. In $\mathbf{R}$, the positive paradox [[$p \rightarrow (q \rightarrow p)$ is not provable|8V97CTCPS9]].
2. The [[natural deduction system of Anderson and Belnap|BGNGQWVS6R]] records which hypotheses each line really uses.
3. The [[Routley-Meyer semantics|H4Z8J0KMAY]] gives models for $\mathbf{B}$, $\mathbf{R}$ and their relatives with a ternary relation.

### Non-examples

[[Classical logic fails the variable sharing principle|1PBFEHFJMX]]: it proves $(p \wedge \neg p) \rightarrow q$.
[[Intuitionistic logic|Q11N8X99FK]] fails it too, since it proves $p \rightarrow (q \rightarrow q)$.

### Basic properties

1. The SEP entry states that the variable sharing principle is a necessary condition for a relevance logic, but not a sufficient one.
2. The Wikipedia article states that relevance logics are [[paraconsistent|C7YWCR87QJ]]: a contradiction does not imply every formula.
3. The SEP entry states that mainstream relevance logicians reject [[disjunctive syllogism|6EFJF9NAYX]], the inference from $A \vee B$ and $\neg A$ to $B$.
   A [[Routley-Meyer model|PSTKVCYKAB]] shows that it fails in $\mathbf{R}$.
4. The SEP entry states that naive set theory based on $\mathbf{R}$ or $\mathbf{E}$ is trivial, by the Curry paradox, whose derivation uses the contraction axiom.
5. $\mathbf{R}$, $\mathbf{E}$ and $\mathbf{T}$ are [[undecidable|X7F69S7QPX]]; the SEP entry states that many weaker systems are decidable.

### History

The Wikipedia article states that Orlov proposed relevance logic in 1928.
It names early work of Ackermann, Moh and Church in the 1950s.
It states that Anderson and Belnap, with others, wrote *Entailment*, the main work of the subject, with the second volume in the 1990s.
The SEP entry states that the central systems of Anderson and Belnap were $\mathbf{E}$ and $\mathbf{R}$.

### Common errors

"Relevant logic" and "relevance logic" name the same family; the Wikipedia article states that the first name is more common in Britain and Australia.
Variable sharing alone does not make a logic relevant: the SEP entry states that some formulas with shared variables remain paradoxical.
Rejecting disjunctive syllogism as a rule does not mean rejecting every instance of it.

## Explanations

### L1 human

In ordinary logic, "if the moon is cheese, then $2 + 2 = 4$" is true, because $2 + 2 = 4$ is true.
A relevance logic rejects this sentence, since the moon has nothing to do with arithmetic.
It accepts "if $A$ then $B$" only when a proof of $B$ really uses $A$.

### L2 human

We follow the argument of Lewis for explosion, as the SEP entry gives it, and find the step that relevance logic rejects.

1. Assume $p \wedge \neg p$.
2. Conjunction elimination gives $p$.
3. Disjunction introduction gives $p \vee q$.
4. Conjunction elimination on step 1 gives $\neg p$.
5. Disjunctive syllogism on steps 3 and 4 gives $q$.

Steps 2, 3 and 4 are valid in $\mathbf{R}$.
Step 5 is not valid in $\mathbf{R}$, so the argument fails.
The [[two-point model|PSTKVCYKAB]] shows that $(p \wedge \neg p) \rightarrow q$ is not a theorem of $\mathbf{R}$.

The typical use of relevance logic is to reason with inconsistent information without deriving every formula.
A trap: the axiom $A \vee \neg A$ is a theorem of $\mathbf{R}$, so relevance logics are not logics without excluded middle.

### L3 human

From the substructural view, $\mathbf{R}$ has contraction and exchange but no weakening.
Its positive part has a sequent calculus without weakening, due to Mints and Dunn, as the SEP entry states.
Its semantics replaces the binary accessibility relation of modal logic by a ternary relation and treats negation with the Routley star.
