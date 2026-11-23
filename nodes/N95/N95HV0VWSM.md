---
tag: N95HV0VWSM
kind: concept
name: Hilbert-style predicate calculus
aliases: [hilbert-style-predicate-calculus, first-order-hilbert-system, axiomatic-predicate-calculus]
msc: ["03B10", "03F03"]
topics: [TTCRX3NFNY]
audience: ug2
uses: [1MGMQX43B8, 086QKPF0A6, HYJ10AF6RT, NCDZ969V7X, 0Y0MQYST0M, 05006AJ7DZ]
sources:
  - book: isbn:9780122384523
    locator: Section 2.4
  - book: isbn:9781482237726
    locator: Chapter 2
  - url: https://en.wikipedia.org/wiki/Hilbert_system
    locator: Predicate logic (example system)
  - url: https://en.wikipedia.org/wiki/First-order_logic
    locator: Hilbert-style systems and natural deduction
---

## Summary

The Hilbert-style predicate calculus is the first-order form of a [[Hilbert system|1MGMQX43B8]]: a proof is a numbered list of formulas, and almost all of the logic sits in the axioms.
Here is a complete deduction of $Q(c)$ from the hypotheses $\forall x\,(P(x) \to Q(x))$ and $P(c)$, the formal version of "all men are mortal, Socrates is a man, so Socrates is mortal":
$$\begin{array}{rll} 1. & \forall x\,(P(x) \to Q(x)) & \text{hypothesis} \\ 2. & \forall x\,(P(x) \to Q(x)) \to (P(c) \to Q(c)) & \text{instantiation axiom, } t = c \\ 3. & P(c) \to Q(c) & \text{modus ponens, lines 1 and 2} \\ 4. & P(c) & \text{hypothesis} \\ 5. & Q(c) & \text{modus ponens, lines 4 and 3} \end{array}$$
Check: line 2 has the form $\forall x\, \varphi \to \varphi[t/x]$ with $\varphi = P(x) \to Q(x)$ and $t = c$, and a constant has no variable that a quantifier could capture.

