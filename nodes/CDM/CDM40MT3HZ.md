---
tag: CDM40MT3HZ
kind: statement
role: theorem
name: Hölder's theorem on Archimedean groups
msc: ["06F20", "20F60"]
uses: [1P8087YGYQ, 08J2M1JYAG, 0HV9Y7WG5R, 0PVG1CRAJN, 04QNZZ4HHY]
about: [P2E8BNYC7B]
sources:
  - url: https://en.wikipedia.org/wiki/Archimedean_group
---

## Statement

Let $(G, \le)$ be a [[linearly ordered group|1P8087YGYQ]] with identity $e$.
Suppose that $G$ is *Archimedean*: for all $a, b \in G$ with $a > e$, there is an integer $n \ge 1$ with $b < a^n$.
Then there is an injective [[group homomorphism|0HV9Y7WG5R]] $\varphi \colon G \to (\R, +)$ such that $a \le b$ if and only if $\varphi(a) \le \varphi(b)$.
In particular, $G$ is abelian.

## Remarks

If $G = \set{e}$ there is nothing to prove.
Otherwise one fixes an element $u > e$ and sends $g$ to the real number $\sup \set{m/n : n \ge 1, \ u^m \le g^n}$.
The Archimedean property makes this set bounded above and nonempty, and an argument with [[Dedekind cuts|04QNZZ4HHY]] shows that the map is an [[injective|0PVG1CRAJN]] order-preserving homomorphism.
Commutativity of $G$ then follows from commutativity of $\R$.
Example: the subgroup $\Z + \Z\sqrt{2}$ of $\R$ is Archimedean and is already a subgroup of [[the reals|08J2M1JYAG]].
The Archimedean hypothesis is needed: $\Z^2$ with the lexicographic order is linearly ordered, but $n \cdot (0, 1) < (1, 0)$ for all $n$.
No order-preserving injective homomorphism to $\R$ exists for it, since the image of $(0, 1)$ would be positive with all its multiples below the image of $(1, 0)$.

## Explanations

### L1 human

A linearly ordered group is Archimedean if no element is infinitely large compared with another positive element.
Hölder's theorem says that such a group is just a group of real numbers in disguise.
So the real numbers contain every way of measuring with a single scale and no infinitely large or small quantities.

### L2 human

The theorem is the base case for the structure theory of linearly ordered abelian groups.
A general linearly ordered abelian group splits into Archimedean classes, and the quotient attached to each class is Archimedean, so Hölder's theorem embeds it into $\R$.
The [[Hahn embedding theorem|FVPXXFNVQY]] puts these real pieces together in a lexicographic product.
The theorem also explains why the value group of a rank one valuation can be taken inside $\R$.
