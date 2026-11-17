---
tag: N2ES7KCFA2
kind: proof
name: Proof of the worm principle by ordinals below epsilon nought
msc: ["03F30", "03F15", "03F45"]
topics: [T6FK1E7GJ1]
audience: research
proves: MHDZGDNEPS
uses: [EDZN6B9AWQ, KT50SMH3EC, 6GD30FGYDZ, 0F1D6PK9RZ, 0ZHQMQ2C1N, X9WYNYE29C, MPSCREYC3M]
methods: [TP3GC5J08D, 0EFYCFHYFG, 0ASJVEFA9J, 0WCP0PVET6, 0J0XBKG64S]
sources:
  - url: https://en.wikipedia.org/wiki/Japaridze's_polymodal_logic
    locator: History
---

## Proof

We use the worms, the map $\mathrm{next}(w, k)$ and the worm sequences of the [[worm principle|MHDZGDNEPS]].
Ordinals are below [[epsilon nought|KT50SMH3EC]] and are written in [[Cantor normal form|6GD30FGYDZ]].
We use the natural sum $\alpha \# \beta$ and its properties, steps 1 to 6 of the natural sums in the [[proof for the Kirby-Paris hydra|EDZN6B9AWQ]].
In particular $\alpha \# \beta < \alpha \# \beta'$ when $\beta < \beta'$, and $\omega^\beta \cdot c < \omega^{\beta+1}$ for finite $c$.

**The ordinal of a worm.**

1. A *block* of a worm is a maximal nonempty segment of consecutive letters that are all $\ge 1$. For such a segment $B$, let $B - 1$ be $B$ with every letter lowered by $1$.
2. Define $o(w)$ by induction on the largest letter of $w$. Let $o(w)$ be the natural sum of $1$ for each letter $0$ of $w$ and of $\omega^{o(B - 1)}$ for each block $B$ of $w$.
3. The largest letter of $B - 1$ is smaller than that of $w$, so the definition is correct. The empty worm has $o = 0$, and every other worm has $o > 0$.
4. Induction on the largest letter gives $o(w) < \varepsilon_0$, because $\varepsilon_0$ is closed under $\#$ and under $\beta \mapsto \omega^\beta$.
5. Examples: $o(0) = 1$, $o(1) = \omega^{o(0)} = \omega$, $o(11) = \omega^{o(00)} = \omega^2$ and $o(2) = \omega^{o(1)} = \omega^\omega$.

**Lemma: each step lowers the ordinal.**
For every nonempty worm $w$ and every $k \ge 1$, $o(\mathrm{next}(w, k)) < o(w)$.
The proof is by [[induction|0ASJVEFA9J]] on the head $h$ of $w$, with three [[cases|0WCP0PVET6]].

