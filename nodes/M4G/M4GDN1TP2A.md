---
tag: M4GDN1TP2A
kind: proof
name: Proof of the diagram lemmas
proves: EP5E317TNW
msc: ["03C07"]
topics: [2RE7GWWXM5]
audience: ug2
uses: [SCRB74SWQN, CGH8C8EA9N, C9494XYEMN, K7XDVK5854, MCZRXR3SVB, EY20BF96SJ]
methods: [0NTF6DMVAP, 0WCP0PVET6]
sources:
  - url: https://en.wikipedia.org/wiki/Diagram_(mathematical_logic)
    locator: Definition
  - book: isbn:9780387987606
    locator: Chapter 2
---

## Proof

Let $h \colon M \to N$, and let $(\mathcal{N}, h)$ interpret each constant $c_m$ as $h(m)$.
For an $L$-formula $\varphi(x_1, \dots, x_n)$ and $m_1, \dots, m_n \in M$, the [[definition of truth|K7XDVK5854]] gives $(\mathcal{N}, h) \models \varphi(c_{m_1}, \dots, c_{m_n})$ iff $\mathcal{N} \models \varphi(h(m_1), \dots, h(m_n))$.
We call this fact (*).
In the same way, $\mathcal{M}_M \models \varphi(c_{m_1}, \dots, c_{m_n})$ iff $\mathcal{M} \models \varphi(m_1, \dots, m_n)$.

Part 1, from embedding to diagram.

1. Assume $h$ is an [[embedding|SCRB74SWQN]]. Let $\theta$ be a sentence of $\mathrm{Diag}(\mathcal{M})$. Write $\theta = \varphi(c_{m_1}, \dots, c_{m_n})$ with $\varphi$ an atomic or negated atomic $L$-formula.
2. $\theta$ is true in $\mathcal{M}_M$, so $\mathcal{M} \models \varphi(\bar m)$.
3. [[Embeddings preserve quantifier-free formulas|C9494XYEMN]], so $\mathcal{N} \models \varphi(h(\bar m))$.
4. By (*), $(\mathcal{N}, h) \models \theta$.

Part 1, from diagram to embedding.

5. Assume $(\mathcal{N}, h) \models \mathrm{Diag}(\mathcal{M})$.
6. Injective: if $m \ne m'$, then $\neg(c_m = c_{m'})$ is in $\mathrm{Diag}(\mathcal{M})$. By (*), $h(m) \ne h(m')$.
7. Constants: for a constant symbol $d$ of $L$, let $m = d^{\mathcal{M}}$. The [[atomic sentence|MCZRXR3SVB]] $d = c_m$ is in the diagram, so $d^{\mathcal{N}} = h(m)$.
8. Functions: for an $n$-ary $f$ and $\bar m$ in $M$, let $m = f^{\mathcal{M}}(\bar m)$. The sentence $f(c_{m_1}, \dots, c_{m_n}) = c_m$ is in the diagram, so $f^{\mathcal{N}}(h(\bar m)) = h(m)$.
9. Relations: for an $n$-ary $R$ and $\bar m$ in $M$, we consider two cases. If $\mathcal{M} \models R(\bar m)$, then $R(c_{\bar m})$ is in the diagram, and $\mathcal{N} \models R(h(\bar m))$ by (*).
10. If $\mathcal{M} \models \neg R(\bar m)$, then $\neg R(c_{\bar m})$ is in the diagram, and $\mathcal{N} \models \neg R(h(\bar m))$ by (*).
11. By steps 6 to 10, $h$ satisfies every condition in the definition of an embedding.

Part 2.

12. Assume $h$ is an [[elementary embedding|CGH8C8EA9N]], and let $\varphi(c_{\bar m}) \in \mathrm{ElDiag}(\mathcal{M})$. Then $\mathcal{M} \models \varphi(\bar m)$, so $\mathcal{N} \models \varphi(h(\bar m))$ by elementarity, and $(\mathcal{N}, h) \models \varphi(c_{\bar m})$ by (*).
13. Conversely, assume $(\mathcal{N}, h) \models \mathrm{ElDiag}(\mathcal{M})$, and let $\varphi(\bar x)$ be an $L$-formula and $\bar m$ in $M$.
14. If $\mathcal{M} \models \varphi(\bar m)$, then $\varphi(c_{\bar m}) \in \mathrm{ElDiag}(\mathcal{M})$, so $\mathcal{N} \models \varphi(h(\bar m))$ by (*).
15. If $\mathcal{M} \not\models \varphi(\bar m)$, then $\neg\varphi(c_{\bar m}) \in \mathrm{ElDiag}(\mathcal{M})$, so $\mathcal{N} \not\models \varphi(h(\bar m))$ by (*).
16. So $\mathcal{M} \models \varphi(\bar m)$ iff $\mathcal{N} \models \varphi(h(\bar m))$. The diagram $\mathrm{Diag}(\mathcal{M})$ is contained in $\mathrm{ElDiag}(\mathcal{M})$, so $h$ is an embedding by part 1, and it is elementary.

## Idea

The constants $c_m$ name the elements of $\mathcal{M}$, and in $(\mathcal{N}, h)$ they name their images.
A sentence about the names is true in $(\mathcal{N}, h)$ exactly when the formula is true of the images in $\mathcal{N}$.
So the diagram lists the conditions that $h$ must preserve, and each condition of an embedding is one kind of sentence in it.
The negated sentences in the diagram give injectivity and the failure of relations.

## Variants

For the positive diagram, steps 7 to 9 alone show that $h$ is a homomorphism.
Some books state part 1 only for substructures: if $\mathcal{N}_M \models \mathrm{Diag}(\mathcal{M})$ and the constants are interpreted by the identity, then $\mathcal{M}$ is a substructure of $\mathcal{N}$.
The general form follows by renaming the elements of $N$ along $h$.
