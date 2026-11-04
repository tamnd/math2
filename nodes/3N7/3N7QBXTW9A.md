---
tag: 3N7QBXTW9A
kind: proof
name: Proof that the image of an intersection lies in the intersection of the images
msc: ["03E20"]
proves: 0RX7DDBYCK
uses: [0Q3F20XB0A, 0HBRW4E6G1, 0FE8Q5S42Y]
sources:
  - url: https://proofwiki.org/wiki/Image_of_Intersection_under_Mapping
    locator: Proof 1
---

## Proof

We show that each element of the left side is an element of the right side.

1. Let $f \colon A \to B$ be a function and let $S, T \subseteq A$.
2. Let $y \in f(S \cap T)$. By the definition of the [[image|0Q3F20XB0A]], there is $s \in S \cap T$ with $f(s) = y$.
3. By the definition of [[intersection|0HBRW4E6G1]], $s \in S$ and $s \in T$.
4. Since $s \in S$ and $f(s) = y$, the definition of the image gives $y \in f(S)$.
5. Since $s \in T$ and $f(s) = y$, the definition of the image gives $y \in f(T)$.
6. By steps 4 and 5, $y \in f(S) \cap f(T)$.
7. Step 2 took an arbitrary element $y$ of $f(S \cap T)$. So $f(S \cap T)$ is a [[subset|0FE8Q5S42Y]] of $f(S) \cap f(T)$.

## Idea

A point of $S \cap T$ that maps to $y$ is a witness in $S$ and a witness in $T$ at the same time. The reverse inclusion can fail, because $y$ may come from one point of $S$ and a different point of $T$.
