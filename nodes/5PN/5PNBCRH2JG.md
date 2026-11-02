---
tag: 5PNBCRH2JG
kind: example
name: Tropical semiring
msc: [16Y60, 15A80, 14T10]
instance_of: [D31S3GR51T]
uses: [JCSAC9Y1CV, 64G0VSC5F4, AHH97EJ6VH]
sources:
  - url: https://en.wikipedia.org/wiki/Tropical_semiring
same_as:
  wikidata: Q60790098
  wikipedia: Tropical semiring
---

## Example

Let $T = \R \cup \set{+\infty}$.
For $a, b \in T$, define
$$a \oplus b = \min(a, b), \qquad a \otimes b = a + b,$$
with the conventions $\min(a, +\infty) = a$ and $a + (+\infty) = +\infty$.
Then $(T, \oplus, \otimes)$ is a commutative [[semiring|D31S3GR51T]], the *tropical semiring* in its min-plus form.

The check of the semiring axioms:

1. $\oplus$ is associative and commutative, and $+\infty$ is its neutral element, since $\min(a, +\infty) = a$.
2. $\otimes$ is associative and commutative, and $0$ is its neutral element, since $a + 0 = a$.
3. $\otimes$ distributes over $\oplus$: $a + \min(b, c) = \min(a + b, a + c)$, because adding $a$ preserves the order.
4. $+\infty$ is absorbing for $\otimes$: $a + (+\infty) = +\infty$.

For instance, $3 \oplus 5 = 3$ and $3 \otimes 5 = 8$, and $2 \otimes (3 \oplus 7) = 5 = (2 \otimes 3) \oplus (2 \otimes 7)$.

## Remarks

The semiring is [[idempotent|JCSAC9Y1CV]]: $a \oplus a = \min(a, a) = a$.
It is not a ring, since $3$ has no additive inverse: $\min(3, b) = +\infty$ has no solution $b$ in $T$.
Every element $a \ne +\infty$ has the inverse $-a$ for $\otimes$, so the tropical semiring is a [[semifield|AHH97EJ6VH]].
The map $x \mapsto -x$ is an isomorphism onto the max-plus semiring $(\R \cup \set{-\infty}, \max, +)$, the base of [[max-plus algebra|64G0VSC5F4]].
Some authors call that max-plus form the tropical semiring instead.

## Explanations

### L1 human

In tropical arithmetic, "plus" means "take the smaller" and "times" means "add".
So $3 \oplus 5 = 3$ and $3 \otimes 5 = 8$.
These rules still obey the usual laws of reordering, regrouping and distributing.
They describe shortest paths: along a route the lengths add, and between two routes one takes the shorter.
