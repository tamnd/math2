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

We derive [[Peirce's law|GMSZ75D5WE]], the sequent $\Rightarrow ((p \to q) \to p) \to p$, in the calculus G3cp of the [[definition|KP5KA51FC4]].
We build the derivation backwards, from the goal, and at each step only one rule fits.

1. The goal has one formula, an implication on the right, so R${\to}$ reduces it to $(p \to q) \to p \Rightarrow p$.
2. The only compound formula is now $(p \to q) \to p$ on the left, so we apply L${\to}$ with $\Gamma$ empty and $\Delta = p$.
3. The left premise is $\Rightarrow p, p \to q$, and the right premise is $p \Rightarrow p$.
4. The right premise is an axiom.
5. R${\to}$ reduces the left premise to $p \Rightarrow p, q$, an axiom with $\Gamma$ empty and $\Delta = q$.

Read from the top, the main branch is axiom, R${\to}$, L${\to}$, R${\to}$, so the derivation has height $3$.
Check: every leaf has the atom $p$ on both sides, which is the form of a G3cp axiom.

## Remarks

The derivation has no weakening and no contraction, and it does not need them.
In LK, the usual derivation of Peirce's law weakens $p \Rightarrow p$ to $p \Rightarrow p, q$ and later contracts two copies of $p$ on the right.
G3cp builds the weakening into the axiom $p \Rightarrow p, q$.
The shared context of L${\to}$ in step 2 sends the right-hand $p$ to both premises, so the two copies never arise.

Change the calculus and the result changes.
In G3ip every succedent has one formula, so the left premise $\Rightarrow p, p \to q$ of step 3 is not a sequent of the calculus.
Peirce's law has no G3ip derivation at all, because it is not valid in intuitionistic logic.
Change the formula instead, to $((p \to q) \to q) \to p$, and the right premise of step 3 becomes $q \Rightarrow p$, which is not an axiom.
That is as it should be, since the formula is false when $p$ is false and $q$ is true.

## Explanations

### L1 human

Peirce's law is a statement about "if, then" that holds in classical logic but that intuitionistic logic does not prove.
In G3cp its proof has three rule steps and never copies or deletes a formula.
Each step removes one arrow from the goal, until only matching atoms are left.

### L2 human

To find the derivation, look at the shape of the goal at each step.
An implication on the right calls for R${\to}$, and an implication on the left calls for L${\to}$.
After two steps, one branch is the axiom $p \Rightarrow p$, and the other needs one more R${\to}$.
A trap is to look for a contraction, as in LK.
The shared context $\Delta = p$ already sends a copy of $p$ to both premises of L${\to}$.
