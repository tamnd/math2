---
tag: X0XEJQ4TAA
kind: proof
name: Proof of the correspondence theorem for vector spaces
msc: ["15A03"]
topics: [QHKTJ89V6S]
audience: ug1
proves: GCHY414Y11
methods: [0NTF6DMVAP, MKHVRNW68H]
uses: [0SVR29SV1V, 0J0SK5FF4M, 0EPTJA5QV4, 0JB228DCWB]
sources:
  - url: https://en.wikipedia.org/wiki/Correspondence_theorem
---

## Proof

We check that both maps land in the right sets, that each composite is the identity, and that both maps preserve inclusion.

1. The [[quotient map|0J0SK5FF4M]] $\pi \colon V \to V / U$ is linear and surjective, and its kernel is $U$.
2. Let $X$ be a [[subspace|0EPTJA5QV4]] of $V$ with $U \subseteq X$.
   Its [[image|0JB228DCWB]] $\pi(X)$ is a subspace of $V / U$, since the image of a subspace under a linear map is a subspace.
3. Let $Y$ be a subspace of $V / U$.
   Its preimage $\pi^{-1}(Y)$ is a subspace of $V$, since the preimage of a subspace under a linear map is a subspace.
   It contains $U = \pi^{-1}(\{0\})$, since $0 \in Y$.
4. So $X \mapsto \pi(X)$ and $Y \mapsto \pi^{-1}(Y)$ are maps between the two sets of the statement.
5. We show $\pi(\pi^{-1}(Y)) = Y$.
   The inclusion $\pi(\pi^{-1}(Y)) \subseteq Y$ holds for every map.
   For the other inclusion, let $y \in Y$; since $\pi$ is surjective, $y = \pi(v)$ for some $v \in V$, and then $v \in \pi^{-1}(Y)$, so $y \in \pi(\pi^{-1}(Y))$.
6. We show $\pi^{-1}(\pi(X)) = X$.
   The inclusion $X \subseteq \pi^{-1}(\pi(X))$ holds for every map.
7. For the other inclusion, let $v \in \pi^{-1}(\pi(X))$.
   Then $\pi(v) = \pi(x)$ for some $x \in X$, so $v - x \in \ker \pi = U$, and $U \subseteq X$ by hypothesis.
   Hence $v = x + (v - x)$ is a sum of two vectors of $X$, so $v \in X$.
8. By steps 5 to 7, the two maps are inverse to each other, so both are bijections.
9. If $X_1 \subseteq X_2$, then $\pi(X_1) \subseteq \pi(X_2)$, and if $Y_1 \subseteq Y_2$, then $\pi^{-1}(Y_1) \subseteq \pi^{-1}(Y_2)$.
   So both maps preserve inclusion.

## Idea

Two facts about $\pi$ do all the work.
Because $\pi$ is surjective, taking the image of a preimage gives back the subspace of the quotient.
Because $X$ contains the kernel $U$, the subspace $X$ is a union of whole cosets of $U$, so taking the preimage of its image adds nothing new.
Step 7 is exactly where the hypothesis $U \subseteq X$ is used, and it fails for $X = \{0\}$ when $U \ne \{0\}$.

## Variants

The same proof works for submodules of a module, for normal subgroups that contain a fixed normal subgroup, and for ideals that contain a fixed ideal, because it uses only a surjective homomorphism and its kernel.
Step 7 can also be phrased with cosets: since $U \subseteq X$, each coset $x + U$ with $x \in X$ lies inside $X$, and $\pi^{-1}(\pi(X))$ is the union of these cosets.
