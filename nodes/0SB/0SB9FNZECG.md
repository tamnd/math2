---
tag: 0SB9FNZECG
kind: definition
name: Path component
msc: [54D05]
defines: 0X3EG7Y65T
uses: [0K0GE6BCYW, 0SGTMBEWRF]
sources:
  - url: https://en.wikipedia.org/wiki/Connected_space
    locator: Path connectedness
---

## Definition

Let $X$ be a [[topological space|0CNQXVBHCX]].
For $x, y \in X$, write $x \simeq y$ when there is a [[path|0K0GE6BCYW]] in $X$ from $x$ to $y$.
This is an [[equivalence relation|0SGTMBEWRF]] on $X$. Its classes are the path components of $X$.

## Remarks

The relation is reflexive by constant paths, symmetric by $t \mapsto \gamma(1 - t)$, and transitive by joining two paths one after the other.
The path component of $x$ is the largest path-connected subset of $X$ that contains $x$.
Each path component lies in a [[connected component|0NRT0E2QT2]]. The [[topologist's sine curve|0K3T4A659R]] is one connected component but has two path components.
Path components need not be closed.

## Explanations

### L1 human

The path component of a point is the set of all points that you can reach from it along a path.
