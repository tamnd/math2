---
tag: NM4CB7QAYT
kind: statement
role: lemma
name: Truth lemma for canonical models
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
uses: [JS8W7PA6JK, TVE4F04KME, NGHWZ9Y7ZV, VM8TQ70CVJ, SC0BSJ3GT6]
about: [TVE4F04KME]
proofs: [ST0ZHXSKFG]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Canonical models
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds, chapter on completeness and canonical models
---

## Statement

Let $\Lambda$ be a consistent [[normal modal logic|JS8W7PA6JK]], and let $\mathfrak{M}^\Lambda = (W^\Lambda, R^\Lambda, V^\Lambda)$ be its [[canonical model|TVE4F04KME]].
A set $\Gamma$ of formulas is $\Lambda$-[[consistent|VM8TQ70CVJ]] when there are no $\varphi_1, \dots, \varphi_n \in \Gamma$ with $\Lambda \vdash \neg(\varphi_1 \wedge \dots \wedge \varphi_n)$.
The following five facts hold.

1. Lindenbaum's lemma. Every $\Lambda$-consistent set is contained in a maximal $\Lambda$-consistent set.
2. Box lemma. For $\Gamma, \Delta \in W^\Lambda$, the conditions $\{ \varphi : \square\varphi \in \Gamma \} \subseteq \Delta$ and $\{ \lozenge\varphi : \varphi \in \Delta \} \subseteq \Gamma$ are equivalent.
3. Existence lemma. If $\Gamma \in W^\Lambda$ and $\lozenge\varphi \in \Gamma$, then there is $\Delta \in W^\Lambda$ with $\Gamma R^\Lambda \Delta$ and $\varphi \in \Delta$.
4. Truth lemma. For every formula $\varphi$ and every $\Gamma \in W^\Lambda$, $\mathfrak{M}^\Lambda, \Gamma \models \varphi$ holds if and only if $\varphi \in \Gamma$.
5. Canonical model theorem. Every $\Lambda$-consistent set is true at some world of $\mathfrak{M}^\Lambda$, and $\varphi$ is true in $\mathfrak{M}^\Lambda$ if and only if $\Lambda \vdash \varphi$.

The proof is in [[the proof of the truth lemma|ST0ZHXSKFG]].

## Remarks

### Why each hypothesis is needed

Normality is used in the existence lemma.
The step from $\lozenge\varphi \in \Gamma$ to a consistent set $\{ \varphi \} \cup \{ \psi : \square\psi \in \Gamma \}$ needs the rule RK.
That rule turns $\vdash \psi_1 \wedge \dots \wedge \psi_n \to \chi$ into $\vdash \square\psi_1 \wedge \dots \wedge \square\psi_n \to \square\chi$.
For a logic without axiom $\mathrm{K}$ this rule fails, the relational truth lemma fails with it, and [[neighborhood semantics|CN7HK9K1B6]] is used instead.

Maximality is used in the truth lemma.
For a consistent set $\Gamma$ that is not maximal, both $p \notin \Gamma$ and $\neg p \notin \Gamma$ can hold, while one of $p$ and $\neg p$ is true at every world.

Consistency of $\Lambda$ is needed for $W^\Lambda$ to be nonempty.
For the inconsistent logic, the set of all formulas, no set is consistent and there is no canonical model.

### What it gives you

Every normal modal logic is the set of formulas true in one Kripke model, its canonical model.
The lemma even gives strong completeness for that model: if $\Sigma$ does not prove $\varphi$ in $\Lambda$, then $\Sigma \cup \{ \neg\varphi \}$ holds at some world.
If the canonical frame of $\Lambda$ lies in a class $\mathsf{C}$ of frames that validate $\Lambda$, then $\Lambda$ is strongly complete for $\mathsf{C}$.
This gives [[the completeness theorem|FXTCKYR3AQ]] for $\mathsf{K}$, $\mathsf{T}$, $\mathsf{D}$, $\mathsf{K4}$, $\mathsf{S4}$, $\mathsf{B}$ and $\mathsf{S5}$.
[[The KD45 example|1CFMP9DEE6]] and [[the verum logic|B464EAG58T]] apply it to two more logics.

### The converse

The truth lemma is an equivalence, so it has no separate converse.
The converse of its main application does fail: a logic can be complete for a class of frames without its canonical frame being in that class.
The standard example is $\mathsf{GL}$, in [[the GL example|E61769H6KG]].

### Generalizations

For a normal logic with several boxes, the canonical model has one relation $R_i$ for each box, and the same proof gives the truth lemma, as in [[multimodal logic|ERG3KAQWYF]].
For a finite set $\Sigma$ closed under subformulas, the maximal consistent subsets of $\Sigma$ give a finite canonical model, which is a form of [[filtration|6ZZSHAKG5F]].
For first-order logic, Henkin's construction with witnesses plays the role of the existence lemma.

## History

Tarski stated Lindenbaum's lemma for propositional calculi in 1930 and credited it to Lindenbaum.
Henkin used maximal consistent sets in his completeness proof for first-order logic of 1949.
Makinson used maximal consistent sets to prove completeness of normal modal logics in 1966.
Lemmon and Scott developed canonical models in the 1960s, and the Lemmon notes, edited by Segerberg and published in 1977, made them standard.

## Explanations

### L1 human

A canonical model is built out of complete descriptions.
The truth lemma says that each description is true exactly at its own world.
So a statement holds at a world when the description of that world says yes to it.
Since every unprovable statement appears negated in some description, it is false at some world.

### L2 human

We check the box case of the truth lemma at one world.
Let $\Gamma$ be maximal consistent with $\square p \notin \Gamma$.
Then $\neg\square p \in \Gamma$, and this is equivalent to $\lozenge\neg p \in \Gamma$.
The existence lemma gives $\Delta$ with $\Gamma R^\Lambda \Delta$ and $\neg p \in \Delta$.
So $p \notin \Delta$, and $p$ is false at $\Delta$ by the definition of $V^\Lambda$.
So $\square p$ is false at $\Gamma$, as the lemma says.
The typical use is the contrapositive: to refute $\varphi$, we put $\neg\varphi$ into a maximal consistent set.
Watch out: the existence lemma is the only step that builds a new world, and the other cases only track membership.

### L3 human

In algebraic terms, $W^\Lambda$ is the set of ultrafilters of the Lindenbaum algebra of $\Lambda$.
The truth lemma says that the Jónsson-Tarski map $a \mapsto \{ u : a \in u \}$ is an embedding of modal algebras.
The existence lemma represents the operator $\lozenge$ of the algebra by a relation, and it uses the [[ultrafilter lemma|3MKZST79MK]].
The lemma uses no property of the frame, so every frame property must come from the axioms of $\Lambda$, and this is where the notion of canonicity comes from.
