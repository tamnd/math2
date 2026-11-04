---
tag: WS1TA6AK3B
kind: statement
role: proposition
name: A group structure implies the axiom of choice
sources:
  - wikipedia: en:37039918@r1336022484
    locator: Group structure and the axiom of choice, section A group structure implies the axiom of choice
    note: adopted
    mention: wikipedia://en/37039918#54MP
    sections: [Statement]
inventory: [A9KQ26MMSB]
---

## Statement

In this section it is assumed that every set $X$ can be endowed with a group structure $(X, \bullet)$.

Let $X$ be a set. Let $\aleph(X)$ be the Hartogs number of $X$. This is the least [[cardinal number|0EBACQFAZW]] such that there is no injection from $\aleph(X)$ into $X$. It exists without the assumption of the axiom of choice. Assume here for technical simplicity of proof that $X$ has no [[ordinal|0RDJK7EQYY]]. Let $\bullet$ denote multiplication in the group $(X \cup \aleph(X), \bullet)$.

For any $x \in X$ there is an $\alpha \in \aleph(X)$ such that $x \bullet \alpha \in \aleph(X)$. Suppose not. Then there is an $y \in X$ such that $y \bullet \alpha \in X$ *for all* $\alpha \in \aleph(X)$. But by elementary group theory, the $y \bullet \alpha$ are all different as α ranges over $\aleph(X)$ (**i**). Thus such a $y$ gives an injection from $\aleph(X)$ into $X$. This is impossible since $\aleph(X)$ is a cardinal such that no injection into $X$ exists.

Now define a map $j$ of $X$ into $\aleph(X) \times \aleph(X)$ endowed with the lexicographical wellordering by sending $x \in X$ to the least $(\alpha, \beta) \in \aleph(X) \times \aleph(X)$ such that $x \bullet \alpha = \beta$. By the above reasoning the map $j$ exists and is unique since least elements of subsets of wellordered sets are unique. It is, by elementary group theory, injective.

Finally, define a wellordering on $X$ by $x < y$ if $j(x) < j(y)$. It follows that every set $X$ can be wellordered and thus that the axiom of choice is true.

For the crucial property expressed in (**i**) above to hold, and hence the whole proof, it is sufficient for $X$ to be a cancellative magma, e.g. a quasigroup. The cancellation property is enough to ensure that the $y \bullet \alpha$ are all different.
