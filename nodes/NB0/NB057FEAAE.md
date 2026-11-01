---
tag: NB057FEAAE
kind: statement
role: theorem
name: Brauer's main theorems
msc: [20C20]
uses: [G5S1M9, 06QYRTX9KQ, 0YGN3VAA0D, 02YYV36BFM, 0DEBXAJ5SA, RMWMYBY8TC, R2N3GBDBVQ, MNP2HBWB5Q]
about: [R2N3GBDBVQ, RMWMYBY8TC]
sources:
  - url: https://en.wikipedia.org/wiki/Brauer%27s_three_main_theorems
same_as:
  wikidata: Q4958221
  wikipedia: Brauer's three main theorems
---

## Statement

Let $G$ be a finite [[group|G5S1M9]], let $p$ be a prime, and fix a $p$-modular system with residue field $k$ of characteristic $p$.
The $p$-blocks of a finite group $H$ are the blocks of the [[group algebra|MNP2HBWB5Q]] $k[H]$.
Each irreducible complex [[character|RMWMYBY8TC]] and each irreducible [[Brauer character|R2N3GBDBVQ]] of $H$ lies in exactly one block.
Each block $b$ has a defect group, a [[$p$-subgroup|06QYRTX9KQ]] of $H$ determined up to conjugacy.
Each block $b$ of $H$ has a central character $\lambda_b \colon Z(k[H]) \to k$.
For a subset $X$ of $G$, let $\hat{X}$ be the sum of the elements of $X$ in $k[G]$.
Let $H \le G$ and let $b$ be a block of $H$.
Suppose there is a block $B$ of $G$ with $\lambda_B(\hat{C}) = \lambda_b(\widehat{C \cap H})$ for each [[conjugacy class|0DEBXAJ5SA]] $C$ of $G$.
Then $B$ is unique, one says that $b^G$ is defined, and $b^G = B$ is the Brauer correspondent of $b$.
The principal block is the block containing the trivial character.

1. First main theorem. Let $D$ be a $p$-subgroup of $G$ with [[normaliser|0YGN3VAA0D]] $N_G(D)$. The map $b \mapsto b^G$ is a bijection from the blocks of $N_G(D)$ with defect group $D$ onto the blocks of $G$ with defect group $D$.
2. Second main theorem. Let $x \in G$ have order a power of $p$, and let $H = C_G(x)$ be its [[centraliser|02YYV36BFM]]. Let $\chi$ be an irreducible complex character of $G$. There are unique complex numbers $d^x_{\chi\varphi}$, for $\varphi$ in the set of irreducible Brauer characters of $H$, such that $\chi(xy) = \sum_{\varphi} d^x_{\chi\varphi} \, \varphi(y)$ for every $p$-regular $y \in H$. Let $\chi$ lie in the block $B$ and $\varphi$ in the block $b$ of $H$. If $d^x_{\chi\varphi} \ne 0$, then $b^G = B$.
3. Third main theorem. Let $H \le G$ and let $b$ be a block of $H$ with defect group $D$ such that $C_G(D) \le H$. Then $b^G$ is defined, and $b^G$ is the principal block of $G$ if and only if $b$ is the principal block of $H$.

## Remarks

The numbers $d^x_{\chi\varphi}$ are the generalised decomposition numbers; for $x = 1$ they are the ordinary decomposition numbers.
The first main theorem reduces the count of blocks with a given defect group to a question about the normaliser of a $p$-subgroup, a local subgroup.
For example, if $D$ is a normal Sylow $p$-subgroup of $G$, then $N_G(D) = G$ and the theorem is a tautology; the content appears when $N_G(D)$ is much smaller than $G$.
The second main theorem says that the values of characters of a block at elements with $p$-part $x$ are controlled by blocks of $C_G(x)$ that correspond to it.
The third main theorem identifies the principal block of $G$ through principal blocks of local subgroups, which is used in the local analysis of finite simple groups.

## Explanations

### L1 human

Brauer's three main theorems relate the blocks of a finite group, the natural pieces of its representation theory modulo $p$, to blocks of small subgroups built from $p$-subgroups.
They make precise the idea that much of the $p$-modular representation theory of a group is controlled locally, near its $p$-subgroups.

### L2 human

These results are the foundation of block theory.
The first gives the Brauer correspondence with normalisers, the second computes character values through centralisers of $p$-elements, and the third tracks the principal block.
Together they underlie local-global conjectures such as the [[McKay conjecture|WQQTFRZFBD]], Alperin's weight conjecture and [[Brauer's height zero conjecture|5M0HYY3RYV]].
