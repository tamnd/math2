---
tag: H9AFGFG4RB
kind: statement
role: theorem
name: Markov–Kakutani fixed-point theorem
msc: ["47H10", "46A55", "43A07"]
uses: [T32W553W95, 02AS45T3H9, 0R6EWFKRCF, 0JF0TVYGWT, R6QVS6P21N]
about: [R6QVS6P21N]
sources:
  - url: https://en.wikipedia.org/wiki/Markov–Kakutani_fixed-point_theorem
same_as:
  wikidata: Q6771347
  wikipedia: Markov–Kakutani fixed-point theorem
---

## Statement

Let $X$ be a Hausdorff [[topological vector space|T32W553W95]], and let $K \subseteq X$ be a nonempty [[compact|0R6EWFKRCF]] [[convex set|02AS45T3H9]].
Let $\mathcal{F}$ be a family of continuous [[affine maps|0JF0TVYGWT]] $T \colon K \to K$ that commute pairwise: $ST = TS$ for all $S, T \in \mathcal{F}$.
Then there is a point $x \in K$ with $T(x) = x$ for every $T \in \mathcal{F}$.

## Remarks

For $T \in \mathcal{F}$ and $n \ge 1$, let $A_{T,n} = \frac1n (I + T + \cdots + T^{n-1})$, an affine map of $K$ into $K$ by convexity.
If $x = A_{T,n}(y)$, then $T(x) - x = \frac1n (T^n(y) - y)$ lies in $\frac1n(K - K)$.
Since $K - K$ is compact, hence bounded, every point of $\bigcap_n A_{T,n}(K)$ is a [[fixed point|R6QVS6P21N]] of $T$, as $X$ is Hausdorff.
Because the maps commute, the compact sets $A_{T_1,n_1} \cdots A_{T_k,n_k}(K)$ lie in each $A_{T_i,n_i}(K)$, so the family of all $A_{T,n}(K)$ has the finite intersection property, and its intersection is nonempty.

Example: an [[abelian group|082GHNPJ53]] $G$ acts on the weak-$*$ compact convex set of means on $\ell^\infty(G)$ by commuting affine continuous maps.
A common fixed point is an invariant mean, so $G$ is [[amenable|CEAT9BESKK]].

The commutativity hypothesis cannot be dropped.
The affine maps $x \mapsto x/2$ and $x \mapsto (x+1)/2$ of $[0,1]$ do not commute.
Their only fixed points are $0$ and $1$, so they have no common fixed point.

## Explanations

### L1 human

A single continuous affine map of a compact convex set into itself has a fixed point.
The theorem says that a whole family of such maps has a common fixed point, as long as the maps commute.
The trick is to average the iterates of each map, which pushes every point toward the fixed points.

### L2 human

The theorem is the abelian prototype of the fixed point characterizations of amenability.
Applied to the set of means, it shows that abelian groups are amenable; [[Day's fixed point theorem|DC9NJQPF1S]] extends this to all amenable groups.
Compared with the [[Kakutani fixed-point theorem|7V3HWGR32Z]] for set-valued maps, it needs affine maps but allows an arbitrary commuting family.
