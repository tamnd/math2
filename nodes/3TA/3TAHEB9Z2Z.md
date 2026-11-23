---
tag: 3TAHEB9Z2Z
kind: example
name: Algebraically closed fields are infinitely generic
aliases: [algebraically-closed-fields-infinitely-generic]
msc: ["03C25", "12F05"]
topics: [1A9JSC5YG8]
audience: research
instance_of: [2TYY0ZP7YQ]
uses: [04C5ZBG1WT, 0PF6TM8TWT, 0QVD7WBFGN, 61VW0F3R83, 2STE7K6ERM, HYJ10AF6RT]
sources:
  - url: https://en.wikipedia.org/wiki/Existentially_closed_model
    locator: Examples
  - book: isbn:9780521587136
---

## Example

Let $T$ be the theory of [[fields|04C5ZBG1WT]] in $L = \set{+, -, \cdot, 0, 1}$.
The models of $T_\forall$ are the [[integral domains|0QVD7WBFGN]], since these are the substructures of fields.
We show that an [[algebraically closed field|0PF6TM8TWT]] $K$ is infinitely generic: $K \Vdash \varphi \iff K \models \varphi$ for every sentence $\varphi$ with parameters in $K$ built with $\neg$, $\land$ and $\exists$.
We prove this for all algebraically closed fields at once, by induction on the [[formula|HYJ10AF6RT]] $\varphi$.

1. Atomic $\varphi$: $K \Vdash \varphi$ means $K \models \varphi$, by definition.
2. $\varphi \land \psi$: both sides split into the two parts, and the induction hypothesis applies to each.
3. $\exists x \, \varphi(x)$: $K \Vdash \exists x \, \varphi(x)$ means $K \Vdash \varphi(a)$ for some $a \in K$. By the induction hypothesis this means $K \models \varphi(a)$ for some $a$, that is, $K \models \exists x \, \varphi(x)$.
4. $\neg \varphi$, first direction. Suppose $K \Vdash \neg \varphi$. Then $K$ itself does not force $\varphi$, so $K \not\models \varphi$ by the induction hypothesis, and $K \models \neg \varphi$.
5. $\neg \varphi$, second direction. Suppose $K \models \neg \varphi$ and some integral domain $D \supseteq K$ forces $\varphi$. Let $K'$ be an algebraic closure of the fraction field of $D$. Forcing is monotone, so $K' \Vdash \varphi$, and $K' \models \varphi$ by the induction hypothesis for $K'$.
6. The inclusion $K \subseteq K'$ is an inclusion of algebraically closed fields, so it is [[elementary|61VW0F3R83]], and $K \models \varphi$. This contradicts $K \models \neg \varphi$. So no such $D$ exists, and $K \Vdash \neg \varphi$.

So every algebraically closed field is infinitely generic.

## Remarks

Conversely, every infinitely generic field is e.c., so it is algebraically closed by [[this example|2STE7K6ERM]].
So the infinitely generic models of the theory of fields are exactly the algebraically closed fields, and $T^F = \mathrm{ACF}$.

The proof uses only that $\mathrm{ACF}$ is model complete and that every integral domain embeds into a model of $\mathrm{ACF}$.
So the same steps show that the models of the model companion of any inductive theory are infinitely generic.
For groups, where there is no model companion, step 6 has no analogue, and the infinitely generic groups must be found by a construction.

## Explanations

### L1 human

In an algebraically closed field, every polynomial equation that could be solved in a bigger field is already solved.
So when forcing asks "can this statement still become true in a larger domain?", the field already knows the answer.
That is why forcing and truth agree in it.

### L2 human

We check the case $\varphi = \exists x \, (x \cdot x = 2)$ in the algebraic closure $K = \overline{\Q}$.

1. $K$ contains $\sqrt 2$, so $K \models \varphi$.
2. The atomic sentence $\sqrt 2 \cdot \sqrt 2 = 2$ is true in $K$, so $K \Vdash \varphi$ by the atomic and the existential clauses.
3. The negation $\neg \varphi$ is not forced, since $K$ itself forces $\varphi$.

So forcing and truth agree on $\varphi$ and on $\neg \varphi$.
The typical use of the example is as the model case: when a model companion exists, forcing gives nothing new.
A trap is to forget step 5: the negation clause looks at all integral domains above $K$, not only at fields.
