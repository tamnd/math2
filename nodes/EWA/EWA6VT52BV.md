---
tag: EWA6VT52BV
kind: example
name: The sentence that there are at least three elements
msc: ["03B10"]
topics: [NJDME6F845]
audience: ug2
instance_of: [K7XDVK5854]
uses: [71X7TB3F98, 1WTCZB4DVB, 983GZBQYT4]
sources:
  - url: https://en.wikipedia.org/wiki/First-order_logic
    locator: Equality and its axioms
  - book: isbn:9780122384523
    locator: Section 2.2
---

## Example

Let $L$ be any signature, and let $\lambda_3$ be the sentence
$$\exists x \, \exists y \, \exists z \, (\neg x = y \wedge \neg x = z \wedge \neg y = z),$$
which uses only the logical symbol $=$.
We show that $\lambda_3$ is [[true|71X7TB3F98]] in an $L$-structure $\mathcal{M}$ if and only if the domain $M$ has at least three elements.

1. Suppose $M$ has three different elements $a$, $b$ and $c$, and take the witnesses $x \mapsto a$, $y \mapsto b$ and $z \mapsto c$.
2. Under this assignment, $x = y$ fails because $a \neq b$, so $\neg x = y$ holds, by the clauses for equality and negation of [[satisfaction|1WTCZB4DVB]].
   In the same way, $\neg x = z$ and $\neg y = z$ hold.
3. By the clause for $\wedge$ the conjunction holds, and three uses of the clause for $\exists$ give $\mathcal{M} \models \lambda_3$.
4. Conversely, suppose $\mathcal{M} \models \lambda_3$.
   Three uses of the clause for $\exists$ give elements $a, b, c \in M$ that satisfy the conjunction.
5. By the clauses for $\wedge$, $\neg$ and $=$, we get $a \neq b$, $a \neq c$ and $b \neq c$, so $M$ has at least three elements.

For instance, $\lambda_3$ is true in $(\{0, 1, 2\}, <)$, in $(\mathbb{N}, <)$ and in the group $\mathbb{Z} / 4\mathbb{Z}$, and false in $(\{0, 1\}, <)$ and in the trivial group.

## Remarks

First-order sentences can count elements, as long as the count is a fixed finite number.
The same pattern gives, for each $n \geq 1$, a sentence $\lambda_n$ with $n$ variables that is true exactly in the structures with at least $n$ elements.
Then $\lambda_n \wedge \neg \lambda_{n+1}$ is true exactly in the structures with exactly $n$ elements, so $\operatorname{Th}(\mathcal{M})$ always records the size of a finite domain.

The set $\{ \lambda_n : n \geq 1 \}$ has as its models exactly the infinite structures.
No single sentence does this job, and no set of sentences is true exactly in the finite structures.
Both facts follow from the [[compactness theorem|1NR3HAWG9D]].

## Explanations

### L1 human

The sentence says "there are three things that are all different from each other".
It is true in any world with three or more objects: just pick three different ones.
It is false in a world with only two objects, because any three picks must repeat one of them.
So a sentence can say "there are at least three objects" with no symbols except "equals".

### L2 human

We check that $\lambda_3$ is false when $M = \{0, 1\}$, whatever the signature.
Any choice of values for $x$, $y$ and $z$ picks three elements from $\{0, 1\}$.
By the pigeonhole principle, two of the three values are equal.
If, say, the values of $x$ and $y$ are equal, then $\neg x = y$ fails, and the pairs $x, z$ and $y, z$ work the same way.
So no choice satisfies the conjunction, and $\lambda_3$ is false.

The typical use is to fix the size of the models of a theory, or to demand infinite models.
Watch out: $\exists x \, \exists y \, \exists z \, (x = x)$ lacks the inequalities, so its witnesses may coincide, and it is true in every structure.
