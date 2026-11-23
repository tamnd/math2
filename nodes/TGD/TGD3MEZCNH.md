---
tag: TGD3MEZCNH
kind: example
name: The three basic t-norms and their residua at 0.7 and 0.4
msc: ["03B52"]
topics: [WZP584JQ06]
audience: grad
instance_of: [VR6D8JXX1W]
illustrates: [7R2JBNNMT5]
uses: [BHGCVPAJW0]
sources:
  - url: https://plato.stanford.edu/entries/logic-fuzzy/
    locator: 1. Fuzzy connectives based on t-norms
  - url: https://en.wikipedia.org/wiki/T-norm
    locator: Prominent examples; Residua of common left-continuous t-norms
---

## Example

Let $x = 0.7$ and $y = 0.4$.
We compute, for the three basic [[t-norms|BHGCVPAJW0]], the conjunction, the residuum in both directions, the negation and the t-conorm.

1. The three conjunctions are computed below.
   $$0.7 \odot 0.4 = \max(0, 1.1 - 1) = 0.1, \qquad \min(0.7, 0.4) = 0.4, \qquad 0.7 \cdot 0.4 = 0.28.$$
2. So $0.1 \le 0.28 \le 0.4$, as the pointwise order Łukasiewicz, product, minimum requires.
3. The residua at $x > y$ come from [[the residua statement|7R2JBNNMT5]].
   $$0.7 \Rightarrow_{Ł} 0.4 = \min(1, 1 - 0.7 + 0.4) = 0.7, \qquad 0.7 \Rightarrow_{G} 0.4 = 0.4, \qquad 0.7 \Rightarrow_{\Pi} 0.4 = \tfrac{0.4}{0.7} = \tfrac47.$$
4. Check the product residuum: $\tfrac47 \cdot 0.7 = 0.4$, and every $z > \tfrac47$ gives $z \cdot 0.7 > 0.4$.
5. In the other direction, $0.4 \Rightarrow 0.7 = 1$ for all three t-norms, since $0.4 \le 0.7$.
6. The negations of $0.7$ are $1 - 0.7 = 0.3$ for Łukasiewicz, and $0$ for Gödel and product, since $0.7 > 0$.
7. The t-conorms are $\min(1, 1.1) = 1$ for Łukasiewicz, $\max(0.7, 0.4) = 0.7$ for Gödel, and $0.7 + 0.4 - 0.28 = 0.82$ for product.

## Remarks

The numbers show a pattern.
Combine $x$ with $x \Rightarrow y$ by the same t-norm, and in all three cases you get back $\min(x, y) = 0.4$.

$$0.7 \odot 0.7 = 0.4, \qquad \min(0.7, 0.4) = 0.4, \qquad 0.7 \cdot \tfrac47 = 0.4.$$

This is divisibility, and it holds for every continuous t-norm, as [[the divisibility example|E1M4RTRAVS]] proves.

Notice also that the residuum is largest for Łukasiewicz and smallest for Gödel here.
A smaller t-norm makes $z * x$ smaller, so more values of $z$ satisfy $z * x \le y$, and the maximum $z$ is larger.
If $y$ is raised to $0.7$, all three residua become $1$, and the differences between the logics disappear.

## Explanations

### L1 human

The same two degrees, $0.7$ and $0.4$, give three different answers for "and": $0.1$, $0.4$ and $0.28$.
They also give three different answers for "if $0.7$ then $0.4$": $0.7$, $0.4$ and about $0.57$.
Each fuzzy logic picks one rule and keeps it.

### L2 human

The computation has three steps.
First, compute the t-norm from its formula.
Second, for the residuum at $x > y$, solve $z * x \le y$ for the largest $z$.
Third, for the negation, put $y = 0$ in the residuum.
Watch out: the product residuum is $y / x$, not $x / y$ and not $y - x$.
With $x / y$ you would get $1.75$, which is not even a truth value.
