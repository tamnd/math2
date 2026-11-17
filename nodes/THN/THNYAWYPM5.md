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

We show that [[Grzegorczyk logic|2Q8E4GQF3B]] proves the axiom $\mathrm{T}$: $\mathsf{Grz} \vdash \square p \to p$.
We use rule (RM) of $\mathsf{K}$ from [[the proof of the properties of Löb's axiom|17C5DRFAW7]]: if $\vdash A \to B$, then $\vdash \square A \to \square B$.

1. Let $X := \square(p \to \square p)$. The formula $p \to (X \to p)$ is a tautology.
2. Rule (RM) applied to step 1 gives $\mathsf{Grz} \vdash \square p \to \square(X \to p)$.
3. The axiom $\mathrm{Grz}$ is $\square(X \to p) \to p$.
4. Steps 2 and 3 give $\mathsf{Grz} \vdash \square p \to p$.

## Remarks

The same proof shows that every normal logic that contains the Grz axiom contains $\mathrm{T}$, so every frame of $\mathsf{Grz}$ is reflexive.
The derivation of axiom 4 in $\mathsf{Grz}$ is longer, and we do not give it here.
Compare $\mathsf{GL}$: there $\square p \to p$ is not a theorem, see [[Löb's axiom in provability logic|QQ6PZFGGB3]], although the Grz axiom has the same shape as Löb's axiom.
The arithmetical reading agrees: the translation of $\square p \to p$ is $p \wedge \square p \to p$, a tautology.

## Explanations

### L1 human

In Grzegorczyk logic, $\square p$ can be read "$p$ is true and provable".
The example shows that the axioms already force "if $\square p$, then $p$".
The proof only weakens the hypothesis of the Grz axiom.

### L2 human

1. The Grz axiom has the form "if $\square(\text{something} \to p)$, then $p$".
2. If $\square p$ holds, then $\square(\text{anything} \to p)$ holds, because $p$ implies "anything $\to p$".
3. So $\square p$ gives the hypothesis of the axiom, and the axiom gives $p$.

A trap: this argument does not work for Löb's axiom, whose conclusion is $\square p$, not $p$.
