---
tag: 2PD8PPKFAQ
kind: example
name: The two forms of cut derive each other
msc: ["03F05"]
topics: [R10RMQCJQX]
audience: grad
instance_of: [HGVMPZ2DXA]
uses: [PZX9J3VEMT, DAMGTSY6VV]
sources:
  - url: https://en.wikipedia.org/wiki/Cut-elimination_theorem
    locator: The cut rule
---

## Example

In LK, the context-sharing cut is derivable from the context-splitting cut with exchange and contraction, and the context-splitting cut is derivable from the context-sharing cut with exchange and weakening.
We first do a concrete case, then the general pattern.

### A concrete case

Take $\Gamma = p$, $\Delta = p$ and the cut formula $A = q$.

1. The premises of a sharing cut are $p \Rightarrow p, q$ and $q, p \Rightarrow p$.
   Each follows from the axiom $p \Rightarrow p$ by one weakening, WR or WL.
2. A splitting cut on $q$ gives $p, p \Rightarrow p, p$.
3. One contraction on each side gives $p \Rightarrow p$, which is the conclusion of the sharing cut.

### Sharing from splitting

Let $\Gamma \Rightarrow \Delta, A$ and $A, \Gamma \Rightarrow \Delta$ be given.

1. The splitting cut, with $\Pi = \Gamma$ and $\Lambda = \Delta$, gives $\Gamma, \Gamma \Rightarrow \Delta, \Delta$.
2. Exchanges bring the two copies of each formula next to each other.
3. Contractions on both sides remove the second copies and give $\Gamma \Rightarrow \Delta$.

### Splitting from sharing

Let $\Gamma \Rightarrow \Delta, A$ and $A, \Pi \Rightarrow \Lambda$ be given.

1. Weakenings and exchanges turn the left premise into $\Gamma, \Pi \Rightarrow \Delta, \Lambda, A$.
2. Weakenings and exchanges turn the right premise into $A, \Gamma, \Pi \Rightarrow \Delta, \Lambda$.
3. The sharing cut, with the common context $\Gamma, \Pi \Rightarrow \Delta, \Lambda$, gives $\Gamma, \Pi \Rightarrow \Delta, \Lambda$.

## Remarks

The example shows that LK derives the same sequents with either form of the [[cut rule|DAMGTSY6VV]].
The translation spends structural rules: contraction in one direction, weakening in the other.

Take those rules away and the two forms come apart.
In linear logic there is no general weakening or contraction, so neither half of the translation goes through.
In Kleene's calculi G3 the structural rules are not primitive, but weakening and contraction are admissible, so the two forms again derive the same sequents.
Admissible is weaker than derivable here: the translation in G3 goes through the admissibility proofs, not through fixed rule patterns.

## Explanations

### L1 human

There are two ways to write the lemma rule.
In one, the two premises may have different assumptions, and the result collects all of them.
In the other, both premises have the same assumptions, and the result keeps them.
With the rules "you may add an assumption" and "you may drop a repeated one", each way can imitate the other.

### L2 human

To get the sharing form from the splitting form, cut first, then contract the duplicate copies of $\Gamma$ and $\Delta$.
To get the splitting form from the sharing form, first weaken both premises to the same contexts, then cut.
For $\Gamma = p$ and $\Delta = p$ the first direction turns $p, p \Rightarrow p, p$ into $p \Rightarrow p$ with two contractions.
Watch out for the exchanges: LK uses lists, so a contraction needs the two copies of a formula next to each other.
