---
tag: 8BVNQ3R3YP
kind: definition
name: Bar resolution
msc: [20J06, 18G10, "16E40"]
defines: 8BGJ6J9PYF
uses: [G5S1M9, MNP2HBWB5Q, 0DZ9DKAKZR, HK2AA1YSQ2]
sources:
  - url: https://en.wikipedia.org/wiki/Bar_complex
---

## Definition

Let $G$ be a [[group|G5S1M9]] and let $\Z[G]$ be its [[group ring|MNP2HBWB5Q]].
For $n \ge 0$, let $B_n$ be the [[free|0DZ9DKAKZR]] left $\Z[G]$-module with basis the symbols $[g_1 | \cdots | g_n]$ with $g_1, \dots, g_n \in G$; the basis of $B_0$ is the single symbol $[\,]$.
For $n \ge 1$, the $\Z[G]$-linear map $d_n \colon B_n \to B_{n-1}$ is given on the basis by
$$d_n [g_1 | \cdots | g_n] = g_1 [g_2 | \cdots | g_n] + \sum_{i=1}^{n-1} (-1)^i [g_1 | \cdots | g_i g_{i+1} | \cdots | g_n] + (-1)^n [g_1 | \cdots | g_{n-1}].$$
The augmentation $\varepsilon \colon B_0 \to \Z$ sends $[\,]$ to $1$, where every element of $G$ acts on $\Z$ as the identity.
The *bar resolution* of $G$ is the complex $\cdots \to B_2 \xrightarrow{d_2} B_1 \xrightarrow{d_1} B_0 \xrightarrow{\varepsilon} \Z \to 0$.

## Remarks

It is a free [[resolution|HK2AA1YSQ2]] of $\Z$ over $\Z[G]$: one checks $d \circ d = 0$, and a contracting homotopy over $\Z$ is given by $s(g_0 [g_1 | \cdots | g_n]) = [g_0 | g_1 | \cdots | g_n]$.
Check of $d \circ d = 0$ in low degree: $d_1 [g] = g[\,] - [\,]$ and $d_2 [g | h] = g[h] - [gh] + [g]$, so $d_1 d_2 [g | h] = (gh - g)[\,] - (gh - 1)[\,] + (g - 1)[\,] = 0$.
Applying $\Hom_{\Z[G]}(-, M)$ identifies $\Hom_{\Z[G]}(B_n, M)$ with the set of functions $G^n \to M$, the inhomogeneous cochains of group cohomology.
The *normalized* bar resolution uses only symbols with all $g_i \ne 1$; it is also a free resolution of $\Z$.
Non-example: for $G = \Z/2\Z = \set{1, t}$, the periodic complex $\cdots \to \Z[G] \xrightarrow{1 - t} \Z[G] \xrightarrow{1 + t} \Z[G] \xrightarrow{1 - t} \Z[G] \to \Z \to 0$ is a free resolution of $\Z$, but it is not the bar resolution, whose term $B_n$ has rank $2^n$.
