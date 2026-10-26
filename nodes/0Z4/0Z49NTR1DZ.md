---
tag: 0Z49NTR1DZ
kind: definition
name: Symmetric difference
msc: ["03E20"]
defines: 0ME21QN125
uses: [0DT0TCV75N, 07KVB4JSC7]
sources:
  - url: https://en.wikipedia.org/wiki/Symmetric_difference
    locator: lead section
---

## Definition

Let $A$ and $B$ be [[sets|0SJ3RX9TXA]].
The symmetric difference of $A$ and $B$ is the set
$$A \mathbin{\triangle} B = (A \setminus B) \cup (B \setminus A).$$
An object $x$ is an element of $A \mathbin{\triangle} B$ when $x$ is an element of exactly one of $A$ and $B$.

## Remarks

Another notation is $A \ominus B$.
Example: $\{1, 2, 3\} \mathbin{\triangle} \{2, 3, 4\} = \{1, 4\}$.
Also $A \mathbin{\triangle} B = (A \cup B) \setminus (A \cap B)$.
The [[power set|0BC7KX51Z8]] of a set is a [[group|G5S1M9]] under symmetric difference, with identity $\varnothing$.

## Explanations

### L1 human

The symmetric difference is the set version of "exclusive or".
It keeps what is in one set or the other, but not what is in both.
