---
tag: C3RZY20ETK
kind: concept
name: Modal logic
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
uses: [09K9MWD2QQ, 05006AJ7DZ, 0Y0MQYST0M, G8VGTW9P4F]
sources:
  - url: https://en.wikipedia.org/wiki/Modal_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Modal_logic
    locator: History
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds
same_as:
  wikidata: Q210841
  wikipedia: Modal logic
---

## Summary

Propositional modal logic is the study of the [[modal formulas|G8VGTW9P4F]].
These are built from propositional variables $p, q, \dots$ and $\bot$ with $\to$ and a unary operator $\square$, with $\lozenge\varphi := \neg\square\neg\varphi$.
A modal logic is a set of modal formulas that contains every [[tautology|05006AJ7DZ]], and is closed under [[modus ponens|0Y0MQYST0M]] and under uniform substitution.
The box is read as "necessarily", "it is known that", "it is always the case that", "it is obligatory that" or "it is provable that".
Each reading selects its own laws.
The subject gives one mathematical frame for all these readings, with a semantics in [[Kripke models|NGHWZ9Y7ZV]].
It also gives exact methods to compare, axiomatize and decide the resulting logics.

## Motivation

Classical [[propositional calculus|09K9MWD2QQ]] is truth-functional: the value of a compound formula depends only on the values of its parts.
The sentences "it is necessary that $p$" and "the agent knows that $p$" are not truth-functional.
Two true sentences can differ: one is necessary and the other is true by accident.
So a new operator is needed, and its laws must be found and justified.
Philosophers asked which laws hold, such as $\square p \to p$ or $\square p \to \square\square p$.
Modal logic answers such questions with exact tools: axiom systems, possible-world models and completeness theorems.
The same tools then serve computer science, where $\square$ reads "after every step of the program" or "in every state reachable from here".

## Notation

1. The primitive symbols are the variables, $\bot$, $\to$ and $\square$; we write $\neg\varphi := \varphi \to \bot$, $\top := \neg\bot$, and define $\wedge$, $\vee$, $\leftrightarrow$ as usual.
2. The diamond $\lozenge\varphi := \neg\square\neg\varphi$ is the dual of the box; some authors take $\lozenge$ as primitive and define $\square$.
3. Other symbols for the box are $L$ (Hughes and Cresswell), $N$, $K$ (knowledge) and $G$ (future time). For the diamond, $M$, $P$ and $F$ are in use.
4. The modal depth $\operatorname{md}(\varphi)$ is the largest number of nested boxes in $\varphi$; it is defined in [[the definition of modal formulas|G8VGTW9P4F]].
5. We write $\Lambda \vdash \varphi$ for $\varphi \in \Lambda$, and name logics in sans-serif type ($\mathsf{K}$, $\mathsf{S4}$) and axioms in roman type ($\mathrm{T}$, $\mathrm{4}$).

## Remarks

### Examples

1. The smallest normal modal logic $\mathsf{K}$ is a modal logic; it is the logic of all [[Kripke frames|NGHWZ9Y7ZV]], see [[normal modal logic K|~b1c67ad7]].
2. The logic $\mathsf{S5}$ of [[S5|VC3A2VWXND]] fits the alethic reading "true in every possible world".
3. The provability logic $\mathsf{GL}$ of [[provability logic|WJK0YA4GP2]] reads $\square\varphi$ as "Peano arithmetic proves $\varphi$".
4. The formula $\square(p \to \lozenge q) \to \lozenge\square p$ has 8 subformulas and modal depth 2, see [[the worked example|~e7346340]].
5. The axiom $\square p \to p$ is accepted under some readings and rejected under others, see [[the five readings|~5d9df023]].

### Non-examples

1. The set of all tautologies together with the one formula $p \to \square p$ is not a modal logic. It contains $p \to \square p$ but not its substitution instance $q \to \square q$.
2. The set of formulas true at one world of one model is not a modal logic, since uniform substitution fails, see [[the one-world example|~7b0435e6]].
3. Many-valued logics with a truth table for $\square$ are not the usual modal logics; no two-valued table gives $\mathsf{K}$, see [[the truth-table example|~81ccf77c]].

