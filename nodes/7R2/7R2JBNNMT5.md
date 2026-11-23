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

The three basic t-norms have explicit residua, and so the three basic fuzzy logics have explicit implications and negations.

For all $x, y \in [0, 1]$, the residua of the three basic [[t-norms|BHGCVPAJW0]] are as follows.

1. Łukasiewicz: $x \Rightarrow_{Ł} y = \min(1, 1 - x + y)$.
2. Gödel: $x \Rightarrow_{G} y = 1$ if $x \le y$, and $x \Rightarrow_{G} y = y$ if $x > y$.
3. Product: $x \Rightarrow_{\Pi} y = 1$ if $x \le y$, and $x \Rightarrow_{\Pi} y = y / x$ if $x > y$.

Hence the residual negations are $\neg_{Ł} x = 1 - x$, and $\neg_{G} x = \neg_{\Pi} x$, which is $1$ for $x = 0$ and $0$ for $x > 0$.

## Remarks

### What the formulas say

At $x = 0.7$ and $y = 0.4$, the three implications give $0.7$, $0.4$ and $\tfrac47$, as [[the values example|TGD3MEZCNH]] computes.
When the antecedent is at most the consequent, all three give $1$.
When it is larger, each logic measures the drop in its own way: Łukasiewicz by the difference, Gödel by keeping the lower value, product by the ratio.
In all three cases $1 \Rightarrow y = y$, so a fully true antecedent passes its consequent through unchanged.

### Why the hypotheses matter

The formulas belong to these three t-norms, and a different t-norm has a different residuum.
For the nilpotent minimum, the residuum at $x > y$ is $\max(1 - x, y)$, which differs from all three; at $(0.4, 0.3)$ it is $0.6$.
The statement also uses the whole interval $[0, 1]$ as the range of $z$ in the residuation law.
On a finite chain such as $\{0, \tfrac13, \tfrac23, 1\}$ the product is not even an operation, since $\tfrac13 \cdot \tfrac23 = \tfrac29$ is not in the chain.

### What it gives you

Only the Łukasiewicz residuum is continuous.
The Gödel residuum jumps on the diagonal $y = x < 1$, and the product residuum jumps at $(0, 0)$, where $y / x$ takes every value in $[0, 1)$ along different paths.
The minimum and the product share their negation, so $\neg \neg p \to p$ fails in both logics, as [[the double negation example|XXVXP0S5Q0]] shows.
The formulas also give divisibility, $x * (x \Rightarrow y) = \min(x, y)$, by direct computation; see [[the divisibility example|E1M4RTRAVS]].

### The converse

A residuum determines its t-norm.
From residuation, $x * y \le z$ holds exactly when $x \le y \Rightarrow z$, so $x * y$ is the least $z$ with $x \le y \Rightarrow z$.
So each of the three implications also determines its conjunction.

### Generalizations

Every left-continuous t-norm has a residuum, given by $x \Rightarrow y = \max \{ z : z * x \le y \}$; see [[the left-continuity statement|D1R4D2HEPP]].
For any such t-norm the same method works: fix $x > y$ and solve $z * x \le y$ for the largest $z$.

## History

The Łukasiewicz implication $\min(1, 1 - x + y)$ goes back to Łukasiewicz's infinite-valued logic.
The product residuum is also called the Goguen implication.
Hájek's monograph of 1998 treated the three residua together as the implications of the three basic t-norm logics.

## Explanations

### L1 human

An implication between degrees of truth should be fully true when the first degree is at most the second.
When the first degree is bigger, the implication should say how much truth is lost.
Łukasiewicz measures the difference: "if $0.7$ then $0.4$" gets $1 - 0.3 = 0.7$.
Gödel keeps the lower value, $0.4$.
The product logic takes the ratio, $0.4 / 0.7$, about $0.57$.

### L2 human

We find the product residuum at $x = 0.5$, $y = 0.2$ from the definition.
We need the largest $z$ with $z \cdot 0.5 \le 0.2$.

$$z \cdot 0.5 \le 0.2 \iff z \le 0.4.$$

So $0.5 \Rightarrow_\Pi 0.2 = 0.4$, which is $0.2 / 0.5$ as the formula says.
Check: $0.4 \cdot 0.5 = 0.2$, and any larger $z$ gives more than $0.2$.
Watch out: for Gödel and product, $\neg x$ is $0$ for every $x > 0$, not $1 - x$.

### L3 human

The residuum is the right adjoint of the monotone map $z \mapsto z * x$ on the chain $[0, 1]$.
So it exists exactly when that map preserves all suprema, which for a monotone map on $[0, 1]$ means left-continuity.
The three formulas give the three standard algebras: the standard [[MV-algebra|8T4M7RN9AC]], the standard Gödel algebra and the standard product algebra.
These generate the varieties of the three basic fuzzy logics.
