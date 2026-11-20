---
tag: K7Z88ZYSZ7
kind: proof
name: Proof of the Łoś-Vaught test by the Löwenheim-Skolem theorem
msc: ["03C35"]
topics: [6XEXRME4C1]
audience: grad
proves: ZR7Y5C235P
uses: [484M0TZ1S7, 1JJCGNX240, 655K8Y7VS8]
methods: [0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Łoś–Vaught_test
    locator: Statement
  - book: isbn:9780387987606
---

## Proof

Let $T$, $L$ and $\kappa$ be as in the [[statement|ZR7Y5C235P]]: $T$ is satisfiable, has no finite models, is $\kappa$-categorical, and $\kappa \ge \abs{L}$ is infinite.
We argue by contradiction.

1. Suppose that $T$ is not [[complete|655K8Y7VS8]]. Then there is an $L$-sentence $\varphi$ with $T \not\models \varphi$ and $T \not\models \neg\varphi$.
2. Since $T \not\models \neg\varphi$, some model of $T$ satisfies $\varphi$. So $T_1 = T \cup \set{\varphi}$ has a model $\mathcal{M}_1$.
3. Since $T \not\models \varphi$, some model of $T$ satisfies $\neg\varphi$. So $T_2 = T \cup \set{\neg\varphi}$ has a model $\mathcal{M}_2$.
4. $\mathcal{M}_1$ and $\mathcal{M}_2$ are models of $T$, and $T$ has no finite models (hypothesis 1), so both are infinite.
5. $T_1$ and $T_2$ are $L$-theories with infinite models, and $\kappa \ge \abs{L}$. The [[Löwenheim-Skolem theorem|484M0TZ1S7]] gives a model $\mathcal{N}_1$ of $T_1$ and a model $\mathcal{N}_2$ of $T_2$, both of cardinality $\kappa$.
6. $\mathcal{N}_1$ and $\mathcal{N}_2$ are models of $T$ of cardinality $\kappa$. By hypothesis 2 they are isomorphic.
7. Isomorphic structures satisfy the same sentences. Now $\mathcal{N}_1 \models \varphi$ and $\mathcal{N}_2 \models \neg\varphi$, which is a contradiction.
8. So the assumption of step 1 is false, and $T$ is complete.

Hypothesis 1 is used in step 4, hypothesis 2 in step 6, and the bound $\kappa \ge \abs{L}$ in step 5.

## Idea

An incomplete theory splits into two consistent extensions that disagree on one sentence.
Both extensions have infinite models, and the Löwenheim-Skolem theorem moves both to the one size $\kappa$.
There the two models must be isomorphic, and they cannot be, because they disagree on the sentence.

## Variants

Step 5 can use the compactness theorem and the downward Löwenheim-Skolem theorem separately: compactness adds $\kappa$ new constants that are pairwise distinct, and the downward theorem cuts the model to size $\kappa$.
The same argument proves the stronger form in which "isomorphic" is replaced by "elementarily equivalent" in hypothesis 2.
