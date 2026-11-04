---
tag: HAP2G0H9NC
kind: proof
name: Proof that the only ideals of a field are zero and the whole field
msc: ["12E99"]
proves: 0M6G75E95E
uses: [0QA8CHH8MG, 0MYSA6MYNA]
sources:
  - url: https://proofwiki.org/wiki/Ideals_of_Field
---

## Proof

1. Let $K$ be a [[field|0QA8CHH8MG]] and let $I$ be an [[ideal|0MYSA6MYNA]] of $K$.
2. Since $I$ is an additive subgroup of $K$, $0 \in I$. So if $I$ has no nonzero element, then $I = \set{0}$.
3. Otherwise, let $a \in I$ with $a \neq 0$. Since $K$ is a field, there is $b \in K$ with $b a = 1$.
4. Since $I$ is an ideal, $b a \in I$. So $1 \in I$.
5. Let $r \in K$. Since $I$ is an ideal and $1 \in I$, $r = r \cdot 1 \in I$. So $K \subseteq I$, and $I = K$.
6. Hence $I = \set{0}$ or $I = K$.

## Idea

A nonzero element of an ideal of a field can be multiplied by its inverse. So the ideal contains $1$, and then it contains every multiple of $1$, which is every element.
