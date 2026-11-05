---
tag: JBCKKP7866
kind: statement
role: theorem
name: Roth's theorem in finite fields
sources:
  - wikipedia: en:62455443@r1365048018
    locator: Roth's theorem on arithmetic progressions, section Extensions and generalizations > Roth's theorem in finite fields
    note: adopted
    mention: wikipedia://en/62455443#6VPY
    sections: [Statement]
inventory: [S98CT8VATN]
---

## Statement

As a variation, we can consider the analogous problem over [[finite fields|0ZXZ82FTX2]]. Consider the finite field $\mathbb{F}_3^n$, and let $r_3(\mathbb{F}_3^n)$ be the size of the largest subset of $\mathbb{F}_3^n$ which contains no 3-term arithmetic progression. This problem is actually equivalent to the [[cap set|B7SKJ1GP5P]] problem, which asks for the largest subset of $\mathbb{F}_3^n$ such that no 3 points lie on a line. The cap set problem can be seen as a generalization of the card game Set.

In 1982, Brown and Buhler were the first to show that $r_3(\mathbb{F}_3^n) = o(3^n).$ In 1995, Roy Mesuhlam used a similar technique to the Fourier-analytic proof of Roth's theorem to show that $r_3(\mathbb{F}_3^n) = O\left(\frac{3^n}{n}\right).$ This bound was improved to $O(3^n/n^{1 + \epsilon})$ in 2012 by Bateman and Katz.

In 2016, Ernie Croot, Vsevolod Lev, Péter Pál Pach, Jordan Ellenberg and Dion Gijswijt developed a new technique based on the polynomial method to prove that $r_3(\mathbb{F}_3^n) = O(2.756^n)$.

The best known lower bound is $2.2202^{n}$, discovered in December 2023 by Google DeepMind researchers using a large language model (LLM).
