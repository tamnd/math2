---
tag: FWY8A9M5HK
kind: statement
role: theorem
name: Dimension of an eigenspace is at most the algebraic multiplicity
msc: [15A18]
uses: [0BQAA2BK3Q, 0G0RFPG8HR, 0FY42N02DV]
sources:
  - url: https://github.com/davidaustinm/ula/blob/b6ea263ef23703072b7007485bb7a2d89c5f399b/src/section4-2.xml#L797
    locator: src/section4-2.xml:797
---

## Statement

Let $A$ be a square matrix with real entries.
Let $\lambda$ be a real [[eigenvalue|0BQAA2BK3Q]] of $A$, and let $m$ be its [[algebraic multiplicity|0FY42N02DV]], that is, its multiplicity as a root of the characteristic polynomial of $A$.
Then the [[eigenspace|0G0RFPG8HR]] $E_\lambda$ of $\lambda$ satisfies
$$1 \leq \dim E_\lambda \leq m.$$

## Remarks

The lower bound holds because an eigenvalue has at least one nonzero eigenvector.
The number $\dim E_\lambda$ is the geometric multiplicity of $\lambda$.
So the geometric multiplicity never exceeds the algebraic multiplicity.
