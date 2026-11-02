---
tag: AHKJ361FDB
kind: statement
role: theorem
name: Long exact sequence in homology
msc: ["18G35", 55N10]
uses: [Y9CZ3MTNF1, WQ82C0M3QB, HTK9WQZJ1G, 2J4JJJYP22, KJKNJMGKZZ, JB7ZBFBA9C, Q8AYGD93CW]
about: [2J4JJJYP22]
sources:
  - url: https://en.wikipedia.org/wiki/Exact_sequence
---

## Statement

Let $\mathcal{A}$ be an [[abelian category|Y9CZ3MTNF1]], such as the category of modules over a ring.
Let $0 \to A_\bullet \xrightarrow{f} B_\bullet \xrightarrow{g} C_\bullet \to 0$ be a sequence of [[chain complexes|WQ82C0M3QB]] and [[chain maps|HTK9WQZJ1G]] in $\mathcal{A}$ such that $0 \to A_n \to B_n \to C_n \to 0$ is a [[short exact sequence|KJKNJMGKZZ]] for every $n$.
Then there are morphisms $\partial_n \colon H_n(C) \to H_{n-1}(A)$, called *connecting morphisms*, such that the sequence of [[homology|2J4JJJYP22]] objects
$$\cdots \to H_n(A) \xrightarrow{H_n(f)} H_n(B) \xrightarrow{H_n(g)} H_n(C) \xrightarrow{\partial_n} H_{n-1}(A) \xrightarrow{H_{n-1}(f)} H_{n-1}(B) \to \cdots$$
is [[exact|JB7ZBFBA9C]].
The connecting morphisms are natural with respect to morphisms of such short exact sequences of complexes.

## Remarks

For modules, $\partial_n$ is computed as follows.
Lift a cycle $z \in C_n$ to $y \in B_n$.
Then $d y$ maps to $d z = 0$ in $C_{n-1}$, so $d y = f(x)$ for a unique $x \in A_{n-1}$, which is a cycle, and $\partial_n [z] = [x]$.
The proof applies the [[snake lemma|Q8AYGD93CW]] to the map $\operatorname{coker} d^A_{n+1} \to \ker d^A_{n-1}$ induced by $d$, and the same for $B$ and $C$.
The kernels and cokernels of these maps are $H_n$ and $H_{n-1}$, which yields the six-term pieces of the sequence.
Example: let $A_\bullet = \Z$ in degree $0$, let $B_\bullet$ have $B_1 = B_0 = \Z$ with $d_1 = 1_{\Z}$, and let $C_\bullet = \Z$ in degree $1$, with the evident inclusion and projection.
Then $H(B) = 0$, so exactness of $0 = H_1(B) \to H_1(C) \to H_0(A) \to H_0(B) = 0$ makes $\partial_1 \colon \Z \to \Z$ an isomorphism.

## Explanations

### L1 human

A short exact sequence of complexes builds the middle complex from a subcomplex and a quotient complex.
Homology does not keep the sequence short exact, but the theorem says that the failure is controlled.
The three homology sequences link up into one long exact sequence, with a connecting map that lowers the degree by one.

### L2 human

This is the most used tool for computing homology.
In topology, the short exact sequences of singular chains for a pair $(X, A)$ give the long exact sequence of a pair.
For an open cover by two sets they give the Mayer–Vietoris sequence.
In algebra, applying it to a short exact sequence of resolutions gives the long exact sequences of derived functors such as $\mathrm{Ext}$ and $\mathrm{Tor}$.
Together with the [[five lemma|W6AVEAW2WR]], it lets one prove that a map is a quasi-isomorphism by checking pieces.
