---
tag: ET1HPME8VV
kind: definition
name: Hilbert system
msc: ["03B05", "03F03"]
topics: [JDK63589SA]
audience: ug2
defines: 1MGMQX43B8
uses: [09K9MWD2QQ, TT7WT5HPN9, 0NMG7W7Q11, 029JBBF693, 0Y0MQYST0M]
sources:
  - book: isbn:9781482237726
    locator: Chapter 1
  - url: https://en.wikipedia.org/wiki/Hilbert_system
    locator: Propositional logic
---

## Definition

We define the Hilbert system L, the proof system that we fix for classical propositional logic, and the relation $\Gamma \vdash \varphi$ of derivability in it.

Let $P$ be a set of propositional variables.
The formulas of L are the [[propositional formulas|TT7WT5HPN9]] built from the variables with [[negation|029JBBF693]] $\neg$ and [[implication|0NMG7W7Q11]] $\to$ only.
The other connectives are abbreviations: $\varphi \lor \psi$ is $\neg \varphi \to \psi$, $\varphi \land \psi$ is $\neg (\varphi \to \neg \psi)$, and $\varphi \leftrightarrow \psi$ is $(\varphi \to \psi) \land (\psi \to \varphi)$.

For all formulas $\varphi$, $\psi$ and $\chi$, each formula of the following three forms is an axiom of L:
$$\begin{array}{ll} \text{(A1)} & \varphi \to (\psi \to \varphi), \\ \text{(A2)} & (\varphi \to (\psi \to \chi)) \to ((\varphi \to \psi) \to (\varphi \to \chi)), \\ \text{(A3)} & (\neg \psi \to \neg \varphi) \to ((\neg \psi \to \varphi) \to \psi). \end{array}$$
The only rule of inference of L is [[modus ponens|0Y0MQYST0M]] (MP): from $\varphi$ and $\varphi \to \psi$, infer $\psi$.

Let $\Gamma$ be a set of formulas.
A derivation from $\Gamma$ is a finite sequence of formulas $\psi_1, \dots, \psi_n$ such that, for each $i$, at least one of the following holds:

1. $\psi_i$ is an axiom of L;
2. $\psi_i$ is a member of $\Gamma$, called a hypothesis;
3. there are $j, k < i$ such that $\psi_k$ is the formula $\psi_j \to \psi_i$, and then $\psi_i$ follows by MP.

We write $\Gamma \vdash \varphi$, and say that $\varphi$ is derivable from $\Gamma$, when some derivation from $\Gamma$ ends with $\varphi$.
A theorem of L is a formula $\varphi$ with $\emptyset \vdash \varphi$, written $\vdash \varphi$.

More generally, a Hilbert system for a formal language is given by a set of axioms and a finite set of rules of inference, and derivations are defined in the same way.

## Notation

When several systems appear, $\vdash_{\mathrm{L}} \varphi$ marks derivability in L.
We write $\Gamma, \varphi \vdash \psi$ for $\Gamma \cup \{ \varphi \} \vdash \psi$.
The Greek letters in A1 to A3 are metavariables, and an instance replaces each letter by the same formula at each of its occurrences.
Many books call A1 and A2 by the names K and S from combinatory logic.
The relation $\vdash$ is syntactic, and it differs from the semantic relation $\models$ of [[logical consequence|1HK0VYWTV7]].

## Remarks

### Why each part is there

The axioms are schemas so that one line covers infinitely many formulas, and so that no rule of substitution is needed.
A1 lets us add an unused assumption, A2 lets an assumption pass through a step of modus ponens, and A3 carries the classical law of reasoning by contradiction.
The three clauses of a derivation say where a line may come from: the logic itself, the given hypotheses, or an earlier step.
The condition $j, k < i$ makes a derivation a list that can be checked from the top down, with no circular steps.

### A small derivation and a failing one

