---
tag: THNYAWYPM5
kind: example
name: Grz proves the reflexivity axiom
msc: ["03B45"]
topics: [3E7M66WW6Q]
audience: research
instance_of: [2Q8E4GQF3B]
uses: [2Q8E4GQF3B, G989VP2NGP, 17C5DRFAW7, QQ6PZFGGB3]
sources:
  - url: https://en.wikipedia.org/wiki/Modal_companion
    locator: Modal companions
---

## Example

The box of [[Grzegorczyk logic|2Q8E4GQF3B]] is reflexive: what is boxed is true.
We show that $\mathsf{Grz}$ proves the axiom $\mathrm{T}$:

$$\mathsf{Grz} \vdash \square p \to p.$$

We use rule (RM) of $\mathsf{K}$ from [[the proof of the properties of Löb's axiom|17C5DRFAW7]]: if $\vdash A \to B$, then $\vdash \square A \to \square B$.

1. Let $X := \square(p \to \square p)$.
   The formula $p \to (X \to p)$ is a tautology.
2. Rule (RM) applied to step 1 gives $\mathsf{Grz} \vdash \square p \to \square(X \to p)$.
3. The axiom $\mathrm{Grz}$ is $\square(X \to p) \to p$.
4. Steps 2 and 3 give $\mathsf{Grz} \vdash \square p \to p$.

## Remarks

The proof uses only the Grz axiom and rule (RM).
So every normal logic that contains the Grz axiom contains $\mathrm{T}$, and every frame of $\mathsf{Grz}$ is reflexive.
Axiom 4 is also a theorem of $\mathsf{Grz}$, but its derivation is longer, and we do not give it here.

Compare $\mathsf{GL}$, where $\square p \to p$ is not a theorem, as [[Löb's axiom in provability logic|QQ6PZFGGB3]] shows.
The Grz axiom and Löb's axiom have a similar shape, but they end differently.
Löb's axiom ends in $\square p$ and the Grz axiom ends in $p$.
That difference is what lets step 4 reach $p$ itself.

The arithmetical reading agrees.
In $\mathsf{GL}$, the translation of $\square p \to p$ is $(p \wedge \square p) \to p$, a tautology.

## Explanations

### L1 human

In Grzegorczyk logic, $\square p$ can be read "$p$ is true and provable".
The example shows that the axioms already force "if $\square p$, then $p$".
The proof only weakens the hypothesis of the Grz axiom.

### L2 human

The Grz axiom has the form "if $\square(\text{something} \to p)$, then $p$".
If $\square p$ holds, then $\square(\text{anything} \to p)$ holds, because $p$ implies "anything $\to p$".
So $\square p$ gives the hypothesis of the axiom, and the axiom gives $p$.
Watch out: the same argument does not work for Löb's axiom.
There the conclusion is $\square p$, so the argument only gives $\square p \to \square p$.

### L3 human

Weakening the hypothesis of an axiom is a common way to extract simpler laws from it.
In $\mathsf{GL}$ the same move on Löb's axiom gives nothing new, which matches the fact that provability is not reflexive.
The reflexivity of the Grz box is the syntactic side of the reflexivity of its frames, the finite partial orders.
