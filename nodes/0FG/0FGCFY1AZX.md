---
tag: 0FGCFY1AZX
kind: definition
name: Preimage of a set
msc: ["03E20"]
defines: 01AHG4G9RT
uses: [0XHDTE5YMZ, 0FE8Q5S42Y]
sources:
  - url: https://en.wikipedia.org/wiki/Image_(mathematics)
    locator: Inverse image
---

## Definition

Let $f \colon A \to B$ be a [[function|0XHDTE5YMZ]] and let $T$ be a [[subset|0FE8Q5S42Y]] of $B$.
The preimage of $T$ under $f$ is the set
$$f^{-1}(T) = \{a \in A \mid f(a) \in T\}.$$

## Remarks

Another name is the inverse image. The notation $f^{-1}(T)$ makes sense for every $f$, also when $f$ has no [[inverse function|0W766JAPSN]].
Preimages respect all set operations: $f^{-1}(T_1 \cap T_2) = f^{-1}(T_1) \cap f^{-1}(T_2)$, and the same holds for unions and complements.
Example: for $f(x) = x^2$ on $\mathbb{R}$, $f^{-1}([1, 4]) = [-2, -1] \cup [1, 2]$.

## Explanations

### L1 human

The preimage answers the question: which inputs land in $T$?
For the function that sends a student to their grade, the preimage of $\{A\}$ is the set of students with grade $A$.
