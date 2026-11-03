---
tag: FRP6TPF0SV
kind: definition
name: Interactive proof system
msc: [68Q10, 68Q15, 68Q87]
defines: 7PFQZJF1DX
uses: [K99S0Q0814, 5MFZ4VNY6D, ESPYW94XGR]
sources:
  - url: https://en.wikipedia.org/wiki/Interactive_proof_system
---

## Definition

A *verifier* is a [[probabilistic Turing machine|K99S0Q0814]] $V$ that, on input $x$, exchanges messages with a *prover* $P$.
The prover is an arbitrary function from the input and the messages so far to the next message.
Both see the input $x$; only $V$ sees its own random bits.
After the exchange $V$ outputs accept or reject.
Let $L \subseteq \set{0,1}^*$ be a language.
An *interactive proof system* for $L$ is a verifier $V$ together with a polynomial $q$ such that:

1. on every input $x$, the exchange has at most $q(\abs{x})$ messages and $V$ runs in at most $q(\abs{x})$ steps in total, whatever the prover does;
2. (completeness) there is a prover $P$ such that for every $x \in L$, $V$ accepts with probability at least $2/3$ when interacting with $P$;
3. (soundness) for every $x \notin L$ and every prover $P^*$, $V$ accepts with probability at most $1/3$ when interacting with $P^*$.

The class *IP* is the class of languages that have an interactive proof system.

## Remarks

Example: graph non-isomorphism.
On input two graphs $G_0, G_1$ on $n$ vertices, $V$ picks a uniform bit $b$ and a uniform permutation $\pi$ of the vertices.
It sends the graph $\pi(G_b)$ and asks the prover for $b$.
This is done twice, and $V$ accepts if both answers are right.
If $G_0$ and $G_1$ are not isomorphic, an all-powerful prover finds $b$ from $\pi(G_b)$ and $V$ always accepts.
If they are isomorphic, $\pi(G_b)$ has the same distribution for $b = 0$ and $b = 1$, so any prover is right in each round with probability $1/2$, and $V$ accepts with probability $1/4$.

Non-example: a verifier that accepts whenever the prover sends the message "yes" fails clause 3 for every $x \notin L$, since a cheating prover sends "yes".

If $V$ uses no random bits, the prover can compute all of $V$'s messages in advance, and the protocol amounts to a single certificate.
Such systems give exactly the class NP.
Constants $2/3$ and $1/3$ can be replaced by $1 - 2^{-\abs{x}}$ and $2^{-\abs{x}}$ by repetition.
If the verifier's random bits are public, the protocol is an [[Arthur–Merlin protocol|289YQN382E]].
