---
tag: 9KDC2DQ72A
kind: definition
name: Induced representation
msc: [20C15]
defines: JJP4JFH3C6
uses: [WYGRXCG2RN, 0X1JXT47GA, 0DTXBQPA2S, MNP2HBWB5Q, 03DEH43F4H]
sources:
  - url: https://en.wikipedia.org/wiki/Induced_representation
---

## Definition

Let $G$ be a group, let $H$ be a [[subgroup|0X1JXT47GA]] of finite [[index|0DTXBQPA2S]] $n = [G : H]$, and let $F$ be a field.
Let $\theta \colon H \to GL(W)$ be a [[representation|WYGRXCG2RN]] of $H$ on a vector space $W$ over $F$.
Choose representatives $t_1, \ldots, t_n$ of the [[left cosets|03DEH43F4H]] of $H$ in $G$.
For $g \in G$ and each $i$ there are a unique $j$ and a unique $h_i \in H$ with $g t_i = t_j h_i$.
The *induced representation* $\operatorname{Ind}_H^G \theta$ acts on $V = \bigoplus_{i=1}^{n} t_i W$, a direct sum of $n$ copies of $W$, by
$$g \cdot (t_i w) = t_j \, (\theta(h_i) w) \quad (w \in W).$$

## Remarks

Up to isomorphism, the result does not depend on the choice of the $t_i$.
Equivalently, $\operatorname{Ind}_H^G W = F[G] \otimes_{F[H]} W$, using the [[group algebra|MNP2HBWB5Q]].
Its degree is $[G : H] \cdot \dim W$.
For finite $G$, its character is
$$\operatorname{Ind}_H^G \chi(g) = \frac{1}{\abs{H}} \sum_{x \in G,\ x^{-1} g x \in H} \chi(x^{-1} g x).$$
Example: let $G = S_3$, $H = A_3$ and $\theta$ trivial of degree $1$.
Then $V$ has dimension $2$, and the formula gives the values $2$ at $1$, $0$ at transpositions and $2$ at $3$-cycles.
This is the sum of the trivial and sign characters.
Non-example: for $H = \set{0}$ in $G = \Z$, the index is infinite, so the definition does not apply; the space $\bigoplus_{t \in \Z} W$ with the shift action is a different construction, sometimes called compact induction.