We derive $r$ from $\Gamma = \{ p \to q, \ q \to r, \ p \}$:
$$\begin{array}{rll} 1. & p & \text{hypothesis} \\ 2. & p \to q & \text{hypothesis} \\ 3. & q & \text{MP, lines 1 and 2} \\ 4. & q \to r & \text{hypothesis} \\ 5. & r & \text{MP, lines 3 and 4} \end{array}$$
Check: in each MP step, the second line named is the implication whose antecedent is the first line named.
So $\Gamma \vdash r$, and this derivation uses no axioms.

The list $p \to q$, $q$, $p$ from $\{ p \to q, \ q \}$ is not a derivation.
Its last line is not an axiom, not a hypothesis, and no earlier line has the form $\alpha \to p$, so clause 3 fails; see [[this non-example|7MTA90JGPB]].

### Other third axioms

A1 and A2 are kept in almost every book, while the third axiom varies.
Łukasiewicz's third axiom is $(\neg \varphi \to \neg \psi) \to (\psi \to \varphi)$, and with A1, A2 and MP it gives the same theorems as L.
Frege's system of 1879 had six axioms for $\to$ and $\neg$, and Łukasiewicz showed that one of them follows from the others.
Some books take every [[tautology|05006AJ7DZ]] as an axiom and keep only MP.
Enderton's calculus for first-order logic is of this kind: its axioms include all generalizations of tautologies, and MP is its only rule.
The [[concept page|1MGMQX43B8]] compares these systems.

### Derived rules

The [[deduction theorem|9X08XK5RV2]] and the [[basic theorems of L|Y060MF2NZ7]] give rules that shorten derivations.

- Deduction: if $\Gamma, \varphi \vdash \psi$, then $\Gamma \vdash \varphi \to \psi$.
- Hypothetical syllogism: if $\Gamma \vdash \varphi \to \psi$ and $\Gamma \vdash \psi \to \chi$, then $\Gamma \vdash \varphi \to \chi$.
- Contradiction: if $\Gamma \vdash \varphi$ and $\Gamma \vdash \neg \varphi$, then $\Gamma \vdash \psi$ for every formula $\psi$.
- Cases: if $\Gamma, \varphi \vdash \psi$ and $\Gamma, \neg \varphi \vdash \psi$, then $\Gamma \vdash \psi$.

## Explanations

### L1 human

The Hilbert system L is a precise game for writing proofs.
The pieces are formulas made from letters with "not" and "if ... then".
A proof is a numbered list of lines, and each line must be an instance of an axiom pattern, a given assumption, or the result of modus ponens on two earlier lines.
For example, from "$p$" and "if $p$ then $q$" the rule gives "$q$".
A computer can check such a list line by line, with no understanding of the meaning.

### L2 human

We check whether the list $q \to r$, $p \to q$, $q$, $r$ is a derivation from $\{ p \to q, \ q \to r \}$.
The first two lines are hypotheses.
Line 3, $q$, is not an axiom, since every axiom is an implication.
It is not a hypothesis, and modus ponens would need an earlier line $\alpha$ together with $\alpha \to q$; the only candidate is $p \to q$, but $p$ is not an earlier line.
So line 3 fails, and the list is not a derivation.
The typical use of the definition is exactly this kind of line-by-line check.
The trap is the direction of MP: from $\varphi \to \psi$ and $\psi$ nothing follows.

### L3 human

The definition makes $\vdash$ an inductively defined relation: the set of formulas derivable from $\Gamma$ is the least set that contains $\Gamma$ and the axioms and is closed under MP.
Induction on derivations is then the basic method for results about L, such as the deduction theorem and the [[soundness theorem for propositional logic|XD629S54CS]].
Since derivations are finite, $\Gamma \vdash \varphi$ implies $\Gamma_0 \vdash \varphi$ for some finite $\Gamma_0 \subseteq \Gamma$.
The same format, with axioms for quantifiers and the rule of generalization, gives Hilbert systems for [[predicate logic|086QKPF0A6]].
