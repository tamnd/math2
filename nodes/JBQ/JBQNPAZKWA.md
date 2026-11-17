---
tag: JBQNPAZKWA
kind: example
name: Index of nZ in Z
msc: ["20A05"]
topics: [1VHQWXC64D]
audience: ug1
instance_of: [0DTXBQPA2S]
uses: [0C4JS9RF5M, 0X1JXT47GA, 03DEH43F4H, 0DTXBQPA2S, 03VFZ2WETT]
sources:
  - url: https://en.wikipedia.org/wiki/Index_of_a_subgroup
    locator: Examples
  - book: isbn:9781305657960
    locator: Chapter 7
---

## Example

Let $G = (\mathbb{Z}, +)$ be the [[integers|0C4JS9RF5M]] with addition.
Let $n \geq 1$ be an integer, and let $H = n\mathbb{Z} = \{nk : k \in \mathbb{Z}\}$.
We show that the [[index|0DTXBQPA2S]] $[\mathbb{Z} : n\mathbb{Z}]$ is $n$.

1. The set $n\mathbb{Z}$ is a [[subgroup|0X1JXT47GA]]. It contains $0 = n \cdot 0$. It contains $nk + nl = n(k + l)$ and $-nk = n(-k)$ for all $k, l \in \mathbb{Z}$.
2. The [[left cosets|03DEH43F4H]] are the sets $a + n\mathbb{Z}$ for $a \in \mathbb{Z}$.
3. Each coset is one of $0 + n\mathbb{Z}, 1 + n\mathbb{Z}, \ldots, (n - 1) + n\mathbb{Z}$. By division with remainder, $a = qn + r$ with $0 \leq r < n$. Then $a - r = qn \in n\mathbb{Z}$, so $a + n\mathbb{Z} = r + n\mathbb{Z}$.
4. These $n$ cosets are distinct. Let $0 \leq r < s < n$. Then $0 < s - r < n$, so $s - r$ is not a multiple of $n$. Thus $r + n\mathbb{Z} \neq s + n\mathbb{Z}$.
5. By steps 3 and 4, there are exactly $n$ cosets, and $[\mathbb{Z} : n\mathbb{Z}] = n$.

## Remarks

The cosets are the residue classes modulo $n$, and they are the elements of the group [[$\mathbb{Z}/n\mathbb{Z}$|03VFZ2WETT]].
The example shows that an infinite subgroup can have finite index.
Both $\mathbb{Z}$ and $n\mathbb{Z}$ are countably infinite, so here the index is not a quotient of orders.
For $n = 1$ the index is $1$, because $1\mathbb{Z} = \mathbb{Z}$.
For $n = 0$ the subgroup is $\{0\}$, each coset $\{a\}$ has one element, and the index is infinite.
The subgroups $n\mathbb{Z}$ and $(-n)\mathbb{Z}$ are equal, so we can take $n \geq 0$.

## Explanations

### L1 human

Sort the whole numbers by their remainder after division by $5$.
The remainders are $0, 1, 2, 3, 4$, so you get $5$ groups of numbers.
The multiples of $5$ form one group, and the other four groups are shifted copies of it.
So the index of the multiples of $5$ in the whole numbers is $5$.

### L2 human

We find the cosets of $4\mathbb{Z}$ and the coset of $-7$.

1. The cosets are $4\mathbb{Z}$, $1 + 4\mathbb{Z}$, $2 + 4\mathbb{Z}$ and $3 + 4\mathbb{Z}$, by step 3 with $n = 4$.
2. We divide with remainder: $-7 = (-2) \cdot 4 + 1$.
3. So $-7 \in 1 + 4\mathbb{Z}$.
4. Thus $[\mathbb{Z} : 4\mathbb{Z}] = 4$.

The typical use is in number theory, where a statement about all integers splits into $n$ cases, one for each residue class.
A trap is to use a negative remainder.
The remainder of $-7$ after division by $4$ is $1$, not $-3$, although $-3 + 4\mathbb{Z}$ is the same coset.
