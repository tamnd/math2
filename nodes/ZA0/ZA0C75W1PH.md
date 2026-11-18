---
tag: ZA0C75W1PH
kind: example
name: Strict implication is transitive
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
instance_of: [5JW54NP52K]
uses: [5JW54NP52K, JS8W7PA6JK, DJWM6VAW72, E87G6ZTMTN, FDFQFWPM4X, 0X8NMST0J2]
sources:
  - url: https://en.wikipedia.org/wiki/Modal_logic
    locator: lead section
---

## Example

We write the [[strict implication|5JW54NP52K]] of $p$ and $q$ as $\square(p \to q)$.
We show that it is transitive in $\mathsf{K}$, and that its modus ponens needs axiom $\mathrm{T}$.

1. The formula $(p \to q) \wedge (q \to r) \to (p \to r)$ is a tautology.
2. The rule RK for two premises, from [[necessitation gives the boxed tautologies in K|DJWM6VAW72]], gives $\mathsf{K} \vdash \square(p \to q) \wedge \square(q \to r) \to \square(p \to r)$.
3. So strict implication is transitive in every normal modal logic, in particular in $\mathsf{K}$ of [[normal modal logic K|JS8W7PA6JK]].
4. Modus ponens for strict implication is the formula $\square(p \to q) \wedge p \to q$.
5. It fails in $\mathsf{K}$. Take one world $w$ with the empty relation, $V(p) = \set{w}$ and $V(q) = \varnothing$.
6. $\square(p \to q)$ is true at $w$, since $w$ has no successors.
7. $p$ is true and $q$ is false at $w$, so the formula of step 4 fails at $w$. By [[soundness|E87G6ZTMTN]], $\mathsf{K}$ does not prove it.
8. In $\mathsf{T}$, the instance $\square(p \to q) \to (p \to q)$ of axiom $\mathrm{T}$ gives $\square(p \to q) \wedge p \to q$ by propositional logic.

## Remarks

The example shows that the two basic laws of an implication behave differently.
Transitivity holds at every world of every frame.
If every successor with $p$ has $q$, and every successor with $q$ has $r$, then every successor with $p$ has $r$.
Modus ponens concerns the world itself, and the box speaks only about successors.
So modus ponens needs that the world is its own successor, which is reflexivity by [[common modal axiom schemata|FDFQFWPM4X]].
In fact, $\square(p \to q) \wedge p \to q$ is valid on a frame exactly when the frame is [[reflexive|0X8NMST0J2]]: for an irreflexive world $w$, take $V(p) = \set{w}$ and $V(q) = \varnothing$.
If we add the loop $(w, w)$ to the countermodel, then $\square(p \to q)$ becomes false at $w$, and the formula holds.

## Explanations

### L1 human

"$p$ strictly implies $q$" means "in every world we consider, if $p$ then $q$".
If $p$ strictly implies $q$, and $q$ strictly implies $r$, then in every such world, $p$ gives $q$ and $q$ gives $r$.
So $p$ strictly implies $r$.
But if our own world is not among the worlds we consider, then "if $p$ then $q$" need not hold here.
Then $p$ can be true here while $q$ is false.

### L2 human

1. Take $W = \set{1, 2}$, $R = \set{(1, 2)}$, $V(p) = \set{1, 2}$, $V(q) = \set{2}$ and $V(r) = \set{2}$.
2. At $2$, $p \to q$ and $q \to r$ are true, so $\square(p \to q)$ and $\square(q \to r)$ are true at $1$.
3. By step 2 of the example, $\square(p \to r)$ is true at $1$; indeed $r$ is true at $2$.
4. Modus ponens fails at $1$: $\square(p \to q)$ and $p$ are true there, and $q$ is false.

The typical use of transitivity is to chain entailments in a derivation, as in a proof that runs through several lemmas.
A trap: a strict implication $\square(p \to q)$ with a true antecedent $p$ does not give $q$ in $\mathsf{K}$ or $\mathsf{D}$; the logic must contain $\mathrm{T}$.
