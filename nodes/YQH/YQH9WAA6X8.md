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

1. $S_1$ is true. For $x \in \mathbb{N} = \{0, 1, 2, \dots\}$ the consequent $x \ge 0$ holds. For $x \notin \mathbb{N}$ the antecedent is false, so the [[implication|0NMG7W7Q11]] is true.
2. $S_2$ is false. Take $x = -1$. Then $x \in \mathbb{N}$ is false, so the [[conjunction|025YZN3VJW]] $x \in \mathbb{N} \land x \ge 0$ is false, and $x = -1$ is a counterexample.
3. The instance $x = \frac{1}{2}$ also refutes $S_2$, although $\frac{1}{2} \ge 0$: the first conjunct fails.
4. So $S_1$ and $S_2$ have different truth values, and $S_2$ is not a form of the statement "every natural number is at least $0$".
5. $S_2$ says something else: every real number is a natural number and is at least $0$.

## Remarks

The example shows why the restricted universal quantifier uses $\to$ and not $\land$.
With $\to$, the elements outside $\mathbb{N}$ give true instances and do not matter.
With $\land$, every element of the domain must belong to $\mathbb{N}$, which is a different claim.

If the domain of discourse is $\mathbb{N}$ itself, then $x \in \mathbb{N}$ is true for each $x$, and $S_1$ and $S_2$ are both true and equivalent.
The difference appears only when the domain is larger than the restricting set.
The mirror error for the existential quantifier, $\to$ in place of $\land$, is on the page [[the formula "there is x with x natural implies x negative" is not a restricted existential statement|RKBRXZ5FPE]].

## Explanations

### L1 human

"Every natural number is at least $0$" talks only about natural numbers.
It is true, and other numbers such as $-1$ are not its business.
The formula with "and" says "every number is natural and at least $0$".
That claim is about all numbers, and $-1$ breaks it.
So the word "and" changes the meaning.

### L2 human

We translate "every positive real number has a square root in $\mathbb{R}$" with the domain $\mathbb{R}$.

1. The restricting condition is $x > 0$, and the property is $\exists y \, (y^2 = x)$.
2. The restricted form is $\forall x \, (x > 0 \to \exists y \, (y^2 = x))$. It is true, with $y = \sqrt{x}$.
3. The form with $\land$ is $\forall x \, (x > 0 \land \exists y \, (y^2 = x))$. It is false: $x = -1$ is not positive.

The typical use of this check is the translation of a sentence with "every" into logical form, as on the page [[translating statements into logical form|WGZX7GV3PP]].
A trap is that "and" sounds natural in the English sentence "for all $x$ that are natural and ...", but the logical form needs "if ..., then".
