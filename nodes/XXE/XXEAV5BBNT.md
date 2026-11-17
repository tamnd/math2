---
tag: XXEAV5BBNT
kind: example
name: Unique factorization fails in Z[√-5]
msc: ["00A35", "11R04"]
topics: [X1NSTVGDNQ]
audience: ug2
not_instance_of:
  - target: 7KDT0R1HF2
    note: the analogy between Z[√-5] and the integers suggests unique factorization, but the step from irreducible to prime has no analogue, and the factorization of 6 is not unique
uses: [7KDT0R1HF2, 084HH1NDCB, 0BSJYCG7NM, 052SDEPZH7]
sources:
  - url: https://en.wikipedia.org/wiki/Unique_factorization_domain
    locator: Non-examples
---

## Example

Claim suggested by [[analogy|7KDT0R1HF2]]: in the ring $R = \mathbb{Z}[\sqrt{-5}] = \{a + b\sqrt{-5} : a, b \in \mathbb{Z}\}$, every nonzero non-unit is a product of irreducible elements in only one way, up to order and units, as in the [[fundamental theorem of arithmetic|084HH1NDCB]].
The analogy is natural: $R$ is a ring of numbers that contains $\mathbb{Z}$, with the same addition and multiplication rules.
We show that the claim is false.

1. The norm. For $\alpha = a + b\sqrt{-5}$ let $N(\alpha) = a^2 + 5b^2$. Then $N(\alpha\beta) = N(\alpha) N(\beta)$, by direct expansion.
2. The units. If $\alpha\beta = 1$, then $N(\alpha)N(\beta) = 1$, so $N(\alpha) = 1$, so $b = 0$ and $a = \pm 1$. The units are $\pm 1$.
3. Two factorizations of $6$: $6 = 2 \cdot 3$ and $6 = (1 + \sqrt{-5})(1 - \sqrt{-5})$, since $(1 + \sqrt{-5})(1 - \sqrt{-5}) = 1 - (-5) = 6$.
4. The norms of the factors are $N(2) = 4$, $N(3) = 9$ and $N(1 \pm \sqrt{-5}) = 6$.
5. No element has norm $2$ or $3$. If $b \ne 0$, then $a^2 + 5b^2 \ge 5$. If $b = 0$, then $a^2 \in \{2, 3\}$ has no integer solution.
6. So each of the four factors is [[irreducible|052SDEPZH7]]: a factorization into two non-units would split its norm $4$, $9$ or $6$ into two factors greater than $1$, so one factor would have norm $2$ or $3$.
7. The factorizations differ: $2$ is not a unit times $1 \pm \sqrt{-5}$, because the units are $\pm 1$ and $\pm 2 \ne 1 \pm \sqrt{-5}$.

So $6$ has two essentially different factorizations into irreducibles, and the claim fails.

The step of the integer proof that does not transfer is Euclid's lemma: "if an irreducible $p$ divides $xy$, then $p$ divides $x$ or $y$".
In $R$, the element $2$ divides $(1 + \sqrt{-5})(1 - \sqrt{-5}) = 6$, but $2$ divides neither factor, since $\frac{1 \pm \sqrt{-5}}{2} \notin R$.
In $\mathbb{Z}$, Euclid's lemma comes from division with remainder, and $R$ has no division with remainder of that kind.

## Remarks

The analogy was based on a likeness of objects, numbers of the form $a + b\sqrt{-5}$, and not on the relation that the proof uses, division with remainder.
This is the typical way in which an analogy misleads.
The page [[Z[√-5] is not a UFD|0BSJYCG7NM]] gives the same counterexample in the language of ring theory.

The error has a famous history.
In 1847 Gabriel Lamé presented to the Paris Academy a proof of Fermat's Last Theorem that factored $x^n + y^n$ in a ring of cyclotomic integers and assumed unique factorization there.
Ernst Kummer had already found that unique factorization fails in some of these rings, and his repair, ideal numbers, became the theory of ideals.

For $\mathbb{Z}[i]$, the Gaussian integers, the analogy does work: there is division with remainder for the norm $a^2 + b^2$, and unique factorization holds.

## Explanations

### L1 human

Among ordinary whole numbers, each number breaks into primes in only one way, for example $6 = 2 \cdot 3$.
It is natural to expect the same in a larger number system.
In the system of numbers $a + b\sqrt{-5}$, the number $6$ breaks in two ways: $2 \cdot 3$ and $(1 + \sqrt{-5})(1 - \sqrt{-5})$.
None of these four pieces can be broken further.
So the guess "it works like the whole numbers" is wrong here.

### L2 human

We find the failing step by testing the analogy on a simpler claim.

1. Claim in $\mathbb{Z}$: if $2$ divides $xy$, then $2$ divides $x$ or $y$.
2. Proof in $\mathbb{Z}$: an odd $x$ and an odd $y$ have an odd product.
3. Test in $R$: $x = 1 + \sqrt{-5}$, $y = 1 - \sqrt{-5}$, $xy = 6 = 2 \cdot 3$.
4. Does $2$ divide $x$? That would need $\frac{1}{2} + \frac{1}{2}\sqrt{-5} \in R$, which fails since $\frac{1}{2} \notin \mathbb{Z}$.

The typical use of such a test: before a transfer, check the lemma on which the old proof rests.

A trap: the claim "every element is a product of irreducibles" does transfer to $R$, by induction on the norm; only uniqueness fails.
