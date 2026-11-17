---
tag: ~e8fafa0d
kind: proof
name: Proof of the compactness theorem from the completeness theorem
msc: ["03C07", "03B10"]
topics: [FBWW4J1XWG]
audience: ug2
proves: 1NR3HAWG9D
uses: [G0DTR159RN, WQ1ZE255SF, ~331f6430, ~bc83b0fa, VM8TQ70CVJ, QN7M1JCGT9, MVCH6N9SNW]
methods: [0J0XBKG64S, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Compactness_theorem
    locator: Proofs
  - book: isbn:9780122384523
    locator: Section 2.5
---

## Proof

Derivability $\vdash$ is in the Hilbert system $H$ of the [[soundness theorem|~331f6430]].

Part 1.

1. Let $\Gamma$ be satisfiable, with a model $\mathcal{A}$. Every finite $\Gamma_0 \subseteq \Gamma$ has the model $\mathcal{A}$. So $\Gamma$ is finitely satisfiable.
2. Conversely, let $\Gamma$ be finitely satisfiable. Suppose that $\Gamma$ is not [[consistent|VM8TQ70CVJ]], so $\Gamma \vdash \psi$ and $\Gamma \vdash \neg \psi$ for some $\psi$.
3. The two derivations are finite lists. Together they use a finite set $\Gamma_0 \subseteq \Gamma$, and $\Gamma_0 \vdash \psi$, $\Gamma_0 \vdash \neg \psi$.
4. $\Gamma_0$ has a model by step 2. By part 3 of the soundness theorem, $\Gamma_0$ is consistent. This contradicts step 3.
5. So $\Gamma$ is consistent. The [[model existence theorem|G0DTR159RN]] gives a model of $\Gamma$, with at most $\max(|L|, \aleph_0)$ elements. This proves parts 1 and 3.

Part 2.

6. If $\Gamma_0 \subseteq \Gamma$ and $\Gamma_0 \models \varphi$, then every model of $\Gamma$ is a model of $\Gamma_0$, so $\Gamma \models \varphi$.
7. Conversely, let $\Gamma \models \varphi$. By [[Gödel's completeness theorem|WQ1ZE255SF]], $\Gamma \vdash \varphi$.
8. The derivation uses a finite $\Gamma_0 \subseteq \Gamma$, so $\Gamma_0 \vdash \varphi$. By the soundness theorem, $\Gamma_0 \models \varphi$.

## Idea

A contradiction is derived in finitely many steps, so it uses finitely many hypotheses.
If every finite part has a model, then no finite part is contradictory, by soundness.
So the whole set is consistent, and a consistent set has a model.

## Variants

- Part 2 also follows from part 1 directly: $\Gamma \models \varphi$ iff $\Gamma \cup \set{\neg \varphi}$ is not satisfiable. Apply part 1 to $\Gamma \cup \set{\neg \varphi}$.
- The [[ultraproduct proof|~e411426e]] avoids proof systems.
- For countable $L$, the proof needs no axiom of choice, because the model existence theorem for countable $L$ does not use it.