In general, the calculus has a set of logical axioms and one rule, [[modus ponens|0Y0MQYST0M]]: from $\varphi$ and $\varphi \to \psi$, infer $\psi$.
A deduction of $\varphi$ from a set $\Gamma$ of formulas is a finite list of formulas that ends with $\varphi$.
Each formula in the list is a logical axiom, a member of $\Gamma$, or follows from two earlier formulas by modus ponens.
In Enderton's form, which we call $\mathsf{H}$, the logical axioms are all generalizations $\forall x_1 \cdots \forall x_n\, \theta$, with $n \ge 0$, of the formulas $\theta$ in six groups:
$$\begin{array}{ll} 1. & \text{every tautology} \\ 2. & \forall x\, \varphi \to \varphi[t/x], \text{ where } t \text{ is substitutable for } x \text{ in } \varphi \\ 3. & \forall x\,(\varphi \to \psi) \to (\forall x\, \varphi \to \forall x\, \psi) \\ 4. & \varphi \to \forall x\, \varphi, \text{ where } x \text{ is not free in } \varphi \\ 5. & x = x \\ 6. & x = y \to (\alpha \to \alpha'), \text{ where } \alpha \text{ is atomic} \end{array}$$
In group 6, $\alpha'$ comes from $\alpha$ by replacing $x$ by $y$ at some of its places.
The [[definition|2B00FE6K5W]] states each group with its conditions.

## Motivation

A propositional Hilbert system derives the laws of the connectives, but first-order logic also needs laws for the quantifiers.
Two of them carry almost all the weight.
The first says that what holds for every object holds for the object that a term names, so from $\forall x\, \varphi$ we may pass to $\varphi[t/x]$.
The second says how to reach a universal statement: if we prove $\varphi$ about an $x$ that the hypotheses say nothing about, then we have proved $\forall x\, \varphi$.
The calculus puts the first law into the axioms of group 2.
It puts the second law either into a rule of generalization, as Mendelson does, or into axioms that are closed under generalization, as Enderton does.

Why keep only one rule?
The calculus is made for proving facts about all proofs, such as "every deducible formula is valid".
Such facts are proved by induction on the length of a deduction, and one rule means few cases.
The [[generalization theorem|VKSK35Y52Z]], the [[deduction theorem for predicate logic|8M9ZFDR4DH]] and the [[soundness|4A84VHDTHV]] proof all work this way.
Later, [[Gödel's completeness theorem|WQ1ZE255SF]] shows that the calculus deduces every valid formula.

## Notation

We write $\Gamma \vdash_{\mathsf{H}} \varphi$, or $\Gamma \vdash \varphi$ when the system is clear, for "there is a deduction of $\varphi$ from $\Gamma$".
The name $\mathsf{H}_G$ is for Mendelson's variant with a rule of generalization.
The [[substitution|NCDZ969V7X]] $\varphi[t/x]$ appears as $\varphi^x_t$ in Enderton and as $\varphi(t)$ in Mendelson.
Books also differ in their primitive symbols.
Enderton uses $\neg$, $\to$ and $\forall$, and reads $\exists x\, \varphi$ as $\neg \forall x\, \neg \varphi$; other books add $\wedge$, $\vee$, $\exists$ or $\bot$, each with its own axioms.

## Remarks

### What each group says

Group 1 does all the propositional work at once.
A formula counts as a tautology when it is true under every assignment of truth values to its prime formulas, which are its atomic formulas and its formulas of the form $\forall x\, \psi$.
So $\forall x\, P(x) \to \forall x\, P(x)$ is a tautology, and $\forall x\, P(x) \to P(c)$ is not one, because its two prime formulas are different.

Group 2 is instantiation, and its condition matters: no variable of $t$ may become bound when $t$ replaces $x$.
Group 3 lets $\forall x$ pass over an implication, and group 4 says that a quantifier on a variable that does not occur free changes nothing.
Groups 5 and 6 make $=$ reflexive and let equals replace equals inside atomic formulas.
From them the [[rules for equality|Y90Z13AXY8]] derive symmetry and transitivity.

### Worked deductions

The deduction in the Summary uses instantiation once.
A second deduction, [[for all implies there exists|BAKPBE2677]], proves $\forall x\, P(x) \to \exists x\, P(x)$ in five lines.
It instantiates $\forall x\, P(x)$ and $\forall x\, \neg P(x)$ at the variable $x$, and one tautology joins the two pieces.
The variable $x$ is always substitutable for itself, so both instances are legal.

A third deduction gets $\forall x\, Q(x)$ from $\forall x\,(P(x) \to Q(x))$ and $\forall x\, P(x)$ with group 3:
$$\forall x\,(P(x) \to Q(x)) \to (\forall x\, P(x) \to \forall x\, Q(x))$$
is an axiom, and two steps of modus ponens finish.
In Mendelson's $\mathsf{H}_G$ the same consequence comes from a [[derivation with the rule of generalization|C8ANFQQ843]]: drop the quantifiers, reason about $x$, and put $\forall x$ back.
For equality, the [[derivations of symmetry and transitivity|ZPMY0MMTVP]] use groups 5 and 6 and one tautology.

### What is not a deduction

The list "$\forall x\, \neg \forall y\,(x = y)$, then $\neg \forall y\,(y = y)$" looks like one step of instantiation, but it is not.
The term $y$ is not substitutable for $x$ in $\neg \forall y\,(x = y)$, so the implication between the two lines is not an axiom; [[the captured variable example|YJPNPDDJQT]] checks every case.

The two-line list "$P(x)$, then $\forall x\, P(x)$" is not a deduction from $\{ P(x) \}$ in $\mathsf{H}$.
The second line is not an axiom, not a hypothesis and not a result of modus ponens.
The formula $P(x) \to \forall x\, P(x)$ is not in group 4 either, because $x$ is free in $P(x)$.
In $\mathsf{H}_G$ the same list is a derivation, which is the main difference between the two systems.

### The rules you can use

Several facts about $\mathsf{H}$ make it usable in practice, and each has its own page.
The [[generalization theorem|VKSK35Y52Z]] says that $\Gamma \vdash \varphi$ gives $\Gamma \vdash \forall x\, \varphi$ when $x$ is not free in $\Gamma$.
The [[deduction theorem|8M9ZFDR4DH]] says that $\Gamma \cup \{ \psi \} \vdash \varphi$ exactly when $\Gamma \vdash \psi \to \varphi$, with no restriction in $\mathsf{H}$.

Existential introduction is also deducible.
For $t$ substitutable for $x$ in $\varphi$, group 2 gives $\forall x\, \neg \varphi \to \neg \varphi[t/x]$, and the tautology $(A \to \neg B) \to (B \to \neg A)$ turns it into
$$\varphi[t/x] \to \neg \forall x\, \neg \varphi,$$
which is $\varphi[t/x] \to \exists x\, \varphi$.

The calculus is [[sound|4A84VHDTHV]], by induction on deductions, and complete, by [[Gödel's completeness theorem|WQ1ZE255SF]].
Its theorems form a computably enumerable set, since we can list all finite lists and check each one.
By [[Church's theorem|VA6BNNY2YC]] the set is not decidable once the language has a binary relation symbol.
The [[equivalence of proof systems|A9AAHN4BMH]] shows that natural deduction, the sequent calculus and tableaux deduce the same sentences.

### Watch out

The first trap is instantiation with a term that is not substitutable.
In a structure with two elements, $\forall x\, \neg \forall y\,(x = y)$ is true, since each element differs from the other one.
But $\neg \forall y\,(y = y)$ is false, so the "instance" between them would make the calculus unsound.
The fix is to rename the bound variable first: $\forall x\, \neg \forall z\,(x = z) \to \neg \forall z\,(y = z)$ is a real axiom.

The second trap is group 4 with $x$ free in $\varphi$.
Take a structure with two elements, $P$ true of the first only, and $x$ assigned to the first.
Then $P(x)$ is true and $\forall x\, P(x)$ is false, so $P(x) \to \forall x\, P(x)$ is not valid and cannot be an axiom.

The third trap is to mix $\mathsf{H}$ and $\mathsf{H}_G$.
The two systems prove their metatheorems with different conditions, so a lemma from one book may not hold in the system of the other.

### History

Frege gave the first formal system with quantifiers in his *Begriffsschrift* of 1879.
Hilbert and Ackermann stated a first-order calculus of this kind in their book *Grundzüge der theoretischen Logik* of 1928, and they asked whether it deduces every valid formula.
Gödel answered yes in his dissertation of 1929, with the completeness theorem.

### Try it

First, is $\forall x\, R(x, y) \to R(y, y)$ an axiom of group 2, and is $\forall x\, \forall y\, R(x, y) \to \forall y\, R(y, y)$ one?
The first is, since $R(x, y)$ has no quantifier and so $y$ is substitutable for $x$.
The second is not, since the free $x$ in $\forall y\, R(x, y)$ lies inside $\forall y$, and the new $y$ would be captured.

Second, deduce $P(c)$ from $\forall x\, P(x)$.
Write the hypothesis, then the group 2 axiom $\forall x\, P(x) \to P(c)$, then $P(c)$ by modus ponens.

Third, is $P(x) \to \forall y\, P(x)$ an axiom?
Yes, it is in group 4, because $y$ is not free in $P(x)$.

## Explanations

### L1 human

A Hilbert-style calculus is a game with fixed starting positions and one move.
The starting positions are the axioms, such as "if everything has a property, then this particular thing has it".
The only move is modus ponens: from "A" and "if A then B", write "B".
A proof is a numbered list of lines, and a reader checks each line against the list of axioms and the one move.
For example, from "every square has four sides" an axiom gives "if every square has four sides, then this square has four sides".
Modus ponens then gives "this square has four sides".

### L2 human

We deduce $\forall x\, P(x) \to \exists x\, P(x)$, where $\exists x\, P(x)$ stands for $\neg \forall x\, \neg P(x)$.
Write $A$ for $\forall x\, P(x)$, $B$ for $P(x)$ and $C$ for $\forall x\, \neg P(x)$, so the goal is $A \to \neg C$.
Group 2 with $t = x$ gives two axioms:
$$A \to B \qquad \text{and} \qquad C \to \neg B.$$
The formula $(A \to B) \to ((C \to \neg B) \to (A \to \neg C))$ is a tautology: if $A$, $A \to B$ and $C \to \neg B$ are true, then $B$ is true, so $C$ must be false.
Two steps of modus ponens then give $A \to \neg C$, and the [[full deduction|BAKPBE2677]] writes out the five lines.
This is the typical use: the quantifier axioms remove the quantifiers, and group 1 does the propositional reasoning.
Watch out: the tautology is a tautology because of its propositional form alone, with $A$, $B$ and $C$ as three unrelated letters.
The formula is valid only because the domain of a structure is not empty, and the calculus builds that assumption into group 2.

### L3 human

The calculus is the first-order case of a general pattern: a set of axioms and a set of rules whose closure is the set of theorems.
The same pattern gives the modal logics K and S4, the intuitionistic predicate calculus (replace the tautologies by intuitionistic axiom schemas) and theories of arithmetic, which add non-logical axioms to $\Gamma$.
Its short list of rules makes it the usual system for Gödel's incompleteness theorems and for the arithmetization of syntax.

Its proofs are hard to find by hand.
[[Natural deduction|6KT3BJZ7D1]] and the [[sequent calculus|W72CA3R9MP]] were designed to fix this, and the [[equivalence of proof systems|A9AAHN4BMH]] shows that nothing is lost.
In proof complexity, propositional Hilbert systems are called Frege systems, and any two of them simulate each other with a polynomial increase in proof length.
