---
tag: 9FQ5VAKJCS
kind: definition
name: Gersten complex
msc: ["19E08", "19D45", "14C35"]
defines: W4BRV4PT2F
uses: [ND6XEY68P4, G51E8MW7J1, 5GVFZWMWC8, GG8AYV847V, WQ82C0M3QB]
sources:
  - url: https://en.wikipedia.org/wiki/Bloch%27s_formula
---

## Definition

Let $X$ be a [[Noetherian scheme|ND6XEY68P4]] of finite Krull dimension.
For $p \ge 0$ let $X^{(p)}$ be the set of points $x \in X$ of codimension $p$, that is, with $\dim \mathcal{O}_{X,x} = p$.
Let $k(x)$ be the [[residue field|G51E8MW7J1]] of $x$.
Let $K_m$ be Quillen's [[algebraic K-groups|5GVFZWMWC8]], with $K_m = 0$ for $m < 0$.
Let $G_m$ be the K-theory of coherent sheaves.
The filtration of coherent sheaves by codimension of support gives Quillen's coniveau [[spectral sequence|GG8AYV847V]]
$$E_1^{p,q} = \bigoplus_{x \in X^{(p)}} K_{-p-q}(k(x)) \Rightarrow G_{-p-q}(X).$$
For $n \ge 0$, the *Gersten complex* of $X$ in degree $n$ is the row $q = -n$ of its $E_1$ page.
It is the [[chain complex|WQ82C0M3QB]]
$$\bigoplus_{x \in X^{(0)}} K_n(k(x)) \xrightarrow{d_1} \bigoplus_{x \in X^{(1)}} K_{n-1}(k(x)) \xrightarrow{d_1} \cdots \xrightarrow{d_1} \bigoplus_{x \in X^{(n)}} K_0(k(x)).$$
The same construction applies to $\operatorname{Spec} R$ for a Noetherian local ring $R$.
Applied to each open subset of $X$, it gives a complex of sheaves on $X$.

## Remarks

Each differential $d_1$ is a sum of components $K_m(k(x)) \to K_{m-1}(k(y))$, which are $0$ unless $y$ lies in the closure of $x$ and has codimension one more.
Suppose $y$ has codimension one in the closure of $x$, and the local ring of that closure at $y$ is a discrete valuation ring.
Then the component $K_1(k(x)) = k(x)^\times \to K_0(k(y)) = \Z$ is the valuation, and $K_2 \to K_1$ is the tame symbol.

Example: for $X = \operatorname{Spec} \Z$ and $n = 1$ the complex is $\Q^\times \to \bigoplus_p \Z$, $r \mapsto (v_p(r))_p$.
Its kernel is $\{\pm 1\} = \Z^\times = K_1(\Z)$, and it is surjective.

The augmented complex $0 \to K_n(R) \to K_n(F) \to \cdots$ for a regular local ring $R$ with fraction field $F$ is the subject of the [[Gersten conjecture|N0ZTHA8YBB]].
