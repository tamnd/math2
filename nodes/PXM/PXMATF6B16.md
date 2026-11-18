---
tag: PXMATF6B16
kind: example
name: An artificial notation system of type ω
msc: ["03F15", "03F30"]
topics: [XTTKZTYDSD]
audience: research
instance_of: [7MBX59Y7N9]
uses: [3CNSYYX2HF, 0QFT7Z76N5, NB2BCZR40F, 4PZM5GJTR5, QQQRJA90EP, 0ZHQMQ2C1N]
sources:
  - url: https://en.wikipedia.org/wiki/Ordinal_analysis
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Gödel%27s_incompleteness_theorems
    locator: Second incompleteness theorem
---

## Example

Let $\operatorname{Prf}(z, \ulcorner 0 = 1 \urcorner)$ be the primitive recursive relation "$z$ codes a PA-proof of $0 = 1$", as in the [[provability predicate|NB2BCZR40F]].
Define the primitive recursive predicate
$$B(x) :\equiv \exists z \le x \; \operatorname{Prf}(z, \ulcorner 0 = 1 \urcorner).$$
So $B(x)$ says "a proof of $0 = 1$ with code at most $x$ exists".
Define a relation $\lhd$ on $\N$ by: $x \lhd y$ if and only if one of the following holds.

- $\neg B(x)$, $\neg B(y)$ and $x < y$.
- $B(x)$, $B(y)$ and $y < x$.
- $B(x)$ and $\neg B(y)$.

We check that $(\N, \lhd)$ is an [[ordinal notation system|3CNSYYX2HF]] of type $\omega$, and that PA does not prove [[transfinite induction|0ZHQMQ2C1N]] along it.

1. The relation $\lhd$ is primitive recursive, because $B$ is: the quantifier $\exists z \le x$ is bounded. See [[primitive recursive relation|QQQRJA90EP]].
2. [[Peano arithmetic|0QFT7Z76N5]] is consistent, so no $z$ codes a proof of $0 = 1$, and $B(x)$ is false for every $x$.
3. So $x \lhd y$ holds if and only if $x < y$. The order $\lhd$ is the usual order of $\N$, a well-order of type $\omega$.
4. PA proves $\operatorname{Prog}(\neg B)$. In PA, assume that $\neg B(y)$ for all $y \lhd x$, and assume $B(x)$. Then $B(x + 1)$ and $x + 1 \lhd x$ by the second clause, so $\neg B(x + 1)$, a contradiction, and hence $\neg B(x)$.
5. Transfinite induction along $\lhd$ for $\neg B$ is $\operatorname{Prog}(\neg B) \to \forall x \, \neg B(x)$. With step 4 it gives $\forall x \, \neg B(x)$, which is $\operatorname{Con}(\mathrm{PA})$.
6. By [[Gödel's second incompleteness theorem|4PZM5GJTR5]], PA does not prove $\operatorname{Con}(\mathrm{PA})$. So PA does not prove transfinite induction along $\lhd$ for $\neg B$.

## Remarks

The order $\lhd$ is a true well-order of the smallest infinite type, but PA cannot prove this, because the definition hides the consistency of PA.
In contrast, PA proves transfinite induction along the standard notations up to every ordinal below $\varepsilon_0$.
So the proof-theoretic ordinal of a theory cannot be defined as "the least type of a notation system along which the theory fails to prove induction".
With this example, that value would be $\omega$ for PA.
The same construction works for every consistent recursively axiomatized theory $T$ that contains PA, with proofs in $T$ in place of proofs in PA.
This is the reason why ordinal analysis fixes natural notation systems, or uses the $\Pi^1_1$ definition of the [[proof-theoretic ordinal|C72RBH0CDR]].

## Explanations

### L1 human

The numbers $0, 1, 2, \ldots$ in their usual order are the simplest infinite list with a first element and no endless way down.
Here the same list is described by a strange rule: "use the usual order, unless arithmetic is contradictory, and then turn part of the list upside down".
Arithmetic is not contradictory, so the strange rule gives the usual order.
But arithmetic cannot prove its own consistency, so it cannot see that the list is the usual one.
So the length of a list does not show how hard it is to prove that it has no endless way down.

### L2 human

We follow the order $\lhd$ in an imagined case where a proof of $0 = 1$ has the code $p$.

1. For $x < p$, $B(x)$ is false, and these numbers come in the usual order $0 \lhd 1 \lhd \cdots \lhd p - 1$.
2. For $x \ge p$, $B(x)$ is true, and these numbers come before all the others, in reverse order.
3. So $\cdots \lhd p + 2 \lhd p + 1 \lhd p \lhd 0 \lhd 1 \lhd \cdots \lhd p - 1$, and the sequence $p, p + 1, p + 2, \ldots$ descends for ever.

So the well-foundedness of $\lhd$ is equivalent to the consistency of PA, and PA can prove this equivalence.
The trap: a statement such as "theory $T$ proves the well-foundedness of an order of type $\alpha$" says nothing until the order is given.
