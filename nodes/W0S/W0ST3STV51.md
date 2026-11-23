---
tag: W0ST3STV51
kind: example
name: The Tarski-Mostowski-Robinson theory R
msc: ["03F30", "03B25"]
topics: [QHCRN4JVG0]
audience: research
instance_of: [Q5MT8WY7JM]
uses: [3K1AKGXF8A, TT8MXRTVBM, Y8X8D9YJF8, MVCH6N9SNW]
sources:
  - url: https://en.wikipedia.org/wiki/Robinson_arithmetic
  - book: isbn:9780521857840
---

## Example

The theory $\mathsf{R}$ knows the addition and multiplication tables and how each element compares with each numeral, and nothing more.
Let $L_{\le}$ be the signature $\{ 0, S, +, \cdot, \le \}$, and write $\overline{n}$ for the numerals.
The theory $\mathsf{R}$ has the following axioms, one for each $n, m \in \mathbb{N}$:

- $\Omega_1$: $\overline{n} + \overline{m} = \overline{n + m}$;
- $\Omega_2$: $\overline{n} \cdot \overline{m} = \overline{n m}$;
- $\Omega_3$: $\overline{n} \ne \overline{m}$, when $n \ne m$;
- $\Omega_4$: $\forall x\,\bigl(x \le \overline{n} \to (x = \overline{0} \lor x = \overline{1} \lor \cdots \lor x = \overline{n})\bigr)$;
- $\Omega_5$: $\forall x\,(x \le \overline{n} \lor \overline{n} \le x)$.

Tarski, Mostowski and Robinson proved that $\mathsf{R}$ is essentially undecidable, so it is one of the [[weak theories of arithmetic|Q5MT8WY7JM]].
We check two facts that place it: [[Robinson arithmetic|3K1AKGXF8A]] proves every axiom of $\mathsf{R}$, and $\mathsf{R}$ is not finitely axiomatizable.

### Robinson arithmetic proves every axiom of R

In $\mathsf{Q}$ we read $x \le y$ as $x < y \lor x = y$.

1. $\Omega_1$ follows in $\mathsf{Q}$ by induction on $m$ in the metatheory.
   For $m = 0$, the sentence $\overline{n} + 0 = \overline{n}$ is an instance of $\mathsf{Q}4$.
   For $m + 1$, $\mathsf{Q}5$ gives $\overline{n} + S\,\overline{m} = S(\overline{n} + \overline{m})$, and the induction hypothesis turns this into $S\,\overline{n + m}$.
2. $\Omega_2$ follows in the same way from $\mathsf{Q}6$, $\mathsf{Q}7$ and $\Omega_1$.
   The step reads $\overline{n} \cdot S\,\overline{m} = \overline{n} \cdot \overline{m} + \overline{n} = \overline{n m} + \overline{n} = \overline{n m + n}$.
3. $\Omega_3$ and $\Omega_4$ are lemmas in the [[proof of Σ1-completeness|Y8X8D9YJF8]]: $\overline{n} \ne \overline{m}$, and the description of $x < \overline{n}$ as a finite disjunction.
4. $\Omega_5$ follows from trichotomy with numerals, $\mathsf{Q} \vdash \forall x\,(x < \overline{n} \lor x = \overline{n} \lor \overline{n} < x)$, which is proved in steps 8 to 10 of the [[proof of representability|4T3MSP1SPK]].
5. So $\mathsf{Q} \vdash \mathsf{R}$ under this reading of $\le$.

### R is not finitely axiomatizable

Now let $A$ be a finite set of axioms of $\mathsf{R}$.

6. Choose $k$ larger than every number whose numeral occurs in $A$, including the results $n + m$ and $n m$ of the axioms $\Omega_1$ and $\Omega_2$ in $A$.
7. Let $\mathfrak{F}_k$ have domain $\{ 0, 1, \ldots, k \}$, with the usual order $\le$ and with operations capped at $k$.
   That is, $S(x) = \min(x + 1, k)$, $x + y = \min(x + y, k)$ and $x \cdot y = \min(x y, k)$.
8. For $i \le k$, the numeral $\overline{i}$ has the value $i$ in $\mathfrak{F}_k$, by induction on $i$.
9. Each axiom in $A$ mentions only numerals below $k$, so its sums and products are below $k$ and are computed without capping.
   So $\mathfrak{F}_k \models A$.
10. Every model of $\mathsf{R}$ is infinite, since $\Omega_3$ makes the values of $\overline{0}, \overline{1}, \overline{2}, \ldots$ distinct.
11. If $A$ axiomatized $\mathsf{R}$, then the finite structure $\mathfrak{F}_k$ would be a model of $\mathsf{R}$, against step 10.
    So no finite set of axioms is equivalent to $\mathsf{R}$.

## Remarks

The example shows that essential undecidability needs no general law such as commutativity or the recursion equations for $+$ and $\cdot$.
The axioms $\Omega_4$ and $\Omega_5$ are universal sentences, but each of them compares an arbitrary element with one fixed numeral.
The other axioms are numerical facts.
Step 9 works for $\Omega_4$ and $\Omega_5$ because $\le$ is a linear order on $\{ 0, \ldots, k \}$ and the elements up to $i$ are exactly $0, \ldots, i$.

$\mathsf{R}$ still proves every true $\Sigma_1$ sentence of $L_{\le}$ whose bounded quantifiers use $\le$.
Tarski, Mostowski and Robinson showed that every recursive function is representable in $\mathsf{R}$, as [[for Q|BJF29XET83]], and deduced that $\mathsf{R}$ is essentially undecidable.
Since $\mathsf{Q}$ has no finite model, steps 6 to 9 also show that $\mathsf{Q}$ is not interpretable in $\mathsf{R}$.

## Explanations

### L1 human

The theory $\mathsf{R}$ lists true facts about particular numbers, such as $2 + 3 = 5$, $2 \cdot 3 = 6$ and $2 \ne 3$.
It also says, for each $n$, that the only numbers up to $n$ are $0, 1, \ldots, n$, and that every number is either up to $n$ or at least $n$.
It never says anything like "for all $x$ and $y$, $x + y = y + x$".
Even so, no computer program can decide which sentences follow from these facts.

### L2 human

We check the axiom $\Omega_1$ with $n = 2$ and $m = 3$ in the finite structure $\mathfrak{F}_6$.

1. The numerals $\overline{2}$, $\overline{3}$ and $\overline{5}$ have the values $2$, $3$ and $5$, since all are below $6$.
2. In $\mathfrak{F}_6$, $2 + 3 = \min(5, 6) = 5$.
3. So $\mathfrak{F}_6 \models \overline{2} + \overline{3} = \overline{5}$.
4. The axiom $\overline{4} + \overline{4} = \overline{8}$ holds in $\mathfrak{F}_6$ only by accident: both sides have the value $\min(8, 6) = 6$.
5. The axiom $\overline{6} \ne \overline{8}$ of $\Omega_3$ fails, since both numerals have the value $6$.
   So $\mathfrak{F}_6$ is not a model of all of $\mathsf{R}$.

The typical use of $\mathsf{R}$ is as a very weak base theory: to show a theory undecidable, it suffices to interpret $\mathsf{R}$ in it.
A trap is to think that $\mathsf{R}$ proves $\forall x\,(x + 0 = x)$.
It does not.
Add to $\mathbb{N}$ one element $c$ above all numbers, and let $c + y = 0$ for every $y$.
All axioms of $\mathsf{R}$ still hold, but $c + 0 = 0 \ne c$.
