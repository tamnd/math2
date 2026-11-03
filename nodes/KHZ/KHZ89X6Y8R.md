---
tag: KHZ89X6Y8R
kind: definition
name: Words and profiles
msc: [05-XX]
defines: 28M8XD8EA9
sources:
  - arxiv: 2610.13556v1
    locator: Definition 2.1
    mention: ax://paper/2610.13556#TOY4
    licence: cc-by
    note: the paper that states the item (corpus arxiv AX9.2)
history:
  notes: The source is arXiv:2610.13556v1 (2026-10), by Jiang Jiang, Yuhan Jiang, Yiyang Li, Lujia Wang, Aitao Zhang. A paper also restates older results, so this is not the first statement until a person or a later pass confirms it.
inventory: [86VNXJWJ14]
uses: [0JD5C82QMB, 0NCPXH194Y, 0VHJRXNAAS]
---

## Definition

Let $G$ be a finite [[graph|0JD5C82QMB]] with [[chromatic number|0VHJRXNAAS]] $\chi(G)$. Let $\mathcal C$ be a set of colors with $|\mathcal C|=\chi(G)$.

**Words and profiles** are defined as follows.

A word on $G$ is any map $w:V(G)\to\mathcal C$. The word need not be a proper [[colouring|0NCPXH194Y]]: adjacent vertices may get the same color.

The profile of a word $w$ is the vector $\mathbf m(w)=(m_X(w))_{X\in\mathcal C}$. Its entry $m_X(w)=|w^{-1}(X)|$ is the number of vertices of color $X$.

Vectors are written in bold, and inequalities between vectors hold in every coordinate. The vector $\mathbf e_X$ has entry $1$ at $X$ and $0$ elsewhere. The vector $\mathbf 1$ has every entry equal to $1$.

Let $\mathcal P(G)$ be the set of proper colorings of $G$ with palette $\mathcal C$. Since $|\mathcal C|=\chi(G)$, each coloring in $\mathcal P(G)$ uses every color.

A profile $\mathbf m$ is feasible if $\mathbf m=\mathbf m(w)$ for some $w\in\mathcal P(G)$.
