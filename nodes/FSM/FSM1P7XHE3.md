---
tag: FSM1P7XHE3
kind: example
name: A variable that is both free and bound in one formula
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: ug2
instance_of: [9CNGDRAMGC]
uses: [Y3FZTH5158, HYJ10AF6RT]
sources:
  - url: https://en.wikipedia.org/wiki/Free_variables_and_bound_variables
    locator: lead section
  - book: isbn:9780122384523
    locator: Section 2.1
---

## Example

Let $P$ and $Q$ be unary relation symbols, and let
$$\varphi = (P(x) \land \forall x \, Q(x)).$$
We compute the free and bound variables of $\varphi$ by the [[recursive definition|Y3FZTH5158]].

1. $P(x)$ is atomic, so $\operatorname{FV}(P(x)) = \{ x \}$ and $\operatorname{BV}(P(x)) = \emptyset$.
2. $\operatorname{FV}(Q(x)) = \{ x \}$, so $\operatorname{FV}(\forall x \, Q(x)) = \{ x \} \setminus \{ x \} = \emptyset$.
3. $\operatorname{BV}(\forall x \, Q(x)) = \emptyset \cup \{ x \} = \{ x \}$.
4. The conjunction takes unions, so $\operatorname{FV}(\varphi) = \{ x \} \cup \emptyset = \{ x \}$ and $\operatorname{BV}(\varphi) = \emptyset \cup \{ x \} = \{ x \}$.
5. So $x \in \operatorname{FV}(\varphi) \cap \operatorname{BV}(\varphi)$.
6. Occurrence by occurrence, the $x$ in $P(x)$ lies in the scope of no quantifier, so it is free, and the $x$ in $Q(x)$ lies in the scope of $\forall x$, so it is bound.

## Remarks

The example shows that $\operatorname{FV}$ and $\operatorname{BV}$ need not be disjoint.
The two occurrences of $x$ stand for different things: the first is a value given from outside, and the second runs over the whole domain.

Renaming the bound variable gives the alpha-equivalent formula $P(x) \land \forall z \, Q(z)$, with $\operatorname{FV} = \{ x \}$ and $\operatorname{BV} = \{ z \}$.
This formula is logically equivalent to $\varphi$ and has no clash.

Watch out when you move quantifiers.
Pulling $\forall x$ to the front of $\varphi$ without renaming gives $\forall x \, (P(x) \land Q(x))$, which captures the free $x$.
That is a sentence with a different meaning.
After renaming, $\forall z \, (P(x) \land Q(z))$ is correct, and this is the first step toward a [[prenex normal form|CS82V969DE]].

## Explanations

### L1 human

Read $\varphi$ in the natural numbers, with $P$ meaning "is even" and $Q$ meaning "is at least $0$".
Then $\varphi$ says "$x$ is even, and every number is at least $0$".
The first $x$ is the number we ask about, and the second $x$ is a placeholder for "every number".
For $x = 4$ the claim is true, and for $x = 5$ it is false.

### L2 human

We check, with the same reading in $\mathbb{N}$, that renaming the bound $x$ changes nothing.
The formula $\forall x \, Q(x)$ is a sentence, and it is true, since every natural number is at least $0$.
The formula $\forall z \, Q(z)$ is a sentence, true for the same reason.
So $\varphi$ and $P(x) \land \forall z \, Q(z)$ both reduce to "$x$ is even", and they hold for the same values of $x$.
Now compare the wrong move $\forall x \, (P(x) \land Q(x))$: it says that every number is even, which is false, so it is not equivalent to $\varphi$ at $x = 4$.