1. Case $h = 0$. The step removes one letter $0$ and changes no block. So $o(\mathrm{next}(w, k)) \# 1 = o(w)$.
2. Case $h = 1$. The last smaller letter is a $0$, or there is none. So $w = u\, v 1$, where $u$ is empty or ends with that $0$, and $v$ has letters $\ge 1$.
3. Then $\mathrm{next}(w, k) = u\, (v 0)^{k+1}$. The block $v 1$ of $w$ is replaced by $k + 1$ blocks $v$ and $k + 1$ letters $0$. Other blocks do not change.
4. Let $\beta = o(v - 1)$. The old block counts $\omega^{o((v-1) 0)} = \omega^{\beta \# 1} = \omega^{\beta + 1}$. The new letters count $\omega^\beta \cdot (k+1) \# (k+1)$.
5. All exponents of the new part are at most $\beta$, so the new part is below $\omega^{\beta + 1}$. If $v$ is empty, the new part is $k + 1 < \omega$.
6. By monotonicity of $\#$, $o(\mathrm{next}(w, k)) < o(w)$.
7. Case $h \ge 2$. Let $B$ be the block that ends with the head. The last letter smaller than $h$ is in $B$, or it is the $0$ just before $B$, or there is none.
8. So the step changes only $B$, into a segment $B'$ of letters $\ge 1$. This segment $B'$ is the new last block.
9. A letter of $B$ is smaller than $h$ exactly when the same letter of $B - 1$ is smaller than $h - 1$. So $B' - 1 = \mathrm{next}(B - 1, k)$, computed in $B - 1$ alone.
10. The head of $B - 1$ is $h - 1 \ge 1$, so the induction hypothesis gives $o(B' - 1) < o(B - 1)$.
11. Then $\omega^{o(B' - 1)} < \omega^{o(B - 1)}$, the letters $0$ and the other blocks do not change, and monotonicity of $\#$ gives $o(\mathrm{next}(w, k)) < o(w)$.

**Part 1: termination.**

1. Let $w_0$ be a worm, and suppose that its worm sequence never reaches the empty worm.
2. By the lemma, $o(w_0) > o(w_1) > o(w_2) > \cdots$ is an infinite decreasing sequence of ordinals.
3. This contradicts the [[well-ordering|0F1D6PK9RZ]] of the ordinals. So the sequence reaches the empty worm.

**Part 4: the stronger theories.**

1. The ordinals below $\varepsilon_0$ have a primitive recursive notation, and the lemma is a finite check on notations, so $\mathsf{PA}$ proves it.
2. Apply [[transfinite induction|0ZHQMQ2C1N]] up to $\varepsilon_0$ to the formula "for every $w$ with $o(w) = \alpha$ and every $k$, the sequence that starts with $w$ at step $k$ ends". This proves $\mathrm{WP}$.
3. So $\mathsf{PA}$ plus transfinite induction up to $\varepsilon_0$ proves $\mathrm{WP}$, and so does $\mathsf{ZFC}$.
4. The proof in $\mathsf{PA} + 1\text{-}\mathrm{Con}(\mathsf{PA})$ is the direction from $1\text{-}\mathrm{Con}(\mathsf{PA})$ to $\mathrm{WP}$ of cited lemma B below.

**Parts 2 and 3: cited results.**

1. **Cited lemma A** (Beklemishev). $\mathsf{PA}$ proves that $\mathrm{WP}$ implies $1\text{-}\mathrm{Con}(\mathsf{PA})$. This lemma is cited without proof. Its proof reads worms as formulas of $\mathsf{GLP}$ and uses reflection principles.
2. **Cited lemma B** (Beklemishev). $\mathsf{PA}$ proves that $1\text{-}\mathrm{Con}(\mathsf{PA})$ implies $\mathrm{WP}$. This lemma is cited without proof.
3. Lemmas A and B together are part 3.
4. Suppose that $\mathsf{PA}$ proves $\mathrm{WP}$. Then lemma A gives a proof of $1\text{-}\mathrm{Con}(\mathsf{PA})$ in $\mathsf{PA}$.
5. The sentence $0 = 1$ is $\Sigma_1$ and false, so $1\text{-}\mathrm{Con}(\mathsf{PA})$ implies $\mathrm{Con}(\mathsf{PA})$, and $\mathsf{PA}$ proves this implication.
6. So $\mathsf{PA}$ proves $\mathrm{Con}(\mathsf{PA})$. This contradicts the second [[incompleteness theorem|X9WYNYE29C]], because [[Peano arithmetic|MPSCREYC3M]] is consistent.
7. So $\mathsf{PA}$ does not prove $\mathrm{WP}$, which is part 2.

## Idea

Each block of a worm is a power of $\omega$, and its letters, lowered by one, give the exponent.
A step either removes a $0$, or replaces one power $\omega^{\beta + 1}$ by finitely many smaller powers, or works inside one block one level down.
So the ordinal goes down at every step, and termination follows from well-ordering.
The unprovability comes from the link between worms and the $1$-consistency of $\mathsf{PA}$, which is the cited part.

## Variants

- Beklemishev's analysis uses the order of worms as formulas of $\mathsf{GLP}$, which has type $\varepsilon_0$, in place of the explicit map $o$.
- The same method of an ordinal that falls at each step proves the [[Kirby-Paris hydra theorem|C028FF4TWM]] and [[Goodstein's theorem|XQMNJF241J]].
