---
tag: 7MFGBVDVG9
kind: statement
role: theorem
name: Omitting types theorem
msc: [03C07, 03C15]
uses: [9V71Q3SD1G, 92SWXST1ZM, MVCH6N9SNW, 01TQB88H4C]
about: [9V71Q3SD1G]
sources:
  - url: https://en.wikipedia.org/wiki/Type_(model_theory)
---

## Statement

Let $L$ be a countable signature, let $T$ be a satisfiable $L$-[[theory|92SWXST1ZM]], and let $p(x_1, \dots, x_n)$ be an $n$-[[type|9V71Q3SD1G]] of $T$.
Call $p$ isolated if there is an $L$-formula $\varphi(x_1, \dots, x_n)$ such that $T \cup \set{\varphi}$ is satisfiable and $T \models \forall \bar{x} \, (\varphi(\bar{x}) \to \psi(\bar{x}))$ for every $\psi \in p$.
If $p$ is not isolated, then $T$ has a [[countable|01TQB88H4C]] [[model|MVCH6N9SNW]] that omits $p$.

## Remarks

The proof is a Henkin construction.
One adds countably many new constants, lists all tuples of constants, and builds a complete theory with witnesses step by step.
At the step for a tuple $\bar{c}$, one adds the negation of some formula of $p$ at $\bar{c}$.
This is possible because no formula consistent with what has been built so far implies all of $p$.
The canonical model of the final theory is countable and no tuple in it realizes $p$.
The same argument omits countably many non-isolated types at once.

Example: let $T$ be the theory of $(\N, 0, 1, +, \cdot, <)$ and $p(x) = \set{x \ne 0, x \ne 1, x \ne 1 + 1, \dots}$.
The type $p$ is not isolated, and $\N$ is a countable model of $T$ that omits it.

If $T$ is complete, an isolated type is realized in every model of $T$, so the hypothesis cannot be dropped.
Countability of $L$ is also needed.
Take constants $c_\alpha$ for $\alpha < \omega_1$ and $d_k$ for $k \in \N$, let $T$ say that the $c_\alpha$ are pairwise distinct, and let $p(x) = \set{x \ne d_k : k \in \N}$.
Then $p$ is not isolated, but every model of $T$ is uncountable and so has an element different from all $d_k$.

## Explanations

### L1 human

A type is a wish list of properties for an element.
Some wish lists are forced: a single property, consistent with the theory, already implies the whole list.
For a complete theory, every model then has an element that meets the whole list.
The theorem says that, in a countable language, every list that is not forced in this way can be avoided by some countable model.

### L2 human

The omitting types theorem is the main tool for building countable models with prescribed properties.
It shows that a complete theory in a countable language has an atomic model, that is, a prime model, when the isolated types are dense.
It is used in the proof of the Ryll-Nardzewski theorem and in the study of the number of countable models, the subject of the Vaught conjecture.
It is a counterpart of the compactness theorem: compactness produces models that realize types, and this theorem produces models that omit them.
