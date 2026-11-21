---
tag: ZZ4Y8P9V9Q
kind: proof
name: Proof of the reconstruction theorem for omega-categorical structures
aliases: [proof-of-ahlbrandt-ziegler-reconstruction-theorem, proof-of-reconstruction-of-omega-categorical-structures]
msc: ["03C35", "20B27"]
topics: [SZRM3N6BXW]
audience: research
proves: AM0523XJ9D
uses: [ZA0RN56STN, C5BWHPHAGA, 1513J40TKA, A22K1X8GKD, 9V71Q3SD1G, 0K1SCPBNKJ, FVGB8ZP67B, QYCFH68RD1, 92700QAB5Y]
methods: [0NTF6DMVAP, TFQ1845T84, 41JZ39GE3F]
sources:
  - book: isbn:9780521587136
---

## Proof

Let $G = \operatorname{Aut}(M)$ and $K = \operatorname{Aut}(N)$, with the [[topology of pointwise convergence|FVGB8ZP67B]].
The pointwise stabilizers $G_{\bar a}$ of finite tuples form a base of [[open subgroups|QYCFH68RD1]] at the identity, and likewise for $K$.
We use the notation of [[bi-interpretations|ZA0RN56STN]]: $f_\Gamma$ is the coordinate map of $\Gamma$, and $h_M$, $h_N$ are the composites.

### Step 1: invariant sets are definable

1. By the [[Ryll-Nardzewski theorem|1513J40TKA]], $\operatorname{Th}(M)$ has finitely many complete $k$-[[types|9V71Q3SD1G]] for each $k$, and each is isolated by a formula.
2. So $M$ is a countable atomic model, and a back-and-forth argument shows that tuples with the same type lie in the same $G$-orbit.
3. Each $G$-orbit on $M^k$ is then the set of realizations of an isolated type, defined by its isolating formula.
4. A $G$-invariant subset of $M^k$ is a union of orbits, of which there are finitely many. So every $G$-invariant subset of $M^k$ is $\emptyset$-definable, and the same holds for $N$ and $K$.

### Step 2: from a bi-interpretation to an isomorphism

5. Let $(\Gamma, \Delta)$ be a $\emptyset$-bi-interpretation. For $\sigma \in G$, set $\hat\sigma(f_\Gamma \bar a) = f_\Gamma(\sigma \bar a)$. This is well defined, since the domain formula and $\varepsilon$ have no parameters, so $\sigma$ preserves them.
6. The formulas $\varphi_R$ have no parameters, so $\hat\sigma$ preserves each relation and function of $N$. Also $\widehat{\sigma \tau} = \hat\sigma \hat\tau$, so $\widehat{\sigma^{-1}}$ is an inverse and $\hat\sigma \in K$.
7. Continuity. Let $\bar b = (f_\Gamma \bar a_1, \dots, f_\Gamma \bar a_k)$. If $\sigma$ fixes all entries of the $\bar a_i$, then $\hat\sigma$ fixes $\bar b$. So the preimage of $K_{\bar b}$ contains an open subgroup, and the homomorphism is continuous.
8. In the same way, $\Delta$ gives a continuous homomorphism $\tau \mapsto \check\tau$ from $K$ to $G$.
9. Inverse. Let $x = h_M(\bar a_1, \dots, \bar a_m)$. Then $\check{\hat\sigma}(x) = f_\Delta(f_\Gamma \sigma \bar a_1, \dots, f_\Gamma \sigma \bar a_m) = h_M(\sigma \bar a_1, \dots, \sigma \bar a_m)$. The graph of $h_M$ is $\emptyset$-definable, so this equals $\sigma x$.
10. By the same computation in $N$, the two homomorphisms are inverse to each other. So $\sigma \mapsto \hat\sigma$ is an isomorphism of [[topological groups|92700QAB5Y]]. Step 1 was not used here.

### Step 3: coordinate maps from an isomorphism

