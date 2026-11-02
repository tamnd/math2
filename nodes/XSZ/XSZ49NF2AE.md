---
tag: XSZ49NF2AE
kind: conjecture
name: Manin conjecture
msc: [14G05, 11G50, 14J45]
uses: [FMHA649HJ9, MWBDFS2KJ5, F1FF505PWH, W05VYY4HBR, 3Z9DCWYXQZ, 8SQK7RTB63, SWJYG87QQH]
about: [SWJYG87QQH, FMHA649HJ9]
sources:
  - url: https://en.wikipedia.org/wiki/Manin_conjecture
same_as:
  wikidata: Q17080204
  wikipedia: Manin conjecture
history:
  posed_by: "Yuri Manin, with Jens Franke and Yuri Tschinkel"
  first_stated: "1989"
---

## Statement

Let $K$ be an [[algebraic number field|MWBDFS2KJ5]] and let $V$ be a smooth [[Fano variety|FMHA649HJ9]] over $K$.
Assume that $V(K)$ is dense in $V$ for the [[Zariski topology|8SQK7RTB63]].
Let $H$ be a [[height|F1FF505PWH]] on $V(K)$ relative to the anticanonical divisor $-K_V$, and let $\rho$ be the rank of the [[Picard group|3Z9DCWYXQZ]] of $V$.
Then there are a nonempty Zariski open subset $U \subseteq V$ and a constant $c > 0$ such that the number
$$N_U(B) = \#\set{P \in U(K) : H(P) \le B}$$
satisfies
$$N_U(B) \sim c \, B (\log B)^{\rho - 1} \quad \text{as } B \to \infty.$$

## Remarks

Franke, Manin and Tschinkel stated it in 1989, and Batyrev and Manin extended it to other heights; Peyre later gave a conjectural formula for the constant $c$.
The open set $U$ is needed, since a subvariety such as a line on a cubic surface can contain more points of bounded height than the rest of the variety.
For $V = \mathbb{P}^n$ over $\Q$ one has $\rho = 1$, and the anticanonical height is $H_0^{n+1}$ with $H_0$ the usual height.
So the prediction $N(B) \sim cB$ follows from Schanuel's count of points of bounded height.
The conjecture is proved for flag varieties, toric varieties and several other families, and is open in general.
Batyrev and Tschinkel found examples in which removing a Zariski closed set is not enough, and current formulations remove a thin set instead.

## Explanations

### L1 human

A Fano variety, such as projective space or a smooth cubic surface, usually has infinitely many rational points.
The Manin conjecture predicts how many of them have height at most $B$: roughly a constant times $B$ times a power of $\log B$.
The power of the logarithm is fixed by the geometry, namely by the number of independent divisor classes.
It turns a counting problem in number theory into a statement about the geometry of the variety.
