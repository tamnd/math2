---
tag: EHMQC1ZBK9
kind: definition
name: Tits–Kantor–Koecher construction
msc: [17C50, 17B60, 17B70]
defines: FZM1A8HAHD
uses: [CDN2B4S8YW, M13DZ6YXH1, 6C2MCVB8C7, 5JJYBJ6A8K]
sources:
  - url: https://en.wikipedia.org/wiki/Kantor–Koecher–Tits_construction
---

## Definition

Let $F$ be a field of characteristic different from $2$, and let $(V^+, V^-)$ be a [[Jordan pair|CDN2B4S8YW]] over $F$ with triple products $\set{\cdot, \cdot, \cdot}$.
For $x \in V^+$ and $y \in V^-$, let $D(x, y)$ be the linear map of $V^+ \oplus V^-$ given by $z \mapsto \set{x, y, z}$ on $V^+$ and $w \mapsto -\set{y, x, w}$ on $V^-$.
Let $\mathfrak{d}$ be the linear span of all $D(x, y)$.
The *Tits–Kantor–Koecher algebra* is the vector space $\mathrm{TKK}(V^+, V^-) = V^- \oplus \mathfrak{d} \oplus V^+$ with the bilinear bracket defined by:

1. $[x, x'] = 0$ for $x, x' \in V^+$, and $[y, y'] = 0$ for $y, y' \in V^-$;
2. $[x, y] = D(x, y) = -[y, x]$ for $x \in V^+$ and $y \in V^-$;
3. $[D, v] = D(v) = -[v, D]$ for $D \in \mathfrak{d}$ and $v \in V^+ \cup V^-$;
4. $[D, D'] = DD' - D'D$ for $D, D' \in \mathfrak{d}$.

For a [[Jordan algebra|6C2MCVB8C7]] $J$, one applies this to the pair $(J, J)$ with $\set{x, y, z} = (xy)z + (zy)x - (zx)y$.

## Remarks

The identity of a Jordan pair gives $[D(u, v), D(x, y)] = D(\set{u, v, x}, y) - D(x, \set{v, u, y})$, so clause 4 stays in $\mathfrak{d}$.
With these clauses, $\mathrm{TKK}(V^+, V^-)$ is a [[Lie algebra|5JJYBJ6A8K]], graded with $V^-$, $\mathfrak{d}$, $V^+$ in degrees $-1$, $0$, $1$.

Example: $J = F$ with its usual product, so $\set{x, y, z} = xyz$.
Put $e = 1 \in V^+$, $f = 2 \in V^-$ and $h = D(1, 2)$.
Then $h$ acts by $2$ on $V^+$ and by $-2$ on $V^-$, so $[h, e] = 2e$, $[h, f] = -2f$ and $[e, f] = h$.
These are the relations of $\mathfrak{sl}_2(F)$.

Non-example: $\mathfrak{gl}_2(F)$ with the grading by $e_{12}$, the diagonal matrices and $e_{21}$ is not the TKK algebra of $(F, F)$.
Its degree $0$ part is $2$-dimensional, while $\mathfrak{d}$ is spanned by the single map $D(1, 1)$.
