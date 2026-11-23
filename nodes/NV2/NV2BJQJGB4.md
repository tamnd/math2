---
tag: NV2BJQJGB4
kind: proof
name: Proof of Craig interpolation for propositional logic
msc: ["03B05"]
topics: [JDK63589SA]
audience: ug2
proves: TRS2HY57EG
uses: [TT7WT5HPN9, H31CS3HK5P, 1HK0VYWTV7]
methods: [12MQ2NJ29A, 0NTF6DMVAP, 01XM7JEKHY]
sources:
  - url: https://en.wikipedia.org/wiki/Craig_interpolation
    locator: Proof of Craig's interpolation theorem
---

## Proof

We remove the variables that only $\varphi$ mentions by trying both constants for each, and check the three properties for the disjunction of the results.
For an assignment $v$, a variable $q$ and $b \in \{ 0, 1 \}$, let $v[q \mapsto b]$ agree with $v$ except that it sends $q$ to $b$.
For $b = 1$ let $c_b = \top$, and for $b = 0$ let $c_b = \bot$.
We write $v(\chi)$ for the [[truth valuation|H31CS3HK5P]] of $v$ at a formula $\chi$.

1. Coincidence: if $v$ and $w$ agree on $\operatorname{var}(\chi)$, then $v(\chi) = w(\chi)$.
   This holds by [[structural induction|12MQ2NJ29A]] on $\chi$, since the value of a compound formula depends only on the values of its parts.
2. Substitution: for every formula $\chi$, $v(\chi[c_b/q]) = v[q \mapsto b](\chi)$.
   This holds by structural induction on $\chi$.
3. In step 2 the base cases are these: $\chi = q$ gives $v(c_b) = b$ on both sides, and a variable $p \ne q$ or a constant is unchanged on both sides.
   The compound cases follow from the values of the parts.
4. Now let $\varphi \models \psi$.
   Let $q_1, \dots, q_k$ be the variables of $\varphi$ that do not occur in $\psi$.
5. For $\vec b = (b_1, \dots, b_k) \in \{ 0, 1 \}^k$ let $\varphi_{\vec b}$ be $\varphi$ with each $q_i$ replaced by $c_{b_i}$.
   Let $\theta$ be the disjunction of the $2^k$ formulas $\varphi_{\vec b}$.
6. Property 3: the variables of $\varphi_{\vec b}$ are those of $\varphi$ other than $q_1, \dots, q_k$.
   These occur in $\varphi$ and in $\psi$, so $\operatorname{var}(\theta) \subseteq \operatorname{var}(\varphi) \cap \operatorname{var}(\psi)$.
7. Property 1: let $v(\varphi) = 1$, and put $b_i = v(q_i)$ for each $i$.
   Then $v[q_1 \mapsto b_1, \dots, q_k \mapsto b_k] = v$.
8. By step 2, used $k$ times, $v(\varphi_{\vec b}) = v(\varphi) = 1$.
   So the disjunct $\varphi_{\vec b}$ of $\theta$ is true, and $v(\theta) = 1$.
9. Property 2: let $v(\theta) = 1$.
   Then some disjunct $\varphi_{\vec b}$ is true under $v$, by the truth table of [[disjunction|0F72FK8EKB]].
10. Let $w = v[q_1 \mapsto b_1, \dots, q_k \mapsto b_k]$.
    By step 2, used $k$ times, $w(\varphi) = v(\varphi_{\vec b}) = 1$.
11. Since $\varphi \models \psi$, we get $w(\psi) = 1$, by the definition of [[logical consequence|1HK0VYWTV7]].
12. The assignments $v$ and $w$ differ only at $q_1, \dots, q_k$, which do not occur in $\psi$.
    By step 1, $v(\psi) = w(\psi) = 1$.
13. So $\varphi \models \theta$ by steps 7 and 8, $\theta \models \psi$ by steps 9 to 12, and $\theta$ has property 3 by step 6.
    Hence $\theta$ is an interpolant of $\varphi$ and $\psi$.

## Idea

The variables that only $\varphi$ mentions are the obstacle, so we remove them by trying both truth values for each.
The disjunction of all such instances of $\varphi$ is what $\varphi$ says about the shared variables.
It follows from $\varphi$, and it implies $\psi$ because $\psi$ does not depend on the removed variables.

## Variants

The same argument can remove one variable $q$ at a time, with $\varphi[\top/q] \lor \varphi[\bot/q]$ at each step.
This is an induction on the number of variables of $\varphi$ that do not occur in $\psi$.
Dually, one can remove the variables that only $\psi$ mentions, with $\psi_{\vec b}$ defined in the same way, and take $\theta = \bigwedge_{\vec b} \psi_{\vec b}$, the weakest interpolant.
A proof-theoretic route builds $\theta$ by induction on a cut-free derivation of $\varphi \Rightarrow \psi$ in the [[sequent calculus|W72CA3R9MP]].
This route extends to first-order logic, where the substitution of constants above does not apply.
Another route reads an interpolant off a [[resolution|ZDW6N1PGJ7]] refutation of $\varphi$ and $\neg \psi$ in clause form.
