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

Modal logic is propositional logic with one more operator, the box $\square$, read "necessarily", and its dual, the diamond $\lozenge$, read "possibly".
Suppose that three situations $1$, $2$ and $3$ are possible from the situation $1$, and that $p$ holds in $2$ and $3$ but not in $1$.
Then at $1$ the formula $p$ is false, $\lozenge p$ is true, and $\square p$ is false, since $p$ fails in the possible situation $1$.
So the value of $\square p$ is not fixed by the value of $p$, and that is the whole reason for a new kind of logic.

The [[modal formulas|G8VGTW9P4F]] are built from variables $p, q, \dots$ and $\bot$ with $\to$ and $\square$, and we put $\lozenge\varphi := \neg\square\neg\varphi$.
A *modal logic* is a set $\Lambda$ of modal formulas that contains every [[tautology|05006AJ7DZ]], and is closed under [[modus ponens|0Y0MQYST0M]] and under uniform substitution.
The *modal depth* $\operatorname{md}(\varphi)$ is the largest number of boxes nested inside each other in $\varphi$.

## Motivation

Classical [[propositional calculus|09K9MWD2QQ]] is truth-functional: the value of a compound formula depends only on the values of its parts.
The sentences "it is necessary that $p$" and "Ann knows that $p$" are not of this kind.
Two true sentences can differ, because one is necessary and the other is true by accident.
So we need a new operator, and we must find and justify its laws, such as $\square p \to p$ or $\square p \to \square\square p$.

Modal logic answers such questions with exact tools: axiom systems, the possible-world models of [[Kripke semantics|NGHWZ9Y7ZV]], and completeness theorems.
The same tools serve computer science, where $\square\varphi$ reads "after every step of the program, $\varphi$" or "in every state reachable from here, $\varphi$".
The rest of the sub-area builds the theory step by step: models, the logic $\mathsf{K}$ and its extensions up to $\mathsf{S5}$, and then completeness, filtration and decidability.

## Notation

We take the variables, $\bot$, $\to$ and $\square$ as primitive, and define $\neg\varphi := \varphi \to \bot$, $\top := \neg\bot$, $\wedge$, $\vee$ and $\leftrightarrow$ as usual.
Some books take $\lozenge$ as primitive and define $\square\varphi := \neg\lozenge\neg\varphi$, and the two choices give the same logics.
Hughes and Cresswell write $L$ for the box and $M$ for the diamond.
Epistemic logic writes $K$ for "knows", and tense logic writes $G$ and $F$ for "always in the future" and "at some future time".
We write $\Lambda \vdash \varphi$ for $\varphi \in \Lambda$, logics in sans-serif type ($\mathsf{K}$, $\mathsf{S4}$) and axioms in roman type ($\mathrm{T}$, $\mathrm{4}$).

## Remarks

### Five readings of one box

The box has many readings, and each reading picks its own laws.
Read as "necessarily" (alethic), as "the agent knows" (epistemic) or as "now and at every later time" (temporal), the axiom $\square p \to p$ is a law.
Read as "the agent believes" (doxastic) or "it is obligatory" (deontic), it fails, because beliefs can be false and duties can be broken.
Read as "Peano arithmetic proves", it is not a law of the [[provability logic|WJK0YA4GP2]] $\mathsf{GL}$, by Löb's theorem.
[[The axiom □p → p under five readings|N5XH6GR9XK]] works through each case with a two-world countermodel.

### Depth and subformulas

Take $\varphi = \square(p \to \lozenge q) \to \lozenge\square p$.
It has four modal operators, but no chain of them is longer than two, so $\operatorname{md}(\varphi) = 2$.
The depth has a meaning: the truth of $\varphi$ at a world depends only on the worlds that we reach from it in at most $2$ steps.
[[Subformulas and modal depth of a modal formula|1GQEQHQ57F]] counts the subformulas of $\varphi$ and computes the depth step by step.

### What is not a modal logic

The set of formulas true at one world of one model is not a modal logic.
In the one-world model with $p$ true, the formula $p$ is true, but its substitution instance $\bot$ is false, so uniform substitution fails; see [[the formulas true at one world|ESBQKZG00Q]].
A truth table for the box does not give the logic $\mathsf{K}$ either.
Each of the four unary truth functions either misses the theorem $\square\top$ or adds a non-theorem such as $\square p \to p$, as [[no two-valued truth table gives K|H22GJGKD5M]] shows.

