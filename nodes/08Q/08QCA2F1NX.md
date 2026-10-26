---
tag: 08QCA2F1NX
kind: statement
role: proposition
name: Independence means the joint law is the product of the marginals
msc: [60A05]
uses: [0E9502NT92, 0QAR0XDZH4, 0AXP2Z5N9H, 0TST4MHA3A]
sources:
  - url: https://en.wikipedia.org/wiki/Independence_(probability_theory)
    locator: Two random variables
---

## Statement

Let $X$ and $Y$ be random variables on one probability space, with values in measurable spaces $(E_1, \mathcal{E}_1)$ and $(E_2, \mathcal{E}_2)$.
Let $\mu_X$ and $\mu_Y$ be their laws, and let $\mu_{(X, Y)}$ be the [[joint law|0QAR0XDZH4]] of the pair $(X, Y)$ on $E_1 \times E_2$.
Then $X$ and $Y$ are [[independent|0E9502NT92]] if and only if $\mu_{(X, Y)} = \mu_X \otimes \mu_Y$, the product measure of the two [[marginal laws|0AXP2Z5N9H]].

## Remarks

The statement is a direct translation of the definition: $\mu_{(X, Y)}(A \times B) = P(X \in A, Y \in B)$ and $(\mu_X \otimes \mu_Y)(A \times B) = \mu_X(A) \, \mu_Y(B)$.
Two probability measures on $E_1 \times E_2$ that agree on all rectangles $A \times B$ are equal, because the rectangles form a π-system that generates the product σ-algebra.
For real random variables, it follows that $F_{(X, Y)}(x, y) = F_X(x) \, F_Y(y)$. If $X$ and $Y$ have densities, the joint density is $f_X(x) \, f_Y(y)$.
The same result holds for $n$ random variables: they are independent if and only if their joint law is $\mu_{X_1} \otimes \dots \otimes \mu_{X_n}$.

## Explanations

### L1 human

For independent variables, the full joint picture is fixed by the two separate pictures.
You find the chance of a pair of outcomes by multiplying the chances of the two outcomes.
