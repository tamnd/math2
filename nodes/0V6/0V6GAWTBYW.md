---
tag: 0V6GAWTBYW
kind: definition
name: Biconditional
msc: [03B05]
defines: 0S6GMNJ62Y
uses: [0ZNX6DQ3EJ, 0M28ASWG8T]
sources:
  - url: https://en.wikipedia.org/wiki/Logical_biconditional
    locator: lead section
---

## Definition

Let $p$ and $q$ be [[propositions|0ZGC7ZESYN]].
The biconditional of $p$ and $q$ is the proposition $p \leftrightarrow q$, read "$p$ if and only if $q$".
The proposition $p \leftrightarrow q$ is true when $p$ and $q$ are both true or both false. Otherwise, it is false.

| $p$ | $q$ | $p \leftrightarrow q$ |
|---|---|---|
| T | T | T |
| T | F | F |
| F | T | F |
| F | F | T |

## Remarks

Other notations are $p \Leftrightarrow q$ and "$p$ iff $q$".
The proposition $p \leftrightarrow q$ has the same truth value as $(p \to q) \land (q \to p)$.

## Explanations

### L1 human

"A triangle has three equal sides if and only if it has three equal angles" is a biconditional.
It says two things: each property gives the other.
To prove a biconditional, you usually prove the two [[implications|0ZNX6DQ3EJ]] separately.
