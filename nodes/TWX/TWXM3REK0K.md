---
tag: TWXM3REK0K
kind: example
name: Gentzen's LK has no display property
msc: ["03F05"]
topics: [R10RMQCJQX]
audience: grad
not_instance_of:
  - target: 2Q62W689SC
    note: the structural rules of LK never move a formula to the other side of the sequent arrow, so a part such as p in p, q ⇒ r cannot be displayed
uses: [1X7D5CBXB7, PZX9J3VEMT, VHRXX0T5XT, YAFD18WYJ8]
sources:
  - url: https://en.wikipedia.org/wiki/Sequent_calculus
    locator: Inference rules
  - url: https://en.wikipedia.org/wiki/Structural_proof_theory
    locator: Structures and connectives
---

## Example

Consider Gentzen's calculus [[LK|PZX9J3VEMT]] with sequents $\Gamma \Rightarrow \Delta$, where $\Gamma$ and $\Delta$ are finite sequences of formulas.
Its structural rules are [[weakening|VHRXX0T5XT]], contraction and [[exchange|YAFD18WYJ8]] on each side.
Gentzen also counts cut as a structural rule, but cut needs a second premise and changes the formulas, so we leave it out.
Take the following sequent:
$$p, q \Rightarrow r.$$
The display property of the [[definition of display calculus|1X7D5CBXB7]] would require a sequent $p \Rightarrow W$, obtained from $p, q \Rightarrow r$ by structural rules alone.
We show that no sequent whose antecedent is $p$ alone can be reached in this way.

**Claim.** Every sequent obtained from $p, q \Rightarrow r$ by structural rules of LK has at least one occurrence of $q$ in its antecedent.

1. The claim holds for $p, q \Rightarrow r$ itself.
2. Weakening adds a formula to the antecedent or to the succedent.
   It removes nothing, so an occurrence of $q$ stays.
3. Exchange swaps two neighboring formulas on one side.
   It keeps every formula on its side, so an occurrence of $q$ stays.
4. Contraction replaces two equal neighboring formulas $A, A$ on one side by one $A$.
   If it acts on $q$, one occurrence of $q$ stays, and otherwise all occurrences stay.
5. So each structural rule turns a sequent with $q$ in its antecedent into another such sequent, and the claim follows by induction on the number of steps.

**Consequence.**

6. A sequent of the form $p \Rightarrow W$ has the antecedent $p$, which has no occurrence of $q$.
7. By the claim, no such sequent arises from $p, q \Rightarrow r$ by structural rules, so LK cannot display $p$ in this sequent.

In the display calculus, by contrast, D1 turns $p \circ q \vdash r$ into $p \vdash {*}q \circ r$ in one step.

## Remarks

The condition that fails is the display property, and the reason is a missing structural connective.
LK has a structural conjunction, the comma on the left, and a structural disjunction, the comma on the right.
It has no structural negation, so no structural rule can move $q$ to the other side.
The logical rule ${\to}$R does give $p \Rightarrow q \to r$, but it builds a new formula, so it is not a display step.

What changes if we add a rule that moves formulas across, for example "from $A, \Gamma \Rightarrow \Delta$ infer $\Gamma \Rightarrow \Delta, {*}A$" with a structural negation ${*}$?
Then $p, q \Rightarrow r$ gives $p \Rightarrow r, {*}q$, and $p$ is displayed, so the invariant of the claim breaks exactly at the new rule.
The failure is harmless for LK itself, because Gentzen's proof of cut elimination handles each rule by hand.
It matters only when we want one cut-elimination proof for a whole family of calculi, which is Belnap's aim.

## Explanations

### L1 human

In a display calculus, any piece of a sequent can be moved to stand alone, without changing the meaning.
In Gentzen's calculus, the bookkeeping rules can add, copy or reorder formulas, but they never move a formula across the arrow.
So in "$p$ and $q$ give $r$", the assumption $q$ always stays on the left.
That means $p$ can never stand alone on the left, and the display property fails.

### L2 human

The argument is an invariant.
We choose a property of sequents, "$q$ occurs in the antecedent", check that the starting sequent has it, and check that each structural rule keeps it.
Then every reachable sequent has the property, so $p$ never stands alone on the left.
The typical use of an invariant is to show that a target can never be reached by a given set of moves.
Watch out: the logical rule ${\to}$R is not a structural move, because it builds the new formula $q \to r$.
