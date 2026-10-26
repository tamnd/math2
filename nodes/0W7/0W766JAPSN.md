---
tag: 0W766JAPSN
kind: definition
name: Inverse function
msc: ["03E20"]
defines: 0J2WAR83WP
uses: [0SNQEF7Z53]
sources:
  - url: https://en.wikipedia.org/wiki/Inverse_function
    locator: lead section
---

## Definition

Let $f \colon A \to B$ be a [[bijective function|0SNQEF7Z53]].
The inverse function of $f$ is the function $f^{-1} \colon B \to A$ such that, for each $b \in B$, $f^{-1}(b)$ is the unique $a \in A$ with $f(a) = b$.

## Remarks

Then $f^{-1} \circ f = \mathrm{id}_A$ and $f \circ f^{-1} = \mathrm{id}_B$. See [[bijective iff it has a two-sided inverse|01VG2A0BHW]].
The inverse $f^{-1}$ is a bijection, and its inverse is $f$.
Example: the inverse of $x \mapsto 2x + 1$ on $\mathbb{R}$ is $y \mapsto (y - 1)/2$.
Do not confuse $f^{-1}(b)$ with the [[preimage|0FGCFY1AZX]] $f^{-1}(\{b\})$, which exists for every function.

## Explanations

### L1 human

To find the inverse of $y = 2x + 1$, solve for $x$: $x = (y - 1)/2$.
The inverse runs the function backwards.
Its graph is the graph of $f$ reflected in the line $y = x$.
