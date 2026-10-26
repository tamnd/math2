---
tag: 0BSJYCG7NM
kind: counterexample
name: Z[√-5] is not a UFD
msc: [11R11]
uses: [06YMXJMXYS, 052SDEPZH7, 053E86NWVK]
sources:
  - url: https://en.wikipedia.org/wiki/Unique_factorization_domain
    locator: Non-examples
---

## Counterexample

The integral domain $\mathbb{Z}[\sqrt{-5}] = \{a + b\sqrt{-5} : a, b \in \mathbb{Z}\}$ is not a [[unique factorisation domain|06YMXJMXYS]].
In this ring,
$$6 = 2 \cdot 3 = (1 + \sqrt{-5})(1 - \sqrt{-5}).$$
Let $N(a + b\sqrt{-5}) = a^2 + 5b^2$. Then $N$ is multiplicative, and $N(2) = 4$, $N(3) = 9$, $N(1 \pm \sqrt{-5}) = 6$.
No element has norm $2$ or $3$, because $a^2 + 5b^2 \notin \{2, 3\}$ for integers $a, b$. So the four factors are [[irreducible|052SDEPZH7]].
The only units are $\pm 1$, so $2$ is not an [[associate|053E86NWVK]] of $1 + \sqrt{-5}$ or of $1 - \sqrt{-5}$. The two factorisations are different.

## Remarks

The element $2$ is [[irreducible but not prime|0CHE3J7QMX]] in this ring.
Every nonzero nonunit of $\mathbb{Z}[\sqrt{-5}]$ is still a product of irreducibles. Only the uniqueness fails.
Unique factorisation holds again for ideals: $\mathbb{Z}[\sqrt{-5}]$ is a Dedekind domain.

## Explanations

### L1 human

The number $6$ has two essentially different factorisations into irreducible elements in this ring.
The norm shows that none of the four factors can be split further.
So unique factorisation, which we take for granted in the integers, can fail.
