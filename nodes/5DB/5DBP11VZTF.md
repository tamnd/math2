---
tag: 5DBP11VZTF
kind: example
name: Ramsey's theorem for triples is equivalent to ACA0
msc: ["03B30", "03F35", "05D10"]
topics: [BY8AAFN7C5]
audience: research
not_instance_of:
  - target: E3X5B175ZR
    note: Ramsey's theorem for triples is equivalent over RCA0 to ACA0, one of the five main subsystems, so it is not an in-between principle of the zoo
uses: [E3X5B175ZR, XQENB067R3, NAASTN80QN, 00TQV3F5S4, 09NWETVTNY, 0HGVCWQGY3]
sources:
  - url: https://en.wikipedia.org/wiki/Ramsey%27s_theorem
    locator: Reverse mathematics
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Arithmetical comprehension ACA0
---

## Example

One more element in each colored set takes Ramsey's theorem from the middle of the zoo to the top of the arithmetical level.
Let $\mathrm{RT}^3_2$ be the statement: for every coloring $c$ of the three-element subsets of $\mathbb{N}$ with colors $0$ and $1$, there is an infinite set $H$ such that $c$ is constant on the three-element subsets of $H$.
We show that $\mathrm{RT}^3_2$ implies [[ACA0|NAASTN80QN]] over [[RCA0|XQENB067R3]].
We cite one lemma about $\mathsf{ACA}_0$: over $\mathsf{RCA}_0$, arithmetical comprehension follows from the statement that every [[one-to-one function|09NWETVTNY]] $f \colon \mathbb{N} \to \mathbb{N}$ has a range, a set $R$ with $n \in R \iff \exists i \, f(i) = n$.
We argue in $\mathsf{RCA}_0 + \mathrm{RT}^3_2$ and fix a one-to-one function $f$.

1. For $x < y < z$, put $c(\{x, y, z\}) = 1$ if some $i$ with $y \le i < z$ has $f(i) < x$, and $c(\{x, y, z\}) = 0$ otherwise.
   The quantifier on $i$ is bounded by $z$, so $c$ exists by $\Delta^0_1$ comprehension.
2. By $\mathrm{RT}^3_2$ there is an infinite set $H$ on whose triples $c$ is constant.
   Let $h_0 < h_1 < h_2 < \cdots$ list $H$ in increasing order.
3. Suppose that the constant color is $1$, and put $x = h_0$.
   For each $j = 1, \dots, x + 1$ the triple $\{x, h_j, h_{j+1}\}$ has color $1$, so some $i_j$ with $h_j \le i_j < h_{j+1}$ has $f(i_j) < x$.
4. The intervals $[h_j, h_{j+1})$ are disjoint, so the $x + 1$ numbers $i_j$ are distinct.
   Since $f$ is one-to-one, the $x + 1$ values $f(i_j)$ are distinct numbers in $\{0, \dots, x - 1\}$.
5. This contradicts the finite [[pigeonhole principle|0HGVCWQGY3]], which $\mathsf{RCA}_0$ proves.
   So the constant color is $0$.
6. Let $x < y$ be in $H$ and let $n < x$.
   We claim that $n$ is in the range of $f$ if and only if $f(i) = n$ for some $i < y$.
7. The direction from right to left holds by definition.
   For the other direction, suppose $f(i) = n$ with $i \ge y$, and choose $z \in H$ with $z > i$; then $c(\{x, y, z\}) = 1$, which contradicts step 5.
8. For each $n$, let $k(n)$ be the least $k$ with $h_k > n$, and define $R$ by: $n \in R$ if and only if $f(i) = n$ for some $i < h_{k(n) + 1}$.
   The definition uses only the function $k \mapsto h_k$, which exists in $\mathsf{RCA}_0$, and bounded quantifiers, so $R$ exists by $\Delta^0_1$ comprehension.
9. Step 6 with $x = h_{k(n)}$ and $y = h_{k(n) + 1}$ shows that $R$ is exactly the range of $f$.
   So every one-to-one function has a range, and the cited lemma gives $\mathsf{ACA}_0$.

Conversely, $\mathsf{ACA}_0$ proves $\mathrm{RT}^n_k$ for each fixed $n$ and $k$, by induction on $n$ in the metatheory.
So $\mathrm{RT}^3_2$ is equivalent to $\mathsf{ACA}_0$ over $\mathsf{RCA}_0$.

## Remarks

### What the example shows

$\mathrm{RT}^3_2$ is not a member of the [[reverse mathematics zoo|E3X5B175ZR]], because its strength is exactly one of the Big Five.
The coloring hides a search in the third coordinate: the triple $\{x, y, z\}$ asks whether a value below $x$ appears between positions $y$ and $z$.
The homogeneous set then turns the unbounded question "is $n$ ever a value?" into the bounded question "is $n$ a value before the next checkpoint?".

### What changes with pairs

For pairs, the coloring has only two coordinates, so it cannot hold the bound $x$, the start $y$ and the end $z$ at once.
That is the intuition behind Seetapun's theorem that $\mathrm{RT}^2_2$ does not imply $\mathsf{ACA}_0$; see [[Ramsey's theorem for pairs|ZT5KV6KJ3E]].
In the other direction, the statement $\forall n \, \mathrm{RT}^n_2$ for all exponents at once is stronger than $\mathsf{ACA}_0$.
It proves the Paris-Harrington principle, which [[Ramsey's theorem|00TQV3F5S4]] gives by compactness, and which $\mathsf{ACA}_0$ does not prove, since $\mathsf{ACA}_0$ is conservative over Peano arithmetic.

## Explanations

### L1 human

The range of a function is the set of all its values.
To decide whether a number is a value, you may have to search forever, and arithmetical comprehension is the axiom that allows such searches.
Ramsey's theorem for triples hands you an infinite list of checkpoints.
Between two checkpoints $x < y$, every value smaller than $x$ that the function ever takes has already appeared before position $y$.
So the endless search becomes a finite one, and the range can be computed from the checkpoints.

### L2 human

Take $f(i) = i + 1$, whose range is $\{1, 2, 3, \dots\}$.
For $x < y < z$, some $i \ge y$ with $i + 1 < x$ would need $y + 1 < x$, which fails because $y > x$.
So every triple has color $0$, and $H = \mathbb{N}$ is homogeneous, with $h_k = k$.
For $n = 3$ we get $k(3) = 4$ and $h_{k(3) + 1} = 5$, and the search over $i < 5$ finds $f(2) = 3$, so $3 \in R$.
For $n = 0$ we get $k(0) = 1$ and $h_2 = 2$, and no $i < 2$ has $i + 1 = 0$, so $0 \notin R$.
Check: $R = \{1, 2, 3, \dots\}$, the true range.
The typical use of this argument is to show that a combinatorial principle reaches $\mathsf{ACA}_0$, by coding a jump into the coloring.
The trap is the role of $x$: it must be the smallest element of the triple, or step 3 no longer finds $x + 1$ disjoint intervals with values below $x$.
