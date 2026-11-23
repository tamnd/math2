---
tag: 1PMN1CASZG
kind: example
name: A McNaughton function and its Łukasiewicz formula
msc: ["03B50"]
topics: [WZP584JQ06]
audience: research
instance_of: [NFCEM44XYH]
illustrates: [E11A9H8Z7Q]
uses: [JQ713VVD0G]
sources:
  - url: https://plato.stanford.edu/entries/logic-fuzzy/
    locator: 3. Łukasiewicz logic
---

## Example

Let $f(x) = \lvert 2x - 1 \rvert$ on $[0, 1]$.
It is continuous, and its two pieces $2x - 1$ and $1 - 2x$ have integer coefficients.
So [[McNaughton's theorem|E11A9H8Z7Q]] promises a formula of [[Łukasiewicz logic|JQ713VVD0G]] that defines it.
We check that $(p \odot p) \oplus (\neg p \odot \neg p)$ is such a formula.

1. The first part has the value $x \odot x = \max(0, 2x - 1)$.
2. The second part has the value $(1 - x) \odot (1 - x) = \max(0, 1 - 2x)$.
3. For $x \ge \tfrac12$, the first value is $2x - 1$ and the second is $0$.
4. For $x \le \tfrac12$, the first value is $0$ and the second is $1 - 2x$.
5. So the two values add up to $\lvert 2x - 1 \rvert$, which is at most $1$.
   The cut of $\oplus$ at $1$ never acts, and the formula defines $f$.

Check at $x = 0.3$: we get $0.3 \odot 0.3 = 0$ and $0.7 \odot 0.7 = 0.4$, so the formula has the value $0.4$, and $\lvert 0.6 - 1 \rvert = 0.4$.

## Remarks

The example shows the shape of McNaughton's theorem in one variable.
Each linear piece with integer coefficients comes from a short formula, and the pieces are glued with $\oplus$ or $\max$.
Two simpler cases are $x \oplus x = \min(1, 2x)$ and $\neg x \odot y = \max(0, y - x)$.

Change one coefficient and the formula disappears.
The function $g(x) = x / 2$ is continuous and linear, but its slope $\tfrac12$ is not an integer, so no formula defines it.
In fact no formula in one variable has a value strictly between $0$ and $1$ at $x = 1$, because the operations keep $\{0, 1\}$ closed.

The function $f$ takes the value $1$ at $0$ and at $1$.
So its formula is a classical tautology, but it is not a Łukasiewicz tautology, since $f(\tfrac12) = 0$.

## Explanations

### L1 human

The graph of $\lvert 2x - 1 \rvert$ is a V shape with its tip at $x = \tfrac12$.
The formula builds the right arm with $p \odot p$ and the left arm with $\neg p \odot \neg p$.
Then it adds the two arms, and at each point only one of them is nonzero.

### L2 human

The method has three steps.
First split the function at the points where its pieces meet.
Then find, for each piece, a formula that gives the piece where it is active and $0$ elsewhere.
Finally join these formulas with $\oplus$ when they are never nonzero at the same point, and with $\max$ in general.
Watch out: $\oplus$ cuts at $1$, so joining overlapping pieces with $\oplus$ can give a wrong value.
For example, $x \oplus x$ is $1$ at $x = 0.7$, while $\max(x, x) = 0.7$, so $\max$ is the safe join.
