---
tag: 2BPS2FMDE6
kind: statement
role: lemma
name: Hypergraph removal lemma
sources:
  - wikipedia: en:69380218@r1247154057
    locator: Hypergraph regularity method, section Applications > Hypergraph removal lemma
    note: adopted
    mention: wikipedia://en/69380218#QSQ5
    sections: [Statement]
inventory: [A85C16XBJV]
---

## Statement

> For all $l \geq k \geq 2$ and every $\mu > 0$, there exists $\zeta > 0$ and $n_0 > 0$ so that the following holds. Suppose $\mathcal{F}^{(k)}$ is a $k$-uniform hypergraph on $l$ vertices and $\mathcal{H}^{(k)}$ is that on $n \geq n_0$ vertices. If $\mathcal{H}^{(k)}$ contains at most $\zeta n^l$ copies of $\mathcal{F}^{(k)}$, then one can delete $\mu n^k$ hyperedges in $\mathcal{H}^{(k)}$ to make it $\mathcal{F}^{(k)}$-free.

One of the original motivations for graph regularity method was to prove Szemerédi's theorem, which states that every dense subset of $\mathbb{Z}$ contains an arithmetic progression of arbitrary length. In fact, by a relatively simple application of the triangle removal lemma, one can prove that every dense subset of $\mathbb{Z}$ contains an arithmetic progression of length 3.

The hypergraph regularity method and hypergraph removal lemma can prove high-dimensional and ring analogues of density version of Szemerédi's theorems, originally proved by Furstenberg and Katznelson. In fact, this approach yields first quantitative bounds for the theorems.

This theorem roughly implies that any dense subset of $\mathbb{Z}^d$ contains any finite pattern of $\mathbb{Z}^d$. The case when $d = 1$ and the pattern is arithmetic progression of length some length is equivalent to Szemerédi's theorem.

> \==== Furstenberg and Katznelson Theorem ====
>
> Source:
>
> Let $T$ be a finite subset of $\mathbb{R}^d$ and let $\delta > 0$ be given. Then there exists a finite subset $C \subset \mathbb{R}^d$ such that every $Z \subset C$ with $|Z| > \delta |C|$ contains a homothetic copy of $T$. (i.e. set of form $z + \lambda T$, for some $z \in \mathbb{R}^d$ and $t \in \mathbb{R}$)
>
> Moreover, if $T \subset [-t; t]^d$ for some $t \in \mathbb{N}$, then there exists $N_0 \in \mathbb{N}$ such that $C = [-N,N]^d$ has this property for all $N \geq N_0$.

Another possible generalization that can be proven by the removal lemma is when the dimension is allowed to grow.

> \==== Tengan, Tokushige, Rödl, and Schacht Theorem ==== Let $A$ be a finite ring. For every $\delta > 0$, there exists $M_0$ such that, for $M \geq M_0$, any subset $Z \subset A^M$ with $|Z| > \delta |A^M|$ contains a coset of an isomorphic copy of $A$ (as a left $A$-module).
>
> In other words, there are some $\mathbf{r}, \mathbf{u} \in A^M$ such that $r + \varphi(A) \subset Z$, where $\varphi \colon A \to A^M$, $\varphi(a)=a \mathbf{u}$ is an injection.
