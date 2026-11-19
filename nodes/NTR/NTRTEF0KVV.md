---
tag: NTRTEF0KVV
kind: proof
name: Proof of the undecidability of the Halpern–Shoham interval logic
msc: ["03B44", "03B25", "03D35"]
topics: [CQM9SRN8PM]
audience: research
proves: 9BE0H3W9QG
uses: [991B5RR6X4, AJH5HPD2B7, BBYNPDWR5R, 3J6YG01N22, V0K79AD81V]
methods: [0J0XBKG64S, 0WCP0PVET6]
sources:
  - book: isbn:9780198537694
    locator: Gabbay, Hodkinson and Reynolds, Temporal Logic, volume 1
  - url: https://en.wikipedia.org/wiki/Wang_tile
    locator: lead section
---

## Proof

We prove [[the theorem|9BE0H3W9QG]] by a reduction from a tiling problem.
We prove the step from the plane to the octant in full.
We cite two results without proof: Berger's theorem on [[Wang tiles|AJH5HPD2B7]], and the encoding lemma of step 9, which builds the HS formula.

1. Octant tiling. Let $O = \set{(i, j) \in \mathbb{N}^2 : i \le j}$. A finite set $W$ of [[Wang tiles|BBYNPDWR5R]] tiles $O$ if some $\tau \colon O \to W$ matches colours on every pair of horizontal or vertical neighbours inside $O$.
2. Lemma: $W$ tiles $O$ if and only if $W$ tiles the plane $\mathbb{Z}^2$.
3. If $W$ tiles the plane, the restriction of the tiling to $O$ tiles $O$.
4. Conversely, let $W$ tile $O$. For each $m$, the square $\set{0, \dots, m} \times \set{m, \dots, 2m}$ lies in $O$, since $i \le m \le j$ there.
5. Matching is invariant under translation, so $W$ tiles every square $\set{0, \dots, m}^2$.
6. Cited: $W$ tiles the plane if and only if it tiles all finite squares. This is the compactness argument recorded with Berger's theorem. So $W$ tiles the plane.
7. Cited: whether a finite set $W$ tiles the plane is undecidable, by Berger's theorem. By step 2, the octant tiling problem is undecidable too.
8. The grid of intervals. Fix points $x_0 < x_1 < \cdots$ in an order. Send the octant point $(i, j)$ to the interval $[x_i, x_{j+1}]$.
   The right neighbour $(i + 1, j)$ goes to $[x_{i+1}, x_{j+1}]$, a proper end part of $[x_i, x_{j+1}]$, reached by $\langle E \rangle$.
   The upper neighbour $(i, j + 1)$ goes to $[x_i, x_{j+2}]$, which $[x_i, x_{j+1}]$ begins, reached by $\langle \bar B \rangle$.
9. Encoding lemma, cited. From $W$ one can compute an HS formula $\varphi_W$ with an atom $t_w$ for each tile $w$, and atoms that mark the points $x_k$ through the unit intervals $[x_k, x_{k+1}]$. It has two properties.
10. First property. Suppose $\varphi_W$ holds in some model over a linear order.
   Then the marked points form a chain $x_0 < x_1 < \cdots$.
   The tile atoms on the intervals of step 8 then define a tiling of $O$.
11. Second property. Suppose $W$ tiles $O$ by $\tau$, and the order has an infinite ascending sequence.
   Take that sequence as the points $x_k$, and put $t_{\tau(i, j)}$ on $[x_i, x_{j+1}]$.
   This gives a model of $\varphi_W$.
12. Ascending case. Let $\mathcal{C}$ contain an order $K$ with an infinite ascending sequence. By steps 10 and 11, $\varphi_W$ is satisfiable over $\mathcal{C}$ if and only if $W$ tiles $O$.
13. Descending case. Let $K \in \mathcal{C}$ have an infinite descending sequence. The reverse order $K^{\mathrm{op}}$ has an infinite ascending sequence.
14. Let $\varphi^*$ be $\varphi$ with each modality replaced by its mirror image. Swap $\langle B \rangle$ with $\langle E \rangle$, $\langle \bar B \rangle$ with $\langle \bar E \rangle$, and $\langle A \rangle$ with $\langle \bar A \rangle$.
   Reversing the order turns "begins" into "ends" and "after" into its inverse.
   So $\varphi^*$ is satisfiable over $K$ exactly when $\varphi$ is satisfiable over $K^{\mathrm{op}}$.
15. Then $\varphi_W^*$ is satisfiable over $\mathcal{C}$ if and only if $W$ tiles $O$.
   For one direction apply step 11 to $K^{\mathrm{op}}$.
   For the other apply step 10 to the reverse of the order in $\mathcal{C}$ that satisfies $\varphi_W^*$.
16. Conclusion. In both cases, a decision procedure for HS satisfiability over $\mathcal{C}$ would decide the octant tiling problem, against step 7.
17. Validity is the dual problem: $\varphi$ is satisfiable exactly when $\neg\varphi$ is not valid. So validity over $\mathcal{C}$ is undecidable as well.

## Idea

An interval is a pair of points, so the intervals over a chain form a half-grid above the diagonal.
The modalities $\langle E \rangle$ and $\langle \bar B \rangle$ move one step right and one step up in this grid.
A formula can then force a correct tiling, and tiling problems are undecidable.

## Variants

1. Halpern and Shoham's own proof encodes Turing machine computations directly in the half-grid.
2. Proofs for small fragments of HS replace the octant by other grid-like structures, which the weaker modalities can still describe.
