---
tag: 90RA6TAT7H
kind: conjecture
name: 11/8 conjecture
msc: [57K40, 57R55, 57R15]
uses: [8H58Q6YJCH, F45VQ47GPV, RSPZ9TCFQ8, WK8GKRKAVD, 07EZA80NEH]
about: [8H58Q6YJCH, WK8GKRKAVD]
sources:
  - url: https://en.wikipedia.org/wiki/4-manifold
history:
  posed_by: "Yukio Matsumoto"
  first_stated: "1982"
---

## Statement

Let $M$ be a closed, oriented, [[smooth|F45VQ47GPV]] [[4-manifold|8H58Q6YJCH]] that admits a [[spin structure|RSPZ9TCFQ8]].
Let $b_2(M)$ be the rank of $H_2(M; \Z)$ and $\sigma(M)$ the [[signature|07EZA80NEH]] of its [[intersection form|WK8GKRKAVD]].
Then
$$b_2(M) \ge \frac{11}{8} \abs{\sigma(M)}.$$

## Remarks

The conjecture is open.
The K3 surface has $b_2 = 22$ and $\sigma = -16$, so it attains equality.
For a simply connected $M$, the intersection form is even, and by [[Donaldson's theorem|34B7K77P31]] it is indefinite unless it is zero.
So it is a sum of copies of $\pm E_8$ and of the hyperbolic plane.
The conjecture then says that each pair of $E_8$ summands needs at least three hyperbolic summands, as in the K3 surface.
Mikio Furuta proved the $10/8$ theorem: if $\sigma(M) \ne 0$, then $b_2(M) \ge \frac{10}{8} \abs{\sigma(M)} + 2$.
Later work has improved the constant term of this bound.
Without smoothness the inequality fails: the [[$E_8$ manifold|BNDRN0G9BR]] is a closed topological manifold with an even form, $b_2 = 8$ and $\sigma = 8$.

## Explanations

### L1 human

For a smooth four-dimensional space of spin type, the conjecture compares two numbers read off from how surfaces cross inside it.
It predicts that the total number of independent surfaces is at least $11/8$ times the size of the signature.
The K3 surface, a famous complex surface, shows that $11/8$ cannot be improved.
