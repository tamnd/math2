---
tag: E1M4RTRAVS
kind: example
name: Divisibility for the three basic t-norms
msc: ["03B52"]
topics: [WZP584JQ06]
audience: grad
instance_of: [3AQ5GHTXA4, PT5PHKJDYM]
uses: [BHGCVPAJW0, 7R2JBNNMT5, FQZ04D0HH3]
sources:
  - url: https://en.wikipedia.org/wiki/T-norm
    locator: Residuum; Basic properties of residua
  - url: https://en.wikipedia.org/wiki/BL_(logic)
    locator: Language; Axioms
---

## Example

Divisibility is the identity $x * (x \Rightarrow y) = \min(x, y)$, the algebraic form of the axiom BL4 of [[BL|FQZ04D0HH3]].
We check it at $x = 0.7$, $y = 0.4$ for the three basic [[t-norms|BHGCVPAJW0]], with the residua from [[the residua statement|7R2JBNNMT5]].

1. Łukasiewicz: $0.7 \Rightarrow 0.4 = \min(1, 1 - 0.7 + 0.4) = 0.7$, and $0.7 \odot 0.7 = \max(0, 1.4 - 1) = 0.4$.
2. Gödel: $0.7 \Rightarrow 0.4 = 0.4$, and $\min(0.7, 0.4) = 0.4$.
3. Product: $0.7 \Rightarrow 0.4 = 0.4 / 0.7 = \tfrac47$, and $0.7 \cdot \tfrac47 = 0.4$.
4. In each case the result is $0.4 = \min(0.7, 0.4)$.
5. For $x \le y$: $x \Rightarrow y = 1$ and $x * 1 = x = \min(x, y)$, for every t-norm.

Divisibility holds for every continuous t-norm $*$; we prove the case $x > y$.

6. Let $f(z) = x * z$ on $[0, 1]$; it is continuous, with $f(0) = 0$ and $f(1) = x$.
7. Since $0 \le y < x$, the intermediate value theorem gives $z_0$ with $f(z_0) = y$.
8. Residuation and $z_0 * x \le y$ give $z_0 \le x \Rightarrow y$, so $y = x * z_0 \le x * (x \Rightarrow y)$ by monotonicity.
9. Residuation with $z = x \Rightarrow y$ gives $(x \Rightarrow y) * x \le y$.
10. So $x * (x \Rightarrow y) = y = \min(x, y)$.

## Remarks

1. Steps 5 to 10 show that BL4 has the value $\min(x, y) \Rightarrow \min(y, x) = 1$ in every standard algebra of a continuous t-norm.
2. For a left-continuous t-norm, Wikipedia gives only the inequality $x * (x \Rightarrow y) \le \min(x, y)$, with equality when $*$ is continuous.
3. [[The nilpotent minimum|ZJX7P6TVG9]] shows that the inequality can be strict.
4. With $\land$ defined as $A \otimes (A \to B)$, divisibility says that this defined connective is the minimum.

## Explanations

### L1 human

Take $x$, then "and" it with "$x$ implies $y$".
For the three basic t-norms the result is the smaller of $x$ and $y$.
So the fuzzy rule "from $x$ and $x$ implies $y$, get $y$" loses nothing beyond $\min(x, y)$.

### L2 human

1. Compute $x \Rightarrow y$ from the residuum formula of the t-norm.
2. Combine it with $x$ by the t-norm.
3. Compare with $\min(x, y)$.

A trap: step 7 needs continuity in the second argument; for a t-norm with a jump, the value $y$ can be skipped.
