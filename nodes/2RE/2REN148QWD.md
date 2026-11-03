---
tag: 2REN148QWD
kind: definition
name: Repair radii and villainy
msc: [05-XX]
defines: EBNHD7FQ23
sources:
  - arxiv: 2610.13556v1
    locator: Definition 2.2
    mention: ax://paper/2610.13556#L0DK
    licence: cc-by
    note: the paper that states the item (corpus arxiv AX9.2)
history:
  notes: The source is arXiv:2610.13556v1 (2026-10), by Jiang Jiang, Yuhan Jiang, Yiyang Li, Lujia Wang, Aitao Zhang. A paper also restates older results, so this is not the first statement until a person or a later pass confirms it.
inventory: [GY5XXNYENM]
uses: [28M8XD8EA9, 0874138YP6, 07TXYYVYZR]
---

## Definition

**Repair radii and villainy** are defined for a finite graph $G$ as follows.

Use [[words and profiles|28M8XD8EA9]] with palette size $\chi(G)$. For a profile $\mathbf m$, let $\mathcal W_{\mathbf m}(G)$ be the set of words on $G$ with profile $\mathbf m$.

Let $\mathcal P_{\mathbf m}(G)$ be the set of [[proper colourings|0874138YP6]] of $G$ with profile $\mathbf m$. Let $\mathcal P(G)$ be the set of all proper colourings of $G$ with this palette.

For two words $w$ and $y$ on $G$, the Hamming distance $d_{\mathrm H}(w,y)$ is the number of vertices on which they differ.

1. The **repair radius** of $\mathbf m$ is $R_G(\mathbf m)=\max_{w\in\mathcal W_{\mathbf m}(G)}\min_{y\in\mathcal P_{\mathbf m}(G)} d_{\mathrm H}(w,y)$.

2. The **weak repair radius** of $\mathbf m$ is $R^{\mathrm w}_G(\mathbf m)=\max_{w\in\mathcal W_{\mathbf m}(G)}\min_{y\in\mathcal P(G)} d_{\mathrm H}(w,y)$.

3. The **villainy** of $G$ is $B(G)=\max R_G(\mathbf m)$, taken over all feasible profiles $\mathbf m$.

4. The **weak villainy** of $G$ is $B_{\mathrm w}(G)=\max R^{\mathrm w}_G(\mathbf m)$, taken over all feasible profiles $\mathbf m$.

Each inner quantity is the [[distance from a point to a set|07TXYYVYZR]] for the Hamming distance. Both $B(G)$ and $B_{\mathrm w}(G)$ are zero when $G$ is the empty graph.
