---
tag: RC7EHXQS8F
kind: definition
name: Zero-knowledge proof
msc: [68Q10, 94A60, 68Q15]
defines: 8JGQQCPNQT
uses: [7PFQZJF1DX, K99S0Q0814]
sources:
  - url: https://en.wikipedia.org/wiki/Zero-knowledge_proof
    locator: Definition
---

## Definition

Let $L \subseteq \set{0,1}^*$ be a language, and let $(P, V)$ be an [[interactive proof system|7PFQZJF1DX]] for $L$, with prover $P$ and verifier $V$.
Let $V^*$ be an interactive algorithm and $x$ an input.
The *view* of $V^*$ on $x$ is the random variable made of $x$, the random bits of $V^*$ and the messages it receives from $P$.
The system $(P, V)$ is *computational zero-knowledge* if the following holds.

Let $V^*$ be any [[probabilistic|K99S0Q0814]] polynomial-time interactive algorithm.
Then there is a probabilistic algorithm $S$ in expected polynomial time, the *simulator*, such that these two families of random variables
$$\set{S(x)}_{x \in L} \quad\text{and}\quad \set{\mathrm{view}_{V^*}(x)}_{x \in L}$$
are computationally indistinguishable.
This means that for every probabilistic polynomial-time algorithm $D$ and every polynomial $p$, for all sufficiently long $x \in L$,
$$\abs{\Pr[D(x, S(x)) = 1] - \Pr[D(x, \mathrm{view}_{V^*}(x)) = 1]} < \frac{1}{p(\abs{x})}.$$

If the two distributions are equal for every $x \in L$, the system is *perfect zero-knowledge*.
If their statistical distance is negligible in $\abs{x}$, it is *statistical zero-knowledge*.

## Remarks

Example: the protocol for graph isomorphism is perfect zero-knowledge.
The common input is two graphs $G_0, G_1$ on $n$ vertices, and the prover knows an isomorphism $\pi \colon G_0 \to G_1$.
The prover sends $H = \sigma(G_1)$ for a uniformly random permutation $\sigma$; the verifier sends a random bit $b$; the prover sends an isomorphism from $G_b$ to $H$, namely $\sigma \circ \pi$ or $\sigma$.
If $G_0 \not\cong G_1$, a cheating prover fails with probability at least $1/2$ in each round.
The simulator guesses $b'$, sends $H = \tau(G_{b'})$ for a random $\tau$, and restarts when the verifier's bit differs from $b'$; when it does not, the transcript has exactly the right distribution.

Non-example: the protocol in which the prover simply sends the isomorphism $\pi$ is an interactive proof, but it is not known to be zero-knowledge.
A simulator would have to output an isomorphism between $G_0$ and $G_1$, and no efficient algorithm for that is known.

Zero-knowledge is a property of the prover's strategy: soundness and completeness still come from the interactive proof system.
Under the assumption that one-way functions exist, every language in NP has a computational zero-knowledge proof (Goldreich, Micali and Wigderson).
