---
tag: E2KHD79NF4
kind: proof
name: Proof of soundness of a Hilbert system for propositional logic
msc: ["03B05"]
topics: [H8QZY0RZXZ]
audience: ug2
proves: HZCFTQDRA5
uses: [05RSK4Q657, 0Y0MQYST0M, EDRV3N0SA3, 0ASJVEFA9J]
methods: [0ASJVEFA9J, 0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Soundness
    locator: lead section
  - book: isbn:9781482237726
  - book: isbn:9781447145578
---

## Proof

The plan: show by strong induction on the position in a derivation that every line is true under each valuation that makes the hypotheses true.

We use the notation of [[the statement|HZCFTQDRA5]].
The value $v(\varphi)$ of a formula under a valuation $v$ is defined by [[recursion on formulas|EDRV3N0SA3]].
We have $v(\lnot\varphi) = \mathsf{T}$ exactly when $v(\varphi) = \mathsf{F}$.
We have $v(\varphi \to \psi) = \mathsf{F}$ exactly when $v(\varphi) = \mathsf{T}$ and $v(\psi) = \mathsf{F}$.

1. Fix a set $\Gamma$, a derivation $\varphi_1, \ldots, \varphi_n$ from $\Gamma$, and a valuation $v$ with $v(\gamma) = \mathsf{T}$ for every $\gamma \in \Gamma$.
2. We prove by strong [[induction|0ASJVEFA9J]] on $i$ that $v(\varphi_i) = \mathsf{T}$ for $i = 1, \ldots, n$.
   Assume $v(\varphi_j) = \mathsf{T}$ for all $j < i$.
3. Case $\varphi_i \in \Gamma$.
   Then $v(\varphi_i) = \mathsf{T}$ by the choice of $v$ in step 1.
4. Case $\varphi_i$ is an instance $\varphi \to (\psi \to \varphi)$ of A1.
   Suppose its value is $\mathsf{F}$.
   Then $v(\varphi) = \mathsf{T}$ and $v(\psi \to \varphi) = \mathsf{F}$.
5. The second fact gives $v(\varphi) = \mathsf{F}$, which contradicts the first.
   So the value of the instance is $\mathsf{T}$.
6. Case $\varphi_i$ is an instance of A2.
   Suppose its value is $\mathsf{F}$.
   Then $v(\varphi \to (\psi \to \chi)) = \mathsf{T}$ and $v((\varphi \to \psi) \to (\varphi \to \chi)) = \mathsf{F}$.
7. The second fact gives $v(\varphi \to \psi) = \mathsf{T}$ and $v(\varphi \to \chi) = \mathsf{F}$, so $v(\varphi) = \mathsf{T}$ and $v(\chi) = \mathsf{F}$.
8. From $v(\varphi) = \mathsf{T}$ and $v(\varphi \to \psi) = \mathsf{T}$ we get $v(\psi) = \mathsf{T}$.
9. From $v(\varphi) = \mathsf{T}$ and $v(\varphi \to (\psi \to \chi)) = \mathsf{T}$ we get $v(\psi \to \chi) = \mathsf{T}$.
   With step 8 this gives $v(\chi) = \mathsf{T}$.
10. Step 9 contradicts $v(\chi) = \mathsf{F}$ from step 7.
    So the value of the instance of A2 is $\mathsf{T}$.
11. Case $\varphi_i$ is an instance $(\lnot\varphi \to \lnot\psi) \to (\psi \to \varphi)$ of A3.
    Suppose its value is $\mathsf{F}$.
    Then $v(\lnot\varphi \to \lnot\psi) = \mathsf{T}$, $v(\psi) = \mathsf{T}$ and $v(\varphi) = \mathsf{F}$.
12. From $v(\varphi) = \mathsf{F}$ we get $v(\lnot\varphi) = \mathsf{T}$, and then $v(\lnot\psi) = \mathsf{T}$ by the first fact of step 11.
13. So $v(\psi) = \mathsf{F}$, which contradicts $v(\psi) = \mathsf{T}$.
    So the value of the instance of A3 is $\mathsf{T}$.
14. Case $\varphi_i$ follows by [[modus ponens|0Y0MQYST0M]] from $\varphi_j$ and $\varphi_k = (\varphi_j \to \varphi_i)$ with $j, k < i$.
    By the induction hypothesis, $v(\varphi_j) = \mathsf{T}$ and $v(\varphi_j \to \varphi_i) = \mathsf{T}$.
15. If $v(\varphi_i)$ were $\mathsf{F}$, the truth table of $\to$ would give $v(\varphi_j \to \varphi_i) = \mathsf{F}$.
    So $v(\varphi_i) = \mathsf{T}$.
16. Steps 3 to 15 cover every way in which $\varphi_i$ can enter a derivation.
    So $v(\varphi_i) = \mathsf{T}$ for all $i$, and in particular $v(\varphi_n) = \mathsf{T}$.
17. Now let $\Gamma \vdash_{\mathsf{H}} \varphi$, and take a derivation from $\Gamma$ with $\varphi_n = \varphi$.
    By step 16, every valuation that makes $\Gamma$ true makes $\varphi$ true.
18. So $\Gamma \models \varphi$, which is the statement.
    With $\Gamma = \varnothing$, every theorem of $\mathsf{H}$ is true under every valuation, that is, a tautology.

## Idea

Every line of a derivation is true under each valuation that makes the hypotheses true.
The axioms are tautologies, which steps 4 to 13 check by contradiction instead of by a full truth table.
Modus ponens keeps truth, so the property passes from earlier lines to later lines.

## Variants

The axioms can also be checked by truth tables.
A1 and A3 have 4 rows each, A2 has 8 rows, and every row gives $\mathsf{T}$.

One can first prove weak soundness, "every theorem is a tautology", and then derive strong soundness with the [[deduction theorem|9X08XK5RV2]].
A derivation of $\varphi$ from $\gamma_1, \ldots, \gamma_m$ gives the theorem $\gamma_1 \to (\cdots \to (\gamma_m \to \varphi))$.
This theorem is a tautology, so every valuation that makes all $\gamma_i$ true makes $\varphi$ true.

For derivations written as trees, the induction runs on the height of the tree instead of the position in a list.
