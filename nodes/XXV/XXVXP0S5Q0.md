---
tag: XXVXP0S5Q0
kind: example
name: Double negation fails in Gödel and product logic
msc: ["03B52"]
topics: [WZP584JQ06]
audience: research
instance_of: [474SGS2N0X]
not_instance_of:
  - target: NFCEM44XYH
    note: the formula ¬¬p → p is a Łukasiewicz tautology but fails here
uses: [JQ713VVD0G, BHR2YXEQZT]
sources:
  - url: https://plato.stanford.edu/entries/logic-fuzzy/
    locator: 1. Fuzzy connectives based on t-norms
---

## Example

In Gödel logic on $[0, 1]$, $x \to y = 1$ if $x \le y$ and $x \to y = y$ otherwise, and $\neg x = x \to 0$.
In product logic, $x \to y = 1$ if $x \le y$ and $x \to y = y / x$ otherwise, and again $\neg x = x \to 0$.
We evaluate $\neg \neg p \to p$ at $v(p) = \tfrac12$.

1. In both logics $\neg x = 1$ if $x = 0$, and $\neg x = 0$ if $x > 0$.
2. So $v(\neg p) = 0$, since $\tfrac12 > 0$.
3. Then $v(\neg \neg p) = \neg 0 = 1$.
4. In Gödel logic $v(\neg \neg p \to p) = 1 \to \tfrac12 = \tfrac12$, since $1 > \tfrac12$.
5. In product logic $v(\neg \neg p \to p) = \tfrac12 / 1 = \tfrac12$.
6. In [[Łukasiewicz logic|JQ713VVD0G]], $\neg \neg x = 1 - (1 - x) = x$, so $\neg \neg p \to p$ has value $1$ everywhere.

So $\neg \neg p \to p$ separates both Gödel and product logic from Łukasiewicz logic.

## Remarks

The negation of Gödel and product logic is the Gödel negation of the [[Gödel chain|BHR2YXEQZT]], and it takes only the values $0$ and $1$.
The minimum and the product t-norms give the same residual negation, though their implications differ.

The formula $\neg p \lor \neg \neg p$ goes the other way.
It is a tautology of both logics, since one of its disjuncts is always $1$.
In Łukasiewicz logic it has value $\max(\tfrac12, \tfrac12) = \tfrac12$ at $p = \tfrac12$.
So the two formulas together show that neither Łukasiewicz logic nor Gödel logic contains the other.

## Explanations

### L1 human

In Gödel and product logic, "not $p$" is fully true only when $p$ is fully false.
So "not not $p$" is fully true as soon as $p$ is a little true.
Then "not not $p$ implies $p$" fails when $p$ is only half true.

### L2 human

Compute $\neg$ as $x \to 0$ for the residuum of the logic, and note that it jumps from $1$ to $0$ at $x = 0$.
Then evaluate the formula at an intermediate value, which is the usual way to separate the three basic t-norm logics by one formula.
Watch out: the negation $1 - x$ is not the residual negation of the Gödel or product t-norm, so do not mix it in.
