---
tag: FQMBWRM4R8
kind: statement
role: lemma
name: Foata's transition lemma
msc: [05A05]
sources:
  - wikipedia: en:44027@r1375229548
    locator: Permutation, section Permutations of totally ordered sets > Foata's transition lemma
    note: adopted
    mention: wikipedia://en/44027#63QH
    sections: [Statement]
inventory: [7DWSKZDARR]
---

## Statement

Foata's *fundamental bijection* transforms a permutation $\sigma$ with a given canonical cycle form into the permutation $f(\sigma) = \hat\sigma$ whose one-line notation has the same sequence of elements with parentheses removed. For example:

$$\sigma = (513)(6)(827)(94) = \begin{pmatrix} 1&2&3&4&5&6&7&8&9\\ 3&7&5&9&1&6&8&2&4 \end{pmatrix},$$

$$\hat\sigma = 513682794 = \begin{pmatrix} 1&2&3&4&5&6&7&8&9\\ 5&1&3&6&8&2&7&9&4 \end{pmatrix}.$$

Here the first element in each canonical cycle of $\sigma$ becomes a record (left-to-right maximum) of $\hat\sigma$. Given $\hat\sigma$, one may find its records and insert parentheses to construct the inverse transformation $\sigma=f^{-1}(\hat\sigma)$. Underlining the records in the above example: $\hat\sigma = \underline{5}\, 1\, 3\, \underline{6}\, \underline{8}\,2\,7\,\underline{9}\,4$, which allows the reconstruction of the cycles of $\sigma$.

The following table shows $\hat\sigma$ and $\sigma$ for the six permutations of *S* = {1, 2, 3}, with the bold text on each side showing the notation used in the bijection: one-line notation for $\hat\sigma$ and canonical cycle notation for $\sigma$.

$$\begin{array}{l|l} \hat\sigma = f(\sigma) & \sigma=f^{-1}(\hat\sigma) \\ \hline \mathbf{123}=(\,1\,)(\,2\,)(\,3\,) & 123=\mathbf{(\,1\,)(\,2\,)(\,3\,)} \\ \mathbf{132}=(\,1\,)(\,3\,2\,) & 132=\mathbf{(\,1\,)(\,3\,2\,)} \\ \mathbf{213}=(\,2\,1\,)(\,3\,) & 213=\mathbf{(\,2\,1\,)(\,3\,)} \\ \mathbf{231}=(\,3\,1\,2\,) & 321=\mathbf{(\,2\,)(\,3\,1\,)} \\ \mathbf{312}=(\,3\,2\,1\,) & 231=\mathbf{(\,3\,1\,2\,)} \\ \mathbf{321}=(\,2\,)(\,3\,1\,) & 312=\mathbf{(\,3\,2\,1\,)} \end{array}$$

As a first corollary, the number of *n*-permutations with exactly *k* records is equal to the number of *n*-permutations with exactly *k* cycles: this last number is the signless Stirling number of the first kind, $c(n, k)$. Furthermore, Foata's mapping takes an *n*-permutation with *k* weak exceedances to an *n*-permutation with $k - 1$ ascents. For example, (2)(31) = 321 has *k =* 2 weak exceedances (at index 1 and 2), whereas $f(321) = 231$ has $k - 1 = 1$ ascent (at index 1; that is, from 2 to 3).
