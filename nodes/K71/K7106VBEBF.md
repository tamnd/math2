---
tag: K7106VBEBF
kind: definition
name: Dehn function
msc: [20F65, 20F06, 20F10]
defines: Q4HGMRA9JQ
uses: [0JGEQXQ4AC, TJKANTKASZ, 0KTW26C80J, 0DXD4QSZ8A, 4GNPFMT7DZ, 429JJ5ZNBY]
sources:
  - url: https://en.wikipedia.org/wiki/Dehn_function
---

## Definition

Let $G$ be a [[finitely presented group|TJKANTKASZ]] with a finite [[presentation|0JGEQXQ4AC]] $\langle S \mid R \rangle$, and let $F(S)$ be the [[free group|0KTW26C80J]] on $S$.
Let $w$ be a word over $S \cup S^{-1}$ that represents the identity of $G$.
Its *area* $\mathrm{Area}(w)$ is the least $N \ge 0$ such that $w$ is a product of $N$ [[conjugates|0DXD4QSZ8A]] of relators and their inverses in $F(S)$.
This means an equality $w = \prod_{i=1}^{N} u_i \, r_i^{\pm 1} \, u_i^{-1}$ in $F(S)$, with words $u_i$ and relators $r_i \in R$.
The *Dehn function* of the presentation is the function $\delta \colon \N \to \N$ given by
$$\delta(n) = \max \set{\mathrm{Area}(w) : \abs{w} \le n, \ \bar w = 1 \text{ in } G}.$$

## Remarks

For functions $f, g \colon \N \to \N$, write $f \preceq g$ if there is $C \ge 1$ with $f(n) \le C g(Cn + C) + Cn + C$ for all $n$, and $f \simeq g$ if $f \preceq g \preceq f$.
The Dehn functions of two finite presentations of the same group are $\simeq$-equivalent, so one speaks of the Dehn function of $G$.

Example: for $\Z^2 = \langle a, b \mid aba^{-1}b^{-1} \rangle$, the word $a^n b^n a^{-n} b^{-n}$ of length $4n$ has area $n^2$, and every null-homotopic word of length $n$ has area at most a constant times $n^2$; so $\delta(n) \simeq n^2$.

Example: free groups and finite groups have Dehn function $\simeq n$.

Non-example: the [[lamplighter group|4GNPFMT7DZ]] is finitely generated but not finitely presented, so it has no Dehn function in this sense.

A finitely presented group has a solvable word problem if and only if its Dehn function is bounded above by a recursive function.
The [[Baumslag–Solitar group|429JJ5ZNBY]] $\langle a, b \mid b a b^{-1} = a^2 \rangle$ has an exponential Dehn function.
