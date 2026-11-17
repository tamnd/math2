---
tag: BM4VXG92DT
kind: example
name: The cosets of 3Z in the integers
msc: ["20A05"]
topics: [1VHQWXC64D]
audience: ug1
instance_of: [564VVAQTNR, 03DEH43F4H, 0NE1DK7H4T]
uses: [0C4JS9RF5M, 0X1JXT47GA, 564VVAQTNR, 03DEH43F4H, 0NE1DK7H4T, 05FD317V2W, 03VFZ2WETT, 0DTXBQPA2S, 082GHNPJ53]
sources:
  - url: https://en.wikipedia.org/wiki/Coset
    locator: Integers
  - book: isbn:9781305657960
    locator: Chapter 7
---

## Example

Let $G = (\mathbb{Z}, +)$ be the [[integers|0C4JS9RF5M]] with addition, and let $H = 3\mathbb{Z} = \{\ldots, -6, -3, 0, 3, 6, \ldots\}$.
In additive notation, the [[left coset|03DEH43F4H]] of $a$ is $a + H = \{a + 3k : k \in \mathbb{Z}\}$.

1. The set $3\mathbb{Z}$ is a [[subgroup|0X1JXT47GA]]. It contains $0$, and $3k + 3l = 3(k + l)$ and $-3k = 3(-k)$ are in $3\mathbb{Z}$.
2. The coset of $0$ is $3\mathbb{Z}$. The coset of $1$ is $1 + 3\mathbb{Z} = \{\ldots, -5, -2, 1, 4, 7, \ldots\}$. The coset of $2$ is $2 + 3\mathbb{Z} = \{\ldots, -4, -1, 2, 5, 8, \ldots\}$.
3. Each integer $a$ lies in exactly one of these three cosets. By division with remainder, $a = 3q + r$ with $r \in \{0, 1, 2\}$, and then $a \in r + 3\mathbb{Z}$.
4. Two integers $a$ and $b$ lie in the same coset if and only if $a - b \in 3\mathbb{Z}$, that is, $a \equiv b \pmod 3$.
5. The group is [[abelian|082GHNPJ53]], so $a + H = H + a$. Each left coset is also a [[right coset|0NE1DK7H4T]].
6. So $H$ has exactly $3$ cosets, and the [[index|0DTXBQPA2S]] is $[\mathbb{Z} : 3\mathbb{Z}] = 3$.

## Remarks

The three [[cosets|564VVAQTNR]] are the elements of the group [[$\mathbb{Z}/3\mathbb{Z}$|03VFZ2WETT]].
The example shows that each coset other than $H$ is not a subgroup: $1 + 3\mathbb{Z}$ does not contain $0$.
The union $3\mathbb{Z} \cup (1 + 3\mathbb{Z})$ is not a subgroup either, because $1 + 1 = 2$ is not in it.
If we replace $3$ by a positive integer $n$, there are $n$ cosets, one for each remainder $0, 1, \ldots, n - 1$.

## Explanations

### L1 human

Sort the whole numbers by their remainder after division by $3$.
The numbers $0, 3, 6, \ldots$ have remainder $0$.
The numbers $1, 4, 7, \ldots$ have remainder $1$, and $2, 5, 8, \ldots$ have remainder $2$.
These three piles are the cosets of the multiples of $3$.
Each pile is the first pile shifted by $0$, $1$ or $2$.

### L2 human

We find the coset of $-7$.

1. We divide with remainder: $-7 = (-3) \cdot 3 + 2$.
2. So $-7 \in 2 + 3\mathbb{Z}$.
3. Check: $-7 - 2 = -9 = 3 \cdot (-3)$, which is in $3\mathbb{Z}$.

The typical use is modular arithmetic: to compute with remainders is to compute with cosets.
A trap is to think that $1 + 3\mathbb{Z}$ is a subgroup because it looks like $3\mathbb{Z}$.
It is a shifted copy, and it does not contain $0$.
