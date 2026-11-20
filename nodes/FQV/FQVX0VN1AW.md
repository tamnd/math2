---
tag: FQVX0VN1AW
kind: example
name: The ideals of the integers as a residuated lattice
msc: ["06F05", "13A15"]
topics: [QYA4H5Y7VR]
audience: research
instance_of: [E337A6WVH3]
uses: [S9Z6PKTXAS, 096Z9MP2ME, 16J9DM8V57]
sources:
  - url: https://en.wikipedia.org/wiki/Residuated_lattice
    locator: Examples
  - book: isbn:9780444521415
---

## Example

Every [[ideal|096Z9MP2ME]] of $\mathbb{Z}$ has the form $n\mathbb{Z}$ for a unique $n \ge 0$.
Let $\mathrm{Id}(\mathbb{Z})$ be the set of these ideals, ordered by inclusion.
We check the conditions of [[the definition of a residuated lattice|S9Z6PKTXAS]].

1. Lattice. The meet is $n\mathbb{Z} \cap m\mathbb{Z} = \operatorname{lcm}(n, m)\mathbb{Z}$, and the join is $n\mathbb{Z} + m\mathbb{Z} = \gcd(n, m)\mathbb{Z}$.
2. Monoid. The product of ideals is $(n\mathbb{Z})(m\mathbb{Z}) = nm\mathbb{Z}$. It is associative and commutative, and its unit is $\mathbb{Z} = 1\mathbb{Z}$.
3. Residuals. The product is commutative, so both residuals are the [[ideal quotient|16J9DM8V57]] $(n\mathbb{Z} : m\mathbb{Z}) = \set{r \in \mathbb{Z} : r m \in n\mathbb{Z}}$.
4. Formula. Let $m \ne 0$ and $d = \gcd(n, m)$. Then $n \mid rm$ iff $\tfrac{n}{d} \mid r \tfrac{m}{d}$ iff $\tfrac{n}{d} \mid r$, because $\gcd(\tfrac{n}{d}, \tfrac{m}{d}) = 1$. So $(n\mathbb{Z} : m\mathbb{Z}) = \tfrac{n}{d}\mathbb{Z}$.
5. The case $m = 0$. Then $r \cdot 0 = 0 \in n\mathbb{Z}$ for every $r$, so $(n\mathbb{Z} : 0) = \mathbb{Z}$.
6. Residuation. For $k\mathbb{Z}$ we have $(k\mathbb{Z})(m\mathbb{Z}) \subseteq n\mathbb{Z}$ iff $n \mid km$ iff $k \in (n\mathbb{Z} : m\mathbb{Z})$ iff $k\mathbb{Z} \subseteq (n\mathbb{Z} : m\mathbb{Z})$.

So $\mathrm{Id}(\mathbb{Z})$ is a commutative [[residuated lattice|E337A6WVH3]].

## Remarks

1. The unit $\mathbb{Z}$ is the top element, so the residuated lattice is integral.
2. The product is not the meet: $(2\mathbb{Z})(2\mathbb{Z}) = 4\mathbb{Z}$, but $2\mathbb{Z} \cap 2\mathbb{Z} = 2\mathbb{Z}$. So this is not a Heyting algebra with $\cdot = \land$.
3. The lattice is distributive, since $\gcd$ and $\operatorname{lcm}$ distribute over each other.
4. For every commutative ring $R$, the ideals of $R$ form a commutative integral residuated lattice in the same way. The lattice need not be distributive when $R$ is not a principal ideal domain.

## Explanations

### L1 human

The ideal $6\mathbb{Z}$ is the set of all multiples of $6$.
Multiplying the multiples of $2$ by the multiples of $3$ gives the multiples of $6$.
"Dividing" the multiples of $12$ by the multiples of $8$ asks: which numbers $r$ make $8r$ a multiple of $12$?
The answer is the multiples of $3$, because $8 \cdot 3 = 24$.

### L2 human

1. Compute $(12\mathbb{Z} : 8\mathbb{Z})$. Here $d = \gcd(12, 8) = 4$, so the quotient is $3\mathbb{Z}$.
2. Check: $(3\mathbb{Z})(8\mathbb{Z}) = 24\mathbb{Z} \subseteq 12\mathbb{Z}$.
3. The only ideal that contains $3\mathbb{Z}$ properly is $\mathbb{Z}$, and $(\mathbb{Z})(8\mathbb{Z}) = 8\mathbb{Z} \not\subseteq 12\mathbb{Z}$.
4. So $3\mathbb{Z}$ is the largest ideal $K$ with $K \cdot 8\mathbb{Z} \subseteq 12\mathbb{Z}$.

The typical use: ideal lattices of rings were the first model of residuation, and they give integral commutative examples.
The trap: inclusion reverses divisibility, so $n\mathbb{Z} \subseteq m\mathbb{Z}$ iff $m \mid n$.
