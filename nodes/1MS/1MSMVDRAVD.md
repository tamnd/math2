---
tag: 1MSMVDRAVD
kind: object
name: Albert algebra
msc: [17C40, 17C20, 17C90]
instance_of: [6C2MCVB8C7, N184N4TVZ2]
uses: [1HRMT3DSX2, 6C2MCVB8C7, N184N4TVZ2, T4AWF1BRZB, G127K65CSX]
sources:
  - url: https://en.wikipedia.org/wiki/Albert_algebra
same_as:
  wikidata: Q12204658
  wikipedia: Albert algebra
---

## Description

Let $\mathbb{O}$ be the real [[octonions|1HRMT3DSX2]], with conjugation $a \mapsto \bar{a}$.
The *Albert algebra* is the real vector space $H_3(\mathbb{O})$ of $3 \times 3$ matrices $X$ with entries in $\mathbb{O}$ such that $\bar{X}^T = X$.
Its product is $X \circ Y = \frac{1}{2}(XY + YX)$, where $XY$ is the usual matrix product computed with octonion multiplication.
An element has the form
$$X = \begin{pmatrix} \alpha & c & \bar{b} \\ \bar{c} & \beta & a \\ b & \bar{a} & \gamma \end{pmatrix}, \qquad \alpha, \beta, \gamma \in \R,\ a, b, c \in \mathbb{O},$$
so $\dim_\R H_3(\mathbb{O}) = 3 + 3 \cdot 8 = 27$.

## Remarks

$H_3(\mathbb{O})$ is a [[Jordan algebra|6C2MCVB8C7]], although $\mathbb{O}$ is not associative; the proof uses that $\mathbb{O}$ is alternative.
The trace form $\ip{X}{Y} = \tr(X \circ Y)$ makes it a [[Euclidean Jordan algebra|N184N4TVZ2]], and it is simple.
Albert proved that it is exceptional: it is not a [[special Jordan algebra|T4AWF1BRZB]].
Its automorphism group is the compact Lie group of type $F_4$, whose Lie algebra is the compact real form of [[F4|G127K65CSX]].
More generally, over any field of characteristic not $2$, an Albert algebra is a $27$-dimensional simple exceptional Jordan algebra.
The same construction with $3 \times 3$ Hermitian matrices over $\R$, $\C$ or the quaternions gives special Jordan algebras of dimensions $6$, $9$ and $15$.

## Explanations

### L1 human

Take $3 \times 3$ matrices whose entries are octonions and which equal their own conjugate transpose.
Multiply them by averaging $XY$ and $YX$.
The result is a $27$-dimensional algebra, and it is the most famous Jordan algebra.
It cannot be built from any associative algebra, which makes it exceptional.
It is closely tied to the exceptional Lie groups $F_4$, $E_6$ and $E_7$.
