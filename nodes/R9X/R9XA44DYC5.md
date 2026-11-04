---
tag: R9XA44DYC5
kind: proof
name: Proof of Ping-pong lemma for several subgroups
proves: K71BN4C02T
sources:
  - wikipedia: en:18786361@r1361203357
    locator: Ping-pong lemma, section Formal statements > Ping-pong lemma for several subgroups > Proof
    note: adopted
    mention: wikipedia://en/18786361#HWB7
    sections: [Proof]
---

## Proof

By the definition of free product, it suffices to check that a given (nonempty) reduced word represents a nontrivial element of $G$. Let $w$ be such a word of length $m\geq 2$, and let

$$w = \prod_{i=1}^m w_i,$$

where $w_i \in H_{\alpha_i}$ for some $\alpha_i \in \{1,\dots,k\}$. Since $w$ is reduced, we have $\alpha_i \neq \alpha_{i+1}$ for any $i = 1, \dots, m-1$ and each $w_i$ is distinct from the [[identity element|07WYQPB8E3]] of $H_{\alpha_i}$. We then let $w$ [[act|0WCY42EV9V]] on an element of one of the sets $X_i$. As we assume that at least one subgroup $H_i$ has order at least 3, without loss of generality we may assume that $H_1$ has order at least 3. We first make the assumption that $\alpha_1$and $\alpha_m$ are both 1 (which implies $m \geq 3$). From here we consider $w$ acting on $X_2$. We get the following chain of containments:

$$w(X_2) \subseteq \prod_{i=1}^{m-1} w_i(X_1) \subseteq \prod_{i=1}^{m-2} w_i(X_{\alpha_{m-1}}) \subseteq \dots \subseteq w_1(X_{\alpha_2}) \subseteq X_1.$$

By the assumption that different $X_i$'s are disjoint, we conclude that $w$ acts nontrivially on some element of $X_2$, thus $w$ represents a nontrivial element of $G$.

To finish the proof we must consider the three cases:

- if $\alpha_1 = 1,\,\alpha_m \neq 1$, then let $h\in H_1\setminus \{w_1^{-1},1\}$ (such an $h$ exists since by assumption $H_1$ has order at least 3);
- if $\alpha_1 \neq 1,\,\alpha_m=1$, then let $h\in H_1\setminus \{w_m,1\}$;
- and if $\alpha_1\neq 1,\,\alpha_m\neq 1$, then let $h\in H_1\setminus \{1\}$.

In each case, $hwh^{-1}$ after reduction becomes a reduced word with its first and last letter in $H_1$. Finally, $hwh^{-1}$ represents a nontrivial element of $G$, and so does $w$. This proves the claim.