11. Let $\alpha : G \to K$ be an isomorphism of topological groups. By step 1 with $k = 1$, $K$ has finitely many orbits on $N$; choose representatives $b_1, \dots, b_r$.
12. Each $K_{b_j}$ is open, so $H_j = \alpha^{-1}(K_{b_j})$ is open in $G$. Choose a nonempty finite tuple $\bar a_j$ with $G_{\bar a_j} \subseteq H_j$, and let $O_j = G \bar a_j$.
13. Define $f_j(\sigma \bar a_j) = \alpha(\sigma) b_j$ on $O_j$. If $\sigma \bar a_j = \tau \bar a_j$, then $\tau^{-1} \sigma \in G_{\bar a_j} \subseteq H_j$, so $\alpha(\sigma) b_j = \alpha(\tau) b_j$. So $f_j$ is well defined, and it maps $O_j$ onto $K b_j$.
14. Equivariance. For $\rho \in G$, $f_j(\rho \sigma \bar a_j) = \alpha(\rho) \alpha(\sigma) b_j$, so $f_j(\rho \bar x) = \alpha(\rho) f_j(\bar x)$.

### Step 4: the interpretation

15. Tags. Let $\ell$ be the largest length of the $\bar a_j$. Use tuples $(\bar x, z_0, \dots, z_r)$ with $\bar x$ of length $\ell$. The tag $j$ means $z_0 = z_j$ and $z_0 \neq z_i$ for $i \neq j$; this is possible since $M$ is infinite.
16. The piece $D_j$ consists of the tuples with tag $j$ whose first $|\bar a_j|$ entries form a tuple $\bar y \in O_j$, the remaining entries of $\bar x$ being equal to the last entry of $\bar y$. Put $f(\bar x, \bar z) = f_j(\bar y)$ on $D_j$.
17. The domain $D = \bigcup_j D_j$ is $G$-invariant, $f$ maps it onto $N$, and $f(\rho \bar u) = \alpha(\rho) f(\bar u)$ by step 14.
18. Let $\varepsilon$ be the kernel of $f$, and for each relation $R$ of $N$ let $\varphi_R$ be the preimage of $R$ under $f$; treat graphs of functions the same way. Since $R$ is $K$-invariant, equivariance makes these sets $G$-invariant.
19. By step 1, $D$, $\varepsilon$ and the $\varphi_R$ are $\emptyset$-definable. So they form a $\emptyset$-[[interpretation|C5BWHPHAGA]] $\Gamma$ of $N$ in $M$, and $\hat\sigma = \alpha(\sigma)$ by equivariance.

### Step 5: the composites

20. Steps 3 and 4 applied to $\alpha^{-1}$ give a $\emptyset$-interpretation $\Delta$ of $M$ in $N$ with $f_\Delta(\tau \bar v) = \alpha^{-1}(\tau) f_\Delta(\bar v)$.
21. For $\sigma \in G$, $h_M(\sigma \bar a_1, \dots, \sigma \bar a_m) = f_\Delta(\alpha(\sigma) f_\Gamma \bar a_1, \dots) = \alpha^{-1}(\alpha(\sigma)) \, h_M(\bar a_1, \dots, \bar a_m)$.
22. So the domain and the graph of $h_M$ are $G$-invariant, and they are $\emptyset$-definable by step 1. The same argument applies to $h_N$.
23. Hence $(\Gamma, \Delta)$ is a $\emptyset$-bi-interpretation, and it induces $\alpha$. $\blacksquare$

## Idea

A $\emptyset$-interpretation commutes with automorphisms, so it carries automorphisms across.
Conversely, in an $\omega$-categorical structure, every invariant set is definable.
So any coordinate map built from group data is automatically definable, as soon as it commutes with the group.
Open subgroups give such maps, because their coset spaces are orbits of finite tuples, up to a quotient.

## Variants

- Steps 3 and 4 only use that $\alpha$ is a continuous homomorphism and that $\alpha(G)$ has finitely many orbits on $N$. This gives the generalization in the statement.
- Step 13 with $N$ replaced by a coset space $G / H$, for $H$ open, shows that $G / H$ is the orbit of an imaginary element $\bar a_j / \varepsilon_j$ of $M^{\mathrm{eq}}$.
- With $M^{\mathrm{eq}}$ in place of tags, one can interpret each orbit of $N$ in its own sort, and step 15 becomes unnecessary.
