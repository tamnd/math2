---
tag: 0QE5PFJY7V
kind: definition
name: Equivalence relation induced by a function
msc: ["03E20"]
defines: 0KT8TGXD8K
uses: [0XHDTE5YMZ, 0SGTMBEWRF]
sources:
  - url: https://en.wikipedia.org/wiki/Kernel_(set_theory)
    locator: lead section
---

## Definition

Let $f \colon A \to B$ be a [[function|0XHDTE5YMZ]].
The equivalence relation induced by $f$ is the relation $\sim_f$ on $A$ with
$$a \sim_f a' \iff f(a) = f(a')$$
for all $a, a' \in A$.

## Remarks

Another name is the kernel of $f$.
The relation $\sim_f$ is an [[equivalence relation|0SGTMBEWRF]], because equality is one.
Its classes are the nonempty preimages $f^{-1}(\{b\})$ of the points $b \in B$.
The function $f$ is [[injective|0PVG1CRAJN]] exactly when $\sim_f$ is equality.

## Explanations

### L1 human

Take the function that sends each person to their birthday.
Two people are equivalent under it when they have the same birthday.
The function forgets everything except its value, and the relation records what it forgets.
