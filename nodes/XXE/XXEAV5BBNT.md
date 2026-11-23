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

The ring $R = \mathbb{Z}[\sqrt{-5}] = \{a + b\sqrt{-5} : a, b \in \mathbb{Z}\}$ contains $\mathbb{Z}$ and has the same rules of addition and multiplication.
An [[analogy|7KDT0R1HF2]] with the integers suggests the claim that every nonzero non-unit of $R$ factors into irreducible elements in only one way, up to order and units, as in the [[fundamental theorem of arithmetic|084HH1NDCB]].
We show that the claim is false.

1. We define a norm.
   For $\alpha = a + b\sqrt{-5}$ let $N(\alpha) = a^2 + 5b^2$.
   Expanding both sides shows $N(\alpha\beta) = N(\alpha) N(\beta)$.
2. We find the units.
   If $\alpha\beta = 1$, then $N(\alpha) N(\beta) = 1$, so $N(\alpha) = 1$, which forces $b = 0$ and $a = \pm 1$.
   So the units are $\pm 1$.
3. We write $6$ in two ways:
   $$6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5}),$$
   where the second product is $1 - (-5) = 6$.
4. We compute the norms of the four factors: $N(2) = 4$, $N(3) = 9$ and $N(1 \pm \sqrt{-5}) = 6$.
5. We show that no element has norm $2$ or $3$.
   If $b \ne 0$, then $a^2 + 5b^2 \ge 5$, and if $b = 0$, then $a^2 = 2$ or $a^2 = 3$ has no integer solution.
6. We conclude that the four factors are [[irreducible|052SDEPZH7]].
   A splitting into two non-units would split the norm $4$, $9$ or $6$ into two factors greater than $1$, so one factor would have norm $2$ or $3$, which step 5 rules out.
7. We check that the two factorizations really differ.
   The units are $\pm 1$, and $\pm 2 \ne 1 \pm \sqrt{-5}$, so $2$ is not a unit times either factor on the right.

So $6$ has two essentially different factorizations into irreducible elements, and the claim fails.

## Remarks

Which step of the integer proof fails to transfer?
It is Euclid's lemma: if an irreducible element divides a product, it divides one of the factors.
In $R$, the element $2$ divides $(1 + \sqrt{-5})(1 - \sqrt{-5}) = 6$ but divides neither factor, since $\frac{1}{2} \pm \frac{1}{2}\sqrt{-5}$ is not in $R$.
In $\mathbb{Z}$, Euclid's lemma comes from division with remainder, and $R$ has no division with remainder for its norm.

The analogy rested on a likeness of the objects, numbers of the form $a + b\sqrt{-5}$, and not on the relation that the proof uses.
That is the typical way an analogy misleads.
For the Gaussian integers $\mathbb{Z}[i]$ the analogy does work, because division with remainder holds for the norm $a^2 + b^2$, and unique factorization follows.
The counterexample in the language of ring theory is [[Z[√-5] is not a UFD|0BSJYCG7NM]].

The same trap has a famous history.
In 1847 Gabriel Lamé presented to the Paris Academy a proof of Fermat's Last Theorem that factored $x^n + y^n$ in a ring of cyclotomic integers and assumed unique factorization there.
Ernst Kummer had already found that unique factorization fails in some of these rings, and his repair, ideal numbers, grew into the theory of ideals.

## Explanations

### L1 human

Among whole numbers, each number breaks into primes in only one way, for example $6 = 2 \cdot 3$.
It is natural to expect the same in a larger number system.
In the system of numbers $a + b\sqrt{-5}$, the number $6$ breaks in two ways, as $2 \cdot 3$ and as $(1 + \sqrt{-5})(1 - \sqrt{-5})$.
None of the four pieces breaks any further.
So the guess "it works like the whole numbers" is wrong here.

### L2 human

The quick way to catch a false analogy is to test the lemma that the old proof uses.
In $\mathbb{Z}$, if $2$ divides $xy$, then $2$ divides $x$ or $y$, because an odd number times an odd number is odd.
In $R$, take $x = 1 + \sqrt{-5}$ and $y = 1 - \sqrt{-5}$, so that
$$xy = 6 = 2 \cdot 3.$$
For $2$ to divide $x$ we would need $\frac{1}{2} + \frac{1}{2}\sqrt{-5} \in R$, and $\frac{1}{2}$ is not an integer, so the lemma fails.

The typical use of such a test is to run it before a transfer, on the one lemma the old proof rests on.
Watch out: not everything fails.
The claim "every nonzero non-unit is a product of irreducible elements" does transfer to $R$, by induction on the norm; only the uniqueness fails.
