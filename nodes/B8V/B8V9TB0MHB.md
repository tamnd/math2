---
tag: B8V9TB0MHB
kind: statement
role: proposition
name: The generalized continuum hypothesis holds in L
sources:
  - wikipedia: en:343335@r1372309993
    locator: Constructible universe, section The generalized continuum hypothesis holds in L
    note: adopted
    mention: wikipedia://en/343335#YM9I
    sections: [Statement]
inventory: [99MTB94Y8D]
---

## Statement

Let $S \in L_\alpha$, and let $T$ be any constructible subset of $S$. Then there is some $\beta$ with $T \in L_{\beta+1}$, so $T = \{x \in L_\beta : x \in S \wedge \Phi(x, z_i)\} = \{x \in S : \Phi(x, z_i)\}$, for some formula $\Phi$ and some $z_i$ drawn from $L_\beta$. By the downward Löwenheim–Skolem theorem and Mostowski collapse, there must be some transitive set $K$ containing $L_\alpha$ and some $w_i$, and having the same first-order theory as $L_\beta$ with the $w_i$ substituted for the $z_i$; and this $K$ will have the same cardinal as $L_\alpha$. Since $V = L$ is true in $L_\beta$, it is also true in $K$, so $K = L_\gamma$ for some $\gamma$ having the same cardinal as $\alpha$. And $T = \{x \in L_\beta : x \in S \wedge \Phi(x, z_i)\} = \{x \in L_\gamma : x \in S \wedge \Phi(x, w_i)\}$ because $L_\beta$ and $L_\gamma$ have the same theory. So $T$ is in fact in $L_{\gamma+1}$.

So all the constructible subsets of an infinite set $S$ have ranks with (at most) the same cardinal $\kappa$ as the rank of $S$; it follows that if $\delta$ is the initial ordinal for $\kappa^+$, then $L \cap \mathcal{P}(S) \subseteq L_\delta$ serves as the "power set" of $S$ within $L$ Thus this "power set" $L \cap \mathcal{P}(S) \in L_{\delta+1}$. And this in turn means that the "power set" of $S$ has cardinal at most $\vert\delta\vert$. Assuming $S$ itself has cardinal $\kappa$, the "power set" must then have cardinal exactly $\kappa^+$. But this is precisely the generalized continuum hypothesis relativized to $L$.
