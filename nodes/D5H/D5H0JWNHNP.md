---
tag: D5H0JWNHNP
kind: example
name: The entries of a matrix with two subscripts
msc: ["00A35", "15A99"]
topics: [Z2WNQ1DNTX, Y1ESNQ2V52]
audience: school
instance_of: [QKEX4PD029, 0VD9ZSWWJG]
uses: [QKEX4PD029, 0VD9ZSWWJG, 09DXWYRD43]
sources:
  - url: https://en.wikipedia.org/wiki/Matrix_(mathematics)
    locator: lead section
---

## Example

Let $A = (a_{ij})$ be the [[matrix|0VD9ZSWWJG]] with $2$ rows and $3$ columns whose entries follow the rule $a_{ij} = 10i + j$.
We write out $A$ and read its subscripts.

1. The first subscript $i$ names the row, and it takes the values $1$ and $2$.
2. The second subscript $j$ names the column, and it takes the values $1$, $2$ and $3$.
3. Row 1 has $a_{11} = 11$, $a_{12} = 12$ and $a_{13} = 13$. Row 2 has $a_{21} = 21$, $a_{22} = 22$ and $a_{23} = 23$. So
$$A = \begin{pmatrix} 11 & 12 & 13 \\ 21 & 22 & 23 \end{pmatrix}.$$
4. The order of the subscripts matters: $a_{12} = 12$ but $a_{21} = 21$.
5. The entry $a_{31}$ does not exist, because $A$ has no third row.
6. The [[transpose|09DXWYRD43]] $B = A^{\mathsf{T}}$ has entries $b_{ij} = a_{ji}$. So it is a $3 \times 2$ matrix, and $b_{12} = a_{21} = 21$.

## Remarks

The rule $a_{ij} = 10i + j$ makes the convention visible, since the tens digit of each entry is its row and the units digit is its column.
The trick stops working at $10$ columns.
Then $a_{1,10} = 20$, and the digits of $20$ suggest row 2 and column 0, a position that does not exist.
The same problem appears in the subscripts themselves: $a_{110}$ could mean row 1 and column 10 or row 11 and column 0, so books write a comma, as in $a_{1,10}$, once an index has two digits.

## Explanations

### L1 human

A matrix is a table of numbers.
To point at one number, we give its row and its column, like the seat "row 2, seat 3" in a theater.
In the matrix above, the number in row 2 and column 3 is $23$, and we write $a_{23} = 23$.
The row always comes first.

### L2 human

The subscripts do their real work inside formulas, and one entry of a product shows this.
Let $B = A^{\mathsf{T}}$, the $3 \times 2$ matrix with $b_{ij} = a_{ji}$.
The product $C = AB$ is $2 \times 2$, and its entries are
$$c_{ij} = \sum_{k=1}^{3} a_{ik} b_{kj} = \sum_{k=1}^{3} a_{ik} a_{jk}.$$
For $i = j = 1$ we add the squares of row 1:
$$c_{11} = 11^2 + 12^2 + 13^2 = 121 + 144 + 169 = 434.$$
The index $k$ is used up by the sum, while the free indices $i$ and $j$ name the entry of $C$.
Watch out: some books and most programming languages number rows and columns from $0$, so their $a_{00}$ is our $a_{11}$.
