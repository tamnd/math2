---
tag: JVV2QRX0H2
kind: example
name: The rules of tonk
msc: ["03F03", "03A05"]
topics: [R10RMQCJQX]
audience: ug2
not_instance_of:
  - target: XJSQVK0G71
    note: tonk-I followed by tonk-E has no reduction, so the tonk rules are not locally sound
  - target: K97KZB5R7N
    note: the tonk rules cannot define a connective in proof-theoretic semantics, since adding them makes every formula derivable from every formula
uses: [QSVQ1KPNBX, PAQ4ZX2TX1, N238J43XNE]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_harmony
    locator: Overview
  - url: https://en.wikipedia.org/wiki/Proof-theoretic_semantics
    locator: Philosophical motivation
---

## Example

Prior's connective [[tonk|QSVQ1KPNBX]] is given by two rules.

- tonk-I: from $A$ infer $A \mathbin{\mathrm{tonk}} B$, for any formula $B$.
- tonk-E: from $A \mathbin{\mathrm{tonk}} B$ infer $B$.

The introduction rule is that of disjunction and the elimination rule is that of conjunction.
We show that these rules are not in [[harmony|XJSQVK0G71]].

1. In propositional [[natural deduction|PAQ4ZX2TX1]] with tonk, take the assumption $p$, apply tonk-I to get $p \mathbin{\mathrm{tonk}} q$, and apply tonk-E to get $q$.
2. This is a detour on $p \mathbin{\mathrm{tonk}} q$. A reduction, as for $\wedge$ and ${\to}$, rebuilds the conclusion from the derivations of the premises of the introduction, with no new rule steps.
3. Here the only such derivation is the assumption $p$, and its conclusion is $p$, not $q$. So the detour has no reduction.
4. Natural deduction without tonk is sound. Under the valuation with $p$ true and $q$ false, the assumption $p$ is true and $q$ is false, so the system without tonk does not derive $q$ from $p$.
5. Step 1 derives $q$ from $p$ in the extended system. So by step 4 the extension is not [[conservative|N238J43XNE]].

## Remarks

Step 4 shows more than step 3: no derivation without tonk, of any shape, can replace the detour.
Step 1 works for any formulas $A$ and $B$ in place of $p$ and $q$, so with tonk every formula is derivable from every other one.
Belnap's reply to Prior asked that the rules of a new connective give a conservative extension, and step 5 shows that tonk fails this.
Harmony is the local version of the same requirement.

## Explanations

### L1 human

Tonk is a made-up word with two rules.
To prove "$A$ tonk $B$", it is enough to prove $A$, as with "or".
From "$A$ tonk $B$" we may conclude $B$, as with "and".
Together, these rules take us from any statement to any other, so they cannot be the rules of a sensible word.

### L2 human

To see that rules are not in harmony, look for a detour whose result cannot be reached without it.
Here, the detour turns $p$ into $q$, and a truth table shows that nothing else does.
A trap is to blame each rule separately: each one is the rule of a harmless connective, and only the pair is bad.
