---
tag: 0RWQ5VZ6VQ
kind: statement
role: theorem
name: Every infinite set has a countably infinite subset
msc: ["03E10"]
uses: [01MKW4R283, 0SEZ3JGZP7, 0PVG1CRAJN, 0HTGB13FE2]
sources:
  - url: https://en.wikipedia.org/wiki/Infinite_set
    locator: Properties
---

## Statement

Assume the [[axiom of choice|0HTGB13FE2]].
Let $A$ be an [[infinite set|01MKW4R283]].
Then there is an [[injective function|0PVG1CRAJN]] $f \colon \mathbb{N} \to A$, so $A$ has a [[countably infinite|0SEZ3JGZP7]] subset $f(\mathbb{N})$.

## Remarks

The proof chooses $a_0 \in A$, then $a_1 \in A \setminus \{a_0\}$, and so on. Each set $A \setminus \{a_0, \dots, a_n\}$ is nonempty because $A$ is infinite.
The axiom of countable choice is enough, but some choice is needed: in ZF alone, the statement cannot be proved.
It follows that $\aleph_0$ is the least infinite cardinal.

## Explanations

### L1 human

In an infinite set you can always pick one more element.
Picking forever gives a sequence of different elements, which is a copy of $\mathbb{N}$ inside the set.
