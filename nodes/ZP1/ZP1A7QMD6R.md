---
tag: ZP1A7QMD6R
kind: definition
name: Radical of an ideal
msc: [13A15]
defines: 437YRCNYRJ
uses: [0GYGHKX834, 0MYSA6MYNA]
sources:
  - url: https://en.wikipedia.org/wiki/Radical_of_an_ideal
---

## Definition

Let $R$ be a [[commutative ring|0GYGHKX834]] and let $I$ be an [[ideal|0MYSA6MYNA]] of $R$.
The *radical* of $I$ is the set
$$\sqrt{I} = \set{r \in R : r^n \in I \text{ for some integer } n \ge 1}.$$

## Remarks

The set $\sqrt{I}$ is an ideal of $R$ that contains $I$: if $a^m \in I$ and $b^n \in I$, then every term of the binomial expansion of $(a + b)^{m + n - 1}$ lies in $I$.
Example: in $\Z$, $\sqrt{12\Z} = 6\Z$, since $6^2 = 36 \in 12\Z$, and if $r^n \in 12\Z$ then the primes $2$ and $3$ divide $r$.
Non-example: $4 \notin \sqrt{12\Z}$, because no power of $4$ is divisible by $3$.
The radical of the zero ideal is the [[nilradical|QQDN6EYQNJ]] of $R$.
An ideal equal to its radical is a [[radical ideal|S4GQN5V54X]].
Other notations are $\operatorname{rad}(I)$ and $r(I)$.
