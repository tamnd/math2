---
tag: 8QTP2EFA92
kind: definition
name: Bernstein–Gelfand–Ponomarev reflection functors
msc: [16G20]
defines: MG4RNMA8AR
uses: [RE9YFFS3TS, TXVWFWP6VQ, 04C5ZBG1WT, 28NQ0KRHD3, E2P29GCD9T]
sources:
  - url: https://en.wikipedia.org/wiki/Gabriel%27s_theorem
---

## Definition

Let $k$ be a [[field|04C5ZBG1WT]] and let $Q$ be a finite [[quiver|RE9YFFS3TS]].
A vertex $i$ is a *sink* if no arrow has source $i$, and a *source* if no arrow has target $i$.
Let $\sigma_i Q$ be the quiver obtained from $Q$ by reversing every arrow incident to $i$; write $a^*$ for the reverse of $a$.
Let $i$ be a sink of $Q$ and $V$ a [[representation|TXVWFWP6VQ]] of $Q$ over $k$.
The representation $S_i^+ V$ of $\sigma_i Q$ is defined by:

1. $(S_i^+ V)_j = V_j$ and $(S_i^+ V)_b = V_b$ for vertices $j \ne i$ and arrows $b$ not incident to $i$;
2. $(S_i^+ V)_i = \ker \big( \bigoplus_{a \colon j \to i} V_j \xrightarrow{(V_a)} V_i \big)$, the sum taken over the arrows $a$ ending at $i$;
3. for an arrow $a \colon j \to i$, the map $(S_i^+ V)_{a^*} \colon (S_i^+ V)_i \to V_j$ is the inclusion of the kernel followed by the projection onto the summand $V_j$ of index $a$.

With the evident action on morphisms, $S_i^+$ is a [[functor|28NQ0KRHD3]].
Dually, for a source $i$, $S_i^-$ replaces $V_i$ by the cokernel of $V_i \to \bigoplus_{a \colon i \to j} V_j$.

## Remarks

Let $S_i$ be the simple representation at $i$.
If $V$ is [[indecomposable|E2P29GCD9T]] and $V \not\cong S_i$, then $S_i^+ V$ is indecomposable, $S_i^- S_i^+ V \cong V$, and the dimension vector changes by $\dim (S_i^+ V)_i = \sum_{a \colon j \to i} \dim V_j - \dim V_i$.
Also $S_i^+ S_i = 0$.
Example: for $Q = (1 \xrightarrow{a} 2)$, the vertex $2$ is a sink.
For $V = (k \xrightarrow{\id} k)$, the kernel of $\id \colon k \to k$ is $0$, so $S_2^+ V$ is the representation $k \leftarrow 0$ of $1 \leftarrow 2$.
Its dimension vector $(1, 0)$ is the image of $(1, 1)$ under the reflection $x_2 \mapsto x_1 - x_2$.
Non-example: $S_1^+$ is not defined on $Q$, because vertex $1$ is not a sink.
