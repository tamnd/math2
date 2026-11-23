---
tag: KGGR81G9DV
kind: example
name: The formula "exists x for all y, P(y) implies y = x" says "at most one"
msc: ["03B10"]
topics: [PM1AYWABA7]
audience: school
not_instance_of:
  - target: 0QAJHFGZZJ
    note: the formula expresses at most one, without existence, so it is true when P has no witness at all
uses: [0QAJHFGZZJ, 0N3ADS4CHH, 0V4QXPGJQK]
sources:
  - url: https://en.wikipedia.org/wiki/Uniqueness_quantification
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 3.6
---

## Example

Let $P(x)$ be the predicate "$x^2 = -1$" on the domain $\mathbb{R}$.
Consider the formula
$$\Phi \;=\; \exists x \, \forall y \, \bigl( P(y) \to y = x \bigr).$$
It looks like the definition of the [[uniqueness quantifier|0N3ADS4CHH]], but the conjunct $P(x)$ is missing.
We show that $\Phi$ is true while $\exists! x \, P(x)$ is false.

1. For every real $y$, $y^2 \geq 0 > -1$, so $P(y)$ is false.
2. Take $x = 0$.
   For every real $y$, the implication $P(y) \to y = 0$ has a false antecedent by step 1, so it is true by [[vacuous truth|0V4QXPGJQK]].
3. So $\forall y \, (P(y) \to y = 0)$ is true, and $\Phi$ is true with the witness $0$.
4. By step 1, $\exists x \, P(x)$ is false.
   Since $\exists! x \, P(x)$ implies $\exists x \, P(x)$, the statement $\exists! x \, P(x)$ is false.
5. So $\Phi$ and $\exists! x \, P(x)$ have different truth values, and $\Phi$ is not a formula for "exactly one".

## Remarks

The formula $\Phi$ expresses "at most one $x$ has property $P$".
On every nonempty domain it is equivalent to $\forall x \, \forall y \, (P(x) \land P(y) \to x = y)$.
The table compares $\Phi$ with $\exists! x \, P(x)$ by the size of the truth set of $P$.

| truth set of $P$ | $\Phi$ | $\exists! x \, P(x)$ |
|---|---|---|
| empty | T | F |
| one element | T | T |
| two or more elements | F | F |

The two formulas differ only when the truth set is empty, as in this example.
Adding the conjunct $P(x)$ inside the quantifier, or the conjunct $\exists x \, P(x)$ outside, repairs the formula.

## Explanations

### L1 human

"At most one student in the class has a red bicycle" is true when nobody has a red bicycle.
"Exactly one student has a red bicycle" is false in that case.
So "at most one" and "exactly one" are different claims.
The formula $\Phi$ says only "at most one", because it never says that someone has the property.

### L2 human

To test whether a formula expresses "exactly one", evaluate it on three predicates over $\mathbb{R}$, with empty, one-element and two-element truth sets.
For "$x^2 = -1$", the truth set is empty, and $\Phi$ is true while "exactly one" is false.
For "$x = 5$", the truth set is $\{5\}$, and $\Phi$ is true with $x = 5$, as is "exactly one".
For "$x^2 = 1$", the truth set is $\{1, -1\}$, and for any $x$ one of $y = 1$ and $y = -1$ differs from $x$, so $\Phi$ is false, as is "exactly one".
The formula fails the first test, so it is wrong.
Watch out: most wrong formulas give the right answer on the one-element case, so testing only that case proves nothing.
