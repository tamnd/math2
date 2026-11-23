---
tag: 57BVV7TVAW
kind: example
name: Display derivation of a box over a conjunction
msc: ["03F05", "03B45"]
topics: [R10RMQCJQX]
audience: grad
instance_of: [2Q62W689SC]
uses: [1X7D5CBXB7, FDFQFWPM4X]
sources:
  - url: https://en.wikipedia.org/wiki/Structural_proof_theory
    locator: Structures and connectives
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Common modal axiom schemata
---

## Example

We give a cut-free derivation of the following sequent in the calculus $\mathrm{DK_t}$ of the [[definition of display calculus|1X7D5CBXB7]]:
$$\mathrm{I} \vdash (\Box p \wedge \Box q) \to \Box(p \wedge q).$$
The formula is valid in every Kripke model, and it follows from the axiom K in the list of [[common modal axiom schemata|FDFQFWPM4X]].
Each step names the rule and its instance.

### Building the two halves

1. $p \vdash p$ is an axiom, and ${\Box}$L with $A = p$ and $X = p$ gives $\Box p \vdash {\bullet}p$.
2. W with $Y = \Box q$ gives $\Box p \circ \Box q \vdash {\bullet}p$.
3. D4 gives ${\bullet}(\Box p \circ \Box q) \vdash p$.
4. $q \vdash q$ is an axiom, and ${\Box}$L gives $\Box q \vdash {\bullet}q$.
5. W with $Y = \Box p$ gives $\Box q \circ \Box p \vdash {\bullet}q$, and E gives $\Box p \circ \Box q \vdash {\bullet}q$.
6. D4 gives ${\bullet}(\Box p \circ \Box q) \vdash q$.

### Joining them

7. ${\wedge}$R on steps 3 and 6, with $X = Y = {\bullet}(\Box p \circ \Box q)$, gives ${\bullet}(\Box p \circ \Box q) \circ {\bullet}(\Box p \circ \Box q) \vdash p \wedge q$.
8. C gives ${\bullet}(\Box p \circ \Box q) \vdash p \wedge q$.
9. D4 gives $\Box p \circ \Box q \vdash {\bullet}(p \wedge q)$, and ${\Box}$R gives $\Box p \circ \Box q \vdash \Box(p \wedge q)$.
10. ${\wedge}$L gives $\Box p \wedge \Box q \vdash \Box(p \wedge q)$.
11. IL gives $\mathrm{I} \circ (\Box p \wedge \Box q) \vdash \Box(p \wedge q)$.
12. D1 in the form $X \circ Y \vdash Z \iff X \vdash {*}Y \circ Z$ gives $\mathrm{I} \vdash {*}(\Box p \wedge \Box q) \circ \Box(p \wedge q)$.
13. ${\to}$R gives $\mathrm{I} \vdash (\Box p \wedge \Box q) \to \Box(p \wedge q)$.

Every step is an axiom, a display postulate or one rule of $\mathrm{DK_t}$, and no step uses cut.

We check one step semantically.
Step 3 reads $\blacklozenge(\Box p \wedge \Box q) \to p$.
If $w$ satisfies $\blacklozenge(\Box p \wedge \Box q)$, then some $v$ with $v R w$ satisfies $\Box p$, so $p$ holds at $w$.

## Remarks

The derivation shows the pattern of modal reasoning in a display calculus.
Steps 3, 6 and 9 move ${\bullet}$ across the turnstile, so that the rules ${\wedge}$R and ${\Box}$R can act on a displayed formula.
The two premises of ${\wedge}$R have the same antecedent, so contraction in step 8 merges them.
What changes without C?
The derivation would then end with two copies of ${\bullet}(\Box p \circ \Box q)$ in the antecedent, and it would prove a weaker sequent.

The converse $\Box(p \wedge q) \to (\Box p \wedge \Box q)$ is also derivable.
From $p \vdash p$, W gives $p \circ q \vdash p$, ${\wedge}$L gives $p \wedge q \vdash p$, and ${\Box}$L gives $\Box(p \wedge q) \vdash {\bullet}p$.
Then ${\Box}$R gives $\Box(p \wedge q) \vdash \Box p$, and the same steps with $q$ give $\Box(p \wedge q) \vdash \Box q$.

## Explanations

### L1 human

The claim is: if $p$ is necessary and $q$ is necessary, then "$p$ and $q$" is necessary.
In the display calculus, "necessary" is handled by a marker that can move from one side of a sequent to the other.
We move the marker to the left to get "$p$" and "$q$" on their own, combine them into "$p$ and $q$", and then move the marker back.
Every move is one rule of the calculus, and no step uses a lemma.

### L2 human

The derivation has four phases.
Steps 1 to 6 make $\Box p$ and $\Box q$ from the axioms and move ${\bullet}$ to the left with D4.
Steps 7 and 8 combine the halves with ${\wedge}$R and contract.
Steps 9 and 10 move ${\bullet}$ back with D4, then apply ${\Box}$R and ${\wedge}$L.
Steps 11 to 13 turn the sequent into a theorem with IL, D1 and ${\to}$R.
The typical use of D4 is to put a formula in position for a modal rule.
Watch out at step 7: ${\wedge}$R joins the two antecedents with $\circ$, so the two premises need the same antecedent if we want to contract afterwards.
