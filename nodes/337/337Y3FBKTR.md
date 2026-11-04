---
tag: 337Y3FBKTR
kind: proof
name: Proof of the homotopy invariance of line integrals of curl-free fields by local potentials
msc: ["26B20"]
proves: 0YVVN6R715
uses: [0GDNHS9J2X, 0YS8RX87F4, 0D032NSZKY, 0B22P010D6, 05R9NF2J49, 0SD237FEJD, 00ZEBSMNNV, 040CFNJEAP, 07PFYV65MB, 0692CGQF00, 0DC3MPR7C9, 0K06X9QXDX, 03HF5PMY5T]
sources:
  - url: https://www.maths.tcd.ie/~zaitsev/topics-ca/wedhorn-Complex-Analysis.pdf
    locator: Theorem 3.12
---

## Proof

We cut the square into small squares whose images lie in balls, use a potential on each ball, and add up. Only the continuity of $H$ is used.

1. Let $K = [0, 1]^2$. It is compact by the [[Heine–Borel theorem|07PFYV65MB]], and $H \colon K \to U$ is continuous.
2. Each [[open ball|0DC3MPR7C9]] $B = B(y, r)$ is [[convex|0K06X9QXDX]]: for $z, w \in B$ and $\lambda \in [0, 1]$, the [[triangle inequality|03HF5PMY5T]] gives $\norm{(1 - \lambda) z + \lambda w - y} < r$. So an intersection of two open balls is convex.
3. On each open ball $B \subseteq U$, the field $F$ is $C^1$ with $\nabla \times F = 0$. By the [[curl-free fields on convex sets|0B22P010D6]] result, there is a $C^1$ function $\phi_B$ on $B$ with $\nabla \phi_B = F$.
4. Claim: let $B, B' \subseteq U$ be open balls and $y, z \in B \cap B'$. Then $\phi_B(z) - \phi_B(y) = \phi_{B'}(z) - \phi_{B'}(y)$.
5. Proof of the claim. By step 2, the segment $\sigma$ from $y$ to $z$ lies in $B \cap B'$. The [[gradient theorem|0SD237FEJD]] on $B$ and on $B'$ gives $\int_\sigma F \cdot d\mathbf{r} = \phi_B(z) - \phi_B(y)$ and $\int_\sigma F \cdot d\mathbf{r} = \phi_{B'}(z) - \phi_{B'}(y)$.
6. The sets $H^{-1}(B)$, for open balls $B \subseteq U$, are open in $K$ and cover $K$, since $U$ is open. By the [[Lebesgue number lemma|040CFNJEAP]] there is $\eta > 0$ such that each subset of $K$ of [[diameter|0692CGQF00]] less than $\eta$ lies in one of them.
7. Choose an integer $N$ with $\sqrt{2} / N < \eta$. For $j, k \in \set{1, \dots, N}$, let $Q_{jk} = [\tfrac{j-1}{N}, \tfrac{j}{N}] \times [\tfrac{k-1}{N}, \tfrac{k}{N}]$. Its diameter is $\sqrt{2} / N$, so $H(Q_{jk}) \subseteq B_{jk}$ for some open ball $B_{jk} \subseteq U$. Write $\phi_{jk} = \phi_{B_{jk}}$.
8. For $j, k \in \set{0, \dots, N}$, let $v_{jk} = (j/N, k/N)$ and $P_{jk} = H(v_{jk})$. An edge is a side of some $Q_{jk}$, from $v$ to $w$, directed so that one coordinate increases.
9. For an edge from $v$ to $w$ and a square $Q_{jk}$ that contains it, let $E = \phi_{jk}(H(w)) - \phi_{jk}(H(v))$. If two squares contain the edge, then $H(v)$ and $H(w)$ lie in both balls. By step 4 they give the same $E$. So each edge $e$ has a well-defined value $E(e)$.
10. Let $h_{jk}$ be the edge from $v_{j-1, k}$ to $v_{jk}$, and $s_{jk}$ the edge from $v_{j, k-1}$ to $v_{jk}$. The boundary of $Q_{jk}$ consists of $h_{j, k-1}$, $s_{jk}$, $h_{jk}$ and $s_{j-1, k}$.
11. Compute all four values with $\phi_{jk}$. Then $E(h_{j, k-1}) + E(s_{jk}) - E(h_{jk}) - E(s_{j-1, k})$ equals $[\phi_{jk}(P_{j, k-1}) - \phi_{jk}(P_{j-1, k-1})] + [\phi_{jk}(P_{jk}) - \phi_{jk}(P_{j, k-1})] - [\phi_{jk}(P_{jk}) - \phi_{jk}(P_{j-1, k})] - [\phi_{jk}(P_{j-1, k}) - \phi_{jk}(P_{j-1, k-1})]$, which is $0$.
12. Sum step 11 over all $j, k \in \set{1, \dots, N}$. The terms with $h$ telescope in $k$, and the terms with $s$ telescope in $j$. This gives $\sum_{j=1}^N \big( E(h_{j0}) - E(h_{jN}) \big) + \sum_{k=1}^N \big( E(s_{Nk}) - E(s_{0k}) \big) = 0$.
13. Since $H(0, s) = H(1, s)$, we have $P_{0k} = P_{Nk}$ for all $k$. The points $P_{0, k-1}$ and $P_{0, k}$ lie in $H(Q_{1k}) \subseteq B_{1k}$, and as $P_{N, k-1}$ and $P_{N, k}$ they lie in $H(Q_{Nk}) \subseteq B_{Nk}$.
14. By step 4, $E(s_{Nk}) = \phi_{Nk}(P_{0k}) - \phi_{Nk}(P_{0, k-1}) = \phi_{1k}(P_{0k}) - \phi_{1k}(P_{0, k-1}) = E(s_{0k})$. With step 12, $\sum_j E(h_{j0}) = \sum_j E(h_{jN})$.
15. Let $\beta_j$ be the restriction of $c_0$ to $[\tfrac{j-1}{N}, \tfrac{j}{N}]$. It is piecewise $C^1$, and its image $H(h_{j0})$ lies in $B_{j1}$, since $H(t, 0) = c_0(t)$.
16. By the gradient theorem on $B_{j1}$, $\int_{\beta_j} F \cdot d\mathbf{r} = \phi_{j1}(P_{j0}) - \phi_{j1}(P_{j-1, 0}) = E(h_{j0})$. By [[additivity|00ZEBSMNNV]], $\oint_{c_0} F \cdot d\mathbf{r} = \sum_j E(h_{j0})$.
17. In the same way, using $H(t, 1) = c_1(t)$ and the balls $B_{jN}$, $\oint_{c_1} F \cdot d\mathbf{r} = \sum_j E(h_{jN})$.
18. By steps 14, 16 and 17, $\oint_{c_0} F \cdot d\mathbf{r} = \oint_{c_1} F \cdot d\mathbf{r}$.

## Idea

A curl-free field has a potential on every ball, though maybe not on all of $U$. Cut the square into pieces so small that each piece of the homotopy lies in one ball. Around each small square the potential differences cancel, and adding all squares leaves only the two loops, because the two sides are glued by $H(0, s) = H(1, s)$.
