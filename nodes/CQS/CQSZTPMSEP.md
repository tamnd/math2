---
tag: CQSZTPMSEP
kind: definition
name: Center of a ring
msc: [16U70]
defines: MVT64B3B6H
uses: [0894J980RK, 0859D58WPD]
sources:
  - url: https://en.wikipedia.org/wiki/Center_(ring_theory)
---

## Definition

Let $R$ be a [[ring|0894J980RK]].
The *center* of $R$ is the set
$$Z(R) = \set{z \in R : zr = rz \text{ for all } r \in R}.$$

## Remarks

$Z(R)$ is a commutative [[subring|0859D58WPD]] of $R$, and $R$ is commutative if and only if $Z(R) = R$.
Example: for a field $K$ and $n \ge 1$, the center of $M_n(K)$ is the set of scalar matrices $cI_n$ with $c \in K$.
The check: a matrix $Z$ that commutes with every matrix unit $E_{ij}$ satisfies $Z E_{ij} = E_{ij} Z$; comparing entries shows that $Z$ is diagonal with equal diagonal entries.
Non-example: for $n \ge 2$, the matrix $E_{11}$ is not in the center of $M_n(K)$, since $E_{11} E_{12} = E_{12}$ but $E_{12} E_{11} = 0$.
Some authors write $C(R)$ for the center.
