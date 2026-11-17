---
tag: MHDZGDNEPS
kind: statement
role: theorem
name: Beklemishev's worm principle
aliases: [worm-principle]
msc: ["03F30", "03F45", "03F15"]
topics: [T6FK1E7GJ1]
audience: research
uses: [MPSCREYC3M, KT50SMH3EC, WJK0YA4GP2, 509ZWA0R26, X9WYNYE29C]
about: [MPSCREYC3M]
history:
  first_stated: "2003"
  notes: "Beklemishev, 'The worm principle', Logic Group Preprint Series 219, Utrecht (2003); published in Logic Colloquium '02, Lecture Notes in Logic 27 (2006). The principle comes from Japaridze's polymodal provability logic GLP."
sources:
  - url: https://en.wikipedia.org/wiki/Japaridze's_polymodal_logic
    locator: History
  - url: https://en.wikipedia.org/wiki/Japaridze's_polymodal_logic
    locator: Provability semantics
---

## Statement

A *worm* is a finite word $x_0 x_1 \dots x_n$ of natural numbers, and the empty word is the empty worm.
The last letter $x_n$ is the *head*.
For a nonempty worm $w = x_0 \dots x_n$ and a number $k \ge 1$, define the worm $\mathrm{next}(w, k)$ as follows.

1. If $x_n = 0$, then $\mathrm{next}(w, k) = x_0 \dots x_{n-1}$: the head is cut away.
2. If $x_n > 0$, let $j$ be the largest index $j < n$ with $x_j < x_n$, and $j = -1$ if there is none.
3. Let $s = x_{j+1} \dots x_{n-1} (x_n - 1)$. Then $\mathrm{next}(w, k) = x_0 \dots x_j\, s^{k+1}$, where $s^{k+1}$ is $s$ written $k + 1$ times.

The *worm sequence* of $w_0$ is $w_0, w_1, w_2, \dots$ with $w_k = \mathrm{next}(w_{k-1}, k)$, as long as $w_{k-1}$ is nonempty.
The *worm principle* $\mathrm{WP}$ is the $\Pi_2$ sentence "for every worm $w_0$ there is $m$ with $w_m$ empty".

**Theorem** (Beklemishev).

1. $\mathrm{WP}$ is true: every worm sequence reaches the empty worm.
2. $\mathrm{WP}$ is not provable in [[Peano arithmetic|MPSCREYC3M]] $\mathsf{PA}$.
3. $\mathsf{PA}$ proves that $\mathrm{WP}$ is equivalent to $1\text{-}\mathrm{Con}(\mathsf{PA})$, the statement that every $\Sigma_1$ sentence provable in $\mathsf{PA}$ is true.
4. $\mathrm{WP}$ is provable in $\mathsf{PA} + 1\text{-}\mathrm{Con}(\mathsf{PA})$, in $\mathsf{PA}$ with transfinite induction up to [[epsilon nought|KT50SMH3EC]], and in $\mathsf{ZFC}$.

The [[proof|N2ES7KCFA2]] proves part 1 in full by ordinals, and it cites lemmas for parts 2 and 3.

**Example.** The worm sequence of $2031$ starts as follows.

1. $w_0 = 2031$. The head is $1$, and the last smaller letter is the $0$ at index $1$. So $s = 30$, and $w_1 = 20\,(30)^2 = 203030$.
2. The head of $w_1$ is $0$, so $w_2 = 20303$.
3. The head of $w_2$ is $3$, and the last smaller letter is the $0$ at index $3$. So $s = 2$, and $w_3 = 2030\,(2)^4 = 20302222$.
4. The head of $w_3$ is $2$, and the last smaller letter is again the $0$ at index $3$. So $s = 2221$, and $w_4 = 2030\,(2221)^5$.

## Remarks

### Why each hypothesis is needed

