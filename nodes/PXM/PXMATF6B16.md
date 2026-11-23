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

We build an order on $\mathbb{N}$ that is the usual order in fact, but whose definition hides the consistency of PA.
Let $\operatorname{Prf}(z, \ulcorner 0 = 1 \urcorner)$ be the primitive recursive relation "$z$ codes a PA proof of $0 = 1$", as in the [[provability predicate|NB2BCZR40F]].
Define the primitive recursive predicate

$$B(x) :\equiv \exists z \le x \; \operatorname{Prf}(z, \ulcorner 0 = 1 \urcorner),$$

which says "a proof of $0 = 1$ with code at most $x$ exists".
Define $x \lhd y$ to hold exactly when one of these holds:

- $\neg B(x)$, $\neg B(y)$ and $x < y$;
- $B(x)$, $B(y)$ and $y < x$;
- $B(x)$ and $\neg B(y)$.

We check that $(\mathbb{N}, \lhd)$ is an [[ordinal notation system|3CNSYYX2HF]] of type $\omega$, and that PA does not prove [[transfinite induction|0ZHQMQ2C1N]] along it.

1. The relation $\lhd$ is primitive recursive, because the quantifier $\exists z \le x$ in $B$ is bounded; see [[primitive recursive relation|QQQRJA90EP]].
2. [[Peano arithmetic|0QFT7Z76N5]] is consistent, so no $z$ codes a proof of $0 = 1$, and $B(x)$ is false for every $x$.
3. So $x \lhd y$ holds exactly when $x < y$, and $\lhd$ is the usual well-order of $\mathbb{N}$, of type $\omega$.
4. PA proves that $\neg B$ is progressive along $\lhd$.
   Argue in PA: assume $\neg B(y)$ for all $y \lhd x$, and suppose $B(x)$.
   Then $B(x + 1)$ holds too, so $x + 1 \lhd x$ by the second clause, and the assumption gives $\neg B(x + 1)$, a contradiction.
5. Transfinite induction along $\lhd$ for $\neg B$ would turn step 4 into $\forall x \, \neg B(x)$, which is $\operatorname{Con}(\mathrm{PA})$.
6. By [[Gödel's second incompleteness theorem|4PZM5GJTR5]], PA does not prove $\operatorname{Con}(\mathrm{PA})$, so PA does not prove transfinite induction along $\lhd$.

## Remarks

The order $\lhd$ is a true well-order of the smallest infinite type, yet PA cannot prove it well-founded.
In contrast, PA proves transfinite induction along the standard notations up to every ordinal below $\varepsilon_0$.
So we cannot define the ordinal of a theory as "the least type of a notation system along which it fails to prove induction": by this example, PA would get $\omega$.
The supremum definition of the [[proof-theoretic ordinal|C72RBH0CDR]] is not affected, because a bad system only removes one case from the supremum.
The same construction works for every consistent recursively axiomatized theory $T$ that contains PA, with proofs in $T$ in place of proofs in PA.

## Explanations

### L1 human

The numbers $0, 1, 2, \ldots$ in their usual order are the simplest infinite list with no endless way down.
Here the same list is described by a strange rule: "use the usual order, unless arithmetic is contradictory, and in that case turn part of the list upside down".
Arithmetic is not contradictory, so the strange rule gives the usual order.
But arithmetic cannot prove its own consistency, so it cannot see that the list is the usual one.
So the length of a list does not show how hard it is to prove that it has no endless way down.

### L2 human

What would $\lhd$ look like if a proof of $0 = 1$ had the code $p$?
For $x < p$, $B(x)$ is false, and these numbers keep their usual order $0 \lhd 1 \lhd \cdots \lhd p - 1$.
For $x \ge p$, $B(x)$ is true, and these numbers come before all the others, in reverse order.
So the whole order would be

$$\cdots \lhd p + 2 \lhd p + 1 \lhd p \lhd 0 \lhd 1 \lhd \cdots \lhd p - 1,$$

and $p, p + 1, p + 2, \ldots$ would descend for ever.
So the well-foundedness of $\lhd$ is equivalent to the consistency of PA, and PA can prove this equivalence.
Watch out: "$T$ proves the well-foundedness of an order of type $\alpha$" says nothing until the order is given.
