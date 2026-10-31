---
records:
    - id: MD2ZBBWFKQ
      kind: monograph
      title: Topological Vector Spaces
      creators:
        - name: H. H. Schaefer
          role: author
        - name: M. P. Wolff
          role: author
      date: "1971"
      expressions:
        - key: e1
          kind: edition
          date: "1971"
          ids:
            doi:
                - 10.1007/978-1-4612-1468-7
                - 10.1007/978-1-4684-9928-5
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1999"
              ids:
                isbn:
                    - "9781461271550"
                    - "9781461214687"
            - key: m2
              kind: print
              publisher: Springer New York
              date: "1971"
              ids:
                isbn:
                    - "9780387053806"
                    - "9781468499285"
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4612-1468-7
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4684-9928-5
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
