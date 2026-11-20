---
tag: ZJX7P6TVG9
kind: example
name: The nilpotent minimum refutes divisibility
msc: ["03B52"]
topics: [WZP584JQ06]
audience: grad
instance_of: [PT5PHKJDYM]
not_instance_of:
  - target: 3AQ5GHTXA4
    note: the divisibility axiom BL4 has the value 0.7 at A = 0.3, B = 0.4
uses: [BHGCVPAJW0, D1R4D2HEPP, FQZ04D0HH3]
sources:
  - url: https://en.wikipedia.org/wiki/T-norm
    locator: Prominent examples; Residua of common left-continuous t-norms
  - url: https://en.wikipedia.org/wiki/T-norm_fuzzy_logics
    locator: lead
---

## Example

The *nilpotent minimum* is the [[t-norm|BHGCVPAJW0]] $x * y = \min(x, y)$ if $x + y > 1$, and $x * y = 0$ otherwise.
Wikipedia gives it as the standard example of a t-norm that is left-continuous and not continuous.
Its residuum is $x \Rightarrow y = 1$ if $x \le y$, and $\max(1 - x, y)$ otherwise.

1. Discontinuity: $0.5 * 0.5 = 0$, since $0.5 + 0.5 = 1$ is not $> 1$.
   But $(0.5 + \varepsilon) * 0.5 = 0.5$ for every $\varepsilon > 0$, so $*$ jumps on the line $x + y = 1$.
2. Check of the residuum at $x = 0.4$, $y = 0.3$: for $z > 0.6$, $z * 0.4 = 0.4 > 0.3$; for $z \le 0.6$, $z * 0.4 = 0 \le 0.3$.
   So the largest $z$ with $z * 0.4 \le 0.3$ is $0.6 = \max(1 - 0.4, 0.3)$.
3. Divisibility fails: $0.4 * (0.4 \Rightarrow 0.3) = 0.4 * 0.6 = 0$, since $0.4 + 0.6 = 1$.
   But $\min(0.4, 0.3) = 0.3 \ne 0$.
4. The axiom BL4 at $A = 0.3$, $B = 0.4$: $A \Rightarrow B = 1$, so $A * (A \Rightarrow B) = 0.3$.
5. Also $B \Rightarrow A = 0.6$ by step 2, and $B * (B \Rightarrow A) = 0$ by step 3.
6. So BL4 has the value $0.3 \Rightarrow 0 = \max(1 - 0.3, 0) = 0.7 < 1$.

So the standard algebra of the nilpotent minimum is a model of [[MTL|PT5PHKJDYM]] and not a model of [[BL|FQZ04D0HH3]].

## Remarks

1. The nilpotent minimum has a residuum because it is left-continuous; see [[the left-continuity statement|D1R4D2HEPP]].
2. Its negation is $x \Rightarrow 0 = 1 - x$ for every $x$, so $\neg \neg x = x$.
3. Wikipedia names the nilpotent minimum logic among the important t-norm fuzzy logics.
4. Despite its name, the nilpotent minimum is not a nilpotent t-norm, as Wikipedia notes.

## Explanations

### L1 human

The nilpotent minimum acts like the minimum when the two inputs are large together.
When their sum is at most $1$, it gives $0$.
This jump breaks the law "$x$ and ($x$ implies $y$) equals the smaller of $x$ and $y$".

### L2 human

1. Find a pair with $x > y$ where $x + (x \Rightarrow y) \le 1$.
2. Then $x * (x \Rightarrow y) = 0$, which is below $\min(x, y)$ when $y > 0$.

A trap: the residuum is still well defined, so MTL is sound here; only the BL axiom of divisibility fails.
