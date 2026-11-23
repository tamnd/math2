---
tag: V36AHEN7ZE
kind: proof
name: Proof of Robinson's joint consistency theorem from Craig's interpolation theorem
msc: ["03C07", "03C40"]
topics: [FBWW4J1XWG]
audience: ug3
proves: R6AN38DNBD
uses: [E2CBFNAVZY, 1NR3HAWG9D, WQ1ZE255SF, AVD7T7J063, DKFGQTRYZE]
methods: [0J0XBKG64S, 0BB5TPGQ1N]
sources:
  - url: https://en.wikipedia.org/wiki/Robinson%27s_joint_consistency_theorem
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Craig_interpolation
    locator: lead section
---

## Proof

We assume that the union has no model, cut the conflict down to two finite pieces by compactness, and let Craig's theorem produce a separating sentence in the common language.

We prove part 1, and part 2 follows from part 1, as the statement shows.
Let $\Gamma$ in $L_1$ and $\Sigma$ in $L_2$ be such that no sentence of $L_0 = L_1 \cap L_2$ separates them.

1. Suppose, for a contradiction, that $\Gamma \cup \Sigma$ has no model.
2. By the [[compactness theorem|1NR3HAWG9D]], some finite $\Gamma_0 \subseteq \Gamma$ and $\Sigma_0 \subseteq \Sigma$ have no common model.
3. Let $\varphi$ be the conjunction of $\Gamma_0$, and let $\sigma$ be the conjunction of $\Sigma_0$.
   An empty conjunction is $\forall x \, (x = x)$.
4. Then $\varphi \land \sigma$ has no model, so $\varphi \models \neg \sigma$.
5. [[Craig's interpolation theorem|E2CBFNAVZY]] gives a sentence $\theta$ with $\varphi \models \theta$ and $\theta \models \neg \sigma$, whose non-logical symbols occur both in $\varphi$ and in $\sigma$.
6. The symbols of $\varphi$ lie in $L_1$, and those of $\sigma$ lie in $L_2$, so $\theta$ is a sentence of $L_0$.
7. Every model of $\Gamma$ satisfies $\varphi$, and $\varphi \models \theta$, so $\Gamma \models \theta$.
8. Every model of $\Sigma$ satisfies $\sigma$, and $\theta \models \neg \sigma$, so such a model fails $\theta$.
   Hence $\Sigma \models \neg \theta$.
9. By [[Gödel's completeness theorem|WQ1ZE255SF]], $\Gamma \vdash \theta$ and $\Sigma \vdash \neg \theta$.
   So $\theta$ separates $\Gamma$ from $\Sigma$, against the hypothesis.
10. Hence $\Gamma \cup \Sigma$ has a model, and it is consistent by the [[soundness theorem|AVD7T7J063]].

## Idea

If the two sets have no common model, then by compactness a finite part of each side already conflicts.
The conflict is an implication from a sentence of $L_1$ to the negation of a sentence of $L_2$.
Craig's theorem puts a sentence of the common language between them, and this sentence separates the two sides.
For example, let $\Gamma = \{ \forall x \, \forall y \, (x = y) \land P c \}$ and $\Sigma = \{ Q a \land \neg Q b \}$, which share no non-logical symbol.
The first set allows only one element, the second forces $a \ne b$, and the interpolant $\theta = \forall x \, \forall y \, (x = y)$ separates them.

## Variants

The argument also runs backwards: [[Craig's theorem follows from Robinson's theorem|JP8J5RJM6W]].
So the two theorems are equivalent, given compactness and completeness.

The [[joint Henkin construction|VNABTNK13X]] proves Robinson's theorem without interpolation.
