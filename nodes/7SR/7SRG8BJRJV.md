---
tag: 7SRG8BJRJV
kind: example
name: The finite stages of the consistency progression over PA
msc: ["03F40", "03F15"]
topics: [HXHHWY3328]
audience: research
instance_of: [F7Z4BV2KHD]
uses: [F7Z4BV2KHD, 4NBAX3VRQ7, 4PZM5GJTR5, MPSCREYC3M, 4A84VHDTHV, WHAP0K600D, 0ASJVEFA9J]
sources:
  - url: https://en.wikipedia.org/wiki/G%C3%B6del%27s_incompleteness_theorems
    locator: Second incompleteness theorem
  - url: https://en.wikipedia.org/wiki/Systems_of_Logic_Based_on_Ordinals
    locator: lead section
---

## Example

Define theories in the language $\set{0, S, +, \cdot}$ by $T_0 = \mathsf{PA}$ and $T_{k+1} = T_k + \mathrm{Con}(T_k)$ for $k \in \N$.
Here $\mathrm{Con}(T_k)$ is the [[consistency statement|4NBAX3VRQ7]] built from the natural formula that defines the axioms of $T_k$: the axioms of $\mathsf{PA}$ together with $\mathrm{Con}(T_0), \ldots, \mathrm{Con}(T_{k-1})$.
Let $T_\omega = \bigcup_k T_k$.
In the notation of [[Kleene's O|WHAP0K600D]], $T_k$ is the stage at the notation $1$, $2$, $4$, $16$, $65536, \ldots$ of $k$, where each notation is $2$ to the power of the one before.
The theory $T_\omega$ is the stage at a notation $3 \cdot 5^e$ where $\varphi_e$ lists these notations.
These are the first stages of Turing's consistency progression, an instance of the [[Turing and Feferman progressions|F7Z4BV2KHD]].
We check that the stages are sound and strictly increasing, and that $T_\omega$ again does not prove its own consistency.

1. Each $T_k$ has a decidable set of axioms. The axioms of $\mathsf{PA}$ form a decidable set, and $T_k$ adds $k$ further sentences, each computed from the previous ones.
2. Each $T_k$ is sound, that is, all its axioms are true in $\N$. We use [[induction|0ASJVEFA9J]] on $k$. For $k = 0$, the axioms of $\mathsf{PA}$ are true in $\N$.
3. Induction step: assume that $T_k$ is sound. By the [[soundness theorem|4A84VHDTHV]], every theorem of $T_k$ is true in $\N$, so $T_k$ does not prove the false sentence $0 = S0$.
4. The sentence $\mathrm{Con}(T_k)$ is true in $\N$ exactly when $T_k$ does not prove $0 = S0$, by the meaning of the provability predicate. So $\mathrm{Con}(T_k)$ is true, and all axioms of $T_{k+1}$ are true.
5. Each $T_k$ is consistent, because a sound theory proves no false sentence (step 3).
6. $T_k$ does not prove $\mathrm{Con}(T_k)$. The theory $T_k$ is consistent (step 5), contains $\mathsf{PA}$, and has decidable axioms (step 1), so [[Gödel's second incompleteness theorem|4PZM5GJTR5]] applies.
7. So $T_{k+1}$ proves a sentence that $T_k$ does not prove, and $T_0 \subsetneq T_1 \subsetneq T_2 \subsetneq \cdots$ as sets of theorems.
8. The map $k \mapsto \mathrm{Con}(T_k)$ is computable, so the axioms of $T_\omega$ form a computably enumerable set, defined by a $\Sigma_1$ formula. All of them are true (step 4), so $T_\omega$ is sound and consistent.
9. By the second incompleteness theorem for $T_\omega$, with the $\Sigma_1$ formula of step 8 as its axiom formula, $T_\omega$ does not prove $\mathrm{Con}(T_\omega)$. So the progression continues with the sound theory $T_{\omega + 1} = T_\omega + \mathrm{Con}(T_\omega)$.

## Remarks

The example shows the two basic facts of a consistency progression: soundness is preserved, and each successor step is a proper extension.
All the added axioms $\mathrm{Con}(T_k)$ are true $\Pi_1$ sentences.
By [[consistency as Π1 reflection|JHGJ6APMRF]], $T_{k+1}$ proves every instance of local reflection for $T_k$ restricted to $\Pi_1$ sentences.
If we start from an unsound base, such as $\mathsf{PA} + \neg \mathrm{Con}(\mathsf{PA})$, then step 2 fails.
That base proves $\neg \mathrm{Con}(\mathsf{PA})$, and so also $\neg \mathrm{Con}(T_0)$ for itself as $T_0$, because a proof of $0 = S0$ in $\mathsf{PA}$ is also a proof in $T_0$.
So $T_1$ is inconsistent.
If we change the formula that defines the axioms of $T_\omega$, the theory $T_\omega$ keeps the same theorems, but $\mathrm{Con}(T_\omega)$ can change; this is the dependence on notations at stage $\omega + 1$.

## Explanations

### L1 human

Start with the usual axioms of arithmetic.
Add the axiom "the usual axioms never lead to a contradiction"; this is true, and Gödel showed it is new.
The bigger list again cannot prove its own consistency, so add that too.
Repeat forever: we get a chain of lists, each one stronger than the last.
Put all lists of the chain together; the result still cannot prove its own consistency, so the process goes on beyond the finite steps.

### L2 human

We follow the first two steps with the notations of Kleene's $\mathcal{O}$.

1. Stage $0$ has notation $1$ and theory $T_0 = \mathsf{PA}$.
2. Stage $1$ has notation $2^1 = 2$ and theory $T_1 = \mathsf{PA} + \mathrm{Con}(\mathsf{PA})$, which is sound by step 4 and strictly stronger than $\mathsf{PA}$ by step 6.
3. Stage $2$ has notation $2^2 = 4$ and theory $T_2 = T_1 + \mathrm{Con}(T_1)$.
4. Stage $3$ has notation $2^4 = 16$, and stage $4$ has notation $2^{16} = 65536$.
5. $T_2$ proves $\mathrm{Con}(\mathsf{PA})$ and $\mathrm{Con}(T_1)$, but not $\mathrm{Con}(T_2)$.

The typical use of these stages is as a scale: one asks which stage proves the same $\Pi_1$ sentences as a given theory.
A trap is to think that $\mathrm{Con}(T_1)$ follows from $\mathrm{Con}(\mathsf{PA})$; in fact $T_1$ does not prove it, by step 6 for $k = 1$.
