---
tag: MNEF21BD71
kind: example
name: Cut-free LK without contraction
msc: ["03F05"]
topics: [R10RMQCJQX]
audience: grad
not_instance_of:
  - target: BZ59F5GBRR
    note: contraction is removed as a rule but is not admissible, so the calculus is incomplete
uses: [PZX9J3VEMT, 0RYYK8PG4S]
sources:
  - url: https://en.wikipedia.org/wiki/Sequent_calculus
    locator: Structural rules
---

## Example

Let LK$^-$ be Gentzen's [[LK|PZX9J3VEMT]] without cut and without the contraction rules CL and CR.
We show that contraction is not admissible in LK$^-$.
First, the sequent $\Rightarrow p \vee \neg p, p \vee \neg p$ is derivable.

1. $p \Rightarrow p$ is an axiom.
2. ${\neg}$R gives $\Rightarrow p, \neg p$.
3. ${\vee}$R, with $\neg p$ as the right disjunct, gives $\Rightarrow p, p \vee \neg p$.
4. Exchange on the right gives $\Rightarrow p \vee \neg p, p$.
5. ${\vee}$R, with $p$ as the left disjunct, gives $\Rightarrow p \vee \neg p, p \vee \neg p$.

Second, the sequent $\Rightarrow p \vee \neg p$ is not derivable in LK$^-$.
We look at the possible last rules.

6. The antecedent is empty, so the last step is not a left rule, and exchange needs two formulas.
7. A weakening would come from the empty sequent $\Rightarrow$, which LK$^-$ cannot derive, since LK$^-$ is sound and the empty sequent is false.
8. So the last step is ${\vee}$R, from $\Rightarrow p$ or from $\Rightarrow \neg p$.
9. Neither of these is valid, so neither is derivable, again by soundness.

So contraction is not admissible in LK$^-$, and LK$^-$ is not a contraction-free calculus.

## Remarks

The [[law of excluded middle|0RYYK8PG4S]] is valid, so LK$^-$ is also incomplete.
Full LK derives it by one CR after step 5.

In G3cp the same sequent has a derivation without contraction.
Its R${\vee}$ keeps both disjuncts in one premise, $\Rightarrow p, \neg p$, which comes from the axiom $p \Rightarrow p, \bot$ by R${\to}$.
So the difference lies in the logical rules, not in the missing structural rule.
G3cp keeps the formulas that a later step needs, while the LK rule ${\vee}$R throws one disjunct away.

What if we keep contraction and delete weakening instead?
Then $\Rightarrow p \vee \neg p$ is derivable again, by steps 1 to 5 and one CR, so in this case weakening was not the missing piece.

## Explanations

### L1 human

Deleting the copying rule from Gentzen's calculus is not enough to get a contraction-free calculus.
Without it, the calculus can prove "$p$ or not $p$" twice in one sequent, but not once.
A contraction-free calculus must change the other rules so that the copy is never needed.

### L2 human

The test for a contraction-free calculus is whether contraction is admissible.
So we look for a derivable sequent with two copies of a formula whose one-copy version is not derivable.
Here the sequent with two copies of $p \vee \neg p$ is derivable and the one with one copy is not.
A trap is to think that any calculus without a contraction rule is contraction-free.
The name refers only to calculi in which contraction is admissible.
