---
tag: QWWR80Y2XT
kind: example
name: Harmony of the implication rules
msc: ["03F03"]
topics: [R10RMQCJQX]
audience: ug2
instance_of: [XJSQVK0G71, K97KZB5R7N]
uses: [PAQ4ZX2TX1, W33WAE1XTC]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_harmony
    locator: Overview
  - url: https://en.wikipedia.org/wiki/Proof-theoretic_semantics
    locator: Philosophical motivation
---

## Example

In [[natural deduction|PAQ4ZX2TX1]], implication has the following rules.

- ${\to}$I: from a derivation of $B$ from the assumption $A$, labelled $u$, infer $A \to B$ and discharge the assumptions labelled $u$.
- ${\to}$E: from $A \to B$ and $A$ infer $B$.

We check the two conditions of [[harmony|XJSQVK0G71]].

1. Local soundness. Let $D_1$ derive $B$ from open assumptions that include some occurrences of $A$ labelled $u$, and let $D_2$ derive $A$.
2. Apply ${\to}$I to $D_1$, discharging $u$, to get $A \to B$, and then ${\to}$E with $D_2$ to get $B$.
3. This reduces to $D_1[D_2/u]$, the derivation $D_1$ with a copy of $D_2$ put above each assumption $A$ labelled $u$.
4. The open assumptions of $D_1[D_2/u]$ are those of $D_1$ other than $u$, and those of $D_2$ when $u$ labels at least one assumption. All of them are open in the derivation of step 2.
5. Local completeness. Let $D$ derive $A \to B$, and take a label $u$ that does not occur in $D$.
6. Apply ${\to}$E to $D$ and the assumption $A$ labelled $u$, to get $B$. Then ${\to}$I discharges $u$ and gives $A \to B$, with the same open assumptions as $D$.

A concrete instance shows the copying of step 3.
Let $D_1$ derive $p \wedge p$ by $\wedge$I from two assumptions $p$ labelled $u$, and let $D_2$ derive $p$ by $\wedge$E$_2$ from the assumption $q \wedge p$.
The detour derives $p \wedge p$ through $p \to p \wedge p$.
It reduces to $\wedge$I applied to two copies of $D_2$, a derivation of $p \wedge p$ from $q \wedge p$.

## Remarks

Step 3 is the detour reduction used in the [[proof of normalization|ZGZC1FDWD5]].
The copying in step 3 is why a reduction can make a derivation longer, and why normalization needs a careful induction.
If $u$ labels no assumption of $D_1$, step 3 deletes $D_2$, and the open assumptions of $D_2$ disappear.
Under the [[Curry-Howard correspondence|A77FER1Q5H]], step 3 is beta reduction, $(\lambda u.\, t)\, s \to t[s/u]$, and step 6 is eta expansion, $t \to \lambda u.\, t\, u$.

## Explanations

### L1 human

To prove "if $A$ then $B$", we assume $A$ and prove $B$.
To use "if $A$ then $B$", we need a proof of $A$, and then we get $B$.
If we prove "if $A$ then $B$" and use it at once on a proof of $A$, we could just put that proof of $A$ where we assumed $A$.

### L2 human

To reduce a detour on $A \to B$, find each assumption of $A$ that the ${\to}$I step discharged, and put the derivation of the minor premise above it.
Then remove the two rule steps.
A trap is to put the minor premise derivation only once: each discharged assumption gets its own copy.
