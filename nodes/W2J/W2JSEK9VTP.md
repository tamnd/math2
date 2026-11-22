---
tag: W2JSEK9VTP
kind: proof
name: Proof that projections correspond to direct sum decompositions
msc: ["15A04"]
topics: [QHKTJ89V6S]
audience: ug1
proves: 2ZX5Q7V4VN
methods: [0NTF6DMVAP, 01XM7JEKHY]
uses: [0RH4E3CAV9, 041JTZCK9Q, 20A0K3KBZD, 02YFME3RGW, 0JB228DCWB]
sources:
  - url: https://en.wikipedia.org/wiki/Projection_(linear_algebra)
    locator: Properties and classification
  - book: isbn:9783031410253
    locator: Section 3E
---

## Proof

We split each vector as $v = Pv + (v - Pv)$ for part 1, we check linearity and idempotence of $P_{U, W}$ for part 2, and we compose the two constructions for part 3.

For part 1, let $P$ be a [[projection|0RH4E3CAV9]] on $V$.

1. Let $v \in \operatorname{im} P$, the [[image|0JB228DCWB]], so $v = P x$ for some $x \in V$.
   Then $P v = P^2 x = P x = v$, so $P$ fixes each vector of its image.
2. For $v \in V$, write $v = P v + (v - P v)$.
   The first term lies in $\operatorname{im} P$.
   The second term lies in the [[kernel|02YFME3RGW]], because $P(v - P v) = P v - P^2 v = 0$.
   Hence $V = \operatorname{im} P + \ker P$.
3. If $v \in \operatorname{im} P \cap \ker P$, then $v = P v$ by step 1, and $P v = 0$ since $v \in \ker P$.
   So $v = 0$.
4. By the [[criteria for a direct sum|20A0K3KBZD]], steps 2 and 3 give $V = \operatorname{im} P \oplus \ker P$.
5. We compute $(I - P)^2 = I - 2P + P^2 = I - 2P + P = I - P$, so $I - P$ is a projection.
6. If $v \in \ker P$, then $(I - P) v = v - 0 = v$, so $v \in \operatorname{im}(I - P)$ and $\ker P \subseteq \operatorname{im}(I - P)$.
   Conversely $P (I - P) = P - P^2 = 0$, so $\operatorname{im}(I - P) \subseteq \ker P$.
7. The equation $(I - P) v = 0$ means $P v = v$.
   This holds for every $v \in \operatorname{im} P$ by step 1, and if $P v = v$ then $v$ is in $\operatorname{im} P$.
   So $\ker(I - P) = \operatorname{im} P$.

For part 2, let $V = U \oplus W$ be a [[direct sum|041JTZCK9Q]].

8. Each $v \in V$ has exactly one decomposition $v = u + w$ with $u \in U$ and $w \in W$, so $P_{U, W}(v) = u$ is well defined.
9. Let $v = u + w$ and $v' = u' + w'$, and let $a \in F$.
   Then $v + v' = (u + u') + (w + w')$ and $a v = a u + a w$ are decompositions of $v + v'$ and of $a v$, so by uniqueness they are the decompositions.
   Hence $P_{U, W}(v + v') = u + u'$ and $P_{U, W}(a v) = a u$, and $P_{U, W}$ is linear.
10. For $u \in U$ the decomposition is $u = u + 0$, so $P_{U, W}(u) = u$.
    Hence $P_{U, W}^2 (v) = P_{U, W}(u) = u = P_{U, W}(v)$ for every $v = u + w$.
11. The image lies in $U$ by definition, and it contains $U$ by step 10, so the image is $U$.
12. We have $P_{U, W}(u + w) = 0$ exactly when $u = 0$, that is, when $v = w \in W$.
    So the kernel is $W$.

For part 3, we show that the two maps are inverse to each other.

13. Start from a pair $(U, W)$ with $V = U \oplus W$.
    By part 2, the projection $P_{U, W}$ has image $U$ and kernel $W$, so going to the projection and back returns $(U, W)$.
14. Start from a projection $P$, and let $U = \operatorname{im} P$ and $W = \ker P$.
    By step 2, the decomposition of $v$ in $U \oplus W$ is $v = P v + (v - P v)$, so $P_{U, W}(v) = P v$.
    Hence $P_{U, W} = P$, and going to the pair and back returns $P$.
15. So the two maps are inverse to each other, and both are bijections.

## Idea

Everything rests on the identity $v = P v + (I - P) v$.
The equation $P^2 = P$ forces the first part into the image and the second part into the kernel, and a vector in both is fixed by $P$ and killed by $P$, so it is $0$.
In the other direction, a unique decomposition defines the map that keeps one part, and uniqueness is exactly what makes that map linear.

## Variants

Part 1 can also be done with polynomials.
The equation $P^2 = P$ says that the polynomial $x^2 - x = x(x - 1)$ kills $P$.
Its two roots $0$ and $1$ are distinct, so $P$ is diagonalizable and $V$ is the direct sum of the eigenspaces for $1$ and $0$, which are $\operatorname{im} P$ and $\ker P$.
The polynomial identity $1 = x - (x - 1)$ gives the splitting $v = Pv - (P - I)v$ that the proof above uses.

The same proof works word for word for modules over any ring.
There it shows that the direct summands of a module are exactly the images of its idempotent endomorphisms.
