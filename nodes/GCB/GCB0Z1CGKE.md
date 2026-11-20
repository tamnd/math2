---
tag: GCB0Z1CGKE
kind: example
name: The liar sentence as a dialetheia in LP
msc: ["03B53", "03A05"]
topics: [NJB94B39QK]
audience: ug2
instance_of: [3P0FM0AQF3]
uses: [3P0FM0AQF3, DYAB23WA1X, W28EY7C3FA, WH94DG6D3Q]
sources:
  - url: https://plato.stanford.edu/entries/dialetheism/
    locator: Dialetheism (SEP entry), section 3.2
  - book: isbn:9780521670265
---

## Example

Take a propositional language with the connectives of the [[logic of paradox|W28EY7C3FA]] and one extra sentence letter $\lambda$, read as the [[liar sentence|DYAB23WA1X]] "$\lambda$ is not true".
Add a sentence $T\lambda$, read "$\lambda$ is true".
A valuation $v$ *respects truth* when $v(T\lambda) = v(\lambda)$, and it *respects the liar* when $v(\lambda) = v(\neg T\lambda)$.

1. Let $v$ respect truth and the liar, and put $a = v(\lambda)$.
2. Then $a = v(\neg T\lambda) = 1 - v(T\lambda) = 1 - a$.
3. So $2a = 1$ and $a = \tfrac12$.
4. Conversely, $v(\lambda) = v(T\lambda) = \tfrac12$ respects truth and the liar, since $1 - \tfrac12 = \tfrac12$.

So there is exactly one value for the liar, and it is $\mathsf{B}$.
Since $\tfrac12$ is designated, $\lambda$ and $\neg\lambda$ are both designated.
So $\lambda$ is a [[dialetheia|3P0FM0AQF3]], a [[truth-value glut|WH94DG6D3Q]].

Under the same valuation, give another letter $q$ the value $0$.
Then $\lambda, \neg\lambda$ are designated and $q$ is not, so the liar does not make every sentence true.

## Remarks

In classical logic the equation $a = 1 - a$ has no solution in $\set{0, 1}$, which is the liar paradox in this setting.
In K3 the solution $a = \tfrac12$ also exists, but it is read as a gap: $\lambda$ and $\neg\lambda$ are both undesignated.
The strengthened liar "$\lambda'$ is not designated" is not expressible here, because "not designated" is not a function of the strong Kleene tables; this is how LP avoids that revenge sentence.
A full theory needs a truth predicate for all sentences; the one-sentence case shows the key step.

## Explanations

### L1 human

The liar says of itself that it is not true.
If it has value true, it must have value false, and the reverse.
LP has a third value "both", and the negation of "both" is "both".
So the liar can consistently have the value "both".

### L2 human

The whole example is the equation $a = 1 - a$.
Over $\set{0, 1}$ it has no solution; over $\set{0, \tfrac12, 1}$ it has the single solution $\tfrac12$.
A trap is to think that the dialetheist "chooses" the value $\mathsf{B}$; the two conditions force it.
