---
tag: 53ERPXVZ3S
kind: example
name: Harmony of the conjunction rules
msc: ["03F03"]
topics: [R10RMQCJQX]
audience: ug2
instance_of: [XJSQVK0G71, K97KZB5R7N]
uses: [PAQ4ZX2TX1]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_harmony
    locator: Overview
  - url: https://en.wikipedia.org/wiki/Proof-theoretic_semantics
    locator: Philosophical motivation
---

## Example

From the assumptions $p$ and $q$, the rule ${\wedge}$I gives $p \wedge q$, and then ${\wedge}$E$_1$ gives $p$.
$$\dfrac{\dfrac{p \qquad q}{p \wedge q}\,{\wedge}\mathrm{I}}{p}\,{\wedge}\mathrm{E}_1$$
The detour on $p \wedge q$ is wasted work: the one-line derivation consisting of the assumption $p$ already proves $p$.
We now check, for arbitrary formulas, that the conjunction rules of [[natural deduction|PAQ4ZX2TX1]] always allow this shortcut, and that they also pass the second test of [[harmony|XJSQVK0G71]].
The rules are ${\wedge}$I, from $A$ and $B$ infer $A \wedge B$, and the two eliminations ${\wedge}$E$_1$, from $A \wedge B$ infer $A$, and ${\wedge}$E$_2$, from $A \wedge B$ infer $B$.

1. Local soundness.
   Let $D_1$ derive $A$ and $D_2$ derive $B$, apply ${\wedge}$I to get $A \wedge B$, and then ${\wedge}$E$_1$ to get $A$.
2. This derivation reduces to $D_1$ alone.
   The open assumptions of $D_1$ are among those of the whole derivation, so nothing new is assumed.
3. In the same way, ${\wedge}$I followed by ${\wedge}$E$_2$ reduces to $D_2$.
4. Local completeness.
   Let $D$ derive $A \wedge B$, apply ${\wedge}$E$_1$ to $D$ to get $A$, and ${\wedge}$E$_2$ to a second copy of $D$ to get $B$.
5. Then ${\wedge}$I gives $A \wedge B$ again, with the same open assumptions as $D$.
   This is the expansion of $D$.

The derivation at the top is step 1 with $D_1$ the assumption $p$ and $D_2$ the assumption $q$, and step 2 reduces it to $p$.
The assumption $q$ disappears in the reduction, which is allowed: a reduction may drop open assumptions but never adds them.

## Remarks

Step 2 is the conjunction case of the detour reduction in the [[normalization theorem|W33WAE1XTC]].
The elimination rules take out exactly the two pieces that the introduction rule puts in.
If ${\wedge}$E$_2$ were dropped, step 1 would still work, but step 4 would fail, since no derivation could recover $B$ from $A \wedge B$.
Under the [[Curry-Howard correspondence|A77FER1Q5H]], step 2 is the reduction of the first projection of a pair, and step 5 is the eta rule for pairs.

## Explanations

### L1 human

To prove "$A$ and $B$", we prove $A$ and we prove $B$.
From "$A$ and $B$" we may conclude $A$, or $B$.
If we prove "$A$ and $B$" only to take $A$ back out, we could have stopped at the proof of $A$.
That is the balance that harmony asks for.

### L2 human

The check is mechanical: write each introduction followed by each elimination, and find the derivation without the detour.
Then apply the eliminations to a proof of the compound formula, and rebuild it with the introduction.
A trap is to forget the second check, since it is the one that fails when an elimination rule is missing.
