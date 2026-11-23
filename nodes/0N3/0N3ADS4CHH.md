---
tag: 0N3ADS4CHH
kind: definition
name: Uniqueness quantifier
msc: ["03B10"]
topics: [PM1AYWABA7]
audience: school
defines: 0QAJHFGZZJ
uses: [0T3DPBG981, 0JW2FHW7G3, 0B88PQTJ66, E918704SKV]
sources:
  - url: https://en.wikipedia.org/wiki/Uniqueness_quantification
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 3.6
---

## Definition

The uniqueness quantifier makes from a predicate the statement that exactly one element of the domain satisfies it.

Let $D$ be a domain of discourse and let $P(x)$ be a [[predicate|0T3DPBG981]] on $D$.
The proposition $\exists! x \, P(x)$ is defined as
$$\exists x \, \bigl( P(x) \land \forall y \, ( P(y) \to y = x ) \bigr),$$
where $y$ is a variable that does not occur in $P(x)$.
It is read "there is exactly one $x$ such that $P(x)$", or "there is a unique $x$ such that $P(x)$".
By the definitions of the [[existential quantifier|0JW2FHW7G3]] and the [[universal quantifier|0B88PQTJ66]], it is true exactly when some $a \in D$ makes $P(a)$ true and $P(b)$ is false for every $b \in D$ with $b \neq a$.
For a set $A$, the restricted form $\exists! x \in A \; P(x)$ means $\exists! x \, (x \in A \land P(x))$.

## Notation

The symbol $\exists!$ is standard, and the variants $\exists_1$ and $\exists^{=1}$ also occur.
The variable $y$ in the definition must be new, because a $y$ inside $P$ would be captured by $\forall y$.
In Mathlib, `ExistsUnique P` is defined as `∃ x, P x ∧ ∀ y, P y → y = x`, and `∃! x, P x` is notation for it.

## Remarks

The definition is equivalent to the conjunction of existence and uniqueness:
$$\exists x \, P(x) \;\land\; \forall x \, \forall y \, \bigl( P(x) \land P(y) \to x = y \bigr).$$
The concept page [[uniqueness quantifier|0QAJHFGZZJ]] proves this equivalence and gives examples, non-examples and the first properties.
The definition needs the [[equality|E918704SKV]] symbol, so it belongs to first-order logic with equality.
For example, $\exists! x \in \mathbb{R} \; (2x + 1 = 7)$ is true with $x = 3$, because $2x + 1 = 7$ and $2y + 1 = 7$ give $2x = 2y$, so $x = y$.

## Explanations

### L1 human

"There is exactly one even prime" says two things.
There is an even prime, namely $2$.
Every even prime is this same number $2$, so there is no second one.
The definition writes these two parts with "there is" and "for every".

### L2 human

To use the definition, find a candidate $a$ and then check two facts: $P(a)$ is true, and every $y$ in the domain with $P(y)$ true equals $a$.
For $P(x)$ meaning "$x^2 = x + 6$" over $\mathbb{N}$, the candidate is $a = 3$, since $9 = 3 + 6$.
If $y \in \mathbb{N}$ and $y^2 = y + 6$, then $(y - 3)(y + 2) = 0$, so $y = 3$ or $y = -2$.
Since $-2 \notin \mathbb{N}$, we get $y = 3$, and $\exists! x \in \mathbb{N} \; P(x)$ is true.
Over $\mathbb{Z}$ the same predicate has the two solutions $3$ and $-2$, so the $\exists!$ statement is false there.
Watch out: stopping after the first fact proves only $\exists x \, P(x)$.
