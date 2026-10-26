---
tag: 0CDWKDYWN6
kind: statement
role: theorem
name: Universal property of the free group
msc: ["20E05"]
uses: [020Z5SEN27, 0HV9Y7WG5R]
sources:
  - url: https://en.wikipedia.org/wiki/Free_group
    locator: Universal property
  - url: https://en.wikipedia.org/wiki/Free_group
    locator: Facts and theorems
---

## Statement

Let $S$ be a set, let $F_S$ be the [[free group|0KTW26C80J]] on $S$, and let $G$ be a [[group|G5S1M9]].
For each function $f \colon S \to G$, there is exactly one [[group homomorphism|0JYTG5K9Y4]] $\varphi \colon F_S \to G$ with $\varphi(s) = f(s)$ for each $s \in S$.

## Remarks

Here $S$ is identified with the set of words of length $1$ in $F_S$.
The homomorphism is $\varphi(t_1 \cdots t_n) = f(t_1)^{\pm 1} \cdots f(t_n)^{\pm 1}$, with the sign of each letter.
This property characterises $F_S$ up to isomorphism, so some texts use it as the definition of a free group.
If the image of $f$ generates $G$, then $\varphi$ is surjective, so $G$ is a quotient of $F_S$.

## Explanations

### L1 human

To define a homomorphism out of a free group, you only choose the images of the generators.
There are no relations to check.
So each choice extends to exactly one homomorphism.
