---
tag: 7R2JBNNMT5
kind: statement
role: proposition
name: Residua of the Łukasiewicz, Gödel and product t-norms
aliases: [residua-of-basic-t-norms]
msc: ["03B52"]
topics: [WZP584JQ06]
audience: grad
about: [VR6D8JXX1W]
uses: [BHGCVPAJW0]
proofs: [Y8EQM4QS3D]
sources:
  - url: https://plato.stanford.edu/entries/logic-fuzzy/
    locator: 1. Fuzzy connectives based on t-norms
  - url: https://en.wikipedia.org/wiki/T-norm
    locator: Residua of common left-continuous t-norms
---

## Statement

For $x, y \in [0, 1]$, the three basic [[t-norms|BHGCVPAJW0]] have these residua:

1. Łukasiewicz: $x \Rightarrow_{Ł} y = \min(1, 1 - x + y)$;
2. Gödel: $x \Rightarrow_{G} y = 1$ if $x \le y$, and $y$ if $x > y$;
3. product (Goguen): $x \Rightarrow_{\Pi} y = 1$ if $x \le y$, and $y / x$ if $x > y$.

So the residual negations are $\neg_{Ł} x = 1 - x$, and $\neg_{G} x = \neg_{\Pi} x = 1$ if $x = 0$, else $0$.

## Remarks

### Why each hypothesis is needed

1. The formulas depend on the t-norm.
   The residuum of the nilpotent minimum is $\max(1 - x, y)$ for $x > y$, by Wikipedia; it differs from all three.
2. The proof lets $z$ range over all of $[0, 1]$.
   On the chain $\set{0, \tfrac13, \tfrac23, 1}$ the product is not even an operation, since $\tfrac13 \cdot \tfrac23 = \tfrac29$.

### Consequences

1. In all three cases $x \Rightarrow y = 1$ iff $x \le y$, and $1 \Rightarrow y = y$.
2. Only the Łukasiewicz residuum is continuous; the Gödel residuum jumps on the line $y = x < 1$, and the product residuum jumps at $(0, 0)$.
3. The minimum and the product t-norms give the same negation, as SEP notes, so $\neg \neg p \to p$ fails in both; see [[the double negation example|XXVXP0S5Q0]].

### Converse

A residuum determines its t-norm: $x * y = \min \set{z : x \le y \Rightarrow z}$.
So the three implications also determine the three conjunctions.

### Generalizations

Every left-continuous t-norm has a residuum, given by $x \Rightarrow y = \max \set{z : z * x \le y}$; see [[the left-continuity statement|D1R4D2HEPP]].
Wikipedia gives a formula for the residuum of an ordinal sum in terms of the residua of its summands.

## History

SEP lists the three residua together; Wikipedia calls the product residuum the Goguen implication.

## Explanations

### L1 human

An implication between degrees of truth should be fully true when the first degree is at most the second.
When the first degree is bigger, each logic measures the drop in its own way.
Łukasiewicz measures the difference, Gödel keeps the lower value, and the product logic takes the ratio.

### L2 human

To find $x \Rightarrow y$, find the largest $z$ with $z * x \le y$.
For example, at $x = 0.7$, $y = 0.4$: Łukasiewicz gives $0.7$, Gödel gives $0.4$, and product gives $4/7$.
A trap: for Gödel and product, $\neg x$ is $0$ for all $x > 0$, not $1 - x$.

### L3 human

The residuum is the right adjoint of $z \mapsto z * x$ in the poset $[0, 1]$.
So it exists iff $z \mapsto z * x$ preserves all suprema, which for a monotone map on $[0, 1]$ means left-continuity.
