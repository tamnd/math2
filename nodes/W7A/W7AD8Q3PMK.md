---
tag: W7AD8Q3PMK
kind: example
name: Chang's MV-algebra
aliases: [changs-mv-algebra]
msc: ["06D35", "03B50"]
topics: [QYA4H5Y7VR]
audience: research
instance_of: [8T4M7RN9AC]
uses: [QVWHWDJ5X1, 64NDFWQEZ2]
sources:
  - url: https://en.wikipedia.org/wiki/MV-algebra
    locator: Examples of MV-algebras
  - book: isbn:9780792360094
---

## Example

Let $G = \mathbb{Z} \times \mathbb{Z}$ with the lexicographic order: $(a, b) < (c, d)$ iff $a < c$, or $a = c$ and $b < d$.
Let $u = (1, 0)$, and let $C = \Gamma(G, u) = \set{x \in G : (0, 0) \le x \le u}$.
Then $C$ is an [[MV-algebra|QVWHWDJ5X1]] by [[the $\Gamma$ theorem|64NDFWQEZ2]], with $x \oplus y = \min(u, x + y)$ and $\neg x = u - x$.
Its elements are the $(0, k)$ and the $(1, -k)$ for $k \ge 0$.

1. Put $\varepsilon = (0, 1)$. Then $n \varepsilon = (0, n)$ for every $n \ge 1$.
2. $\neg \varepsilon = (1, -1)$, and $(0, n) < (1, -1)$ for all $n$.
3. $\varepsilon \odot \varepsilon = \neg(\neg \varepsilon \oplus \neg \varepsilon) = \neg \min(u, (2, -2)) = \neg u = (0, 0)$.

## Remarks

1. The elements $(0, k)$ are the infinitesimals, and the $(1, -k)$ are their negations.
2. $C$ is a chain, but it does not embed in $[0, 1]$: an image of $\varepsilon$ would be a positive real with $n \varepsilon < 1$ for all $n$.
3. $C$ satisfies the same identities as $[0, 1]$, by [[Chang's completeness theorem|QM0F33QE9P]].
   So the first-order property "archimedean" is not an identity.

## Explanations

### L1 human

Here there are truth values that are "a tiny bit true", smaller than any positive real number.
Adding a tiny truth to itself any number of times stays tiny.
The other elements are "true minus a tiny bit".

### L2 human

1. Compute $(0, 2) \oplus (1, -3) = \min((1, 0), (1, -1)) = (1, -1)$.
2. Compute $(1, -1) \oplus (1, -2) = \min((1, 0), (2, -3)) = (1, 0) = 1$.
3. Compute $\neg (0, 2) = (1, -2)$.

The typical use: it shows that MV-chains need not be archimedean.
The trap: the order is lexicographic, so $(0, 1000) < (1, -1000)$.
