---
tag: 1HTW0F4ZZ7
kind: statement
role: theorem
name: Giroux correspondence
msc: [57K33, 53D10]
uses: [HBQ8BZ7XB5, R20TB2KEQQ]
about: [HBQ8BZ7XB5]
sources:
  - url: https://en.wikipedia.org/wiki/Open_book_decomposition
---

## Statement

Let $M$ be a closed oriented [[$3$-manifold|R20TB2KEQQ]].
An *open book decomposition* of $M$ is a pair $(B, \pi)$ of the following kind.
The *binding* $B \subset M$ is an oriented link, and $\pi \colon M \setminus B \to S^1$ is a fibration.
Each fiber $\pi^{-1}(\theta)$ is the interior of a compact surface $\Sigma_\theta$, a *page*, with oriented boundary $\partial \Sigma_\theta = B$.
A cooriented positive contact structure $\xi$ on $M$ is *supported* by $(B, \pi)$ if $\xi = \ker \alpha$ for some contact form $\alpha$ with two properties.
The form $\alpha$ is positive on the oriented binding $B$, and $d\alpha$ is a positive area form on each page.
Then:

1. Every open book decomposition of $M$ supports a [[contact structure|HBQ8BZ7XB5]], and any two contact structures supported by the same open book are isotopic.
2. Every positive contact structure on $M$ is supported by some open book decomposition.
3. Two open book decompositions support isotopic contact structures if and only if they become isotopic after finitely many positive stabilizations of each.

So supporting gives a bijection between two sets.
The first is the set of positive contact structures on $M$ up to isotopy.
The second is the set of open books of $M$ up to isotopy and positive stabilization.

## Remarks

Part 1, the existence, goes back to Thurston and Winkelnkemper; Giroux proved the uniqueness and parts 2 and 3.
The proof of part 2 builds a contact cell decomposition of $M$ and uses a ribbon of its Legendrian $1$-skeleton as a page.
A positive stabilization of an open book adds a $1$-handle to the page and composes the monodromy with a positive Dehn twist along a curve crossing the new handle once.

Example: the open book of $S^3$ whose binding is an unknot and whose pages are discs supports the standard tight contact structure of $S^3$.
The open book with annulus pages and monodromy a negative Dehn twist about the core supports an overtwisted contact structure on $S^3$.

## Explanations

### L1 human

An open book describes a closed three-dimensional space as a family of surfaces, the pages, that all share the same boundary, the binding.
They look like the pages of a book turning around its spine.
Giroux's theorem says that contact structures on such a space correspond exactly to open books, up to a simple move called positive stabilization.
This turns questions about twisting plane fields into questions about surfaces and their diffeomorphisms.

### L2 human

The correspondence lets one study contact $3$-manifolds through the monodromy of an open book, an element of the mapping class group of the page.
For example, a contact structure is Stein fillable exactly when it is supported by some open book whose monodromy is a product of positive Dehn twists.
This is due to work of Giroux, of Loi and Piergallini, and of Akbulut and Ozbagci.
It also gives a route from contact structures to Heegaard Floer invariants, through the contact invariant of Ozsváth and Szabó.
