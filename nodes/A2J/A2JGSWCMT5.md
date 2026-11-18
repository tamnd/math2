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

Take the frame with two worlds and one arrow between them:
$$W = \set{a, b}, \quad R = \set{(a, a), (b, b), (a, b)}, \quad V(p) = \set{a}.$$
We show that axiom $\mathrm{5}$, $\lozenge p \to \square\lozenge p$, fails at $a$, while the frame validates the [[modal logic S4|N60RVXSA5W]].

1. $R$ is reflexive: $(a, a)$ and $(b, b)$ are in $R$.
2. $R$ is transitive: the only pair between different worlds is $(a, b)$, and $b$ sees only $b$, so every chain $x R y R z$ gives $x R z$.
3. So $R$ is a [[preorder|0VABYWJWH9]], and the frame validates $\mathsf{S4}$, by [[common modal axiom schemata|FDFQFWPM4X]] and [[soundness|E87G6ZTMTN]].
4. $\lozenge p$ is true at $a$, since $a$ sees itself and $p$ is true at $a$.
5. $\lozenge p$ is false at $b$, since $b$ sees only $b$ and $p$ is false at $b$.
6. $\square\lozenge p$ is false at $a$, since the successor $b$ makes $\lozenge p$ false.
7. So $\mathrm{5}$ fails at $a$, and $\mathsf{S4} \nvdash \mathrm{5}$.
8. By [[the axioms of S5|ECYRK9C2ZT]], $\mathsf{S5}$ proves $\mathrm{4}$, so $\mathsf{S4} \subseteq \mathsf{S5}$. With step 7, $\mathsf{S4} \subsetneq \mathsf{S5}$.

## Remarks

The example shows that symmetry is what separates the frames of $\mathsf{S5}$ from those of $\mathsf{S4}$.
The relation is not Euclidean: $a R a$ and $a R b$ hold, but $b R a$ fails.
The same model refutes axiom $\mathrm{B}$ at $a$: $p$ is true at $a$, and $\square\lozenge p$ is false at $a$ by step 6.
If we add the pair $(b, a)$, the relation becomes $W \times W$, an equivalence relation, and $\square\lozenge p$ becomes true at $a$.
This two-world frame is the smallest frame of $\mathsf{S4}$ that is not a frame of $\mathsf{S5}$.
The reason is that every preorder on one world is an equivalence relation.
In the [[modal logic S5|VC3A2VWXND]], the formula $\lozenge p \to \square\lozenge p$ says that a possibility is necessarily possible.
In $\mathsf{S4}$ a possibility can be lost by moving to a later world.

## Explanations

### L1 human

Think of two moments, today $a$ and tomorrow $b$, where today one can still see tomorrow, but tomorrow one cannot go back.
Today it is sunny, so today sun is possible.
Tomorrow it is cloudy, and from tomorrow there is no way back to the sunny day.
So "sun is possible" is true today, but "it is settled that sun stays possible" is false today.
In S5 this cannot happen, since every world sees every world of its class.

### L2 human

1. Read $\square\varphi$ in $\mathsf{S4}$ as "$\varphi$ holds now and at every later stage of information".
2. At stage $a$, the agent has not excluded $p$, so $\lozenge p$ holds.
3. At stage $b$, the agent has learned that $p$ fails, so $\lozenge p$ fails there.
4. So at $a$ the possibility of $p$ is not settled, and $\mathrm{5}$ fails.

The typical use of this frame is as the standard witness for $\mathsf{S4} \subsetneq \mathsf{S5}$.
A trap: to refute $\mathrm{5}$ in $\mathsf{S4}$, the frame must still be reflexive and transitive.
So a frame such as $a R b$ alone is not a valid witness for $\mathsf{S4}$.
