---
tag: YQH9WAA6X8
kind: example
name: The formula "for all x, x is natural and x is at least 0" is not a restricted universal statement
msc: ["03B10", "97E30"]
topics: [PM1AYWABA7]
audience: school
not_instance_of:
  - target: 0GHS47PDAQ
    note: the formula uses a conjunction in place of the implication of the restricted universal quantifier, so it claims that every real number is natural and does not express the statement for all x in N
uses: [0GHS47PDAQ, 0B88PQTJ66, 025YZN3VJW, 0NMG7W7Q11]
sources:
  - url: https://en.wikipedia.org/wiki/Universal_quantification
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 2.2
---

## Example

Let the domain of discourse be $\mathbb{R}$.
Compare the restricted [[universal statement|0B88PQTJ66]]
$$S_1: \quad \forall x \in \mathbb{N} \; (x \ge 0), \quad \text{that is,} \quad \forall x \, (x \in \mathbb{N} \to x \ge 0),$$
with the formula
$$S_2: \quad \forall x \, (x \in \mathbb{N} \land x \ge 0).$$
We show that $S_2$ does not express the restricted statement $S_1$.

1. $S_1$ is true.
   For $x \in \mathbb{N} = \{0, 1, 2, \dots\}$ the consequent $x \ge 0$ holds, and for $x \notin \mathbb{N}$ the antecedent is false, so the [[implication|0NMG7W7Q11]] is true.
2. $S_2$ is false.
   Take $x = -1$: then $x \in \mathbb{N}$ is false, so the [[conjunction|025YZN3VJW]] $x \in \mathbb{N} \land x \ge 0$ is false, and $x = -1$ is a counterexample.
3. The instance $x = \frac{1}{2}$ also refutes $S_2$, although $\frac{1}{2} \ge 0$, because the first conjunct fails.
4. So $S_1$ and $S_2$ have different truth values, and $S_2$ is not a form of "every natural number is at least $0$".
   What $S_2$ says is that every real number is a natural number and is at least $0$.

## Remarks

The restricted universal quantifier uses $\to$ and not $\land$ for exactly this reason.
With $\to$, the elements outside $\mathbb{N}$ give true instances and drop out.
With $\land$, every element of the domain must belong to $\mathbb{N}$, which is a different claim.

If the domain of discourse is $\mathbb{N}$ itself, then $x \in \mathbb{N}$ is true for each $x$, and $S_1$ and $S_2$ are both true and equivalent.
The difference appears only when the domain is larger than the restricting set.
The mirror error for the existential quantifier, $\to$ in place of $\land$, is in [[the formula "there is x with x natural implies x negative" is not a restricted existential statement|RKBRXZ5FPE]].

## Explanations

### L1 human

"Every natural number is at least $0$" talks only about natural numbers.
It is true, and other numbers such as $-1$ are none of its business.
The formula with "and" says "every number is natural and at least $0$".
That claim is about all numbers, and $-1$ breaks it.
So the word "and" changes the meaning.

### L2 human

Translate "every positive real number has a square root in $\mathbb{R}$" with the domain $\mathbb{R}$.
The restricting condition is $x > 0$, and the property is $\exists y \, (y^2 = x)$.
The restricted form is
$$\forall x \, (x > 0 \to \exists y \, (y^2 = x)),$$
and it is true, with $y = \sqrt{x}$.
The form with $\land$ is $\forall x \, (x > 0 \land \exists y \, (y^2 = x))$, and it is false, because $x = -1$ is not positive.
This check belongs to every translation of a sentence with "every", as in [[translating statements into logical form|WGZX7GV3PP]].
Watch out: "and" sounds natural in "for all $x$ that are natural and ...", but the logical form needs "if ..., then".
