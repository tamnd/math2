---
tag: J57YRDWX3G
kind: concept
name: Intuitionistic modal logic
msc: ["03B45", "03B20"]
topics: [38EQ20GR7M]
audience: research
uses: [Q11N8X99FK, C3RZY20ETK, NGHWZ9Y7ZV, 35VKJY77TY, G989VP2NGP, 0QV2JS9RJ3]
sources:
  - url: https://en.wikipedia.org/wiki/Modal_logic
    locator: Extensions
  - url: https://arxiv.org/abs/2309.00532
    locator: Definition 16
  - url: https://arxiv.org/abs/2408.00262
    locator: Section II, Constructive K and its extensions
---

## Summary

An *intuitionistic modal logic* is a [[modal logic|C3RZY20ETK]] whose propositional base is [[intuitionistic logic|Q11N8X99FK]], in a language where $\square$ and $\lozenge$ are both primitive.
The main system is $\mathsf{IK}$, the logic of Fischer Servi and of Plotkin and Stirling.
It is the smallest set of formulas that contains every instance of the axioms of intuitionistic propositional logic and of the five schemes
$$\square(A \to B) \to (\square A \to \square B), \quad \square(A \to B) \to (\lozenge A \to \lozenge B), \quad \neg \lozenge \bot, \quad \lozenge(A \vee B) \to \lozenge A \vee \lozenge B, \quad (\lozenge A \to \square B) \to \square(A \to B),$$
and that is closed under modus ponens and the [[necessitation rule|G989VP2NGP]] (from $A$ infer $\square A$).
Its semantics uses *birelational frames* $(W, \le, R)$, where $\le$ is a [[partial order|0QV2JS9RJ3]] on $W$, $R$ is a binary relation on $W$, and two conditions hold:
$$\text{(F1)} \ \ w \le w' \text{ and } w R v \implies \exists v' \, (v \le v' \text{ and } w' R v'), \qquad \text{(F2)} \ \ w R v \text{ and } v \le v' \implies \exists w' \, (w \le w' \text{ and } w' R v').$$
In a birelational model, $\le$ interprets the intuitionistic connectives as in [[Kripke semantics for intuitionistic logic|35VKJY77TY]], and $R$ interprets the modalities as in [[Kripke semantics|NGHWZ9Y7ZV]] for modal logic.
Intuitionistic modal logic matters because modal reasoning in constructive mathematics and in type theory has no classical base, so $\square$ and $\lozenge$ are no longer dual.

## Motivation

In classical modal logic, $\lozenge A$ is an abbreviation of $\neg \square \neg A$, and one axiom for $\square$ is enough.
Over an intuitionistic base, this duality fails, so each modality needs its own axioms, and the axioms must say how the two modalities interact.
Different choices give different logics, and the subject needs a principle to choose among them.
Simpson proposed one principle: read the classical Kripke clauses for $\square$ and $\lozenge$ in an intuitionistic metatheory.
This reading leads to $\mathsf{IK}$ and to its birelational semantics.
A second principle comes from proof theory: take the natural deduction rules for $\square$ and $\lozenge$ that have a good computational reading.
This reading leads to *constructive* $\mathsf{K}$, a weaker logic.

## Notation

The formulas are built from variables $p, q, \dots$ and $\bot$ with $\wedge$, $\vee$, $\to$, $\square$ and $\lozenge$, and $\neg A$ abbreviates $A \to \bot$.
A *birelational model* is a frame $(W, \le, R)$ with a valuation $V$ that sends each variable to an up-set of $(W, \le)$.
The forcing relation $w \Vdash A$ is defined by induction on $A$:

