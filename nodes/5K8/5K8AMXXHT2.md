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
It is not valid in [[first-order Gödel logic|H8C323CV3T]] over $[0, 1]$, and it holds in every structure with a finite domain.
We prove that $\sigma \in \mathrm{G}_V$ holds exactly when every nonempty subset of $V$ has a least element.

1. Let $\mathfrak{M}$ be a $V$-structure, let $X = \{ P^{\mathfrak{M}}(d) : d \in M \}$, and let $c = \inf X$.
   It lies in $V$ since $V$ is closed.
2. The value of $\sigma$ is $\sup_d (P^{\mathfrak{M}}(d) \to c)$, with the Gödel implication.
3. If $X$ has a least element $P^{\mathfrak{M}}(d_0) = c$, then $c \to c = 1$, so $\sigma$ has value $1$.
4. If $X$ has no least element, then $P^{\mathfrak{M}}(d) > c$ for every $d$, so $P^{\mathfrak{M}}(d) \to c = c$.
5. Then $\sigma$ has value $c$, and $c < 1$ because $c$ is below each element of $X$.
6. If every nonempty subset of $V$ has a least element, step 3 applies to each $\mathfrak{M}$, so $\sigma \in \mathrm{G}_V$.
7. If some nonempty $Y \subseteq V$ has no least element, take $M = Y$ and $P^{\mathfrak{M}}(d) = d$.
   Then step 5 gives a value below $1$.

The table covers four closed sets $V$ that contain $0$ and $1$.

| $V$ | least elements | $\sigma \in \mathrm{G}_V$ |
|---|---|---|
| finite $V$ | every nonempty subset has one | yes |
| $\{ 1 - \tfrac1n : n \ge 1 \} \cup \{ 1 \}$ | every nonempty subset has one | yes |
| $\{ 0 \} \cup \{ \tfrac1n : n \ge 1 \}$ | $\{ \tfrac1n : n \ge 1 \}$ has none | no |
| $[0, 1]$ | $(0, 1]$ has none | no |

8. For the third row, $P(n) = \tfrac1n$ on $M = \{ 1, 2, \dots \}$ gives $c = 0$, and $\sigma$ has value $0$.
9. For the second row, $V$ has the order type $\omega + 1$, which is a well order, so every nonempty subset has a least element.

## Remarks

The second and third sets are both infinite and countable, and as propositional Gödel logics they are equal.
So the first-order Gödel logics $\mathrm{G}_V$ are not determined by the cardinality of $V$.
Steps 3 and 4 also explain why $\sigma$ holds on finite domains: then $X$ is finite and has a least element.

## Explanations

### L1 human

The sentence says that some object has the least degree of $P$.
If degrees can decrease forever without reaching their limit, no object has the least degree.
Then the sentence is not fully true.

### L2 human

Compute the infimum $c$ of the values of $P$, and check whether some object attains it.
If one does, $\sigma$ has value $1$, and if none does, $\sigma$ has value $c$.
Watch out: the infimum $c$ is in $V$ because $V$ is closed, but it need not be a value of $P$.
