---
tag: R6MA6TFN5K
kind: example
name: The deduction theorem fails for global consequence
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
instance_of: [G989VP2NGP]
uses: [G989VP2NGP, NGHWZ9Y7ZV, 9X08XK5RV2, JS8W7PA6JK, E87G6ZTMTN]
sources:
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds
---

## Example

We write $\Gamma \models_g \varphi$ when every [[Kripke model|NGHWZ9Y7ZV]] that makes all formulas of $\Gamma$ true at every world makes $\varphi$ true at every world.
This is global consequence.
We show that $p \models_g \square p$ holds while $\models p \to \square p$ fails.

1. Let $\mathfrak{M}$ be a model with $p$ true at every world, and let $w$ be a world of $\mathfrak{M}$.
2. Every successor of $w$ has $p$, so $\square p$ is true at $w$.
3. So $\square p$ is true at every world of $\mathfrak{M}$, and $p \models_g \square p$.
4. Now take $W = \{ 1, 2 \}$, $R = \{ (1, 2) \}$ and $V(p) = \{ 1 \}$.
5. At $1$, $p$ is true, and the successor $2$ lacks $p$, so $\square p$ is false.
6. So $p \to \square p$ is false at $1$, and $\not\models p \to \square p$.
7. Hence the [[deduction theorem|9X08XK5RV2]] in the form "$\Gamma, \varphi \models_g \psi$ implies $\Gamma \models_g \varphi \to \psi$" fails, already for $\Gamma = \varnothing$.

The same happens in derivations.
If [[necessitation|G989VP2NGP]] may be applied to the hypothesis $p$, then $p \vdash \square p$ in one step.
But $\mathsf{K} \nvdash p \to \square p$, by step 6 and [[soundness|E87G6ZTMTN]].

## Remarks

Necessitation acts like an inference from a hypothesis only for global consequence, and there are two correct repairs.

The first repair is local consequence: $\Gamma \models_l \varphi$ when every world that makes $\Gamma$ true makes $\varphi$ true.
In derivations this means that necessitation is applied only to theorems of [[normal modal logic K|JS8W7PA6JK]], and then the deduction theorem holds.

The second repair is a weaker deduction theorem for global consequence.
If $\mathsf{K} \vdash (\varphi \wedge \square\varphi \wedge \dots \wedge \square^n\varphi) \to \psi$, then $\varphi \models_g \psi$.
For the proof, let $\varphi$ be true at every world of a model.
Step 2, with $\varphi$ in place of $p$, shows that $\square\varphi$ is true at every world, and by induction so is each $\square^k\varphi$.
So the antecedent is true at every world, and by soundness $\psi$ is true at every world.
The converse also holds, and its proof uses compactness.
For $\varphi = p$ and $\psi = \square p$, the case $n = 1$ applies, since $(p \wedge \square p) \to \square p$ is a tautology.

## Explanations

### L1 human

Think of the worlds as rooms, where some rooms can see others.
If a fact holds in every room, then in every room it also holds in all the rooms one can see.
But a fact can hold in one room and fail in the next.
So "if $p$ holds everywhere, then box $p$ holds everywhere" is right.
And "in each room, $p$ implies box $p$" is wrong.

### L2 human

Take $\varphi = \square p \to p$ and $\psi = \square\square p \to \square p$.
The formula $\square\varphi \to \psi$ is an instance of the axiom $\mathrm{K}$, so $\mathsf{K} \vdash (\varphi \wedge \square\varphi) \to \psi$.
By the weaker form with $n = 1$, we get $\varphi \models_g \psi$.
But $\varphi \to \psi$ is not valid.
Take $W = \{ 1, 2, 3 \}$, $R = \{ (1, 2), (2, 3) \}$ and $V(p) = \{ 3 \}$.
At $1$, $\square p$ is false, so $\varphi$ is true.
At $2$, $\square p$ is true, so $\square\square p$ is true at $1$ while $\square p$ is false there, and $\psi$ is false at $1$.
The typical use of global consequence is reasoning about a fixed class of models, for example one given by global axioms.
Watch out: a proof that uses necessitation on hypotheses gives a global consequence, and it cannot be turned into a theorem $\varphi \to \psi$.
