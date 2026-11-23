---
tag: A2JGSWCMT5
kind: example
name: Axiom 5 is not a theorem of S4
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
not_instance_of:
  - target: VC3A2VWXND
    note: the countermodel is a preorder that is not symmetric, so it is an S4-model and not an S5-model
uses: [VC3A2VWXND, N60RVXSA5W, 0VABYWJWH9, FDFQFWPM4X, E87G6ZTMTN, ECYRK9C2ZT]
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
---

## Example

Today you can see tomorrow, but tomorrow you cannot go back to today.
This one-way step is a preorder that is not an equivalence relation, and it refutes axiom $\mathrm{5}$.
Take two worlds and one arrow between them:
$$W = \{ a, b \}, \quad R = \{ (a, a), (b, b), (a, b) \}, \quad V(p) = \{ a \}.$$
We show that $\lozenge p \to \square\lozenge p$ fails at $a$, while the frame validates the [[modal logic S4|N60RVXSA5W]].

1. $R$ is reflexive, because $(a, a)$ and $(b, b)$ are in $R$.
2. $R$ is transitive, because the only arrow between different worlds is $(a, b)$, and $b$ sees only $b$, so every chain $x R y R z$ gives $x R z$.
3. So $R$ is a [[preorder|0VABYWJWH9]], and the frame validates $\mathsf{S4}$ by the [[common modal axiom schemata|FDFQFWPM4X]] and [[soundness|E87G6ZTMTN]].
4. $\lozenge p$ is true at $a$, because $a$ sees itself and $p$ is true at $a$.
5. $\lozenge p$ is false at $b$, because $b$ sees only $b$ and $p$ is false at $b$.
6. $\square\lozenge p$ is false at $a$, because the successor $b$ makes $\lozenge p$ false.
7. So $\mathrm{5}$ fails at $a$, and $\mathsf{S4}$ does not prove $\mathrm{5}$.
8. By [[the axioms of S5|ECYRK9C2ZT]], $\mathsf{S5}$ proves $\mathrm{4}$, so $\mathsf{S4} \subseteq \mathsf{S5}$, and with step 7 the inclusion is strict.

## Remarks

The example shows that symmetry is what separates the frames of $\mathsf{S5}$ from those of $\mathsf{S4}$.
The relation is not Euclidean: $a R a$ and $a R b$ hold, but $b R a$ fails.
The same model refutes axiom $\mathrm{B}$ at $a$, since $p$ is true at $a$ and $\square\lozenge p$ is false at $a$ by step 6.

What changes if you add the arrow $(b, a)$?
The relation becomes $W \times W$, an equivalence relation, and $\square\lozenge p$ becomes true at $a$.
So this two-world frame is the smallest frame of $\mathsf{S4}$ that is not a frame of $\mathsf{S5}$, because the only preorder on one world is the loop, which is an equivalence relation.
In the [[modal logic S5|VC3A2VWXND]], axiom $\mathrm{5}$ says that a possibility is necessarily possible, while in $\mathsf{S4}$ a possibility can be lost by moving to a later world.

## Explanations

### L1 human

Think of two moments, today $a$ and tomorrow $b$, where today you can still see tomorrow, but tomorrow you cannot go back.
Today it is sunny, so today sun is possible.
Tomorrow it is cloudy, and from tomorrow there is no way back to the sunny day.
So "sun is possible" is true today, but "it is settled that sun stays possible" is false today.
In $\mathsf{S5}$ this cannot happen, since every world sees every world of its class.

### L2 human

Read $\square\varphi$ in $\mathsf{S4}$ as "$\varphi$ holds now and at every later stage of information".
At stage $a$ the agent has not excluded $p$, so $\lozenge p$ holds there.
At stage $b$ the agent has learned that $p$ fails, so $\lozenge p$ fails there.
So at $a$ the possibility of $p$ is not settled, and $\mathrm{5}$ fails.
This frame is the standard witness for $\mathsf{S4} \subsetneq \mathsf{S5}$.
Watch out: to refute $\mathrm{5}$ in $\mathsf{S4}$, the frame must still be reflexive and transitive, so the frame with the single arrow $a R b$ and no loops is not a valid witness.
