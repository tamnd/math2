---
tag: 0RX7DDBYCK
kind: statement
role: proposition
name: Image of an intersection
msc: ["03E20"]
uses: [0Q3F20XB0A, 0HBRW4E6G1]
sources:
  - url: https://en.wikipedia.org/wiki/Image_(mathematics)
    locator: Properties
---

## Statement

Let $f \colon A \to B$ be a [[function|0XHDTE5YMZ]] and let $S$ and $T$ be [[subsets|0FE8Q5S42Y]] of $A$.
Then the [[image|0Q3F20XB0A]] of $S \cap T$ is a subset of the intersection of the images:
$$f(S \cap T) \subseteq f(S) \cap f(T).$$

## Remarks

The inclusion can be strict. For the constant function $f \colon \{1, 2\} \to \{0\}$, $S = \{1\}$ and $T = \{2\}$, the left side is $\varnothing$ and the right side is $\{0\}$.
Equality holds for all $S$ and $T$ if and only if $f$ is [[injective|0PVG1CRAJN]].
For unions, equality always holds: $f(S \cup T) = f(S) \cup f(T)$.

## Explanations

### L1 human

If $b = f(x)$ with $x$ in both $S$ and $T$, then $b$ is in both images.
But $b$ can be in both images for another reason: $b = f(s) = f(t)$ with $s \in S$, $t \in T$ and $s \neq t$.
