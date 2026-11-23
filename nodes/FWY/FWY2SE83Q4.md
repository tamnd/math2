---
tag: FWY2SE83Q4
kind: example
name: PA plus the negation of Con(PA) proves an ill-founded order well-founded
msc: ["03F15", "03F40"]
topics: [XTTKZTYDSD]
audience: grad
not_instance_of:
  - target: C72RBH0CDR
    note: the theory is consistent but not sound, so the orders it proves well-founded need not be well-orders, and the supremum without the well-order condition would not be a proof-theoretic ordinal
uses: [C19Z3B6V4P, 0QFT7Z76N5, NB2BCZR40F, VM8TQ70CVJ, 4PZM5GJTR5, QQQRJA90EP, PXMATF6B16]
sources:
  - url: https://en.wikipedia.org/wiki/Ordinal_analysis
    locator: Definition
---

## Example

Let $T = \mathrm{PA} + \neg\operatorname{Con}(\mathrm{PA})$, where $\operatorname{Con}(\mathrm{PA})$ is the [[consistency|VM8TQ70CVJ]] sentence built from the [[provability predicate|NB2BCZR40F]].
We build an order that $T$ proves well-founded, although in fact it runs downward forever.
Let $\operatorname{Prf}(z, y)$ be the primitive recursive relation "$z$ codes a PA-proof of the formula with code $y$".
Let $B(x)$ be $\exists z \le x \, \operatorname{Prf}(z, \ulcorner 0 = 1 \urcorner)$, a [[primitive recursive relation|QQQRJA90EP]] that says "a proof of $0 = 1$ has appeared by time $x$".
Define $x \triangleleft y$ by
$$(\neg B(x) \wedge \neg B(y) \wedge y < x) \vee (B(x) \wedge B(y) \wedge x < y) \vee (\neg B(x) \wedge B(y)).$$
In words: the numbers before the first proof of $0 = 1$ come first, in reverse order, and the numbers after it follow in the usual order.

1. $T$ is consistent.
   If it were not, PA would prove $\operatorname{Con}(\mathrm{PA})$, which [[Gödel's second incompleteness theorem|4PZM5GJTR5]] rules out.
2. The relation $\triangleleft$ is primitive recursive, since $B$ and $<$ are.
3. In $\mathbb{N}$, PA is consistent, so $B(x)$ is false for every $x$.
   Then $x \triangleleft y$ holds exactly when $y < x$.
4. So $n + 1 \triangleleft n$ for every $n$, and $0, 1, 2, \ldots$ is an infinite descending sequence.
   The order $\triangleleft$ is not well-founded.
5. Inside $T$, let $p$ be the least $z$ with $\operatorname{Prf}(z, \ulcorner 0 = 1 \urcorner)$.
   It exists by $\neg\operatorname{Con}(\mathrm{PA})$ and the least number principle, and $B(x)$ holds exactly when $x \ge p$.
6. So inside $T$ the order lists $p - 1, p - 2, \ldots, 0$ first, and then $p, p + 1, p + 2, \ldots$ in the usual order.
   Its order type is $p + \omega = \omega$.
7. $T$ proves $\operatorname{TI}(\triangleleft, X)$.
   Assume that $X$ is progressive, and show $X(x)$ for $p - k \le x < p$ by induction on $k \le p$.
   The elements below $p - k - 1$ are exactly the numbers from $p - k$ to $p - 1$, so each step uses progressiveness once.
8. Then strong induction on $x \ge p$ gives $X(x)$, since below $x$ lie the numbers less than $p$ and the numbers from $p$ to $x - 1$.
9. So $T$ proves transfinite induction along $\triangleleft$, but $\triangleleft$ is not a well-order.

## Remarks

The example shows why the definition of the [[proof-theoretic ordinal|C19Z3B6V4P]] takes the supremum only over true well-orders.
It also shows why the bound $\lvert T \rvert < \omega_1^{\mathrm{CK}}$ assumes that $T$ proves only true $\Pi^1_1$ sentences.
Here $T$ proves the false $\Sigma_1$ sentence $\neg\operatorname{Con}(\mathrm{PA})$, so it is not even $\Sigma_1$-sound.

Compare it with [[the artificial notation system|PXMATF6B16]], which goes wrong in the opposite direction.
There, PA cannot prove induction along a true well-order of type $\omega$.
Here, $T$ proves induction along an order that is not well-founded.
In both cases the trick is the same: the order depends on whether a proof of $0 = 1$ exists.

## Explanations

### L1 human

A theory can be free of contradictions and still believe false things.
This theory believes that arithmetic is inconsistent, which is false.
We build an ordering of the numbers that looks harmless if arithmetic is inconsistent, but in fact runs downward forever.
The theory proves that induction works along this ordering.
So a theory's trust in an ordering means nothing unless the theory is sound.

### L2 human

We test the order on small numbers.

1. In the standard model $\mathbb{N}$, no $x$ codes a proof of $0 = 1$, so $B$ is always false.
2. Then $3 \triangleleft 2 \triangleleft 1 \triangleleft 0$, and the chain continues downward without end.
3. Inside $T$, suppose that the least proof of $0 = 1$ has code $p = 3$.
4. Then the order is $2, 1, 0, 3, 4, 5, \ldots$, a well-order of type $3 + \omega = \omega$.

The typical use is to explain the soundness hypothesis in results about proof-theoretic ordinals.
Watch out: consistency of $T$ is not enough, and $T$ must also prove only true $\Pi^1_1$ sentences.
