---
tag: ~beb187ef
kind: definition
name: Surjective function
msc: ["03E20"]
defines: ~f0564789
uses: [~d103e2ff, ~876ab51a]
sources:
  - url: https://en.wikipedia.org/wiki/Surjective_function
    locator: lead section
---

## Definition

Let $f \colon A \to B$ be a [[function|~d103e2ff]].
The function $f$ is surjective when, for each $b \in B$, there is an $a \in A$ with $f(a) = b$.

## Remarks

Other names are onto function and surjection.
Equivalently, the [[range|~54a6afbb]] of $f$ is the whole [[codomain|~876ab51a]] $B$.
The function $x \mapsto x^3$ on $\mathbb{R}$ is surjective, and $x \mapsto x^2$ on $\mathbb{R}$ is not, because $-1$ is not a value.

## Explanations

### L1 human

A surjective function hits every element of the codomain at least once.
To prove surjectivity, take an arbitrary $b \in B$ and find an input $a$ with $f(a) = b$.
