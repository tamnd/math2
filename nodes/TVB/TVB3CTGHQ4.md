---
tag: TVB3CTGHQ4
kind: example
name: A classical natural deduction derivation of a quantifier law
msc: ["03F03", "03B10"]
topics: [TTCRX3NFNY]
audience: ug2
instance_of: [6KT3BJZ7D1]
uses: [PAQ4ZX2TX1, Q11N8X99FK]
sources:
  - url: https://en.wikipedia.org/wiki/Natural_deduction
    locator: First and higher-order extensions
  - book: isbn:9781447145578
    locator: Chapter 3
---

## Example

We derive $\neg \forall x\, P(x) \to \exists x\, \neg P(x)$ with no open assumptions, by the rules of [[natural deduction|PAQ4ZX2TX1]].
In words: if not everything has $P$, then something lacks $P$.
Recall that $\neg \varphi$ abbreviates $\varphi \to \bot$.
We write the tree as a list of its nodes, each with its rule and premises.

1. $[\neg \forall x\, P(x)]^1$ is an assumption with label 1.
2. $[\neg \exists x\, \neg P(x)]^2$ is an assumption with label 2.
3. $[\neg P(y)]^3$ is an assumption with label 3.
4. $\exists x\, \neg P(x)$ follows by ${\exists}\mathrm{I}$ from line 3, with $\varphi = \neg P(x)$ and the term $y$.
5. $\bot$ follows by ${\to}\mathrm{E}$ from lines 4 and 2, because line 2 is $\exists x\, \neg P(x) \to \bot$.
6. $P(y)$ follows by RAA from line 5, which discharges label 3.
7. $\forall x\, P(x)$ follows by ${\forall}\mathrm{I}$ from line 6.
   The open assumptions are now lines 1 and 2, which are sentences, so $y$ is not free in them, and $y$ is not free in $\forall x\, P(x)$.
8. $\bot$ follows by ${\to}\mathrm{E}$ from lines 7 and 1.
9. $\exists x\, \neg P(x)$ follows by RAA from line 8, which discharges label 2.
10. $\neg \forall x\, P(x) \to \exists x\, \neg P(x)$ follows by ${\to}\mathrm{I}$ from line 9, which discharges label 1.

No assumption is open, so $\vdash_{\mathsf{ND}} \neg \forall x\, P(x) \to \exists x\, \neg P(x)$.

## Remarks

### Why the classical rule is needed

The derivation uses RAA twice, and no derivation without RAA exists, because the formula is not a theorem of [[intuitionistic logic|Q11N8X99FK]].
Intuitionistically, "not every $x$ has $P$" gives no method to find an $x$ without $P$.
The converse $\exists x\, \neg P(x) \to \neg \forall x\, P(x)$ needs no classical rule.
Assume $\exists x\, \neg P(x)$ and $\forall x\, P(x)$, take the leaf $\neg P(y)$ for ${\exists}\mathrm{E}$, get $P(y)$ by ${\forall}\mathrm{E}$ and then $\bot$, and close the assumptions.

### The order of the steps matters

Line 6 must come before line 7.
If we tried ${\forall}\mathrm{I}$ while the assumption $\neg P(y)$ of line 3 was still open, the eigenvariable $y$ would be free in an open assumption, and the step would be wrong.
RAA at line 6 closes that assumption first, so the generalization is correct.

## Explanations

### L1 human

The formula says: "if not every object has property $P$, then some object lacks $P$".
The derivation argues by contradiction twice.
Suppose that no object lacks $P$.
Then each object has $P$, so every object has $P$, against the hypothesis.
So some object lacks $P$, although the argument does not tell us which one.

### L2 human

The plan of the derivation follows the goals.

1. To prove the implication, assume $\neg \forall x\, P(x)$.
2. The goal $\exists x\, \neg P(x)$ has no direct proof, so assume its negation and aim for $\bot$.
3. To reach $\bot$ from line 1, prove $\forall x\, P(x)$, so prove $P(y)$ for a new $y$.
4. Prove $P(y)$ by contradiction: from $\neg P(y)$ get $\exists x\, \neg P(x)$, which contradicts the assumption of step 2.

This is the typical classical use of RAA: when no introduction rule fits the goal, assume its negation.
Watch out: apply ${\forall}\mathrm{I}$ only after the assumption $\neg P(y)$ is discharged.
