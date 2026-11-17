---
tag: 0ZQJ7KEFQ5
kind: statement
role: theorem
name: Tower law for indices
aliases: [multiplicativity-of-the-index]
msc: ["20A05"]
topics: [1VHQWXC64D]
audience: ug1
about: [0DTXBQPA2S]
uses: [G5S1M9, 0X1JXT47GA, 0DTXBQPA2S, 03DEH43F4H, 0EBACQFAZW, 04DC0SRN2K]
sources:
  - url: https://en.wikipedia.org/wiki/Index_of_a_subgroup
    locator: Properties
  - book: isbn:9780471433347
    locator: Section 3.2
  - book: isbn:9781305657960
    locator: Chapter 7
---

## Statement

Let $G$ be a [[group|G5S1M9]], let $H$ be a [[subgroup|0X1JXT47GA]] of $G$, and let $K$ be a subgroup of $H$.
Let $[G : H]$ denote the [[index|0DTXBQPA2S]] of $H$ in $G$, that is, the number of [[left cosets|03DEH43F4H]] of $H$ in $G$.
Then $[G : K] = [G : H] \cdot [H : K]$, as an equation of [[cardinal numbers|0EBACQFAZW]].
In particular, $[G : K]$ is finite if and only if $[G : H]$ and $[H : K]$ are both finite.

## Remarks

### Why each hypothesis is needed

- The subgroup $K$ must lie inside $H$, or else $[H : K]$ is not defined. In $(\mathbb{Z}, +)$, take $H = 2\mathbb{Z}$ and $K = 3\mathbb{Z}$. A natural guess is $[\mathbb{Z} : 3\mathbb{Z}] = [\mathbb{Z} : 2\mathbb{Z}] \cdot [2\mathbb{Z} : 2\mathbb{Z} \cap 3\mathbb{Z}]$, but the left side is $3$ and the right side is $2 \cdot [2\mathbb{Z} : 6\mathbb{Z}] = 2 \cdot 3 = 6$.
- The groups need not be finite. The proof uses only cosets and a choice of representatives.

### Consequences

- For finite $G$ and $K = \{e\}$, the law gives $|G| = [G : H] \cdot |H|$, which is the [[counting form of Lagrange's theorem|04DC0SRN2K]].
- If $[G : K]$ is finite, then $[G : H]$ and $[H : K]$ both divide $[G : K]$.
- A subgroup of finite index in a subgroup of finite index has finite index in $G$.
- If $[G : H]$ is a prime $p$ and $K \le H \le G$, then $[G : K]$ is a multiple of $p$.

### Converse

The converse asks: if $K \le G$ and $[G : K] = m \cdot n$, is there a subgroup $H$ with $K \le H \le G$ and $[G : H] = m$?
This is false.
Take $G = A_4$ and $K = \{e\}$, so $[G : K] = 12 = 2 \cdot 6$.
A subgroup $H$ with $[A_4 : H] = 2$ would have order $6$, and [[$A_4$ has no subgroup of order $6$|0PDBVPP233]].

### Generalizations

- For a chain $K_n \le K_{n - 1} \le \cdots \le K_0 = G$, the law gives $[G : K_n] = [K_0 : K_1] \cdot [K_1 : K_2] \cdots [K_{n - 1} : K_n]$, by induction on $n$.
- The tower law for fields, $[L : F] = [L : E] \cdot [E : F]$ for $F \subseteq E \subseteq L$, has the same form, with degrees of field extensions in place of indices.

## Explanations

### L1 human

Think of a building with floors, and rooms on each floor.
Each floor has the same number of rooms.
The number of rooms in the building is the number of floors times the number of rooms on a floor.
In the tower law, the cosets of $H$ are the floors, and the cosets of $K$ are the rooms.
For example, the multiples of $6$ have $6$ cosets in the integers: $2$ "floors" for the even and the odd numbers, each with $3$ "rooms".

### L2 human

We check the law in the [[symmetric group|0515A6D2Y1]] $S_4$, of order $24$.
Let $H \cong S_3$ be the subgroup of permutations that fix $4$, and let $K = \{e, (1\,2)\}$.

1. The group $H$ has order $6$, so $[S_4 : H] = 24 / 6 = 4$, by the counting form of Lagrange's theorem.
2. The subgroup $K$ has order $2$, so $[H : K] = 6 / 2 = 3$.
3. Directly, $[S_4 : K] = 24 / 2 = 12$.
4. The law gives $[S_4 : K] = 4 \cdot 3 = 12$, which agrees with step 3.

The typical use is with infinite groups, where the counting form is not available.
For example, $[\mathbb{Z} : 12\mathbb{Z}] = [\mathbb{Z} : 4\mathbb{Z}] \cdot [4\mathbb{Z} : 12\mathbb{Z}] = 4 \cdot 3$.
A trap is to apply the law when $K$ is not inside $H$, as in the first hypothesis above.

### L3 human

The tower law says that the index is multiplicative along chains of subgroups.
In topology, a chain of subgroups $K \le H \le \pi_1(X)$ of finite index gives a chain of covering spaces, and the degrees multiply in the same way.
In Galois theory, for a finite Galois extension $L/F$ with group $G$, the field tower law and the index tower law match under the Galois correspondence.
A subgroup $K$ of finite index $n$ in a finitely generated group $G$ is again finitely generated.
Schreier's lemma gives explicit generators of $K$, and their number is bounded in terms of $n$ and the number of generators of $G$.
Its proof uses a transversal, as in the proof of the tower law.
