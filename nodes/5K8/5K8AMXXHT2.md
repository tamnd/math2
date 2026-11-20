---
tag: 5K8AMXXHT2
kind: example
name: A sentence that separates truth value sets of Gödel logics
msc: ["03B52"]
topics: [WZP584JQ06]
audience: research
instance_of: [H8C323CV3T]
sources:
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: 6.2 Many-valued first-order logics
---

## Example

Let $\sigma$ be the sentence $\exists x (P(x) \to \forall y P(y))$.
SEP notes that $\sigma$ is not valid in [[first-order Gödel logic|H8C323CV3T]] over $[0, 1]$, and that it holds in every structure with a finite domain.
We prove: $\sigma \in \mathrm{G}_V$ iff every non-empty subset of $V$ has a least element.

1. Let $\mathfrak{M}$ be a $V$-structure, let $X = \set{P^{\mathfrak{M}}(d) : d \in M}$, and let $c = \inf X$, which lies in $V$ since $V$ is closed.
2. The value of $\sigma$ is $\sup_d (P^{\mathfrak{M}}(d) \to c)$, with the Gödel implication.
3. If $X$ has a least element $P^{\mathfrak{M}}(d_0) = c$, then $c \to c = 1$, so $\sigma$ has value $1$.
4. If $X$ has no least element, then $P^{\mathfrak{M}}(d) > c$ for every $d$, so $P^{\mathfrak{M}}(d) \to c = c$.
5. Then $\sigma$ has value $c$, and $c < 1$ because $c$ is below each element of $X$.
6. If every non-empty subset of $V$ has a least element, step 3 applies to each $\mathfrak{M}$, so $\sigma \in \mathrm{G}_V$.
7. If some non-empty $Y \subseteq V$ has no least element, take $M = Y$ and $P^{\mathfrak{M}}(d) = d$; step 5 gives a value below $1$.

The table for four closed sets $V$ that contain $0$ and $1$:

| $V$ | least elements | $\sigma \in \mathrm{G}_V$ |
|---|---|---|
| finite $V$ | every non-empty subset has one | yes |
| $\set{1 - \tfrac1n : n \ge 1} \cup \set{1}$ | every non-empty subset has one | yes |
| $\set{0} \cup \set{\tfrac1n : n \ge 1}$ | $\set{\tfrac1n : n \ge 1}$ has none | no |
| $[0, 1]$ | $(0, 1]$ has none | no |

8. For the third row, $P(n) = \tfrac1n$ on $M = \set{1, 2, \dots}$ gives $c = 0$, and $\sigma$ has value $0$.
9. For the second row, $V$ has the order type $\omega + 1$, which is a well-order, so every non-empty subset has a least element.

## Remarks

1. The second and third sets are both infinite and countable, and as propositional Gödel logics they are equal.
2. So the first-order Gödel logics $\mathrm{G}_V$ are not determined by the cardinality of $V$.
3. Steps 3 and 4 also explain SEP's remark on finite domains: then $X$ is finite and has a least element.

## Explanations

### L1 human

The sentence says: some object has the least degree of $P$.
If degrees can decrease forever without reaching their limit, no object has the least degree.
Then the sentence is not fully true.

### L2 human

1. Compute the infimum $c$ of the values of $P$.
2. Check whether some object attains $c$.

A trap: the infimum $c$ is in $V$ because $V$ is closed; it need not be a value of $P$.