- The theory is $\mathsf{PA}$. The stronger theory $\mathsf{PA} + 1\text{-}\mathrm{Con}(\mathsf{PA})$ proves $\mathrm{WP}$, so the independence is relative to $\mathsf{PA}$.
- The head must go down in rule 3. If rule 3 kept $x_n$, the worm $1$ would give $11$, $111$, and so on, and the sequence would never end.
- The growing number $k + 1$ of copies is not needed for termination: the proof works for any number of copies. It is what makes the sequences long enough to escape $\mathsf{PA}$.

### Consequences

- Let $L(w)$ be the least $m$ with $w_m$ empty in the worm sequence of $w$. By part 2, $\mathsf{PA}$ does not prove that $L$ is total, so $L$ is not a [[provably total function|Z742YPHPNS]] of $\mathsf{PA}$ with this definition.
- Small values, by direct computation: $L(0) = 1$, $L(1) = 3$, $L(10) = 5$, $L(11) = 19$ and $L(2) = 51$.
- By part 3, $\mathsf{PA} + \mathrm{WP}$ proves $\mathrm{Con}(\mathsf{PA})$, as for the [[Paris-Harrington theorem|509ZWA0R26]].

### Converse

$\neg \mathrm{WP}$ is not provable in $\mathsf{PA}$ either, because $\mathrm{WP}$ is true and $\mathsf{PA}$ proves only true sentences.
So $\mathrm{WP}$ is independent of $\mathsf{PA}$.

### Generalizations

- The [[Kirby-Paris hydra|C028FF4TWM]] and [[Goodstein's theorem|XQMNJF241J]] are other terminating processes whose proofs use ordinals up to $\varepsilon_0$ and that $\mathsf{PA}$ does not prove.
- A worm $x_0 \dots x_n$ is read as the formula $\langle x_0 \rangle \cdots \langle x_n \rangle \top$ of Japaridze's logic $\mathsf{GLP}$, a [[provability logic|WJK0YA4GP2]] with one modality for each $n$. Worms of this logic give an ordinal notation system up to $\varepsilon_0$.

## History

Lev Beklemishev introduced the worm principle in a preprint of 2003, published in 2006 in the proceedings of Logic Colloquium 2002.
He derived it from his study of provability algebras for Japaridze's logic $\mathsf{GLP}$.
The Wikipedia article on $\mathsf{GLP}$ lists simple combinatorial independent statements among the main applications of this logic.

## Explanations

### L1 human

A worm is a row of numbers, and its last number is its head.
At each step the head shrinks by one, and a piece of the worm behind it is copied several times.
The worm $1$ becomes $00$, then $0$, then disappears after three steps.
Bigger worms grow enormously before they shrink, but every worm dies in the end.
Ordinary arithmetic cannot prove this, although its truth follows from a simple fact about infinite ordinals.

### L2 human

A full worm sequence for the worm $11$ starts as follows.

1. $w_0 = 11$. No letter before the head is smaller than $1$, so $j = -1$ and $s = 10$.
2. $w_1 = (10)^2 = 1010$.
3. $w_2 = 101$, by cutting the head $0$.
4. In $w_2$ the last smaller letter is the $0$ at index $1$, so $s = 0$ and $w_3 = 10\,(0)^4 = 100000$.
5. The next $5$ steps cut zeros and give $w_8 = 1$. Then $w_9 = (0)^{10}$, and $10$ more steps give $w_{19}$ empty.

The typical use is as a short independence result with a modal logic background.
The trap: the number of copies depends on the step, so the sequence of a worm depends on where it starts in the count.

### L3 human

Beklemishev's analysis reads worms as formulas of $\mathsf{GLP}$, where $\langle n \rangle \varphi$ says that $\varphi$ is consistent with $\mathsf{PA}$ plus all true $\Pi_n$ sentences.
The worms ordered by consistency strength form a well-order of type $\varepsilon_0$, and the worm game is a descent along this order.
So the [[proof-theoretic ordinal|C72RBH0CDR]] of $\mathsf{PA}$ is recovered inside the provability logic itself, and $\mathrm{WP}$ is a combinatorial form of the $1$-consistency of $\mathsf{PA}$.
This links the sub-area to [[Gödel's incompleteness theorems|X9WYNYE29C]] and to [[ordinal analysis|C5E5TG8PGP]].
