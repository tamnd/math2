---
tag: G989VP2NGP
kind: concept
name: Necessitation rule
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
uses: [JS8W7PA6JK, QPD3X471Q1, 9X08XK5RV2, 9TPXQT9625]
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

The formula $p \to p$ is a tautology, so it is a theorem of every modal logic, and the necessitation rule then gives the theorem $\square(p \to p)$.
In general, the rule is the [[rule of inference|QPD3X471Q1]] "from $\vdash \varphi$ infer $\vdash \square\varphi$": the box of a theorem is a theorem.
Together with the axiom $\mathrm{K}$ it makes a modal logic [[normal|JS8W7PA6JK]], and [[the definition|9TPXQT9625]] gives its exact forms.
The rule applies to theorems only, and it is not the formula $\varphi \to \square\varphi$.

## Motivation

On a [[Kripke frame|NGHWZ9Y7ZV]], a formula valid on the frame is true at every world, so it is true at every successor of every world.
Thus $\square\varphi$ is valid whenever $\varphi$ is valid, and the logic of a class of frames is closed under this step.
The philosophical reading is the same: a law of logic holds in every possible world, so it is necessary.
The rule records this, and the axioms of a logic record which further laws of necessity we accept.

## Notation

The rule is written $\varphi \,/\, \square\varphi$, or as a fraction with $\varphi$ above and $\square\varphi$ below.
Its common names are Nec, RN and N, and epistemic logic calls it knowledge generalization.
Its form with several premises is the rule RK of [[normal modal logic K|JS8W7PA6JK]].

## Remarks

### First theorems

Since $\top$ and $p \to p$ are tautologies, $\mathsf{K} \vdash \square\top$ and $\mathsf{K} \vdash \square(p \to p)$; see [[the boxed tautologies|DJWM6VAW72]].
Applying the rule $n$ times gives $\mathsf{K} \vdash \square^n\top$ for every $n$.
From the tautology $(p \wedge q) \to p$, the rule and $\mathrm{K}$ give $\square(p \wedge q) \to \square p$, which is the pattern of the rule RM.

### What the rule does not give

The formula $p \to \square p$ is not a theorem of $\mathsf{K}$; see [[the non-theorem p → □p|R2WWD2R5NV]].
On frames, that formula says $R[w] \subseteq \{ w \}$ for every world $w$.
The rule "from $\vdash \varphi \to \psi$ infer $\vdash \varphi \to \square\psi$" is not sound, since from $p \to p$ it would give $p \to \square p$.
Lewis's systems $\mathsf{S2}$ and $\mathsf{S3}$ lack the full rule, so they are not normal.

### What the rule preserves

Necessitation preserves validity on a frame, which is a step of [[soundness of normal modal logics|E87G6ZTMTN]].
It also preserves truth in a whole model.
It does not preserve truth at one world, since $p$ can be true at $w$ while $\square p$ is false at $w$.

### Primitive or admissible

Take the Hilbert system whose axioms are the tautology instances, the instances of $\mathrm{K}$, and the formulas $\square^n\alpha$ for each such axiom $\alpha$, with modus ponens as the only rule.
It has the same theorems as $\mathsf{K}$, and in it necessitation is admissible but not primitive.
The proof is an induction on derivations.
The box of an axiom is an axiom, and if $\square\psi$ and $\square(\psi \to \varphi)$ are derivable, then $\mathrm{K}$ gives $\square\varphi$.

### Local and global consequence

If the rule is applied only to theorems, the [[deduction theorem|9X08XK5RV2]] holds for local consequence.
That is, $\Gamma \cup \{ \varphi \} \vdash_\Lambda \psi$ if and only if $\Gamma \vdash_\Lambda \varphi \to \psi$.
For global consequence the rule applies to hypotheses, so $p$ entails $\square p$, and the deduction theorem fails; see [[the global consequence example|R6MA6TFN5K]].

### History

Gödel's note of 1933 on intuitionistic logic used a rule of this form for the system now called $\mathsf{S4}$.
Not all of Lewis's systems had it, and Kripke's normal logics of 1963 are those with $\mathrm{K}$ and this rule.

### Watch out

The most common slip is to read the rule as the formula $\varphi \to \square\varphi$.
The second is to apply the rule to a hypothesis and then use the deduction theorem, which "proves" $p \to \square p$.
The rule does not make every true formula necessary; it makes theorems necessary.

## Explanations

### L1 human

The necessitation rule says that what logic proves is necessary.
If we prove "it rains or it does not rain" by logic alone, then it is necessarily so.
The rule does not say that every true statement is necessary.
"It rains" may be true today without being necessary.

### L2 human

We derive $\square(p \wedge q) \to \square q$ in $\mathsf{K}$.

1. $(p \wedge q) \to q$ is a tautology, so it is a theorem.
2. Necessitation gives $\square((p \wedge q) \to q)$.
3. The instance $\square((p \wedge q) \to q) \to (\square(p \wedge q) \to \square q)$ of $\mathrm{K}$ is an axiom.
4. Modus ponens with lines 2 and 3 gives $\square(p \wedge q) \to \square q$.

The typical use is this pattern: a propositional law, then necessitation, then $\mathrm{K}$, then modus ponens.
Watch out: in line 2 the premise must be a theorem, and from a mere assumption $p$ the rule gives nothing that we may discharge.

### L3 human

Necessitation is a rule of the logic, not of the consequence relation, and this explains the two consequence relations of modal logic.
The local one uses the rule only on theorems and has the deduction theorem.
The global one has it only in a weaker form: $\Gamma \cup \{ \varphi \} \vdash^g \psi$ iff $\Gamma \vdash^g \bigwedge_{k \le n} \square^k\varphi \to \psi$ for some $n$.
Algebraically, the rule says that $\square$ fixes the top element, and the axiom $\mathrm{K}$ says that $\square$ preserves binary meets.
In the provability reading the rule is the first Hilbert-Bernays-Löb condition; see [[provability logic|WJK0YA4GP2]].
