---
tag: HYMTN6457G
kind: example
name: An inconsistent set of three propositional formulas
msc: ["03B05"]
topics: [H8QZY0RZXZ]
audience: ug2
not_instance_of:
  - target: VM8TQ70CVJ
    note: modus ponens derives q from p and p → q, and ¬q is a member, so the set derives both q and ¬q
uses: [VM8TQ70CVJ, 0Y0MQYST0M, QN7M1JCGT9, TTKZGJEEK7]
sources:
  - url: https://en.wikipedia.org/wiki/Consistency
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Modus_ponens
    locator: lead section
---

## Example

Let $\Delta = \{ p, \; p \to q, \; \lnot q \}$, a set of formulas of [[propositional logic|09K9MWD2QQ]].
We show that $\Delta$ is not [[consistent|VM8TQ70CVJ]], and separately that it is not satisfiable.

First, a derivation of a contradiction.

1. Line 1 is $p$, a member of $\Delta$.
2. Line 2 is $p \to q$, a member of $\Delta$.
3. Line 3 is $q$, from lines 1 and 2 by [[modus ponens|0Y0MQYST0M]].
4. Line 4 is $\lnot q$, a member of $\Delta$.
5. Lines 3 and 4 show $\Delta \vdash q$ and $\Delta \vdash \lnot q$.
   So $\Delta$ is inconsistent by the definition.

Second, no valuation satisfies $\Delta$.

6. Let $v$ be a valuation with $v(p) = \mathsf{T}$ and $v(p \to q) = \mathsf{T}$.
7. The formula $p \to q$ is false only when $p$ is true and $q$ is false.
   Since it is true and $p$ is true, $v(q) = \mathsf{T}$.
8. Then $v(\lnot q) = \mathsf{F}$.
   So no valuation makes all three members true, and $\Delta$ is not [[satisfiable|QN7M1JCGT9]].

Third, the inconsistency spreads to every formula.

9. In classical logic the formula $\lnot q \to (q \to \psi)$ is derivable for every formula $\psi$.
10. Two applications of modus ponens, to line 4 and then to line 3, give $\Delta \vdash \psi$.
11. So $\Delta$ derives every formula, for example $r$ and $\lnot r$ for an unrelated variable $r$.
    This is [[explosion|TTKZGJEEK7]].

## Remarks

The two sides of the example match, as the soundness and completeness theorems predict for propositional logic.
Each proper subset of $\Delta$ is consistent.
The valuation $p = \mathsf{T}$, $q = \mathsf{T}$ satisfies $\{ p, p \to q \}$.
The valuation $p = \mathsf{F}$, $q = \mathsf{F}$ satisfies $\{ p \to q, \lnot q \}$.
The valuation $p = \mathsf{T}$, $q = \mathsf{F}$ satisfies $\{ p, \lnot q \}$.
By soundness each of these sets is consistent, and so are their subsets.
So $\Delta$ is minimally inconsistent: the contradiction needs all three members.

In a paraconsistent logic such as the logic of paradox, steps 1 to 5 still show that $\Delta$ derives $q$ and $\lnot q$.
But step 9 fails there, so $\Delta$ need not derive every formula.

## Explanations

### L1 human

Take three claims: "it rains", "if it rains, the street is wet", and "the street is not wet".
The first two claims force the street to be wet.
The third claim says it is not wet.
So the three claims cannot all be true, and from them a careless reasoner can "prove" anything at all.

### L2 human

We check the claim of the remarks that $\{ p \to q, \lnot q \}$ is consistent, with a full truth table.

1. $p = \mathsf{T}$, $q = \mathsf{T}$: $\lnot q$ is false.
2. $p = \mathsf{T}$, $q = \mathsf{F}$: $p \to q$ is false.
3. $p = \mathsf{F}$, $q = \mathsf{T}$: $\lnot q$ is false.
4. $p = \mathsf{F}$, $q = \mathsf{F}$: $p \to q$ is true and $\lnot q$ is true.

Row 4 satisfies the set, so by soundness the set is consistent.
Row 4 is the only satisfying row and makes $p$ false, so the set has $\lnot p$ as a consequence, and by completeness it derives $\lnot p$.
This is the pattern of modus tollens.
A trap is to call a set inconsistent because it contains a formula that is sometimes false.
For example $\{ \lnot q \}$ is consistent, although $\lnot q$ is false when $q$ is true.
