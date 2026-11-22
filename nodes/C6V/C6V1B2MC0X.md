---
tag: C6V1B2MC0X
kind: proof
name: Proof of the dimension theorem for infinite bases by cardinal arithmetic
msc: ["15A03", "03E10"]
topics: [MVH97H8B2J]
audience: grad
proves: 0WK0Y8RH1M
methods: [0NTF6DMVAP, 0J0XBKG64S]
uses: [WXB40PTZNV, H75GS7QVPB, 0VTQTPQGAV, 0QKPNZKNEA, 0A9V6RKQG6]
sources:
  - url: https://en.wikipedia.org/wiki/Dimension_theorem_for_vector_spaces
    locator: Proof
  - url: https://en.wikipedia.org/wiki/Cardinal_number
    locator: Cardinal arithmetic
  - book: isbn:9780387728285
    locator: Chapter 1
---

## Proof

We cover one basis by finite pieces, one piece for each vector of the other basis, and then count the pieces.
A basis is an independent family, so its members are distinct, and we may treat bases as sets.
We use one fact of cardinal arithmetic, which rests on the axiom of choice: if $\kappa$ is an infinite [[cardinal|0QKPNZKNEA]], then a union of at most $\kappa$ finite sets has at most $\kappa \cdot \aleph_0 = \kappa$ elements.

1. Let $B$ and $C$ be bases of $V$. If one of them is finite, then both are finite and of the same size, by the [[proof for finite bases|WXB40PTZNV]]. So we may assume that $B$ and $C$ are both infinite.
2. Each $c \in C$ has a unique expansion $c = \sum_{b \in B} a_b b$ in which only finitely many $a_b$ are nonzero, because $B$ is a basis. Let $S_c = \{ b \in B : a_b \ne 0 \}$, a finite subset of $B$.
3. We claim that $B = \bigcup_{c \in C} S_c$. Suppose, for a contradiction, that some $b_0 \in B$ lies in no $S_c$.
4. Then every $c \in C$ is a combination of vectors of $B \setminus \{ b_0 \}$, so $C$ lies in the span of $B \setminus \{ b_0 \}$.
5. This span is a subspace that contains $C$, and $C$ spans $V$, so the span of $B \setminus \{ b_0 \}$ is all of $V$. In particular it contains $b_0$.
6. So $b_0$ is a combination of other vectors of $B$, and $B$ is dependent, as the [[dependence lemma|H75GS7QVPB]] states. This contradicts the independence of $B$, so the claim holds.
7. By the claim, $B$ is a union of at most $|C|$ finite sets. Since $C$ is infinite, the cited fact gives $|B| \le |C| \cdot \aleph_0 = |C|$.
8. Steps 2 to 7 with the roles of $B$ and $C$ exchanged give $|C| \le |B|$.
9. By the [[Schröder-Bernstein theorem|0A9V6RKQG6]], $|B| = |C|$.

## Idea

Each vector of the basis $C$ is built from finitely many vectors of the basis $B$.
Every vector of $B$ must take part in some of these expansions, or else it would not be needed to build $V$ and $B$ would be dependent.
So $B$ is covered by $|C|$ finite sets, and an infinite cardinal does not grow when we multiply it by $\aleph_0$.
For example, a space with a countable basis cannot also have an uncountable basis, because countably many finite sets cover only countably many vectors.

## Variants

Steps 2 to 7 use less than the full hypothesis: they need $B$ to be a basis, but they need only that $C$ spans $V$.
So the same argument shows that if a space has a basis $B$ and an infinite spanning set $C$, then $|B| \le |C|$, which is an infinite form of the [[Steinitz exchange lemma|08ZDRN6H41]].
For the finite case one can use either the exchange proof or the [[proof by row reduction|2BVBSVQYMB]] in step 1.