### The first rules

The intersection of any family of modal logics is a modal logic, because each closure condition survives intersection.
So every set of formulas lies in a smallest modal logic.
The logics of the sub-area are [[normal|D1TJYZZDCY]]: they also contain the axiom $\mathrm{K}$, $\square(p \to q) \to (\square p \to \square q)$, and they are closed under the [[necessitation rule|G989VP2NGP]].
In every normal logic $\square\varphi \leftrightarrow \neg\lozenge\neg\varphi$ is a theorem, since $\neg\neg\psi \leftrightarrow \psi$ is a tautology and the box respects provable equivalence.
Logics that are not normal, such as those of [[neighborhood semantics|CN7HK9K1B6]], still satisfy the definition of a modal logic.

### Watch out

The formula $\square(p \to q)$ does not give $p \to \square q$.
Take two worlds that see each other and themselves, with $p$ and $q$ true at $1$ and both false at $2$.
Then $p \to q$ is true at both worlds, so $\square(p \to q)$ holds at $1$.
But $p$ is true at $1$ and $\square q$ is false at $1$, since $q$ fails at $2$.
The second trap is the box of a disjunction: $\square(p \vee q)$ does not give $\square p \vee \square q$, as [[the three-world model|6JXBZ2C9B4]] shows at its world $1$.

### History

Clarence Irving Lewis introduced [[strict implication|5JW54NP52K]] in 1912, as a reply to the paradoxes of material implication, and he developed it in A Survey of Symbolic Logic (1918).
Lewis and Langford presented the systems $\mathsf{S1}$ to $\mathsf{S5}$ in Symbolic Logic (1932).
Carnap gave a semantics of state descriptions in Meaning and Necessity (1947).
Kanger and Hintikka had related ideas of possible-world semantics in the 1950s.
Kripke proved the completeness of quantified $\mathsf{S5}$ for possible-world models in 1959, and gave the relational semantics of the normal logics in 1963.

### Try it

First, compute the modal depth of $\square p \wedge \lozenge\square\square q$.
The left part has depth $1$ and the right part has depth $3$, so the depth is $3$.

Second, is the set of tautologies together with $p \to \square p$ a modal logic?
No, because it contains $p \to \square p$ but not the instance $q \to \square q$, so it is not closed under substitution.

## Explanations

### L1 human

Ordinary logic says whether a statement is true or false.
Modal logic also says whether a statement must be true, or could be true.
We write "box $p$" for "$p$ must be true" and "diamond $p$" for "$p$ could be true".
For example, "it rains" could be true today and false tomorrow, but "2 plus 2 is 4" must be true.
The word "must" can mean a law of nature, a fact that someone knows, or a rule of a game.
Each meaning has its own rules, and modal logic compares these rules with exact methods.

### L2 human

We check one formula under one reading.
Take $\square\square p \to \square p$ and read $\square\varphi$ as "$\varphi$ holds at every later time" on the time line $(\mathbb{N}, <)$.
Let $p$ be false at time $1$ and true at every time from $2$ on.
At time $0$, the formula $\square\square p$ says that every time $t \ge 1$ is followed only by times where $p$ holds.
That is true, because every time after $t \ge 1$ is at least $2$.
But $\square p$ is false at time $0$, since $p$ fails at time $1$.
So $\square\square p \to \square p$ fails at $0$, and the strict future reading rejects it.
Under the reading "now or later" the same formula holds, because a later time of a later time is a later time.
The typical use is to fix a reading, list the laws that it supports, and then study the smallest normal logic with these laws.

### L3 human

From the algebraic view, a normal modal logic is the equational theory of a variety of Boolean algebras with one operator that preserves finite meets and the top element.
Kripke frames give the complex algebras of this variety, and the [[canonical model|TVE4F04KME]] is the logical form of the representation theorem of Jónsson and Tarski.
From the model-theoretic view, modal formulas are first-order formulas in one free variable, by the [[standard translation|YW6YGBMVQY]].
Up to equivalence they are exactly the first-order formulas invariant under [[bisimulation|X27BR4YP2Y]], by the [[van Benthem characterization theorem|Y89MGMWE4H]].
These questions belong to the sub-area on [[modal model theory|SPQVNPZDTB]].
The applied readings (time, knowledge, obligation) return in [[applied modal logics|CQM9SRN8PM]], and the provability reading in [[provability logics|3E7M66WW6Q]].
