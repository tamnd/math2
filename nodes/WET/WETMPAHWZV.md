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

Let $\mathbf{2}$ be the matrix with values $\{0, 1\}$, designated set $\{1\}$ and the classical tables for $\neg, \land, \lor, \to$.
Let $\mathbf{4} = \mathbf{2} \times \mathbf{2}$ have the values $(0,0), (0,1), (1,0), (1,1)$, the operations taken coordinate by coordinate, and the designated set $\{(1, 1)\}$.
We show that both matrices give the classical consequence relation.

1. The matrix $\mathbf{2}$ gives classical consequence, by the definition of the classical truth tables.
2. A valuation $w$ into $\mathbf{4}$ is a pair of classical valuations $v_1, v_2$ on the variables.
   Since the operations work coordinate by coordinate, induction on $\varphi$ gives $w(\varphi) = (v_1(\varphi), v_2(\varphi))$ for every formula.
3. So $w(\varphi)$ is designated iff $v_1(\varphi) = 1$ and $v_2(\varphi) = 1$.
4. Suppose $\Gamma \models_{\mathbf{2}} \varphi$ and $w$ designates all of $\Gamma$.
   Then $v_1$ and $v_2$ both make $\Gamma$ true, so both make $\varphi$ true, and $w(\varphi)$ is designated.
5. Suppose $\Gamma \models_{\mathbf{4}} \varphi$ and a classical $v$ makes $\Gamma$ true.
   The pair $(v, v)$ designates $\Gamma$, so it designates $\varphi$, and $v(\varphi) = 1$.

Steps 4 and 5 show that $\models_{\mathbf{2}}$ and $\models_{\mathbf{4}}$ are the same relation.
So classical logic is the logic of a two-element matrix, and it is not a [[many-valued logic|DWYCKAKXZD]] in the sense of the [[definition|66NMTCQNQV]].

## Remarks

The matrix $\mathbf{4}$ is the four-element [[Boolean algebra|0XADJKM699]] with its top element designated.
It has four values, yet its logic is classical, so the number of values belongs to a matrix, not to a logic.
The condition of the definition that fails is the last one: a two-element matrix gives the same logic.

Change the designated set of $\mathbf{4}$ to $\{(1,0), (1,1)\}$.
Then $w(\varphi)$ is designated iff $v_1(\varphi) = 1$, and the same argument, with the first coordinate only, again gives classical logic.
The same holds for every finite Boolean algebra with its top element designated, since such an algebra is a power of $\mathbf{2}$.

## Explanations

### L1 human

Classical logic uses two values, true and false.
You can also compute with pairs of truth values, one value from each of two observers, and call a pair good when both observers say true.
This gives exactly the same laws and the same valid arguments as the two values alone.
So having four values on paper does not make a logic many-valued.

### L2 human

Take $\varphi = p \lor \neg p$ in $\mathbf{4}$, with $p = (0, 1)$.
Negation flips each coordinate, so $\neg p = (1, 0)$, and disjunction takes the larger value in each coordinate:
$$p \lor \neg p = (\max(0, 1), \max(1, 0)) = (1, 1).$$
That value is designated, and the same happens for every value of $p$, as for every classical [[tautology|05006AJ7DZ]].
The typical use of the example is as a warning when you count truth values.
Watch out: $\mathbf{4}$ is a many-valued matrix, but its logic is not a many-valued logic, because a two-element matrix gives the same logic.
