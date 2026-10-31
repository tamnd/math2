---
records:
    - id: XYH1BX001E
      kind: monograph
      title: An Index and Other Useful Information
      creators:
        - name: Springer-Verlag Berlin Heidelberg
          role: author
      date: "1975"
      expressions:
        - key: e1
          kind: edition
          date: "1975"
          ids:
            doi: 10.1007/978-1-4899-4581-5
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1975"
              ids:
                isbn:
                    - "9781489945839"
                    - "9781489945815"
              access:
                class: record
      relations:
        - kind: part_of
          to: MYK049V6DA
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.7 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4899-4581-5
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
