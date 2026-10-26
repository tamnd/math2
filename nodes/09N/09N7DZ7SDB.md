---
tag: 09N7DZ7SDB
kind: statement
role: proposition
name: Ring homomorphisms from a field are injective
msc: ["12E99"]
uses: [0GGE0Z0JQ1, 0QA8CHH8MG, 0MMCB8RXGA]
sources:
  - url: https://en.wikipedia.org/wiki/Ring_homomorphism
    locator: Properties
---

## Statement

Let $K$ be a [[field|0QA8CHH8MG]], let $S$ be a nonzero [[ring|0894J980RK]] and let $f \colon K \to S$ be a [[ring homomorphism|0GGE0Z0JQ1]].
Then $f$ is injective.

## Remarks

The proof: if $a \neq 0$ and $f(a) = 0$, then $1 = f(1) = f(a) f(a^{-1}) = 0$ in $S$. This contradicts $S \neq 0$.
The hypothesis $S \neq 0$ is necessary, because the map from $K$ to the [[zero ring|008TBCYDPX]] is a ring homomorphism.
A consequence: a homomorphism of fields makes the first field a copy of a subfield of the second.

## Explanations

### L1 human

A field has no ideal other than $0$ and the whole field.
The kernel of $f$ is an ideal, and it does not contain $1$.
So the kernel is $0$, and $f$ is injective.
