---
tag: WETMPAHWZV
kind: example
name: Classical logic has a two-element characteristic matrix
msc: ["03B50", "03B05"]
topics: [WZP584JQ06]
audience: grad
not_instance_of:
  - target: DWYCKAKXZD
    note: classical consequence is the consequence of the two-element matrix, so it needs no third value, although a four-element matrix gives it too
uses: [66NMTCQNQV, 0XADJKM699, 05006AJ7DZ]
sources:
  - url: https://en.wikipedia.org/wiki/Many-valued_logic
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: 3.2 Logical matrices and the designation-based notion of entailment
---

## Example

Let $\mathbf{2}$ be the matrix with values $\set{0, 1}$, designated set $\set{1}$ and the classical tables for $\neg, \land, \lor, \to$.
Let $\mathbf{4} = \mathbf{2} \times \mathbf{2}$, with values $(0,0), (0,1), (1,0), (1,1)$, the operations taken coordinatewise and designated set $\set{(1, 1)}$.
We show that both matrices give the classical consequence relation.

1. $\mathbf{2}$ gives classical consequence, by the definition of classical truth tables.
2. A valuation $w$ into $\mathbf{4}$ is a pair of classical valuations $v_1, v_2$, with $w(\varphi) = (v_1(\varphi), v_2(\varphi))$ for all $\varphi$, by induction on $\varphi$, since the operations are coordinatewise.
3. $w(\varphi)$ is designated iff $v_1(\varphi) = 1$ and $v_2(\varphi) = 1$.
4. Suppose $\Gamma \models_{\mathbf{2}} \varphi$ and $w$ designates all of $\Gamma$. Then $v_1$ and $v_2$ make $\Gamma$ true, hence $\varphi$ true, so $w(\varphi)$ is designated.
5. Suppose $\Gamma \models_{\mathbf{4}} \varphi$ and $v$ makes $\Gamma$ true. The pair $(v, v)$ designates $\Gamma$, hence $\varphi$, so $v(\varphi) = 1$.

So classical logic is the logic of a two-element matrix, and it is not a [[many-valued logic|DWYCKAKXZD]] in the sense of the [[definition|66NMTCQNQV]].

## Remarks

The four-element matrix is the four-element [[Boolean algebra|0XADJKM699]] with its top element designated.
It shows that the number of values belongs to a matrix, not to a logic.
The condition of the definition that fails is that no two-element matrix gives the logic.
If instead the designated set of $\mathbf{4}$ is $\set{(1,0), (1,1)}$, the matrix again gives classical logic, through the first coordinate.

## Explanations

### L1 human

Classical logic uses two values, true and false.
One can also compute with pairs of truth values, one pair for two observers, and call a pair good when both say true.
This gives exactly the same laws and the same valid arguments.
So having four values on paper does not make a logic many-valued.

### L2 human

1. Take $\varphi = p \lor \neg p$ in $\mathbf{4}$, with $p = (0, 1)$.
2. Then $\neg p = (1, 0)$ and $p \lor \neg p = (1, 1)$, which is designated.
3. The same happens for every value of $p$, as for every classical [[tautology|05006AJ7DZ]].

The typical use is as a warning when one counts truth values.
A trap: the four-element matrix is a many-valued matrix, but its logic is not a many-valued logic, because a two-element matrix gives the same logic.
