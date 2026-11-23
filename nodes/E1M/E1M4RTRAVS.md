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

1. Łukasiewicz gives $0.7 \Rightarrow 0.4 = \min(1, 1 - 0.7 + 0.4) = 0.7$, and then $0.7 \odot 0.7 = \max(0, 1.4 - 1) = 0.4$.
2. Gödel gives $0.7 \Rightarrow 0.4 = 0.4$, and then $\min(0.7, 0.4) = 0.4$.
3. Product gives $0.7 \Rightarrow 0.4 = 0.4 / 0.7 = \tfrac47$, and then $0.7 \cdot \tfrac47 = 0.4$.
4. In each case the result is $0.4 = \min(0.7, 0.4)$.
5. When $x \le y$, every t-norm has $x \Rightarrow y = 1$ and $x * 1 = x = \min(x, y)$.

Divisibility holds for every continuous t-norm $*$, and we prove the remaining case $x > y$.

6. Let $f(z) = x * z$ on $[0, 1]$.
   It is continuous, with $f(0) = 0$ and $f(1) = x$.
7. Since $0 \le y < x$, the intermediate value theorem gives $z_0$ with $f(z_0) = y$.
8. Residuation and $z_0 * x \le y$ give $z_0 \le x \Rightarrow y$, so $y = x * z_0 \le x * (x \Rightarrow y)$ by monotonicity.
9. Residuation with $z = x \Rightarrow y$ gives $(x \Rightarrow y) * x \le y$.
10. So $x * (x \Rightarrow y) = y = \min(x, y)$.

## Remarks

Steps 5 to 10 show that BL4 has value $\min(x, y) \Rightarrow \min(y, x) = 1$ in the standard algebra of every continuous t-norm.
With $\land$ defined as $A \otimes (A \to B)$, divisibility says that this defined connective is the minimum.

For a left-continuous t-norm only the inequality $x * (x \Rightarrow y) \le \min(x, y)$ survives, and it can be strict.
The [[nilpotent minimum|ZJX7P6TVG9]] at $x = 0.6$, $y = 0.3$ has $x \Rightarrow y = \max(0.4, 0.3) = 0.4$.
Then $0.6 * 0.4 = 0$, since $0.6 + 0.4$ is not above $1$, and $0 < 0.3$.
Step 7 is where continuity enters: the nilpotent minimum jumps from $0$ to $0.4$ at $z = 0.4$ in $0.6 * z$, so the value $0.3$ is skipped.

## Explanations

### L1 human

Take $x$, then "and" it with "$x$ implies $y$".
For the three basic t-norms the result is the smaller of $x$ and $y$.
So the fuzzy rule "from $x$, and $x$ implies $y$, get $y$" loses nothing beyond $\min(x, y)$.

### L2 human

To test divisibility, compute $x \Rightarrow y$ from the residuum formula, combine it with $x$ by the t-norm, and compare with $\min(x, y)$.
Only the case $x > y$ needs work, since $x \le y$ always gives $x$.
Watch out: the proof needs continuity in the second argument, and for a t-norm with a jump the value $y$ can be skipped.
