---
tag: G989VP2NGP
kind: concept
name: Necessitation rule
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
uses: [~b1c67ad7, QPD3X471Q1, 9X08XK5RV2, ~4cb83bb6]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_modal_logic
    locator: lead section
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section N
    note: adopted
    mention: wikipedia://en/76765067#18J4
    sections: [Summary]
inventory: [3QAB4ACFEF]
---

## Summary

The necessitation rule is the [[rule of inference|QPD3X471Q1]] "from $\vdash \varphi$ infer $\vdash \square\varphi$".
If a formula is a theorem of a logic, then its box is a theorem too.
Together with the axiom $\mathrm{K}$ it makes a modal logic [[normal|~b1c67ad7]], and its exact form, with admissible and derivable versions, is in [[the definition|~4cb83bb6]].
The rule applies to theorems only, and it is not the formula $\varphi \to \square\varphi$.
It expresses the idea that the laws of logic hold in every possible world, so they are necessary.

## Motivation

On a [[Kripke frame|NGHWZ9Y7ZV]], a formula valid on the frame is true at every world, so it is true at every successor of every world.
Thus $\square\varphi$ is valid whenever $\varphi$ is valid, and a logic of a class of frames must be closed under this step.
Philosophically, a law of logic is not true by accident: it holds in every world, so it is necessary.
The rule records this, while the axioms of the logic record which further laws of necessity we accept.

## Notation

1. The rule is written $\varphi \,/\, \square\varphi$, or as a fraction with $\varphi$ above and $\square\varphi$ below; the names Nec, RN and N are common.
2. Its generalization to several premises is rule RK of [[normal modal logic K|~b1c67ad7]].
3. Epistemic logic calls it knowledge generalization, and deontic logic calls the analogue "obligation of the laws of logic".

## Remarks

### Examples

1. $\mathsf{K} \vdash \square\top$ and $\mathsf{K} \vdash \square(p \to p)$, since $\top$ and $p \to p$ are tautologies, see [[the boxed tautologies|~5b239ce1]].
2. Necessitation applied twice gives $\mathsf{K} \vdash \square\square\top$, and in general $\mathsf{K} \vdash \square^n\top$ for every $n$.
3. From the tautology $(p \wedge q) \to p$, necessitation and $\mathrm{K}$ give $\square(p \wedge q) \to \square p$, the rule RM.
4. For global consequence, $p$ entails $\square p$, but the deduction theorem fails, see [[the global consequence example|~11d8c9d7]].

### Non-examples

1. The formula $p \to \square p$ is not a theorem of $\mathsf{K}$, although the rule holds, see [[the non-theorem p to box p|~b3ba27b3]].
2. The rule "from $\vdash \varphi \to \psi$ infer $\vdash \varphi \to \square\psi$" is not sound: from the tautology $p \to p$ it gives $p \to \square p$.
3. Lewis's systems $\mathsf{S2}$ and $\mathsf{S3}$ do not have the full rule, so they are not normal.

### Basic properties

1. Necessitation preserves validity on a frame, see [[soundness of normal modal logics|~d189ee4b]].
2. It preserves validity in a model, but not truth at a single world: $p$ can be true at $w$ while $\square p$ is false at $w$.
3. Take the Hilbert system whose axioms are all tautology instances, all $\mathrm{K}$ instances and all formulas $\square^n\alpha$ with $\alpha$ such an instance. Its only rule is modus ponens. In this system, necessitation is admissible but not primitive.
4. The admissibility in item 3 has a proof by induction on derivations. The box of an axiom is an axiom, and if $\square\psi$ and $\square(\psi \to \varphi)$ are derivable, then $\mathrm{K}$ gives $\square\varphi$.
5. With necessitation applied only to theorems, the [[deduction theorem|9X08XK5RV2]] holds for local consequence: $\Gamma \cup \set{\varphi} \vdash_\Lambda \psi$ if and only if $\Gamma \vdash_\Lambda \varphi \to \psi$.

### History

Gödel's note of 1933 on the provability interpretation of intuitionistic logic used a rule of this form for the system now called $\mathsf{S4}$.
Lewis's systems did not all have it, and Kripke's normal logics of 1963 are the logics with $\mathrm{K}$ and this rule.

### Common errors

1. Reading the rule as the formula $\varphi \to \square\varphi$; on frames, that formula says $R[w] \subseteq \set{w}$ for every $w$.
2. Applying the rule to a hypothesis in a derivation from assumptions and then using the deduction theorem; this "proves" $p \to \square p$.
3. Believing that the rule makes every true formula necessary; it makes only theorems necessary.

## Explanations

### L1 human

The necessitation rule says: what logic proves is necessary.
If we prove "it rains or it does not rain" by logic alone, then it is necessarily so.
The rule does not say that every true statement is necessary.
"It rains" may be true today without being necessary.

### L2 human

We derive $\square(p \wedge q) \to \square q$ in $\mathsf{K}$.

1. $(p \wedge q) \to q$ is a tautology, so it is a theorem.
2. Necessitation gives $\square((p \wedge q) \to q)$.
3. The instance $\square((p \wedge q) \to q) \to (\square(p \wedge q) \to \square q)$ of $\mathrm{K}$ is an axiom.
4. Modus ponens with 2 and 3 gives $\square(p \wedge q) \to \square q$.

The typical use is in this pattern: a propositional law, then necessitation, then $\mathrm{K}$, then modus ponens.
A trap: in step 2 the premise must be a theorem; from the mere assumption $p$ the rule gives nothing that we may discharge.

### L3 human

Necessitation is a rule of the logic, not of the consequence relation, and this explains the two consequence relations of modal logic.
The local one uses the rule only on theorems and has the deduction theorem.
The global one applies it to assumptions and has the deduction theorem only in the form $\Gamma \cup \set{\varphi} \vdash^g \psi$ iff $\Gamma \vdash^g \bigwedge_{k \le n} \square^k\varphi \to \psi$ for some $n$.
Algebraically, the rule says that the top element is fixed by $\square$, and the axiom $\mathrm{K}$ says that $\square$ preserves meets.
Together they make $\square$ a meet-preserving map, the dual of a relation.
In the provability reading the rule is the first Hilbert-Bernays-Löb condition, see [[provability logic|WJK0YA4GP2]].
