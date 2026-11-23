---
tag: MAQEYCNFST
kind: proof
name: Proof of propositional compactness by Tychonoff's theorem
msc: ["03B05", "54D30"]
topics: [JDK63589SA]
audience: ug2
proves: 4X9126SEMM
uses: [0JTRSJKCFB, 0GBG8B49AA, 0QPHW703PV, DQ4E55T3BW, 00BWV5CKCF, H31CS3HK5P, QN7M1JCGT9]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Compactness_theorem
    locator: Proofs
  - url: https://en.wikipedia.org/wiki/Boolean_prime_ideal_theorem
    locator: Applications
---

## Proof

We view the truth assignments as the points of a compact space, show that the models of each formula form a closed set, and find a common point.
Let $P$ be any set of variables, and let $\Sigma$ be a finitely satisfiable set of formulas.
Give $\{ 0, 1 \}$ the discrete topology, and let $X = \{ 0, 1 \}^P$ have the [[product topology|0GBG8B49AA]].
A point of $X$ is a map $v : P \to \{ 0, 1 \}$, that is, a [[truth assignment|H31CS3HK5P]].

1. The space $\{ 0, 1 \}$ is finite, so it is compact.
   By [[Tychonoff's theorem|0JTRSJKCFB]], $X$ is [[compact|0QPHW703PV]].
2. For a formula $\varphi$, put $M(\varphi) = \{ v \in X : v(\varphi) = 1 \}$, the set of models of $\varphi$.
3. Let $q_1, \dots, q_k$ be the variables of $\varphi$.
   For $s \in \{ 0, 1 \}^k$ put $U_s = \{ v \in X : v(q_i) = s_i \text{ for } i = 1, \dots, k \}$.
4. Each $U_s$ is open.
   It is the intersection of the $k$ sets $\pi_{q_i}^{-1}(\{ s_i \})$, where $\pi_q(v) = v(q)$ is a projection, and each $\{ s_i \}$ is open in the discrete space.
5. The value $v(\varphi)$ depends only on $v(q_1), \dots, v(q_k)$, by the coincidence property of the valuation.
   So $M(\varphi)$ is the union of the sets $U_s$ over those $s$ that make $\varphi$ true.
6. This is a finite union of open sets, so $M(\varphi)$ is open.
7. The complement of $M(\varphi)$ in $X$ is $M(\neg \varphi)$, because $v(\neg \varphi) = 1 - v(\varphi)$.
   Step 6 for $\neg \varphi$ shows that this complement is open.
   So $M(\varphi)$ is closed, and it is a [[clopen set|DQ4E55T3BW]].
8. For a finite set $\{ \varphi_1, \dots, \varphi_n \} \subseteq \Sigma$, a model is a point of $M(\varphi_1) \cap \cdots \cap M(\varphi_n)$.
   Finite satisfiability says that this intersection is never empty.
9. So the closed sets $M(\varphi)$, $\varphi \in \Sigma$, have the [[finite intersection property|00BWV5CKCF]].
10. In a compact space, a family of closed sets with the finite intersection property has a nonempty intersection.
    Choose $v$ in $\bigcap_{\varphi \in \Sigma} M(\varphi)$; if $\Sigma$ is empty, every point of the nonempty space $X$ works.
11. Then $v(\varphi) = 1$ for every $\varphi \in \Sigma$, so $\Sigma$ is [[satisfiable|QN7M1JCGT9]].

## Idea

Truth assignments are the points of a product of two-point spaces, which is compact by Tychonoff's theorem.
Each formula depends on finitely many coordinates, so its set of models is clopen.
Finite satisfiability is then the finite intersection property, and compactness gives a common point, which is a model.

## Variants

Tychonoff's theorem for arbitrary products is equivalent to the axiom of choice.
This proof only needs it for products of compact Hausdorff spaces, and that case is equivalent to the Boolean prime ideal theorem.
For a countably infinite $P$, the space $X$ is the Cantor space, whose compactness needs no choice, and the [[direct proof|71200Z9Z4N]] is the same argument without topology.

An ultrafilter gives the model directly.
Let $I$ be the set of finite subsets of $\Sigma$, and choose a model $v_F$ of each $F \in I$.
Take an ultrafilter $U$ on $I$ that contains every set $\{ F \in I : \varphi \in F \}$; these sets have the finite intersection property.
Put $v(p) = 1$ when $\{ F : v_F(p) = 1 \} \in U$.
Induction on formulas shows that $v(\varphi) = 1$ exactly when $\{ F : v_F(\varphi) = 1 \} \in U$, so $v$ is a model of $\Sigma$.

Compactness also follows from the strong [[completeness theorem|81ZNY1XKYJ]] and the [[soundness theorem|XD629S54CS]].
If $\Sigma$ has no model, then $\Sigma \models \neg (p_0 \to p_0)$, so $\Sigma \vdash \neg (p_0 \to p_0)$.
A derivation uses a finite $\Sigma_0 \subseteq \Sigma$, and soundness gives $\Sigma_0 \models \neg (p_0 \to p_0)$, so $\Sigma_0$ has no model.
