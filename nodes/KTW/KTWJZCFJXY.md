---
tag: KTWJZCFJXY
kind: example
name: The constant domain axiom is valid in every first-order Gödel logic
msc: ["03B52", "03B55"]
topics: [WZP584JQ06]
audience: research
instance_of: [H8C323CV3T]
uses: [42GA7FHGW2]
sources:
  - url: https://plato.stanford.edu/entries/logic-manyvalued/
    locator: 6.2 Many-valued first-order logics
---

## Example

The *constant domain axiom* is $\forall x (p \lor Q(x)) \to (p \lor \forall x Q(x))$, where $x$ is not free in $p$.
We show that it has value $1$ in every $V$-structure $\mathfrak{M}$ of a [[first-order Gödel logic|H8C323CV3T]].
Let $a$ be the value of $p$, let $b_d$ be the value of $Q(d)$ for $d \in M$, and let $b = \inf_d b_d$.

1. The value of the antecedent is $\inf_d \max(a, b_d)$, and the value of the consequent is $\max(a, b)$.
2. In the case $a \ge b$, we have $\max(a, b_d) \ge a$ for all $d$, so the antecedent is at least $a$.
3. Let $\varepsilon > 0$.
   Since $\inf_d b_d = b \le a$, some $d$ has $b_d < a + \varepsilon$, so $\max(a, b_d) < a + \varepsilon$.
4. So in this case the antecedent is $a = \max(a, b)$.
5. In the case $a < b$, we have $b_d \ge b > a$ for all $d$, so $\max(a, b_d) = b_d$.
6. So in this case the antecedent is $\inf_d b_d = b = \max(a, b)$.
7. In both cases the antecedent equals the consequent, and the Gödel implication $x \to x$ has value $1$.

For a numeric check, take $M = \mathbb{N}$, $a = 0.3$ and $b_n = \tfrac{1}{n+1}$.

8. The value $\max(0.3, \tfrac{1}{n+1})$ is $\tfrac{1}{n+1}$ for $n \le 2$ and $0.3$ for $n \ge 3$, so the infimum is $0.3$.
9. The consequent is $\max(0.3, 0) = 0.3$, and $0.3 \to 0.3 = 1$.

## Remarks

The proof uses only that the truth values form a chain, on which $\max(a, \cdot)$ commutes with infima.
In intuitionistic predicate logic the axiom fails, and [[a Kripke model with growing domains|42GA7FHGW2]] refutes it.
So every first-order Gödel logic proves a sentence that intuitionistic predicate logic does not prove.

The two-world Kripke countermodel has a linear frame, so it validates prelinearity.
Hence prelinearity alone does not give the constant domain axiom, and the axiom is a separate law of Gödel logics.

## Explanations

### L1 human

"For every $x$, $p$ or $Q(x)$" and "$p$, or for every $x$, $Q(x)$" get the same degree in Gödel logic.
The reason is that degrees of truth form a single line, and the set of objects is fixed.

### L2 human

Compare $a$ with the infimum $b$ of the values of $Q$.
If $a$ is at least $b$, both sides are $a$, and otherwise both sides are $b$.
Watch out: the step "some $d$ has $b_d < a + \varepsilon$" needs $b \le a$, and the infimum need not be attained.
