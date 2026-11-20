---
tag: JW4MFX4Y8J
kind: proof
name: Proof of the cyclic property of the trace
msc: ["15A15"]
topics: [Y1ESNQ2V52]
audience: ug1
proves: 0Y4NF1DRKD
methods: [0NTF6DMVAP]
uses: [07PTPSZPME, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Trace_(linear_algebra)
    locator: Trace of a product
---

## Proof

We write both traces as the same double sum.

1. Write $A = (a_{ij})$ and $B = (b_{ji})$, with $1 \le i \le m$ and $1 \le j \le n$.
2. The [[product|076JGP6R3T]] $AB$ is $m \times m$ and $BA$ is $n \times n$. So both have a [[trace|07PTPSZPME]].
3. By the definition of the product, $(AB)_{ii} = \sum_{j=1}^{n} a_{ij} b_{ji}$. So $\operatorname{tr}(AB) = \sum_{i=1}^{m} \sum_{j=1}^{n} a_{ij} b_{ji}$.
4. In the same way, $(BA)_{jj} = \sum_{i=1}^{m} b_{ji} a_{ij}$. So $\operatorname{tr}(BA) = \sum_{j=1}^{n} \sum_{i=1}^{m} b_{ji} a_{ij}$.
5. The ring $R$ is commutative, so $b_{ji} a_{ij} = a_{ij} b_{ji}$ for all $i$ and $j$.
6. Addition in $R$ is associative and commutative, so a finite double sum does not depend on the order of summation.
7. By steps 5 and 6, the double sums in steps 3 and 4 are equal. So $\operatorname{tr}(AB) = \operatorname{tr}(BA)$.

## Idea

Both traces are the sum of $a_{ij} b_{ji}$ over all pairs $(i, j)$.
One trace sums first over $j$ and the other first over $i$.
Commutativity lets us match the factors.

## Variants

- By matrix units: both sides are bilinear in $A$ and $B$, so it is enough to take $A = E_{ij}$ and $B = E_{kl}$.
- Then $E_{ij} E_{kl} = \delta_{jk} E_{il}$ has trace $\delta_{jk} \delta_{il}$, and $E_{kl} E_{ij} = \delta_{li} E_{kj}$ has trace $\delta_{li} \delta_{kj}$, the same number; see [[matrix units|A4HTT7JFD1]].
