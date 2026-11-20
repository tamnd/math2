---
tag: 9QB82PPEMV
kind: example
name: Image compression by the SVD
msc: ["15A18", "65F55", "94A08"]
topics: [K0FNC6CWZN]
audience: ug2
instance_of: [000NPTMX6J]
illustrates: [JJT6GC055J]
uses: [000NPTMX6J, 09VMDSRXWJ, JJT6GC055J, JT8Q204E4R, 6VXM1T8PG7]
sources:
  - url: https://en.wikipedia.org/wiki/Singular_value_decomposition
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Low-rank_approximation
    locator: lead section
---

## Example

A grey-scale image of $m \times n$ pixels is an $m \times n$ matrix $A$ of brightness values.
We store an approximation of low rank, made from the largest terms of its [[singular value decomposition|000NPTMX6J]], and we compute the storage and the error.
As a tiny image, take
$$A = \begin{pmatrix} 8 & 4 & 6 & 2 \\ 6 & 2 & 8 & 4 \\ 4 & 8 & 2 & 6 \\ 2 & 6 & 4 & 8 \end{pmatrix}.$$

1. **The SVD.** Let
$v_1 = \tfrac12 (1, 1, 1, 1)$, $v_2 = \tfrac12 (1, -1, 1, -1)$, $v_3 = \tfrac12 (1, 1, -1, -1)$, $v_4 = \tfrac12 (1, -1, -1, 1)$, and
$u_1 = \tfrac12 (1, 1, 1, 1)$, $u_2 = \tfrac12 (1, 1, -1, -1)$, $u_3 = \tfrac12 (1, -1, 1, -1)$.
Both lists are orthonormal: each vector has length $1$, and two different vectors have dot product $0$.
2. **Check.** $A v_1 = (10, 10, 10, 10) = 20\, u_1$, $A v_2 = (4, 4, -4, -4) = 8\, u_2$, $A v_3 = (2, -2, 2, -2) = 4\, u_3$ and $A v_4 = 0$.
3. Since $v_1, \dots, v_4$ is an orthonormal basis, step 2 gives $A = 20\, u_1 v_1^{\mathsf T} + 8\, u_2 v_2^{\mathsf T} + 4\, u_3 v_3^{\mathsf T}$. The [[singular values|09VMDSRXWJ]] are $20$, $8$, $4$ and $0$, and $A$ has rank $3$.
4. **The total energy.** $\norm{A}_F^2 = 20^2 + 8^2 + 4^2 = 480$, which equals the sum of the squares of the $16$ entries. This is the [[Frobenius norm|JT8Q204E4R]] in terms of the singular values.
5. **Rank one.** $A_1 = 20\, u_1 v_1^{\mathsf T}$ is the matrix with all entries $5$, the mean brightness.
6. **Rank two.** $A_2 = A_1 + 8\, u_2 v_2^{\mathsf T} = \begin{pmatrix} 7 & 3 & 7 & 3 \\ 7 & 3 & 7 & 3 \\ 3 & 7 & 3 & 7 \\ 3 & 7 & 3 & 7 \end{pmatrix}$. It shows the main pattern: the top two rows are bright in the columns $1$ and $3$, and the bottom two rows are bright in the columns $2$ and $4$.
7. **The errors.** By the [[Eckart-Young-Mirsky theorem|JJT6GC055J]], $\norm{A - A_1}_2 = \sigma_2 = 8$ and $\norm{A - A_1}_F = \sqrt{64 + 16} = \sqrt{80} \approx 8.94$. Also $\norm{A - A_2}_2 = \norm{A - A_2}_F = \sigma_3 = 4$.
8. **Check of step 7.** $A - A_2 = 4\, u_3 v_3^{\mathsf T}$ has all entries $\pm 1$, so its Frobenius norm is $\sqrt{16} = 4$.
9. **Optimality.** By the same theorem, no matrix of rank at most $2$ is closer to $A$ than $A_2$, in either norm.
10. **Storage.** A rank $k$ approximation needs $k$ singular values, $k$ vectors $u_i$ of length $m$ and $k$ vectors $v_i$ of length $n$: $k (m + n + 1)$ numbers instead of $m n$. Here $A_1$ needs $9$ numbers instead of $16$.
11. **A realistic size.** For a $1000 \times 800$ image and $k = 50$, the storage is $50 \cdot 1801 = 90\,050$ numbers instead of $800\,000$, about $11.3\%$.
12. **The relative error.** $A_2$ keeps the share $(400 + 64)/480 \approx 96.7\%$ of the energy, and its relative Frobenius error is $4 / \sqrt{480} \approx 0.18$.

## Remarks

The example shows that the singular values measure how much each layer contributes, and that the error of truncation is known exactly from the dropped singular values.
For real photographs, the singular values often decay fast, so a small $k$ gives an acceptable picture.

Change the image to make the decay faster or slower.
If the image is $A_2$ itself, with the entries $7$ and $3$, then $\sigma_3 = 0$, and two layers store it exactly.
A random noise image has singular values of similar size, and no small $k$ gives a good approximation.

The SVD is not the method of JPEG.
It needs a new basis for each image, which must be stored, while the cosine basis of JPEG is fixed; see [[change of basis in signal and image processing|6NANBCYMG2]].
The fast algorithms for the SVD of large matrices belong to numerical linear algebra.

## Explanations

### L1 human

A picture is a big table of numbers, one for each pixel.
Many pictures are made of a few simple layers: a background, a big shape, and fine details.
The SVD finds these layers and sorts them by importance.
Keeping only the first few layers gives a picture that looks almost the same and needs much less storage.
In the small example, two layers out of three keep about $97\%$ of the picture's energy.

### L2 human

To compress an image matrix $A$ by the SVD, do these steps.

1. Compute the SVD $A = \sum_i \sigma_i u_i v_i^{\mathsf T}$, with $\sigma_1 \ge \sigma_2 \ge \cdots$.
2. Choose $k$, for example the smallest $k$ with $\sigma_{k+1}^2 + \sigma_{k+2}^2 + \cdots$ below a fixed share of $\norm{A}_F^2$.
3. Store $\sigma_i$, $u_i$, $v_i$ for $i \le k$, which costs $k (m + n + 1)$ numbers.
4. Rebuild $A_k = \sum_{i \le k} \sigma_i u_i v_i^{\mathsf T}$.

The typical use is a first model of data compression and of noise reduction, and the same idea underlies principal component analysis.
The trap is the storage count: for $k \ge mn / (m + n + 1)$, the compressed form is larger than the image.
For the $4 \times 4$ example, $k = 2$ needs $18$ numbers, more than $16$.

### L3 human

The Eckart-Young-Mirsky theorem holds for every unitarily invariant norm, and it is the reason why truncated SVD is the standard low-rank approximation.
For a color image, one can treat each color channel separately, or use a tensor decomposition of the $m \times n \times 3$ array, where the best approximation of low rank need not exist.
Randomized algorithms compute $A_k$ for large $A$ with about $O(m n k)$ operations.
In statistics, the same truncation is principal component analysis, and in information retrieval it is latent semantic analysis.