1. $w \Vdash p$ iff $w \in V(p)$, and $w \Vdash \bot$ never holds.
2. $w \Vdash A \wedge B$ iff $w \Vdash A$ and $w \Vdash B$; $w \Vdash A \vee B$ iff $w \Vdash A$ or $w \Vdash B$.
3. $w \Vdash A \to B$ iff for every $w' \ge w$, if $w' \Vdash A$, then $w' \Vdash B$.
4. $w \Vdash \square A$ iff for every $w' \ge w$ and every $v$ with $w' R v$, we have $v \Vdash A$.
5. $w \Vdash \lozenge A$ iff there is a $v$ with $w R v$ and $v \Vdash A$.

A formula is *valid* on a frame when every world of every model on the frame forces it.
Some authors write $\mathsf{FS}$ for $\mathsf{IK}$, after Fischer Servi.
$\mathsf{CK}$ denotes constructive $\mathsf{K}$, and $\mathsf{IS4}$ denotes the extension of $\mathsf{IK}$ by the $\mathsf{S4}$ axioms for both modalities.

## Remarks

### Examples

1. A [[one-world frame with a reflexive relation|ZYJH0D6Q8D]] satisfies F1 and F2, and it validates $\square p \to p$, because the world sees itself.
2. A [[two-world model where $\lozenge$ is not $\neg \square \neg$|Q4FQGB0GW3]] forces $\neg \square \neg p$ at a world that has no $R$-successor at all.
3. If $R$ is empty, then F1 and F2 hold vacuously. Every world forces $\square \bot$, and no world forces $\lozenge p$.
4. If $\le$ is the identity relation, then F1 and F2 hold with $v' = v$ and $w' = w$. The forcing clauses become the classical clauses, and the logic of these frames is classical $\mathsf{K}$.
5. Constructive $\mathsf{K}$ of Bellin, de Paiva and Ritter keeps the first two modal schemes of $\mathsf{IK}$ and drops $\neg \lozenge \bot$ and $\lozenge(A \vee B) \to \lozenge A \vee \lozenge B$.
6. $\mathsf{IS4}$ is valid on the birelational frames whose relation $R$ is reflexive and transitive.

### Non-examples

1. A [[frame that breaks condition F1|JMT2QW076J]] has a world that forces $\lozenge p$ while a later world does not, so forcing is not persistent.
2. The classical logic $\mathsf{K}$ is not an intuitionistic modal logic: it proves $p \vee \neg p$, so it is not a conservative extension of intuitionistic logic.
3. [[$\mathsf{S4}$|N60RVXSA5W]] is used to interpret intuitionistic logic through the [[Gödel-McKinsey-Tarski translation|BXVNEN55MR]], but its base is classical. The condition that fails is the intuitionistic base.

### Basic properties

1. Persistence: if $w \Vdash A$ and $w \le w'$, then $w' \Vdash A$. For $\square$ this follows from the transitivity of $\le$, and for $\lozenge$ it follows from F1.
2. Soundness and completeness: $\mathsf{IK}$ proves $A$ if and only if $A$ is valid on every birelational frame that satisfies F1 and F2. Simpson gave a proof through labelled natural deduction.
3. The formula $\lozenge p \to \neg \square \neg p$ is a theorem of $\mathsf{IK}$, but its converse is not, by example 2. So the two modalities are not interdefinable.
4. The formula $\square p \to \neg \lozenge \neg p$ is also a theorem of $\mathsf{IK}$; its proof uses no frame condition.
5. A modal formula is a theorem of $\mathsf{IK}$ exactly when its [[standard translation|YW6YGBMVQY]] is provable in intuitionistic first-order logic. This was one of Simpson's justifications of $\mathsf{IK}$.
6. Adding the scheme $A \vee \neg A$ to $\mathsf{IK}$ gives classical $\mathsf{K}$. From $\neg \lozenge p$ the last scheme gives $\square(p \to \neg p)$, hence $\square \neg p$, and classical contraposition gives $\neg \square \neg p \to \lozenge p$.
7. $\mathsf{IK}$ and $\mathsf{CK}$ differ even on formulas without $\lozenge$: the formula $(\neg \square \bot \to \square \bot) \to \square \bot$ is valid on all frames with F1, and it is not a theorem of constructive $\mathsf{K}$.

