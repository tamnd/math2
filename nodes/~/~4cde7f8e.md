---
tag: ~4cde7f8e
kind: definition
name: Preimage of a set
msc: ["03E20"]
defines: ~6453d113
uses: [~d103e2ff, ~a9b9ba7e]
sources:
  - url: https://en.wikipedia.org/wiki/Image_(mathematics)
    locator: Inverse image
---

## Definition

Let $f \colon A \to B$ be a [[function|~d103e2ff]] and let $T$ be a [[subset|~a9b9ba7e]] of $B$.
The preimage of $T$ under $f$ is the set
$$f^{-1}(T) = \{a \in A \mid f(a) \in T\}.$$

## Remarks

Another name is the inverse image. The notation $f^{-1}(T)$ makes sense for every $f$, also when $f$ has no [[inverse function|~6b98c003]].
Preimages respect all set operations: $f^{-1}(T_1 \cap T_2) = f^{-1}(T_1) \cap f^{-1}(T_2)$, and the same holds for unions and complements.
Example: for $f(x) = x^2$ on $\mathbb{R}$, $f^{-1}([1, 4]) = [-2, -1] \cup [1, 2]$.

## Explanations

### L1 human

The preimage answers the question: which inputs land in $T$?
For the function that sends a student to their grade, the preimage of $\{A\}$ is the set of students with grade $A$.
