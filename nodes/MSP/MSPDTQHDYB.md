---
tag: MSPDTQHDYB
kind: example
name: Peirce's law in G3cp
msc: ["03F05", "03B05"]
topics: [R10RMQCJQX]
audience: grad
instance_of: [BZ59F5GBRR]
uses: [KP5KA51FC4, GMSZ75D5WE]
sources:
  - url: https://en.wikipedia.org/wiki/Peirce%27s_law
    locator: lead section
---

## Example

We derive [[Peirce's law|GMSZ75D5WE]] $\Rightarrow ((p \to q) \to p) \to p$ in the calculus G3cp of the [[definition|KP5KA51FC4]].
We build the derivation backwards, from the goal.

1. R${\to}$ reduces the goal to $(p \to q) \to p \Rightarrow p$.
2. L${\to}$, with principal formula $(p \to q) \to p$, $\Gamma$ empty and $\Delta = p$, reduces it to two premises.
3. The left premise is $\Rightarrow p, p \to q$, and the right premise is $p \Rightarrow p$.
4. The right premise is an axiom.
5. R${\to}$ reduces the left premise to $p \Rightarrow p, q$, which is an axiom with $\Gamma$ empty and $\Delta = q$.

Read upwards, the derivation has height $3$: axiom, R${\to}$, L${\to}$, R${\to}$.

## Remarks

The derivation uses no contraction and no weakening.
In LK, the derivation of Peirce's law needs a weakening to add $q$ and a contraction to merge two copies of $p$.
In G3cp the weakening is built into the axiom $p \Rightarrow p, q$, and the shared context of L${\to}$ makes the contraction unnecessary.
By the [[inversion lemma|EXMS77F2XN]], any order of backward steps would succeed, and here only one order is possible.
In G3ip the left premise of step 3 is not a sequent of the calculus, since succedents have one formula, and Peirce's law has no G3ip derivation.

## Explanations

### L1 human

Peirce's law is a statement that is true in classical logic but not provable in intuitionistic logic.
In G3cp its proof has four steps and never copies or deletes a formula.
Each step removes one connective from the goal.

### L2 human

To find the derivation, apply the only rule that fits the goal at each step.
The goal $\Rightarrow ((p \to q) \to p) \to p$ has one formula, an implication on the right, so R${\to}$ applies.
Then the only formula with a connective on the left is $(p \to q) \to p$, so L${\to}$ applies.
A trap is to look for a contraction step, as in LK: the shared context $\Delta = p$ already sends a copy of $p$ to both premises.
