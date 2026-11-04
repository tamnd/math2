---
tag: M8F3PDB9GM
kind: proof
name: Proof that extensions of solvable groups are solvable
msc: [20F16]
proves: 01EY0EM7RP
uses: [0P3KZK0FTV, 096HN851YZ, 0YYWCNTPWR, 0W77CVBCHQ, 0HV9Y7WG5R, 0Z424HK8CQ, 0C9ZKYSPYR, 0CXXJNG5B6]
sources:
  - url: https://en.wikipedia.org/wiki/Solvable_group
    locator: Properties
---

## Proof

We lift a series of $G/N$ to $G$ and put a series of $N$ below it.

1. Since $N$ is [[solvable|0P3KZK0FTV]], it has a [[subnormal series|096HN851YZ]] $\{e\} = N_0 \trianglelefteq \cdots \trianglelefteq N_k = N$ with abelian factors.
2. Since $G/N$ is solvable, it has a subnormal series $\{N\} = Q_0 \trianglelefteq \cdots \trianglelefteq Q_l = G/N$ with abelian factors. Here $N$ is the identity of the [[quotient group|0YYWCNTPWR]].
3. Let $\pi \colon G \to G/N$ be the projection $\pi(g) = gN$. It is a surjective [[homomorphism|0HV9Y7WG5R]] with kernel $N$.
4. For $0 \leq j \leq l$, let $M_j = \pi^{-1}(Q_j) = \{g \in G : \pi(g) \in Q_j\}$. It is a subgroup of $G$, since $\pi(xy^{-1}) = \pi(x)\pi(y)^{-1}$.
5. We have $M_0 = \pi^{-1}(\{N\}) = N$ and $M_l = G$.
6. Fix $j$ with $1 \leq j \leq l$. Since $\pi$ is surjective, $\pi(M_j) = Q_j$.
7. Define $\psi_j \colon M_j \to Q_j/Q_{j-1}$ by $\psi_j(x) = \pi(x) Q_{j-1}$. It is a homomorphism, as a composite of homomorphisms. By step 6 it is surjective.
8. The [[kernel|0Z424HK8CQ]] of $\psi_j$ is $\{x \in M_j : \pi(x) \in Q_{j-1}\} = M_{j-1}$.
9. Since [[the kernel is a normal subgroup|0C9ZKYSPYR]], $M_{j-1} \trianglelefteq M_j$.
10. By the [[first isomorphism theorem|0CXXJNG5B6]], $M_j/M_{j-1} \cong Q_j/Q_{j-1}$, which is abelian. So $M_j/M_{j-1}$ is abelian.
11. Put the two series together: $\{e\} = N_0 \trianglelefteq \cdots \trianglelefteq N_k = N = M_0 \trianglelefteq M_1 \trianglelefteq \cdots \trianglelefteq M_l = G$.
12. Each term is [[normal|0W77CVBCHQ]] in the next, by steps 1 and 9. Each factor is abelian, by steps 1 and 10.
13. So $G$ has a subnormal series with abelian factors, and $G$ is solvable.

## Idea

The series of $G/N$ pulls back to a chain of subgroups of $G$ from $N$ up to $G$, with the same factors. Below $N$ we use the series of $N$. Stacking the two chains gives a series of $G$ with abelian factors.
