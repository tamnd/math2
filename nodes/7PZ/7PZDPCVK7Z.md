---
tag: 7PZDPCVK7Z
kind: statement
role: lemma
name: Strong diagonal lemma
sources:
  - wikipedia: en:348969@r1344931050
    locator: Diagonal lemma, section Some generalizations > Strong diagonal lemma
    note: adopted
    mention: wikipedia://en/348969#XKIH
    sections: [Statement]
inventory: [AY0B1SGR9X]
---

## Statement

Let $\psi (x)$ be any formula in the language of $T$ with only $x$ as free variable. Then there is a term $t$ in the language of $T$ such that $T \vdash t = \ulcorner \psi (t) \urcorner$.

Trivially, the diagonal lemma follows from the strong diagonal lemma (take $\varphi (x)$ to be $\psi (t)$). Note however that the strong diagonal lemma depends on the language of $T$, particularly on whether there is such a term $t$. Typically, the strong diagonal lemma fails for theories in the basic language of arithmetic (such as $\mathsf{Q}$ or $\mathsf{PA}$), but holds for primitive recursive arithmetic $\mathsf{PRA}$ which has a function symbol for each primitive recursive functions.
