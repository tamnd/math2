---
tag: 0GE4DVQKR8
kind: example
name: The quaternions
aliases: [hamilton-quaternions]
msc: [16K20]
instance_of: [0EA5BTA0CX]
uses: [0WZXK05ME7]
sources:
  - url: https://en.wikipedia.org/wiki/Quaternion
    locator: Multiplication of basis elements
same_as:
  wikidata: Q173853
  wikipedia: Quaternion
---

## Example

The quaternions $\mathbb{H}$ are the real vector space with basis $1, i, j, k$.
Each quaternion is $a + b i + c j + d k$ with $a, b, c, d \in \mathbb{R}$.
The multiplication is $\mathbb{R}$-bilinear, $1$ is the identity, and the basis elements obey
$$i^2 = j^2 = k^2 = i j k = -1.$$
These rules give $i j = k = -j i$, $j k = i = -k j$ and $k i = j = -i k$.
With this multiplication, $\mathbb{H}$ is a [[division ring|0WZXK05ME7]] that is not commutative.

## Remarks

The conjugate of $q = a + b i + c j + d k$ is $\bar{q} = a - b i - c j - d k$, and $q \bar{q} = a^2 + b^2 + c^2 + d^2$.
So a nonzero $q$ has the inverse $q^{-1} = \bar{q} / (a^2 + b^2 + c^2 + d^2)$.
The quaternions are not a field, because $i j \neq j i$.

## Explanations

### L1 human

The quaternions extend the complex numbers with two more square roots of $-1$, called $j$ and $k$.
You can divide by every nonzero quaternion.
But the order of multiplication matters: $i j = k$ and $j i = -k$.
