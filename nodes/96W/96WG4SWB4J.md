---
tag: 96WG4SWB4J
kind: example
name: Functorial promotion in elementary linear logic
msc: ["03F52", "68Q15"]
topics: [98QF5J4W16]
audience: research
instance_of: [E7JVJSSWBT]
uses: [H408H4WHBA]
sources:
  - url: https://plato.stanford.edu/entries/logic-linear/
    locator: 6.1 Different treatments of modality
    note: Di Cosmo and Miller, Linear Logic, Stanford Encyclopedia of Philosophy, revision of 2023-09-16
  - doi: 10.1006/inco.1998.2700
    locator: pages 175-204
    note: Girard, Light Linear Logic, Information and Computation 143 (1998)
---

## Example

In elementary linear logic (ELL), the formula $!(A \multimap B) \multimap (!A \multimap !B)$ is derivable.
In one-sided form it is $?(A \otimes B^{\perp}) \mathbin{\wp} (?A^{\perp} \mathbin{\wp} !B)$, since $(A \multimap B)^{\perp} = (A^{\perp} \mathbin{\wp} B)^{\perp} = A \otimes B^{\perp}$.

1. $\vdash A^{\perp}, A$ and $\vdash B^{\perp}, B$ are axioms.
2. The rule $\otimes$ on $A$ and $B^{\perp}$ gives $\vdash A^{\perp}, A \otimes B^{\perp}, B$.
3. Functorial promotion, with $\Gamma = A^{\perp}, A \otimes B^{\perp}$ and main formula $B$, gives $\vdash ?A^{\perp}, ?(A \otimes B^{\perp}), !B$.
4. The rule $\mathbin{\wp}$ on $?A^{\perp}$ and $!B$ gives $\vdash ?(A \otimes B^{\perp}), ?A^{\perp} \mathbin{\wp} !B$.
5. The rule $\mathbin{\wp}$ again gives the formula.

## Remarks

The derivation uses functorial promotion once and no dereliction, so it is a derivation of ELL.
In full [[linear logic|H408H4WHBA]], the same formula is derived with dereliction on $A^{\perp}$ and on $A \otimes B^{\perp}$ before the ordinary promotion.
The formula says that $!$ is a functor: a map from $A$ to $B$, available without limit, gives a map from $!A$ to $!B$.

## Explanations

### L1 human

If we may use a machine that turns $A$ into $B$ as often as we like, then from as many $A$ as we like we get as many $B$ as we like.
The derivation proves this with one rule that adds "!" and "?" together.

### L2 human

We derive the same formula in full linear logic, to compare.

1. Steps 1 and 2 are the same: $\vdash A^{\perp}, A \otimes B^{\perp}, B$.
2. Dereliction on $A^{\perp}$ and on $A \otimes B^{\perp}$ gives $\vdash ?A^{\perp}, ?(A \otimes B^{\perp}), B$.
3. Promotion gives $\vdash ?A^{\perp}, ?(A \otimes B^{\perp}), !B$, since the context has only formulas with $?$.
4. Two $\mathbin{\wp}$ rules finish as before.

The typical use of this example is to see that functorial promotion is derivable in linear logic, with two derelictions and one promotion.
A trap: functorial promotion adds $?$ to every formula of the context, so it cannot be used to keep part of the context without $?$.
