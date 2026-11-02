---
tag: S9VTAYV1VJ
kind: statement
role: theorem
name: Kummer's transformation
msc: [33C15]
uses: [6AZ4ZBN1M8, NT917KFR57]
about: [6AZ4ZBN1M8]
sources:
  - url: https://en.wikipedia.org/wiki/Confluent_hypergeometric_function
---

## Statement

Let $a$ and $b$ be complex numbers with $b \notin \set{0, -1, -2, \dots}$, and let $M$ be [[Kummer's confluent hypergeometric function|6AZ4ZBN1M8]].
Then for every $z \in \C$,
$$M(a, b, z) = e^{z}\, M(b - a, b, -z).$$

## Remarks

Proof idea: put $w(z) = e^z v(-z)$ into [[Kummer's equation|NT917KFR57]] with parameters $a, b$.
A direct computation shows that $w$ is a solution exactly when $v$ solves Kummer's equation with parameters $b - a, b$.
So $e^z M(b - a, b, -z)$ is a solution of the first equation that is analytic at $0$ with value $1$.
For $b \notin \set{0, -1, -2, \dots}$ there is only one such solution, namely $M(a, b, z)$.
Indeed, the other exponent at $0$ is $1 - b$, and a solution with that exponent cannot be analytic with value $1$ there.
Example: for $a = b$, the left side is $e^z$ and the right side is $e^z M(0, b, -z) = e^z \cdot 1$.
Example: for $a = 1$, $b = 2$, the right side is $e^z \frac{e^{-z} - 1}{-z} = \frac{e^z - 1}{z} = M(1, 2, z)$.

## Explanations

### L1 human

Kummer's transformation says that changing $z$ to $-z$ in Kummer's function costs only a factor $e^z$ and a change of the first parameter from $a$ to $b - a$.
It is the confluent analogue of the Pfaff and Euler transformations of the Gauss hypergeometric function.
For instance it turns the trivial fact $M(0, b, z) = 1$ into $M(b, b, z) = e^z$.

### L2 human

The identity is often used to move between large positive and large negative arguments, since one side may be much easier to estimate than the other.
It also shows that if $a$ or $b - a$ is a nonpositive integer, then $M(a, b, z)$ is a polynomial or $e^z$ times a polynomial.
The Tricomi function satisfies a companion identity, $U(a, b, z) = z^{1 - b} U(a - b + 1, 2 - b, z)$, often called Kummer's second transformation.
