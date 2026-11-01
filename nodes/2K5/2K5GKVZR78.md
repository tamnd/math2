---
tag: 2K5GKVZR78
kind: definition
name: Nilradical
msc: [13A15]
defines: QQDN6EYQNJ
uses: [0GYGHKX834, 0N9R5NN6TW]
sources:
  - url: https://en.wikipedia.org/wiki/Nilradical_of_a_ring
---

## Definition

Let $R$ be a [[commutative ring|0GYGHKX834]].
The *nilradical* of $R$ is the set
$$N(R) = \set{r \in R : r^n = 0 \text{ for some integer } n \ge 1}$$
of [[nilpotent elements|0N9R5NN6TW]] of $R$.

## Remarks

$N(R)$ is the [[radical|437YRCNYRJ]] $\sqrt{(0)}$ of the zero ideal, so it is an ideal of $R$.
Example: in $\Z/12\Z$, $N = \set{0, 6}$; indeed $6^2 = 0$, and if $r^n \equiv 0 \pmod{12}$ then $2$ and $3$ divide $r$.
Non-example: $2 \notin N(\Z/12\Z)$, because $2^n$ is never divisible by $3$.
The quotient $R/N(R)$ has zero nilradical, that is, it is [[reduced|SZHY975FFX]].
$N(R)$ is the intersection of all [[prime ideals|06HC6HK0Z8]] of $R$; see [[the nilradical as an intersection of primes|3CZ8PXR9JY]].
Other notations are $\operatorname{nil}(R)$ and $\mathfrak{N}_R$.
