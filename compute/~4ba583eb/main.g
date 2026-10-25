# The subgroups of the symmetric group S4, for the computation node ~4ba583eb.
#
# The program lists each subgroup of S4 with the sorted list of its elements, and writes the list to /out/certificate. An element is the string of the images of 1, 2, 3 and 4, for example 2134 for the transposition (1,2). A line of the certificate is the order of the subgroup and then its elements, with a space between them. The lines are sorted, so the certificate does not depend on the order in which GAP finds the subgroups. The standard output gives the number of subgroups of each order.

SetPrintFormattingStatus("*stdout*", false);
n := 4;
G := SymmetricGroup(n);
word := p -> Concatenation(List([1 .. n], i -> String(i ^ p)));
rows := List(AllSubgroups(G), H -> [Size(H), SortedList(List(AsList(H), word))]);
Sort(rows);

out := OutputTextFile("/out/certificate", false);
SetPrintFormattingStatus(out, false);
for r in rows do
  AppendTo(out, JoinStringsWithSeparator(Concatenation([String(r[1])], r[2]), " "), "\n");
od;
CloseStream(out);

Print("subgroups of S", n, ": ", Length(rows), "\n");
for k in Set(List(rows, r -> r[1])) do
  Print("order ", k, ": ", Number(rows, r -> r[1] = k), "\n");
od;
QuitGap(0);
