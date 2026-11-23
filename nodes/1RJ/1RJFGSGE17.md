---
tag: 1RJFGSGE17
kind: example
name: The evaluation game for every number has a larger one
msc: ["03B10"]
topics: [NJDME6F845]
audience: grad
instance_of: [D45Z7HETDA]
uses: [D45Z7HETDA, WK9J5ZTZGJ]
sources:
  - url: https://en.wikipedia.org/wiki/Game_semantics
    locator: lead section
---

## Example

Let $\sigma = \forall x \, \exists y \, (x < y)$.
We play the [[evaluation game|D45Z7HETDA]] for $\sigma$ in $(\mathbb{N}, <)$ and in $(\{0, 1, 2\}, <)$, and we compare with the [[Tarskian evaluation|WK9J5ZTZGJ]] of the same sentence.

In $(\mathbb{N}, <)$:

1. The first symbol is $\forall x$, so Abelard, the falsifier, picks some $a \in \mathbb{N}$.
2. The next symbol is $\exists y$, so Eloise, the verifier, picks some $b \in \mathbb{N}$, and her strategy is $b = a + 1$.
3. The play reaches the atomic formula $x < y$ with $x \mapsto a$ and $y \mapsto a + 1$.
   Since $a < a + 1$, Eloise wins.
4. The strategy wins against every choice of $a$, so Eloise has a winning strategy, and $\sigma$ is true.

In $(\{0, 1, 2\}, <)$:

1. Abelard picks $a = 2$.
2. Eloise picks some $b \in \{0, 1, 2\}$, and in each case $2 < b$ is false.
3. So Abelard wins every play that starts with $2$.
   This is a winning strategy for him, and $\sigma$ is false.

## Remarks

The example shows the game reading of $\forall \exists$: the challenge comes first, and the answer may depend on it.
Eloise's strategy in $(\mathbb{N}, <)$ is the function $a \mapsto a + 1$, which is a Skolem function for $\sigma$.
Other winning strategies exist, such as $a \mapsto a + 7$ or $a \mapsto 2a + 1$, while $a \mapsto 2a$ loses when Abelard picks $0$.

Swap the quantifiers and the game changes hands.
For $\exists y \, \forall x \, (x < y)$, Eloise must pick $b$ first, then Abelard answers $a = b$, and $b < b$ fails, so Abelard wins in both structures.

## Explanations

### L1 human

Abelard names a number, and Eloise must name a bigger one.
With all the natural numbers, Eloise always wins: she says "your number plus one".
With only $0$, $1$ and $2$, Abelard says $2$, and Eloise has nothing bigger.

### L2 human

We test two of Eloise's strategies in $(\mathbb{N}, <)$.
The strategy $b = a + 1$ wins for every $a$, as shown above.
The constant strategy $b = 5$ wins when $a \le 4$, but it loses when Abelard picks $a = 5$, because $5 < 5$ is false.
So the constant strategy is not winning, although it wins many plays.
Truth needs a strategy that wins every play, not a strategy that wins many.
Watch out: one losing strategy of Eloise does not make the sentence false; it is false only when Abelard has a winning strategy.
