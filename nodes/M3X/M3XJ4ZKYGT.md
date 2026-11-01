---
tag: M3XJ4ZKYGT
kind: definition
name: Place (number field)
msc: [11R04, 12J10]
defines: BT5V3TSNY6
uses: [MWBDFS2KJ5, WGN82TCEF2, 00MHHZ9SNE, M54ADM0CVF, GCQ23XT6VD]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_number_theory
---

## Definition

Let $K$ be a field.
An *absolute value* on $K$ is a map $\abs{\cdot} \colon K \to \R_{\ge 0}$ such that for all $x, y \in K$:

1. $\abs{x} = 0$ if and only if $x = 0$;
2. $\abs{xy} = \abs{x}\abs{y}$;
3. $\abs{x + y} \le \abs{x} + \abs{y}$.

It is *trivial* if $\abs{x} = 1$ for all $x \ne 0$.
Two absolute values $\abs{\cdot}_1$ and $\abs{\cdot}_2$ are *equivalent* if there is a real $c > 0$ with $\abs{x}_2 = \abs{x}_1^{c}$ for all $x \in K$.
A *place* of an [[algebraic number field|MWBDFS2KJ5]] $K$ is an equivalence class of nontrivial absolute values on $K$.

## Remarks

Equivalent absolute values define the same topology on $K$.
A place is *infinite* (archimedean) if the values $\abs{n \cdot 1}$ for $n \in \N$ are unbounded, and *finite* (non-archimedean) otherwise.

Let $K$ be a number field with $r_1$ real embeddings and $r_2$ pairs of complex embeddings.
Each embedding $\sigma \colon K \to \C$ gives the absolute value $\abs{x}_\sigma = \abs{\sigma(x)}$, and conjugate embeddings give the same one.
These give the $r_1 + r_2$ infinite places.
Each nonzero [[prime ideal|00MHHZ9SNE]] $\mathfrak{p}$ of $\mathcal{O}_K$ gives $\abs{x}_{\mathfrak{p}} = N(\mathfrak{p})^{-v_{\mathfrak{p}}(x)}$ for $x \ne 0$.
Here $v_{\mathfrak{p}}(x)$ is the exponent of $\mathfrak{p}$ in the factorisation of $x\mathcal{O}_K$, and $N(\mathfrak{p})$ is the [[norm|M54ADM0CVF]].
These give all finite places.
Every place arises in one of these two ways.

Example: on $\Q$, the [[p-adic absolute value|WGN82TCEF2]] $\abs{x}_p = p^{-v_p(x)}$ satisfies the three clauses, even with $\abs{x + y}_p \le \max(\abs{x}_p, \abs{y}_p)$, and it is nontrivial since $\abs{p}_p = 1/p$; so it defines a place of $\Q$.
By [[Ostrowski's theorem|GCQ23XT6VD]], the places of $\Q$ are these and the place of the usual absolute value.

Non-example: on $\Q$, the map $x \mapsto \abs{x}^2$ fails clause 3, since $\abs{1 + 1}^2 = 4 > 1^2 + 1^2$.
So it is not an absolute value in this sense, although it is a power of one.
