---
tag: SNFGJD6FQE
kind: proof
name: Proof of the criterion for finite axiomatizability by compactness
msc: ["03C52"]
topics: [AY09KYSW81]
audience: ug2
proves: 9XKWFMVKJD
uses: [1NR3HAWG9D, MEC3ZMC4F1, JR6XPJ7X56]
methods: [0NTF6DMVAP, 0J0XBKG64S]
sources:
  - book: isbn:9780387987606
    locator: Chapter 2
  - url: https://en.wikipedia.org/wiki/Elementary_class
    locator: A basic elementary class
---

## Proof

We use the [[compactness theorem|1NR3HAWG9D]] in the form: if $\Sigma \models \sigma$, then some finite $\Sigma_0 \subseteq \Sigma$ has $\Sigma_0 \models \sigma$.

1. *Part 2.* Let $F$ be finite with $\operatorname{Mod}(F) = \operatorname{Mod}(T)$, and let $\sigma = \bigwedge F$, with $\sigma = \forall x \, (x = x)$ if $F$ is empty.
2. Every model of $T$ is a model of $\sigma$, so $T \models \sigma$. By compactness, some finite $T_0 \subseteq T$ has $T_0 \models \sigma$.
3. Then $\operatorname{Mod}(T) \subseteq \operatorname{Mod}(T_0) \subseteq \operatorname{Mod}(\sigma) = \operatorname{Mod}(T)$, since $T_0 \subseteq T$. So $\operatorname{Mod}(T_0) = \operatorname{Mod}(T)$.
4. *Part 1, forward.* If $K = \operatorname{Mod}(\sigma)$, then the complement of $K$ is $\operatorname{Mod}(\neg\sigma)$, and both are elementary.
5. *Part 1, backward.* Let $K = \operatorname{Mod}(T)$ and let the complement of $K$ be $\operatorname{Mod}(U)$. No structure lies in both, so $T \cup U$ has no model.
6. By compactness, $T_0 \cup U_0$ has no model for some finite $T_0 \subseteq T$ and $U_0 \subseteq U$. Let $\sigma = \bigwedge T_0$, as in step 1.
7. $K = \operatorname{Mod}(T) \subseteq \operatorname{Mod}(\sigma)$, since $T_0 \subseteq T$.
8. Let $\mathcal{M} \models \sigma$, and suppose $\mathcal{M} \notin K$. Then $\mathcal{M} \models U$, so $\mathcal{M} \models T_0 \cup U_0$, a contradiction. So $\operatorname{Mod}(\sigma) \subseteq K$, and $K = \operatorname{Mod}(\sigma)$.

## Idea

Compactness says that every contradiction and every consequence of an infinite set of sentences already comes from a finite part.
A finite axiomatization is one consequence; a class together with its complement is one contradiction.

## Variants

Part 2 also follows from part 1 applied to an arbitrary axiomatization, together with the observation that the finite $T_0$ in step 6 is a subset of $T$.
With the completeness theorem, compactness is the statement that a proof uses only finitely many axioms, and step 2 becomes: a proof of $\sigma$ from $T$ uses only finitely many axioms of $T$.
