---
tag: TANAFVY929
kind: proof
name: Proof of the derivative test for repeated roots
msc: [13F20]
proves: 067F8YVYMH
uses: [0GYGHKX834, 0AD4VS02H3, 03XVP8Q4GY, 0K3MWA7DMC, 0125QVNCFQ, 00EHX6FWC0]
sources:
  - url: https://en.wikipedia.org/wiki/Formal_derivative
---

## Proof

Let $R$ be a [[commutative ring|0GYGHKX834]], let $f \in R[x]$ with $f \neq 0$ and let $c \in R$. For $h \in R[x]$, $h'$ is the [[formal derivative|0AD4VS02H3]].

1. The formal derivative is additive, and $(r h)' = r h'$ for $r \in R$. Both follow from the definition, since it acts on each coefficient separately.
2. We show that $((x - c) g)' = g + (x - c) g'$ for every $g \in R[x]$. Write $g = \sum_{k=0}^{n} b_k x^k$.
3. Then $(x - c) g = \sum_{k=0}^{n} b_k x^{k+1} - \sum_{k=0}^{n} c b_k x^k$. By the definition and step 1, its derivative is $\sum_{k=0}^{n} (k + 1) b_k x^k - \sum_{k=1}^{n} k c b_k x^{k-1}$.
4. Also $g' = \sum_{k=1}^{n} k b_k x^{k-1}$. So $g + (x - c) g' = \sum_{k=0}^{n} b_k x^k + \sum_{k=1}^{n} k b_k x^k - \sum_{k=1}^{n} c k b_k x^{k-1}$.
5. The first two sums of step 4 add to $\sum_{k=0}^{n} (k + 1) b_k x^k$, since $(k + 1) b_k = b_k + k b_k$. Also $c (k b_k) = k (c b_k)$. So steps 3 and 4 give the same polynomial.
6. The [[evaluation homomorphism|0125QVNCFQ]] at $c$ sends $x - c$ to $0$. So step 2 gives $((x - c) g)'(c) = g(c)$ for every $g \in R[x]$.
7. Suppose $c$ has [[multiplicity|03XVP8Q4GY]] at least $2$. Then $(x - c)^2$ divides $f$, say $f = (x - c)^2 h$ with $h \in R[x]$.
8. Evaluating at $c$ gives $f(c) = 0 \cdot h(c) = 0$.
9. Put $g = (x - c) h$, so that $f = (x - c) g$. By step 6, $f'(c) = g(c) = (c - c) h(c) = 0$.
10. Conversely, suppose $f(c) = 0$ and $f'(c) = 0$. By the [[factor theorem|0K3MWA7DMC]], $f = (x - c) g$ with $g \in R[x]$.
11. By step 6, $g(c) = f'(c) = 0$. By the factor theorem again, $g = (x - c) h$ with $h \in R[x]$.
12. So $f = (x - c)^2 h$, and $(x - c)^2$ divides $f$. Since the multiplicity is the largest $m$ with $(x - c)^m$ dividing $f$, it is at least $2$.

## Idea

If $f = (x - c) g$, the product rule gives $f' = g + (x - c) g'$, so $f'(c) = g(c)$. Thus $f'(c) = 0$ says exactly that $c$ is also a [[root|00EHX6FWC0]] of the cofactor $g$, which means that $x - c$ divides $f$ a second time.
