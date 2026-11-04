---
tag: 4Y6ZD17WNZ
kind: proof
name: Proof of Induced Graph Removal Lemma
proves: YWZQFCJB2K
sources:
  - wikipedia: en:59842040@r1360690218
    locator: Graph removal lemma, section Induced Graph Removal Lemma > Proof > Proof Sketch of the Induced Graph Removal Lemma
    note: adopted
    mention: wikipedia://en/59842040#C3S1
    sections: [Proof]
---

## Proof

With these results, we are able to prove the induced graph removal lemma. Take any graph $G$ with $n$ vertices that has less than $\delta n^{v(H)}$ copies of $H$. The idea is to start with a collection of vertex sets $W_i$ which satisfy the conditions of the **Corollary of the Strong Regularity Lemma**. We then can perform a "cleaning" process where we remove all edges between pairs of parts $(W_i,W_j)$ with low density, and we can add all edges between pairs of parts $(W_i,W_j)$ with high density. We choose the density requirements such that we added/deleted at most $\epsilon n^2$ edges.

If the new graph has no copies of $H$, then we are done. Suppose the new graph has a copy of $H$. Suppose the vertex $v_i \in v(H)$ is embedded in $W_{f(i)}$. Then if there is an edge connecting $v_i,v_j$ in $H$, then $W_i,W_j$ does not have low density. (Edges between $W_i,W_j$ were not removed in the cleaning process.) Similarly, if there is not an edge connecting $v_i,v_j$ in $H$, then $W_i,W_j$ does not have high density. (Edges between $W_i,W_j$ were not added in the cleaning process.)

Thus, by a similar counting argument to the proof of the triangle counting lemma (that is, the **graph counting lemma**), we can show that $G$ has more than $\delta n^{v(H)}$ copies of $H$.
