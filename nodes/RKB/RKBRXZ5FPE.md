---
tag: RKBRXZ5FPE
kind: example
name: The formula "there is x with x natural implies x negative" is not a restricted existential statement
msc: ["03B10", "97E30"]
topics: [PM1AYWABA7]
audience: school
not_instance_of:
  - target: 0MSRQHCNN9
    note: the formula uses an implication in place of the conjunction of the restricted existential quantifier, so any real number outside N makes it true and it does not express the statement there is x in N with x negative
uses: [0MSRQHCNN9, 0JW2FHW7G3, 025YZN3VJW, 0NMG7W7Q11, 0V4QXPGJQK]
sources:
  - url: https://en.wikipedia.org/wiki/Existential_quantification
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 2.2
---

## Example

Let the domain of discourse be $\mathbb{R}$.
Compare the restricted [[existential statement|0JW2FHW7G3]]
$$S_1: \quad \exists x \in \mathbb{N} \; (x < 0), \quad \text{that is,} \quad \exists x \, (x \in \mathbb{N} \land x < 0),$$
with the formula
$$S_2: \quad \exists x \, (x \in \mathbb{N} \to x < 0).$$
We show that $S_2$ does not express the restricted statement $S_1$.

1. $S_1$ is false.
   For $x \in \mathbb{N} = \{0, 1, 2, \dots\}$ we have $x \ge 0$, so the second conjunct is false, and for $x \notin \mathbb{N}$ the first conjunct is false.
   So every instance of the [[conjunction|025YZN3VJW]] is false.
2. $S_2$ is true.
   For $x = -\frac{1}{2}$, the antecedent $x \in \mathbb{N}$ is false, so the [[implication|0NMG7W7Q11]] $x \in \mathbb{N} \to x < 0$ is true, and $x = -\frac{1}{2}$ is a witness.
3. The instance $x = \frac{1}{2}$ also makes $S_2$ true, although $\frac{1}{2} < 0$ is false, because the implication is [[vacuously true|0V4QXPGJQK]].
4. So $S_1$ and $S_2$ have different truth values, and $S_2$ is not a form of "some natural number is negative".
   What $S_2$ says is that some real number is not natural or is negative.

## Remarks

The restricted existential quantifier uses $\land$ and not $\to$ for exactly this reason.
With $\land$, a witness must lie in $\mathbb{N}$ and have the property.
With $\to$, every element outside $\mathbb{N}$ is a witness, so the formula is true for almost any property once the domain is larger than $\mathbb{N}$.

If the domain of discourse is $\mathbb{N}$ itself, then $x \in \mathbb{N}$ is true for each $x$, and $S_1$ and $S_2$ are both false and equivalent.
The mirror error for the universal quantifier, $\land$ in place of $\to$, is in [[the formula "for all x, x is natural and x is at least 0" is not a restricted universal statement|YQH9WAA6X8]].

## Explanations

### L1 human

"Some natural number is negative" is false, because $0, 1, 2, \dots$ are all at least $0$.
The formula with "if ... then" says "there is a number such that, if it is natural, then it is negative".
The number $-\frac{1}{2}$ is not natural, so the "if" part fails, and the sentence about it counts as true.
So the formula with "if ... then" is true, and it cannot mean the same as the false statement.

### L2 human

Translate "some prime number is even" with the domain $\mathbb{N}$.
The restricting condition is "$x$ is prime", and the property is "$x$ is even".
The restricted form $\exists x \, (x \text{ is prime} \land x \text{ is even})$ is true, with the witness $2$.
The form $\exists x \, (x \text{ is prime} \to x \text{ is even})$ is also true, but for a wrong reason: $x = 4$ is not prime, so the implication holds at $4$.
Replace "even" by "strictly between $100$ and $101$", and the form with $\land$ becomes false, while the form with $\to$ stays true at $x = 4$.
This check belongs to every translation of a sentence with "some", as in [[translating statements into logical form|WGZX7GV3PP]].
Watch out: a formula with $\to$ directly under $\exists$ is almost always true, and so it says almost nothing.