### Basic properties

1. The intersection of any family of modal logics is a modal logic, so every set of formulas lies in a smallest modal logic.
2. The modal logics in this sub-area are normal: they also contain the axiom $\mathrm{K}$ and are closed under the [[necessitation rule|G989VP2NGP]], see [[normal modal logic|~2cd45d93]].
3. In a normal modal logic $\lozenge$ and $\square$ are interdefinable: $\square\varphi \leftrightarrow \neg\lozenge\neg\varphi$ is a theorem.
4. The truth of $\varphi$ at a world depends only on the worlds reachable in at most $\operatorname{md}(\varphi)$ steps, see [[the worked example|~e7346340]].
5. Logics that are not normal, such as those of [[neighborhood semantics|CN7HK9K1B6]], also satisfy the definition of a modal logic.

### History

Clarence Irving Lewis introduced [[strict implication|5JW54NP52K]] in his book A Survey of Symbolic Logic (1918), as a reply to the paradoxes of material implication.
Lewis and Langford presented the systems $\mathsf{S1}$ to $\mathsf{S5}$ in Symbolic Logic (1932).
Carnap gave a semantics of state descriptions in Meaning and Necessity (1947).
Kripke proved completeness of quantified $\mathsf{S5}$ for possible-world models in 1959, and gave the relational semantics of the normal logics in 1963.

### Common errors

1. Confusing $\square(p \to q)$ with $p \to \square q$. The first is [[strict implication|5JW54NP52K]], and the second does not follow from it, even in $\mathsf{S5}$.
2. Reading the [[necessitation rule|G989VP2NGP]] "from $\vdash \varphi$ infer $\vdash \square\varphi$" as the formula $\varphi \to \square\varphi$.
3. Assuming that $\square(p \vee q)$ implies $\square p \vee \square q$. This is not a theorem of $\mathsf{K}$, $\mathsf{S4}$ or $\mathsf{S5}$, see [[the three-world model|~dc32167f]].

## Explanations

### L1 human

Ordinary logic says whether a statement is true or false.
Modal logic also says whether a statement must be true, or could be true.
We write "box $p$" for "$p$ must be true" and "diamond $p$" for "$p$ could be true".
For example, "it rains" could be true today and false tomorrow, but "2 plus 2 is 4" must be true.
The word "must" can mean several things: a law of nature, a fact that someone knows, or a rule of a game.
Each meaning has its own rules, and modal logic compares these rules with exact methods.

### L2 human

We check the modal depth and two readings of one formula.

1. The formula $\square\square p \to \square p$ has the subformulas $p$, $\square p$, $\square\square p$ and the whole formula.
2. Its modal depth is 2, the depth of $\square\square p$.
3. Under the reading "it is known that", it says: if I know that I know $p$, then I know $p$.
4. Take the reading "at every later time" on the time line $(\N, <)$. Then the formula fails at time 0 when $p$ is false at time 1 and true at every time from 2 on.

The typical use is to fix a reading and to list the laws that the reading supports.
Then we study the smallest normal logic with these laws.
A trap: a modal logic is a set of formulas, not one formula, and the rule of uniform substitution is part of the definition.
So a fact about the letter $p$ in a logic is a fact about every formula in the place of $p$.

### L3 human

From the algebraic view, a normal modal logic is the equational theory of a variety of Boolean algebras with an operator.
This operator preserves finite meets and the top element.
Kripke frames give the complex algebras of this variety.
The representation theorem of Jónsson and Tarski links the two views; [[the canonical model|~d626bd63]] is the logical form of that representation.
From the model-theoretic view, modal formulas are first-order formulas in one free variable via the [[standard translation|~ff160d1c]].
Up to equivalence, they are exactly the first-order formulas invariant under bisimulation (van Benthem).
This is a topic of the later sub-area [[modal model theory|SPQVNPZDTB]].
The applied readings (time, knowledge, obligation) are treated in [[applied modal logics|CQM9SRN8PM]], and the provability reading in [[provability logics|3E7M66WW6Q]].
