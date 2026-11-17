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

We derive $\neg \forall x\, P(x) \to \exists x\, \neg P(x)$ with no open assumptions, using the rules of the [[definition|PAQ4ZX2TX1]].
Recall that $\neg \varphi$ abbreviates $\varphi \to \bot$.
We write the tree as a list of lines, each with its rule and premises.

1. $[\neg \forall x\, P(x)]^1$. Assumption with label 1.
2. $[\neg \exists x\, \neg P(x)]^2$. Assumption with label 2.
3. $[\neg P(y)]^3$. Assumption with label 3.
4. $\exists x\, \neg P(x)$. ${\exists}\mathrm{I}$ from line 3, with $\varphi = \neg P(x)$ and $t = y$.
5. $\bot$. ${\to}\mathrm{E}$ from lines 4 and 2, because line 2 is $\exists x\, \neg P(x) \to \bot$.
6. $P(y)$. RAA from line 5, which discharges label 3.
7. $\forall x\, P(x)$. ${\forall}\mathrm{I}$ from line 6. The open assumptions are lines 1 and 2, which are sentences, so $y$ is not free in them. The variable $y$ is not free in $\forall x\, P(x)$.
8. $\bot$. ${\to}\mathrm{E}$ from lines 7 and 1.
9. $\exists x\, \neg P(x)$. RAA from line 8, which discharges label 2.
10. $\neg \forall x\, P(x) \to \exists x\, \neg P(x)$. ${\to}\mathrm{I}$ from line 9, which discharges label 1.

No assumption is open, so $\vdash_{\mathsf{ND}} \neg \forall x\, P(x) \to \exists x\, \neg P(x)$.

## Remarks

The derivation uses RAA twice, and the formula has no derivation without RAA: it is not a theorem of [[intuitionistic logic|Q11N8X99FK]].
Intuitionistically, "not every $x$ has $P$" gives no method to find an $x$ without $P$.
The converse $\exists x\, \neg P(x) \to \neg \forall x\, P(x)$ has an intuitionistic derivation: from $\neg P(y)$ and $\forall x\, P(x)$, the rule ${\forall}\mathrm{E}$ gives $P(y)$ and then $\bot$.
If line 7 came before line 6, the step would be wrong: $y$ would be free in the open assumption $\neg P(y)$.

## Explanations

### L1 human

The formula says: "if not every object has property $P$, then some object lacks $P$".
The derivation argues by contradiction twice.
Assume that no object lacks $P$.
Then each object has $P$, so every object has $P$, against the hypothesis.

### L2 human

The plan of the derivation follows the goals.

1. To prove the implication, assume $\neg \forall x\, P(x)$.
2. The goal $\exists x\, \neg P(x)$ has no direct proof, so assume its negation and aim for $\bot$.
3. To reach $\bot$ from line 1, prove $\forall x\, P(x)$, so prove $P(y)$ for a new $y$.
4. Prove $P(y)$ by contradiction: from $\neg P(y)$ get $\exists x\, \neg P(x)$, which contradicts line 2.

This pattern is the typical classical use of RAA: when a goal has no introduction rule that applies, assume its negation.
A trap is to apply ${\forall}\mathrm{I}$ while the assumption $\neg P(y)$ is still open.
