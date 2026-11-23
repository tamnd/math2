---
tag: JP8J5RJM6W
kind: proof
name: Proof of Craig's interpolation theorem from Robinson's joint consistency theorem
msc: ["03C40", "03B10"]
topics: [FBWW4J1XWG]
audience: ug3
proves: E2CBFNAVZY
uses: [R6AN38DNBD, VNABTNK13X, WQ1ZE255SF, AVD7T7J063, DCR0S91GYY, DKFGQTRYZE]
methods: [0J0XBKG64S, 0BB5TPGQ1N]
sources:
  - url: https://en.wikipedia.org/wiki/Craig_interpolation
    locator: Proof of Craig's interpolation theorem
  - url: https://builds.openlogicproject.org/
    locator: Interpolation
---

## Proof

We assume that no interpolant exists, conclude that $\varphi$ and $\neg \psi$ cannot be separated in the common language, and let Robinson's theorem build a model of both, which contradicts $\varphi \models \psi$.

Let $L_1$ be the language of the non-logical symbols of $\varphi$, and let $L_2$ be that of $\psi$.
We put $L_0 = L_1 \cap L_2$ and assume $\varphi \models \psi$.
We use part 1 of [[Robinson's joint consistency theorem|R6AN38DNBD]], which is proved by a [[joint Henkin construction|VNABTNK13X]] without interpolation.

1. Suppose, for a contradiction, that no sentence $\theta$ of $L_0$ satisfies both $\varphi \models \theta$ and $\theta \models \psi$.
2. Let $\Gamma = \{ \varphi \}$, a set of sentences of $L_1$, and let $\Sigma = \{ \neg \psi \}$, a set of sentences of $L_2$.
3. Suppose that a sentence $\theta$ of $L_0$ separates $\Gamma$ from $\Sigma$, so that $\varphi \vdash \theta$ and $\neg \psi \vdash \neg \theta$.
4. By the [[soundness theorem|AVD7T7J063]], $\varphi \models \theta$ and $\neg \psi \models \neg \theta$.
5. The second fact gives $\theta \models \psi$.
   Indeed, a model of $\theta$ that failed $\psi$ would satisfy $\neg \psi$, and so it would satisfy $\neg \theta$.
6. So $\theta$ is an interpolant, which contradicts step 1.
   Hence no sentence of $L_0$ separates $\Gamma$ from $\Sigma$.
7. Robinson's theorem gives a model $\mathcal{A}$ of $\{ \varphi, \neg \psi \}$.
8. Then $\mathcal{A} \models \varphi$ and $\mathcal{A} \not\models \psi$, which contradicts $\varphi \models \psi$.
9. So some sentence $\theta$ of $L_0$ has $\varphi \models \theta$ and $\theta \models \psi$.
   Its non-logical symbols lie in $L_0$, so they occur in both $\varphi$ and $\psi$.

## Idea

If no sentence of the common language lies between $\varphi$ and $\psi$, then $\varphi$ and $\neg \psi$ cannot be told apart in the common language.
Robinson's theorem then joins a model of $\varphi$ and a model of $\neg \psi$ into one structure, and that structure contradicts $\varphi \models \psi$.
For $\varphi = \forall x \, (P x \to Q x) \land P a$ and $\psi = Q a \lor R a$, the sentence $Q a$ separates $\{ \varphi \}$ from $\{ \neg \psi \}$, so Robinson's theorem gives no joint model, and $Q a$ is the interpolant.

## Variants

The classical form of Robinson's theorem gives a second route.
Suppose that some $\mathcal{M} \models \neg \psi$ satisfies every $L_0$-consequence of $\varphi$, and put $T = \mathrm{Th}_{L_0}(\mathcal{M})$, a complete $L_0$-theory.
Compactness shows that $T \cup \{ \varphi \}$ is consistent, since otherwise the negation of a finite conjunction of members of $T$ would be an $L_0$-consequence of $\varphi$ that fails in $\mathcal{M}$.
Part 2 then gives a model of $\varphi \land \neg \psi$, which is impossible.
So every model of the $L_0$-consequences of $\varphi$ satisfies $\psi$, and compactness turns finitely many of these consequences into one conjunction $\theta$.

The [[proof-theoretic proof|KJ7PEGF7YN]] by the cut-free sequent calculus constructs $\theta$ from a derivation, which this proof does not.