### History

Fischer Servi studied intuitionistic analogues of $\mathsf{K}$ and their birelational models in papers from the late 1970s and the 1980s.
Plotkin and Stirling proposed the same logic, with a Kripke semantics, at the TARK conference in 1986.
Simpson's 1994 Edinburgh PhD thesis, "The proof theory and semantics of intuitionistic modal logic", gave labelled natural deduction systems, a completeness theorem and a list of requirements for an intuitionistic modal logic.
Bellin, de Paiva and Ritter introduced constructive $\mathsf{K}$ in 2001, and Mendler and de Paiva gave it a Kripke semantics with fallible worlds in 2005.

### Common errors

1. Defining $\lozenge A$ as $\neg \square \neg A$. Over an intuitionistic base this gives a different modality, as example 2 shows.
2. Using the local clause "$w \Vdash \square A$ iff every $R$-successor of $w$ forces $A$". Without extra frame conditions, this clause makes $\square A$ non-persistent.
3. Assuming that every intuitionistic modal logic proves $\lozenge(A \vee B) \to \lozenge A \vee \lozenge B$. Constructive $\mathsf{K}$ and constructive $\mathsf{S4}$ of Bierman and de Paiva do not prove it.

## Explanations

### L1 human

Ordinary modal logic talks about what is necessary and what is possible.
Intuitionistic logic accepts a statement only when we have evidence for it, and evidence can grow over time.
Intuitionistic modal logic combines the two ideas, so each situation has two kinds of next situations.
One kind is "later, with more evidence", and the other kind is "an alternative situation" that the modality looks at.
Take two moments, today and tomorrow, and suppose that tomorrow we can point to an alternative where the statement holds.
Today we cannot point to such an alternative yet.
Then today we can say "it is not ruled out that the statement is possible", but we cannot say "the statement is possible".

### L2 human

We check that $\lozenge p \to \neg \square \neg p$ is valid on every birelational frame with F1.

1. Fix a model and a world $w$ with $w \Vdash \lozenge p$. Choose $v$ with $w R v$ and $v \Vdash p$.
2. To show $w \Vdash \neg \square \neg p$, take any $w' \ge w$ and show $w' \not\Vdash \square \neg p$.
3. By F1 there is $v' \ge v$ with $w' R v'$.
4. By persistence of $p$, $v' \Vdash p$. So $v' \not\Vdash \neg p$, since $v' \le v'$ and $v' \not\Vdash \bot$.
5. The pair $w' \le w'$, $w' R v'$ is a witness against $w' \Vdash \square \neg p$.
6. So $w \Vdash \neg \square \neg p$, and the implication holds at every world.

The typical use of birelational models is to refute a candidate theorem by a small countermodel, as in the [[two-world example|Q4FQGB0GW3]].
A trap: the clause for $\lozenge$ looks only at $R$-successors of $w$ itself, while the clause for $\square$ also looks at the $\le$-later worlds.

### L3 human

Under the [[standard translation|YW6YGBMVQY]], $\mathsf{IK}$ is to intuitionistic first-order logic what $\mathsf{K}$ is to classical first-order logic.
A birelational model can be turned into a Kripke model of intuitionistic predicate logic with one binary relation symbol, and this links the two completeness theorems.
Labelled proof systems, such as a [[labelled sequent calculus|F46GV42XCE]], make this view syntactic: a hypothesis $x : A$ says that $A$ holds at $x$, and $x R y$ is a separate kind of hypothesis.
The constructive tradition of $\mathsf{CK}$ and constructive $\mathsf{S4}$ starts instead from the Curry-Howard correspondence for modal [[natural deduction|6KT3BJZ7D1]], and it gives up the distribution of $\lozenge$ over $\vee$.
The logics between $\mathsf{CK}$ and $\mathsf{IK}$ have been studied by giving a frame condition for each separate axiom of $\mathsf{IK}$.
